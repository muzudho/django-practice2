# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.practice_v1.views.page_the_hello.v1o0 import PageTheHello
from apps1.practice_v1.views.page_to_be_added.v2o0 import PageToBeAdded as PageToBeAdded1
from apps1.practice_v1.views.page_to_be_added.v3o0 import PageToBeAdded as PageToBeAdded2
from apps1.practice_v1.views.login_required.v1o0 import LoggingIn
from apps1.practice_v1.views.login_required.v1o0 import LoggingOut
from apps1.practice_v1.views.button_for_member.v1o0 import ButtonForMember
from apps1.practice_v1.views.user_list.v1o0 import UserListV
from apps1.practice_v1.views.extends_user_list.v1o0 import ExtendsUserListV
from apps1.practice_v1.views.session.v1o0 import SessionV
from apps1.practice_v1.views.debug.v1o0 import DebugV
from apps1.practice_v1.views.prefecture.v1o0 import PrefectureV
from apps1.practice_v1.views.prefecture.v1o0 import PrefectureV
from apps1.practice_v1.views.prefecture.v1o0 import PrefectureV
from apps1.practice_v1.views.prefecture.v1o0 import PrefectureV
from apps1.practice_v1.views.prefecture.v1o0 import PrefectureV
from apps1.practice_v1.views.vuetifies import VuetifyV
from apps1.practice_v1.views.vuetifies import VuetifyV
from apps1.practice_v1.views.vuetifies import VuetifyV
from apps1.practice_v1.views.vuetifies import VuetifyV
from apps1.practice_v1.views.vuetifies import VuetifyV
from apps1.practice_v1.views.vuetifies import VuetifyV
from apps1.practice_v1.views.vuetifies import VuetifyV
from apps1.practice_v1.views.vuetifies import VuetifyV
from apps1.practice_v1.views.vuetifies import VuetifyV
from apps1.practice_v1.views.room.v1o0 import RoomV as RoomVV1o0
from apps1.practice_v1.views.room.v1o0 import RoomV as RoomVV1o0
from apps1.practice_v1.views.room.v1o0 import RoomV as RoomVV1o0
from apps1.practice_v1.views.room.v1o0 import RoomV as RoomVV1o0
from apps1.practice_v1.views.room.v1o0 import RoomV as RoomVV1o0
from apps1.practice_v1.views.my.v1o0 import MyV
from apps1.practice_v1.views.lobby.v1o0 import LobbyV
from apps1.practice_v1.views.auto_reload.v1o0 import AutoReloadV
from apps1.practice_v1.views.auto_redirect.v1o0 import AutoRedirectV


