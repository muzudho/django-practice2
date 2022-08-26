# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.tic_tac_toe_vol2o0.views.think.engine_manual.ver1o0 import EngineManual
from apps1.tic_tac_toe_vol2o0.views.msg.c2s_json_gen.ver1o0 import C2sJsonGenView as C2sJsonGenViewV1o0
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.ver1o0 import S2cJsonGenView as S2cJsonGenViewV1o0
from apps1.tic_tac_toe_vol2o0.views.gui.match_application.ver1o0 import MatchApplicationV
from apps1.tic_tac_toe_vol2o0.views.gui.playing.ver1o0 import PlayingV


urlpatterns = [
    # OA16o2o0gA16o1o0 〇×ゲーム2.0巻 思考エンジン手動1.0版
    path('tic-tac-toe/vol2.0/engine-manual/ver1.0/', EngineManual.render),

    # OA16o3o_1o0g4o1o0 〇×ゲーム2.0巻 C2S JSON ジェネレーター1.0版
    path('tic-tac-toe/vol2.0/c2s-json-gen/ver1.0/', C2sJsonGenViewV1o0.render),

    # OA16o3o_2o0g5o1o0 〇×ゲーム2.0巻 S2C JSON ジェネレーター1.0版
    path('tic-tac-toe/vol2.0/s2c-json-gen/ver1.0/', S2cJsonGenViewV1o0.render),

    # OA16o3o0gA15o1o0 〇×ゲーム2.0巻 対局申込中1.0版
    path('tic-tac-toe/vol2.0/match-application/ver1.0/', MatchApplicationV.render),

    # OA16o3o0gA15o1o0 〇×ゲーム2.0巻 対局中1.0版
    path('tic-tac-toe/vol2.0/playing/ver1.0/<str:kw_room_name>/', PlayingV.render),
]

# EOF O3o2o_1o0g4o0
