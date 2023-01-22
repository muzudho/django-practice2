# AutoGenBegin O3o2o_1o0g4o0

from django.urls import path

from apps1.tic_tac_toe_vol3o0.views.match_application.ver1o0 import MatchApplicationView as TicTacToe3o0MatchApplicationView1o0
from apps1.tic_tac_toe_vol3o0.views.playing.ver1o0 import PlayingView as TicTacToe3o0PlayingView1o0
from apps1.tic_tac_toe_vol3o0.views.match_application.ver2o0 import MatchApplicationView as TicTacToe3o0MatchApplicationView2o0
from apps1.tic_tac_toe_vol3o0.views.match_application.ver3o0 import MatchApplicationView as TicTacToe3o0MatchApplicationView3o0
from apps1.tic_tac_toe_vol3o0.views.playing.ver3o0 import PlayingView as TicTacToe3o0PlayingView3o0
from apps1.tic_tac_toe_vol3o0.views.match_application.ver4o0 import MatchApplicationView as TicTacToe3o0MatchApplicationView4o0
from apps1.tic_tac_toe_vol3o0.views.playing.ver4o0 import PlayingView as TicTacToe3o0PlayingView4o0


urlpatterns = [
    # [OA22o1o0gA10o1o0] 〇×ゲーム3.0巻 対局申込中1.0版
    path('tic-tac-toe/vol3.0/match-application/ver1.0/', TicTacToe3o0MatchApplicationView1o0.render),

    # [OA22o1o0gA10o1o0] 〇×ゲーム3.0巻 対局中1.0版
    path('tic-tac-toe/vol3.0/playing/ver1.0/<str:kw_room_name>/', TicTacToe3o0PlayingView1o0.render),

    # [OA23o1o0g4o1o0] 〇×ゲーム3.0巻 対局申込中2.0版
    path('tic-tac-toe/vol3.0/match-application/ver2.0/', TicTacToe3o0MatchApplicationView2o0.render),

    # [OA24o1o0g8o1o0] 〇×ゲーム3.0巻 対局申込中3.0版
    path('tic-tac-toe/vol3.0/match-application/ver3.0/', TicTacToe3o0MatchApplicationView3o0.render),

    # [OA24o1o0g8o1o0] 〇×ゲーム3.0巻 対局中3.0版
    path('tic-tac-toe/vol3.0/playing/ver3.0/<str:kw_room_name>/', TicTacToe3o0PlayingView3o0.render),

    # [OA25o1o0g5o1o0] 〇×ゲーム3.0巻 対局申込中4.0版
    path('tic-tac-toe/vol3.0/match-application/ver4.0/', TicTacToe3o0MatchApplicationView4o0.render),

    # [OA25o1o0g5o1o0] 〇×ゲーム3.0巻 対局中4.0版
    path('tic-tac-toe/vol3.0/playing/ver4.0/<str:kw_room_name>/', TicTacToe3o0PlayingView4o0.render),
]

# AutoGenEnd O3o2o_1o0g4o0
