# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.lifegame_vol1o0.views.board.ver0o1o0 import BoardView as BoardViewV0o1o0
from apps1.lifegame_vol1o0.views.board.ver0o2o0 import BoardView as BoardViewV0o2o0
from apps1.lifegame_vol1o0.views.board.ver0o3o0 import BoardView as BoardViewV0o3o0


urlpatterns = [
    # OAAA1001o1o0ga10o1o0 ライフゲーム v0.1 の盤
    path('lifegame/vol1.0/ver0.1/board', BoardViewV0o1o0.render, name='lifegame_1o0g0o1o0_board'),

    # OAAA1001o1o0ga12o_7o1o0 ライフゲーム v0.2 の盤
    path('lifegame/vol1.0/ver0.2/board', BoardViewV0o2o0.render, name='lifegame_1o0g0o2o0_board'),

    # OAAA1001o1o0ga15o1o0 ライフゲーム v0.3 の盤
    path('lifegame/vol1.0/ver0.3/board', BoardViewV0o3o0.render, name='lifegame_1o0g0o3o0_board'),
]

# EOF O3o2o_1o0g4o0