urlpatterns = [
    # o3o2o_1o0g1o0 こんにちわページ
    path('practice/vol1.0/hello2/ver1.0/',
         PageTheHello.render, name='practice_v1_hello2'),

    # O3o2o0g5o1o0 練習ページ １回追加されたページ
    path('practice/vol1.0/page-to-be-added-1/ver1.0/', PageToBeAdded1.render),

    # O3o3o0g4o1o0 練習ページ ２回追加されたページ
    path('practice/vol1.0/page-to-be-added-2/ver1.0/', PageToBeAdded2.render),

    # O8o2o0g4o1o0 ログイン必須ページでログイン中
    path('practice/vol1.0/login-required/ver1.0/', LoggingIn.render),

    # O8o2o0g4o1o0 ログイン必須ページでログアウト中
    path('practice/vol1.0/logout/ver1.0/', LoggingOut.render),

    # O8o3o0g5o1o0 会員にだけ見えるボタンを説明するページ
    path('practice/vol1.0/buttom_for_member/ver1.0/', ButtonForMember.render),

    # O9o1o0g7o1o0 会員一覧
    path('practice/vol1.0/user-list/ver1.0/', UserListV.render),

    # O9o2o0gA12o1o0 （拡張済）会員一覧
    path('practice/vol1.0/extends-user-list/ver1.0/', ExtendsUserListV.render),

    # O9o3o0g7o1o0 アクティブユーザー一覧
    path('practice/vol1.0/active-user-list/ver1.0/', SessionV.render),

    # OA10o2o0g6o1o0 デバッグ用。モデルをダンプ出力
    path('practice/vol1.0/from-object-to-json-str/ver1.0/',
         DebugV.render_model_as_json),

    # OA11o1o0g5o1o0 都道府県
    path('practice/vol1.0/prefectures/ver1.0/',
         PrefectureV.render_list, name='practice_v1_prefectures'),

    # OA11o2o0g5o1o0 都道府県の詳細
    path('practice/vol1.0/prefectures/read/ver1.0/<int:id>/',
         PrefectureV.render_read, name='practice_v1_prefectures_read'),

    # OA11o3o0g5o1o0 都道府県の削除
    path('practice/vol1.0/prefectures/delete/ver1.0/<int:id>/',
         PrefectureV.render_delete, name='practice_v1_prefectures_delete'),

    # OA11o4o0g6o1o0 都道府県の新規作成
    path('practice/vol1.0/prefectures/create/ver1.0/',
         PrefectureV.render_upsert, name='practice_v1_prefectures_create'),

    # OA11o4o0g6o1o0 都道府県の更新
    path('practice/vol1.0/prefectures/update/ver1.0/<int:id>/',
         PrefectureV.render_upsert, name='practice_v1_refectures_update'),

    # OA12o1o0g5o1o0 ビューティファイでハロー
    path('practice/vol1.0/vuetify/hello1/ver1.0/', VuetifyV.render_hello1),

    # OA12o2o0g5o1o0 ビューティファイでデータテーブル１
    path('practice/vol1.0/vuetify/data-table1/ver1.0/',
         VuetifyV.render_data_table1),

    # OA12o3o0g5o1o0 ビューティファイでバリデーション１
    path('practice/vol1.0/vuetify/validation1/ver1.0/',
         VuetifyV.render_validation1),

    # OA13o1o0g6o1o0 ビューティファイでデザート１
    path('practice/vol1.0/vuetify/desserts1/ver1.0/', VuetifyV.render_desserts1),

    # OA13o2o0g7o1o0 ビューティファイでテキストエリア１
    path('practice/vol1.0/vuetify/textarea1/ver1.0/', VuetifyV.render_textarea1),

    # OA13o2o0g7o1o0 ビューティファイでデザート１ . テキストエリア１から
    path('practice/vol1.0/vuetify/desserts1-from-textarea1/ver1.0/',
         VuetifyV.render_desserts1_from_textarea1),

    # OA13o3o0g5o1o0 ビューティファイでJSON形式のデザート１
    path('practice/vol1.0/vuetify/desserts1-as-json/ver1.0/',
         VuetifyV.render_desserts1_as_json),

    # OA13o4o0gA13o1o0 ビューティファイでテキストエリア入力から保存まで . 入力
    path('practice/vol1.0/vuetify/textarea1-to-model/ver1.0/',
         VuetifyV.render_textarea1_to_model),

    # OA13o4o0gA13o1o0 ビューティファイでテキストエリア入力から保存まで . 保存
    path('practice/vol1.0/vuetify/save-desserts1-from-textarea1/ver1.0/',
         VuetifyV.render_save_result_of_desserts1_from_textarea1),

    # OA18o2o0g7o1o0 対局部屋の一覧 v1.0
    path('practice/vol1.0/rooms/ver1.0/',
         RoomVV1o0.render_list, name='practice_v1_rooms'),

    # OA18o3o0g5o1o0 対局部屋の詳細
    path('practice/vol1.0/rooms/read/ver1.0/<int:id>/',
         RoomVV1o0.render_read, name='practice_v1_rooms_read'),

    # OA18o4o0g5o1o0 対局部屋の削除
    path('practice/vol1.0/rooms/delete/ver1.0/<int:id>/',
         RoomVV1o0.render_delete, name='practice_v1_rooms_delete'),

    # OA18o5o0g6o1o0 対局部屋の新規作成
    path('practice/vol1.0/rooms/upsert/ver1.0/',
         RoomVV1o0.render_upsert, name='practice_v1_rooms_create'),

    # OA18o5o0g6o1o0 対局部屋の更新
    path('practice/vol1.0/rooms/upsert/ver1.0/<int:id>/',
         RoomVV1o0.render_upsert, name='practice_v1_rooms_update'),

    # OA19o1o0g5o1o0 練習1.0巻 マイページ1.0版
    path('practice/vol1.0/my/ver1.0/', MyV.render_my, name='practice_v1_my'),

    # OA20o1o0g7o1o0 ロビー ビュー
    path('practice/vol1.0/lobby/ver1.0/',
         LobbyV.render_lobby, name='practice_v1_lobby'),

    # OA21o1o0g7o1o0 自動リロードページ
    path('practice/vol1.0/auto_reload/ver1.0/', AutoReloadV.render_auto_reload),

    # OA21o2o0g6o1o0 自動リダイレクトページ
    path('practice/vol1.0/auto_redirect/ver1.0/',
         AutoRedirectV.render_auto_redirect),
]

# EOF O3o2o_1o0g4o0
