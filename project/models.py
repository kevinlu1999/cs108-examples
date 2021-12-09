from django.db import models
from django.db.models import Q
import datetime

# Create your models here.


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    image_url = models.URLField(blank=True)
    win_rate = models.FloatField(blank=True, default=0)

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.wins, self.losses)

    def get_players(self):
        return Player.objects.filter(team=self)

    def get_games(self):
        return Game.objects.filter(Q(home_team=self) | Q(away_team=self))

    def update_win_rate(self):
        if self.wins == 0 and self.losses == 0:
            self.win_rate = 0
        else:
            self.win_rate = round(self.wins / (self.wins + self.losses), 2)

    def get_team_players(self):
        return Player.objects.filter(team=self.name)

    def get_game_history(self):
        home_games = Game.objects.filter(home_team=self.name)
        away_games = Game.objects.filter(away_team=self.name)
        return (home_games | away_games).distinct()


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    number = models.IntegerField(default=0)
    position = models.CharField(max_length=10)
    image_url = models.URLField(blank=True)
    team = models.CharField(max_length=30)

    def __str__(self):
        return '{}, {}, {} ({})'.format(self.name, self.number, self.position, self.team)


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.datetime(2021, 12, 1))
    home_team = models.CharField(max_length=15)  # home team name
    away_team = models.CharField(max_length=15)
    home_score = models.IntegerField(default=100)
    away_score = models.IntegerField(default=100)

    def __str__(self):
        return '{} {} : {} {}, {}'.format(self.home_team, self.home_score, self.away_score, self.away_team, self.date)
