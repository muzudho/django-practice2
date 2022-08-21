# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.tic_tac_toe_v2.views.think.engine_manual.v1o0 import EngineManual
from apps1.tic_tac_toe_v2.views.msg.c2s_json_gen.v1o0 import C2sJsonGenView as C2sJsonGenViewV1o0
from apps1.tic_tac_toe_v2.views.msg.s2c_json_gen.v1o0 import S2cJsonGenView as S2cJsonGenViewV1o0
from apps1.tic_tac_toe_v2.views.gui.match_application.v1o0 import MatchApplicationV
from apps1.tic_tac_toe_v2.views.gui.playing.v1o0 import PlayingV


urlpatterns = [
    # OA16o2o0gA16o1o0 〇×ゲーム v2 思考エンジン手動
    path('tic-tac-toe/v2/engine-manual/', EngineManual.render, name='practice_v1_vuetify_textarea1_to_model'),

    # OA16o3o_1o0g4o1o0 〇×ゲーム v2 C2S JSON ジェネレーター
    path('tic-tac-toe/v2/c2s-json-gen/', C2sJsonGenViewV1o0.render, name='practice_v1_vuetify_textarea1_to_model'),

    # OA16o3o_2o0g5o1o0 〇×ゲーム v2 S2C JSON ジェネレーター
    path('tic-tac-toe/v2/s2c-json-gen/', S2cJsonGenViewV1o0.render, name='practice_v1_vuetify_textarea1_to_model'),

    # OA16o3o0gA15o1o0 〇×ゲーム v2 対局申込ページ
    path('tic-tac-toe/v2/match-application/', MatchApplicationV.render, name='practice_v1_vuetify_textarea1_to_model'),

    # OA16o3o0gA15o1o0 〇×ゲーム v2 対局中ページ
    path('tic-tac-toe/v2/playing/<str:kw_room_name>/', PlayingV.render, name='practice_v1_vuetify_textarea1_to_model'),
]

# EOF O3o2o_1o0g4o0
