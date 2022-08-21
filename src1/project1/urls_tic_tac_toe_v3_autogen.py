# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.tic_tac_toe_v3.views.match_application.v1o0 import MatchApplicationV as TicTacToeV3g1o0MatchApplicationV
from apps1.tic_tac_toe_v3.views.playing.v1o0 import PlayingV as TicTacToeV3g1o0PlayingV


urlpatterns = [
    # OA22o1o0gA10o1o0 〇×ゲーム v3.1 対局申込中
    path('tic-tac-toe/v3.1/match-application/', TicTacToeV3g1o0MatchApplicationV.render, name='tic_tac_toe_v3g1o0_match_application'),

    # OA22o1o0gA10o1o0 〇×ゲーム v3.1 対局中
    path('tic-tac-toe/v3.1/playing/<str:kw_room_name>/', TicTacToeV3g1o0PlayingV.render, name='tic_tac_toe_v3g1o0_playing'),
]

# EOF O3o2o_1o0g4o0
