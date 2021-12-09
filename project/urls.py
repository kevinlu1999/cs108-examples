from django.urls import path
from .views import ShowAllTeamsView, ShowTeamPageView, CreateGameView, CreateTeamView, CreatePlayerView,\
    add_game, add_team, add_player

urlpatterns = [
    path('', ShowAllTeamsView.as_view(), name="show_all_teams"),
    path('team/<int:pk>', ShowTeamPageView.as_view(), name="show_team_page"),
    path('create_game', CreateGameView.as_view(), name='create_game'),
    path('create_team', CreateTeamView.as_view(), name='create_team'),
    path('create_player', CreatePlayerView.as_view(), name='create_player'),
    path('add_game', add_game, name="add_game"),
    path('add_team', add_team, name="add_team"),
    path('add_player', add_player, name="add_player")
]
