from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from project.models import Game, Team, Player
from django.shortcuts import redirect
from django.urls import reverse
from .forms import CreateGameForm, CreateTeamForm, CreatePlayerForm


# Create your views here.
class ShowAllTeamsView(ListView):
    model = Team
    template_name = "project/show_all_teams.html"
    context_object_name = "teams"
    # sort the teams by win_rate from high to low
    ordering = ['-win_rate']


class ShowTeamPageView(DetailView):
    model = Team
    template_name = "project/show_team_page.html"
    context_object_name = "team"


class CreateGameView(CreateView):
    form_class = CreateGameForm
    template_name = "project/create_game_form.html"


class CreateTeamView(CreateView):
    form_class = CreateTeamForm
    template_name = "project/create_team_form.html"


class CreatePlayerView(CreateView):
    form_class = CreatePlayerForm
    template_name = "project/create_player_form.html"


def add_game(request):
    date = '{}-{}-{}'.format(request.POST['date_year'], request.POST['date_month'], request.POST['date_day'])
    home_team = request.POST['home_team']
    away_team = request.POST['away_team']
    home_score = int(request.POST['home_score'])
    away_score = int(request.POST['away_score'])
    game = Game(date=date, home_team=home_team, away_team=away_team, home_score=home_score, away_score=away_score)
    game.save()

    home = Team.objects.get(name=home_team)
    away = Team.objects.get(name=away_team)

    if home_score > away_score:
        home.wins += 1
        away.losses += 1
    else:
        away.wins += 1
        home.losses += 1
    home.update_win_rate()
    away.update_win_rate()
    home.save()
    away.save()
    return redirect(reverse('show_all_teams'))


def add_team(request):
    name = request.POST['name']
    img_url = request.POST['img_url']

    team = Team(name=name, image_url=img_url)
    team.save()

    return redirect(reverse('show_all_teams'))


def add_player(request):
    name = request.POST['name']
    number = request.POST['number']
    position = request.POST['position']
    img_url = request.POST['img_url']
    team = request.POST['team']

    player = Player(name=name, number=number, position=position, image_url=img_url, team=team)
    player.save()

    team = Team.objects.get(name=player.team)

    return redirect(reverse('show_team_page', kwargs={'pk': team.id}))
