# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.tic_tac_toe_vol3o0.views.match_application.ver1o0 import MatchApplicationV as TicTacToeV3g1o0MatchApplicationV
from apps1.tic_tac_toe_vol3o0.views.playing.ver1o0 import PlayingV as TicTacToeV3g1o0PlayingV
from apps1.tic_tac_toe_vol3o0.views.match_application.ver2o0 import MatchApplicationV as TicTacToeV3g2o0MatchApplicationV
from apps1.tic_tac_toe_vol3o0.views.match_application.ver3o0 import MatchApplicationV as TicTacToeV3g3o0MatchApplicationV
from apps1.tic_tac_toe_vol3o0.views.playing.ver3o0 import PlayingV as TicTacToeV3g3o0PlayingV
from apps1.tic_tac_toe_vol3o0.views.match_application.ver4o0 import MatchApplicationV as TicTacToeV3g4o0MatchApplicationV
from apps1.tic_tac_toe_vol3o0.views.playing.ver4o0 import PlayingV as TicTacToeV3g4o0PlayingV


urlpatterns = [
    # OA22o1o0gA10o1o0 〇×ゲーム3.0巻 3.1版 対局申込中
    path('tic-tac-toe/vol3.0/ver3.1/match-application/', TicTacToeV3g1o0MatchApplicationV.render, name='tic_tac_toe_v3g1o0_match_application'),

    # OA22o1o0gA10o1o0 〇×ゲーム3.0巻 3.1版 対局中
    path('tic-tac-toe/vol3.0/ver3.1/playing/<str:kw_room_name>/', TicTacToeV3g1o0PlayingV.render, name='tic_tac_toe_v3g1o0_playing'),

    # OA23o1o0g4o1o0 〇×ゲーム3.0巻 3.2版 対局申込中
    path('tic-tac-toe/vol3.0/ver3.2/match-application/', TicTacToeV3g2o0MatchApplicationV.render, name='tic_tac_toe_v3g2o0_match_application'),

    # OA24o1o0g8o1o0 〇×ゲーム3.0巻 3.3版 対局申込中
    path('tic-tac-toe/vol3.0/ver3.3/match-application/', TicTacToeV3g3o0MatchApplicationV.render, name='tic_tac_toe_v3g3o0_match_application'),

    # OA24o1o0g8o1o0 〇×ゲーム3.0巻 3.3版 対局中
    path('tic-tac-toe/vol3.0/ver3.3/playing/<str:kw_room_name>/', TicTacToeV3g3o0PlayingV.render, name='tic_tac_toe_v3g3o0_playing'),

    # OA25o1o0g5o1o0 〇×ゲーム3.0巻 3.4版 対局申込中
    path('tic-tac-toe/vol3.0/ver3.4/match-application/', TicTacToeV3g4o0MatchApplicationV.render, name='tic_tac_toe_v3g4o0_match_application'),

    # OA25o1o0g5o1o0 〇×ゲーム3.0巻 3.4版 対局中
    path('tic-tac-toe/vol3.0/ver3.4/playing/<str:kw_room_name>/', TicTacToeV3g4o0PlayingV.render, name='tic_tac_toe_v3g4o0_playing'),
]

# EOF O3o2o_1o0g4o0
