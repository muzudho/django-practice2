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
    # OA22o1o0gA10o1o0 〇×ゲーム3.0巻 1.0版 対局申込中
    path('tic-tac-toe/vol3.0/match-application/ver1.0/', TicTacToeV3g1o0MatchApplicationV.render),

    # OA22o1o0gA10o1o0 〇×ゲーム3.0巻 1.0版 対局中
    path('tic-tac-toe/vol3.0/playing/ver1.0/<str:kw_room_name>/', TicTacToeV3g1o0PlayingV.render),

    # OA23o1o0g4o1o0 〇×ゲーム3.0巻 2.0版 対局申込中
    path('tic-tac-toe/vol3.0/match-application/ver2.0/', TicTacToeV3g2o0MatchApplicationV.render),

    # OA24o1o0g8o1o0 〇×ゲーム3.0巻 3.0版 対局申込中
    path('tic-tac-toe/vol3.0/match-application/ver3.0/', TicTacToeV3g3o0MatchApplicationV.render),

    # OA24o1o0g8o1o0 〇×ゲーム3.0巻 3.0版 対局中
    path('tic-tac-toe/vol3.0/playing/ver3.0/<str:kw_room_name>/', TicTacToeV3g3o0PlayingV.render),

    # OA25o1o0g5o1o0 〇×ゲーム3.0巻 4.0版 対局申込中
    path('tic-tac-toe/vol3.0/match-application/ver4.0/', TicTacToeV3g4o0MatchApplicationV.render),

    # OA25o1o0g5o1o0 〇×ゲーム3.0巻 4.0版 対局中
    path('tic-tac-toe/vol3.0/playing/ver4.0/<str:kw_room_name>/', TicTacToeV3g4o0PlayingV.render),
]

# EOF O3o2o_1o0g4o0
