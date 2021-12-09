from django import forms
from .models import Game, Team, Player


class CreateGameForm(forms.ModelForm):
    '''A form to create a new basketball game'''
    date = forms.DateField(label='date', required=True, widget=forms.SelectDateWidget(years=[2021]))
    home_team = forms.CharField(label='home_team', required=True)
    away_team = forms.CharField(label='away_team', required=True)
    home_score = forms.IntegerField(label='home_score', required=True)
    away_score = forms.IntegerField(label='away_score', required=True)

    class Meta:
        model = Game
        fields = ['date', 'home_team', 'away_team', 'home_score', 'away_score']


class CreateTeamForm(forms.ModelForm):
    name = forms.CharField(label='name', required=True)
    img_url = forms.URLField(label='img_url', required=True)

    class Meta:
        model = Team
        fields = ['name', 'img_url']


class CreatePlayerForm(forms.ModelForm):
    name = forms.CharField(label='name', required=True)
    number = forms.IntegerField(label='number', required=True)
    position = forms.CharField(label='position', required=True)
    img_url = forms.URLField(label='img_url', required=True)
    team = forms.CharField(label='team', required=True)

    class Meta:
        model = Player
        fields = ['name', 'number', 'position', 'img_url', 'team']
