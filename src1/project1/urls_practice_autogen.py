# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.practice_v1.views.page_the_hello.v1o0 import PageTheHello
from apps1.practice_v1.views.page_to_be_added.v2o0 import PageToBeAdded as PageToBeAdded1
from apps1.practice_v1.views.page_to_be_added.v3o0 import PageToBeAdded as PageToBeAdded2
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
from apps1.practice_v1.views.my.v1o0 import MyV
from apps1.practice_v1.views.lobby.v1o0 import LobbyV
from apps1.practice_v1.views.auto_reload.v1o0 import AutoReloadV
from apps1.practice_v1.views.auto_redirect.v1o0 import AutoRedirectV


urlpatterns = [
    # o3o2o_1o0g1o0 こんにちわページ
    path('practice/v1/hello2', PageTheHello.render, name='practice_v1_hello2'),

    # O3o2o0g5o1o0 練習ページ １回追加されたページ
    path('practice/v1/page-to-be-added-1', PageToBeAdded1.render, name='page_to_be_added_1'),

    # O3o3o0g4o1o0 練習ページ ２回追加されたページ
    path('practice/v1/page-to-be-added-2', PageToBeAdded2.render, name='page_to_be_added_2'),

    # O8o3o0g5o1o0 会員にだけ見えるボタンを説明するページ
    path('practice/v1/buttom_for_member/', ButtonForMember.render),

    # O9o1o0g7o1o0 会員一覧
    path('practice/v1/user-list/', UserListV.render, name='practice_v1_user_list'),

    # O9o2o0gA12o1o0 （拡張済）会員一覧
    path('practice/v1/extends-user-list/', ExtendsUserListV.render, name='practice_v1_extends_user_list'),

    # O9o3o0g7o1o0 アクティブユーザー一覧
    path('practice/v1/active-user-list/', SessionV.render, name='practice_v1_active_user_list'),

    # OA10o2o0g6o1o0 デバッグ用。モデルをダンプ出力
    path('practice/v1/from-object-to-json-str/', DebugV.render_model_as_json, name='practice_v1_from_object_to_json_str'),

    # OA11o1o0g5o1o0 都道府県
    path('practice/v1/prefectures/', PrefectureV.render_list, name='practice_v1_prefectures'),

    # OA11o2o0g5o1o0 都道府県の詳細
    path('practice/v1/prefectures/read/<int:id>/', PrefectureV.render_read, name='practice_v1_prefectures_read'),

    # OA11o3o0g5o1o0 都道府県の削除
    path('practice/v1/prefectures/delete/<int:id>/', PrefectureV.render_delete, name='practice_v1_prefectures_delete'),

    # OA11o4o0g6o1o0 都道府県の新規作成
    path('practice/v1/prefectures/create/', PrefectureV.render_upsert, name='practice_v1_prefectures_create'),

    # OA11o4o0g6o1o0 都道府県の更新
    path('practice/v1/prefectures/update/<int:id>/', PrefectureV.render_upsert, name='practice_v1_refectures_update'),

    # OA12o1o0g5o1o0 ビューティファイでハロー
    path('practice/v1/vuetify/hello1', VuetifyV.render_hello1, name='practice_v1_vuetify_hello1'),

    # OA12o2o0g5o1o0 ビューティファイでデータテーブル１
    path('practice/v1/vuetify/data-table1', VuetifyV.render_data_table1, name='practice_v1_vuetify_data_table1'),

    # OA12o3o0g5o1o0 ビューティファイでバリデーション１
    path('practice/v1/vuetify/validation1', VuetifyV.render_validation1, name='practice_v1_vuetify_validation1'),

    # OA13o1o0g6o1o0 ビューティファイでデザート１
    path('practice/v1/vuetify/desserts1', VuetifyV.render_desserts1, name='practice_v1_vuetify_desserts1'),

    # OA13o2o0g7o1o0 ビューティファイでテキストエリア１
    path('practice/v1/vuetify/textarea1', VuetifyV.render_textarea1, name='practice_v1_vuetify_textarea1'),

    # OA13o2o0g7o1o0 ビューティファイでデザート１ . テキストエリア１から
    path('practice/v1/vuetify/desserts1-from-textarea1', VuetifyV.render_desserts1_from_textarea1, name='practice_v1_vuetify_desserts1_from_textarea1'),

    # OA13o3o0g5o1o0 ビューティファイでJSON形式のデザート１
    path('practice/v1/vuetify/desserts1-as-json', VuetifyV.render_desserts1_as_json, name='practice_v1_vuetify_desserts1_as_json'),

    # OA13o4o0gA13o1o0 ビューティファイでテキストエリア入力から保存まで . 入力
    path('practice/v1/vuetify/textarea1-to-model', VuetifyV.render_textarea1_to_model, name='practice_v1_vuetify_textarea1_to_model'),

    # OA13o4o0gA13o1o0 ビューティファイでテキストエリア入力から保存まで . 保存
    path('practice/v1/vuetify/save-desserts1-from-textarea1', VuetifyV.render_save_result_of_desserts1_from_textarea1, name='vuetify_save_desserts1_from_textarea1'),

    # OA19o1o0g5o1o0 マイページ ビュー
    path('practice/v1/my/', MyV.render_my, name='practice_v1_my'),

    # OA20o1o0g7o1o0 ロビー ビュー
    path('practice/v1/lobby/', LobbyV.render_lobby, name='practice_v1_lobby'),

    # OA21o1o0g7o1o0 自動リロードページ
    path('practice/v1/auto_reload/', AutoReloadV.render_auto_reload, name='practice_v1_auto_reload'),

    # OA21o2o0g6o1o0 自動リダイレクトページ
    path('practice/v1/auto_redirect/', AutoRedirectV.render_auto_redirect, name='practice_v1_auto_redirect'),
]

# EOF O3o2o_1o0g4o0
