# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.tic_tac_toe_vol2o0.views.think.engine_manual.ver1o0 import EngineManual
from apps1.tic_tac_toe_vol2o0.views.msg.c2s_json_gen.ver1o0 import C2sJsonGenView as C2sJsonGenViewV1o0
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.ver1o0 import S2cJsonGenView as S2cJsonGenViewV1o0
from apps1.tic_tac_toe_vol2o0.views.gui.match_application.ver1o0 import MatchApplicationV
from apps1.tic_tac_toe_vol2o0.views.gui.playing.ver1o0 import PlayingV
from apps1.practice_v1.views.room.v1o0 import RoomV as RoomVV1o0
from apps1.practice_v1.views.room.v1o0 import RoomV as RoomVV1o0
from apps1.practice_v1.views.room.v1o0 import RoomV as RoomVV1o0
from apps1.practice_v1.views.room.v1o0 import RoomV as RoomVV1o0
from apps1.practice_v1.views.room.v1o0 import RoomV as RoomVV1o0


urlpatterns = [
    # OA16o2o0gA16o1o0 〇×ゲーム v2 思考エンジン手動
    path('tic-tac-toe/vol2.0/ver1.0/engine-manual/', EngineManual.render),

    # OA16o3o_1o0g4o1o0 〇×ゲーム v2 C2S JSON ジェネレーター
    path('tic-tac-toe/vol2.0/ver1.0/c2s-json-gen/', C2sJsonGenViewV1o0.render),

    # OA16o3o_2o0g5o1o0 〇×ゲーム v2 S2C JSON ジェネレーター
    path('tic-tac-toe/vol2.0/ver1.0/s2c-json-gen/', S2cJsonGenViewV1o0.render),

    # OA16o3o0gA15o1o0 〇×ゲーム v2 対局申込ページ
    path('tic-tac-toe/vol2.0/ver1.0/match-application/', MatchApplicationV.render),

    # OA16o3o0gA15o1o0 〇×ゲーム v2 対局中ページ
    path('tic-tac-toe/vol2.0/ver1.0/playing/<str:kw_room_name>/', PlayingV.render),

    # OA18o2o0g7o1o0 対局部屋の一覧 v1.0
    path('practice/v1/rooms/', RoomVV1o0.render_list, name='practice_v1_rooms'),

    # OA18o3o0g5o1o0 対局部屋の詳細
    path('practice/v1/rooms/read/<int:id>/', RoomVV1o0.render_read, name='practice_v1_rooms_read'),

    # OA18o4o0g5o1o0 対局部屋の削除
    path('practice/v1/rooms/delete/<int:id>/', RoomVV1o0.render_delete, name='practice_v1_rooms_delete'),

    # OA18o5o0g6o1o0 対局部屋の新規作成
    path('practice/v1/rooms/upsert/', RoomVV1o0.render_upsert, name='practice_v1_rooms_create'),

    # OA18o5o0g6o1o0 対局部屋の更新
    path('practice/v1/rooms/upsert/<int:id>/', RoomVV1o0.render_upsert, name='practice_v1_rooms_update'),
]

# EOF O3o2o_1o0g4o0
