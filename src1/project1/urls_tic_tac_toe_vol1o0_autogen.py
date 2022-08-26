# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.tic_tac_toe_vol1o0.views.match_application.ver1o0 import MatchApplicationV
from apps1.tic_tac_toe_vol1o0.views.playing.ver1o0 import PlayingV


urlpatterns = [
    # OA16o1o0gA17o1o0 〇×ゲーム1.0巻 1.0版 対局申込
    path('tic-tac-toe/vol1.0/match-application/ver1.0/', MatchApplicationV.render),

    # OA16o1o0gA17o1o0 〇×ゲーム1.0巻 1.0版 対局中
    path('tic-tac-toe/vol1.0/playing/ver1.0/<str:room_name>/', PlayingV.render),
]

# EOF O3o2o_1o0g4o0
