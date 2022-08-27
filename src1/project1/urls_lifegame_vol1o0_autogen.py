# AutoGenBegin O3o2o_1o0g4o0

from django.urls import path

from apps1.lifegame_vol1o0.views.board.ver0o1o0 import BoardView as Lifegame1o0BoardView0o1o0
from apps1.lifegame_vol1o0.views.board.ver0o2o0 import BoardView as Lifegame1o0BoardView0o2o0
from apps1.lifegame_vol1o0.views.board.ver0o3o0 import BoardView as Lifegame1o0BoardView0o3o0


urlpatterns = [
    # OAAA1001o1o0ga10o1o0 ライフゲーム1.0巻 盤0.1版
    path('lifegame/vol1.0/board/ver0.1', Lifegame1o0BoardView0o1o0.render),

    # OAAA1001o1o0ga12o_7o1o0 ライフゲーム1.0巻 盤0.2版
    path('lifegame/vol1.0/board/ver0.2', Lifegame1o0BoardView0o2o0.render),

    # OAAA1001o1o0ga15o1o0 ライフゲーム1.0巻 盤0.3版
    path('lifegame/vol1.0/board/ver0.3', Lifegame1o0BoardView0o3o0.render),
]

# AutoGenEnd O3o2o_1o0g4o0
