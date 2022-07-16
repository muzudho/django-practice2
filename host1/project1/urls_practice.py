from django.urls import path

# 練習ページ１
from apps1.practice_v1.views.o1.page1 import Page1
#          -----------          -----        -----
#          11                   12           2
#    --------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 練習ページ２
from apps1.practice_v1.views.o1.pages import Page2Patch1
#          -----------          -----        -----------
#          11                   12           2
#    --------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 練習ページ２ パッチ２
from apps1.practice_v1.views.o1.pages import Page2Patch2
#                                                      ^two
#          -----------          -----        -----------
#          11                   12           2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# ログイン必須ページ
from apps1.practice_v1.views.o1 import v_login_required
#    --------------------------        ----------------
#    1                                 2
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き

# 会員用ボタン
from apps1.practice_v1.views.o1.button_for_member import ButtonForMember
#          -----------          -----------------        ---------------
#          11                   12                       2
#    --------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 会員一覧
from apps1.practice_v1.views.o1.user_list import UserListV
#          -----------          ---------        ---------
#          11                   12               2
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# （拡張済）会員一覧
from apps1.practice_v1.views.o1.extends_user_list import ExtendsUserListV
#          -----------          -----------------        ----------------
#          11                   12                       2
#    --------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# アクティブユーザー一覧
from apps1.practice_v1.views.o1.session import SessionV
#          -----------          -------        --------
#          11                   12             2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 都道府県
from apps1.practice_v1.views.o1.prefecture import PrefectureV
#          -----------          ----------        -----------
#          11                   12                2
#    -------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# デバッグ用。モデルをダンプ出力
from apps1.practice_v1.views.o1.debug import DebugV
#          -----------          -----        ------
#          11                   12           2
#    --------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 都道府県ビュー
from apps1.practice_v1.views.o1.vuetify import VuetifyV
#          -----------          -------        --------
#          11                   12             2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 部屋ビュー
from apps1.practice_v1.views.o1.room import RoomV
#          -----------          ----        -----
#          11                   12          2
#    -------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# ロビー ビュー
from apps1.practice_v1.views.o1.lobby import LobbyV
#          -----------          -----        ------
#          11                   12           2
#    --------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# マイページ ビュー
from apps1.practice_v1.views.o1.my import MyV
#          -----------          --        ---
#          11                   12        2
#    -----------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 自動リロード ビュー
from apps1.practice_v1.views.o1.reloader import ReloaderV
#          -----------          --------        ---------
#          11                   12              2
#    -----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 自動リダイレクト ビュー
from apps1.practice_v1.views.o2.redirecter import RedirecterV
#                            ^^.two
#          -----------          ----------        -----------
#          11                   12                2
#    -------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 〇×ゲーム v3 対局申込中
from apps1.tic_tac_toe_v3.views.o1.match_application import MatchApplicationV as TicTacToeV3o0o1MatchApplicationV
#                       ^three
#          --------------          -----------------        -----------------    --------------------------------
#          11                      12                       2                    3
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3 対局中
from apps1.tic_tac_toe_v3.views.o1.playing import PlayingV as TicTacToeV3o0o1PlayingV
#                       ^three
#          --------------          -------        --------    -----------------------
#          11                      12             2           3
#    -------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3.0.3 対局申込中
from apps1.tic_tac_toe_v3.views.o3.match_application import MatchApplicationV as TicTacToeV3o0o3MatchApplicationV
#                       ^three  ^^.three                                                   ^^^^^three.zero.three
#          --------------          -----------------        -----------------    --------------------------------
#          11                      12                       2                    3
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3.0.3 対局中
from apps1.tic_tac_toe_v3.views.o3.playing import PlayingV as TicTacToeV3o0o3PlayingV
#                       ^three  ^^.three                                ^^^^^three.zero.three
#          --------------          -------        --------    -----------------------
#          11                      12             2           3
#    -------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3.0.4 対局申込中
from apps1.tic_tac_toe_v3.views.o4.match_application import MatchApplicationV as TicTacToeV3o0o4MatchApplicationV
#                       ^three  ^^.four                                                    ^^^^^three.zero.four
#          --------------          -----------------        -----------------    --------------------------------
#          11                      12                       2                    3
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3.0.4 対局中
from apps1.tic_tac_toe_v3.views.o4.playing import PlayingV as TicTacToeV3o0o4PlayingV
#                       ^three  ^^.four                                 ^^^^^three.zero.four
#          --------------          -------        --------    -----------------------
#          11                      12             2           3
#    -------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [

    # 練習ページ１
    path('practice/v1/page1', Page1.render, name='page1'),
    #     -----------------   ------------        -----
    #     1                   2                   3
    # 1. 例えば `http://example.com/practice/v1/page1` のようなURLのパスの部分
    #                              -----------------
    # 2. Page1 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page1' %} のような形でURLを取得するのに使える

    # 練習ページ２ パッチ１
    path('practice/v1/page2_patch1', Page2Patch1.render, name='page2_patch1'),
    #     ------------------------   ------------------        ------------
    #     1                          2                         3
    #
    # 1. 例えば `http://example.com/practice/v1/page2_patch1` のようなURLのパスの部分
    #                              ------------------------
    # 2. Page2Patch1 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page2_patch1' %} のような形でURLを取得するのに使える

    # 練習ページ２ パッチ２
    path('practice/v1/page2_patch2', Page2Patch2.render, name='page2_patch2'),
    #                            ^two          ^two                       ^two
    #     ------------------------   ------------------        ------------
    #     1                          2                         3
    #
    # 1. 例えば `http://example.com/practice/v1/page2_patch2` のようなURLのパスの部分
    #                              -------------------------
    # 2. Page2Patch2 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page2_patch2' %} のような形でURLを取得するのに使える

    # ログイン中
    path('practice/v1/login-required', v_login_required.LoggingIn.render,
         # -------------------------   ---------------------------------
         # 1                           2
         name='practice_v1_login_required'),
    #          --------------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/login-required` のような URL のパスの部分
    #                              --------------------------
    # 2. v_login_required.py ファイルの LoggingIn クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_login_required' %} のような形でURLを取得するのに使える

    # ログアウト中
    path('practice/v1/logout', v_login_required.LoggingOut.render,
         # -----------------   ----------------------------------
         # 1                   2
         name='practice_v1_logout'),
    #          ------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/logout` のような URL のパスの部分
    #                              ------------------
    # 2. v_login_required.py ファイルの LoggingOut クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_logout' %} のような形でURLを取得するのに使える

    # 会員にだけ見えるボタンを説明するページ
    path('practice/v1/buttom_for_member/',
         # -----------------------------
         # 1
         ButtonForMember.render),
    #    ----------------------
    #    2
    # 1. 例えば `http://example.com/practice/v1/buttom_for_member/` のような URL のパスの部分
    #                              ------------------------------
    # 2. ButtonForMember クラスの render 静的メソッド

    # 会員一覧
    path('practice/v1/user-list/',
         # ---------------------
         # 1
         UserListV.render, name='practice_v1_user_list'),
    #    ----------------        ---------------------
    #    2                       3
    # 1. 例えば `http://example.com/practice/v1/user-list/` のような URL のパスの部分
    #                              ----------------------
    # 2. UserListV クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_user_list' %} のような形でURLを取得するのに使える

    # （拡張済）会員一覧
    path('practice/v1/extends-user-list/',
         # -----------------------------
         # 1
         ExtendsUserListV.render, name='practice_v1_extends_user_list'),
    #    -----------------------        -----------------------------
    #    2                              3
    # 1. 例えば `http://example.com/practice/v1/extends-user-list/` のような URL のパスの部分
    #                              ------------------------------
    # 2. ExtendsUserListV クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_extends_user_list' %} のような形でURLを取得するのに使える

    # アクティブユーザー一覧
    path('practice/v1/active-user-list/',
         # ----------------------------
         # 1
         SessionV.render, name='practice_v1_active_user_list'),
    #    ---------------        ----------------------------
    #    2                      3
    # 1. 例えば `http://example.com/practice/v1/active-user-list/` のような URL のパスの部分
    #                              -----------------------------
    # 2. UserListV クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_active_user_list' %} のような形でURLを取得するのに使える

    # デバッグ用。モデルをダンプ出力
    path('practice/v1/from-object-to-json-str/',
         # -----------------------------------
         # 1
         DebugV.render_model_as_json, name='practice_v1_from_object_to_json_str'),
    #    ---------------------------        -----------------------------------
    #    2                                  3
    # 1. 例えば `http://example.com/practice/v1/from-object-to-json-str/` のような URL のパスの部分
    #                              ------------------------------------
    # 2. DebugV クラスの render_model_as_json 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_from_object_to_json_str' %} のような形でURLを取得するのに使える

    # 都道府県の一覧
    path('practice/prefectures/', PrefectureV.render_list, name='prefecture_list'),
    #     ---------------------   -----------------------        ---------------
    #     1                       2                              3
    # 1. 例えば `http://example.com/practice/prefectures/` のような URL のパスの部分
    #                              ----------------------
    # 2. PrefectureV クラスの render_list メソッド
    # 3. HTMLテンプレートの中で {% url 'prefecture_list' %} のような形でURLを取得するのに使える

    # 都道府県の詳細
    path('practice/prefectures/read/<int:id>/',
         # ----------------------------------
         # 1
         PrefectureV.render_read, name='prefecture_read'),
    #    -----------------------        ---------------
    #    2                              3
    #
    # 1. 例えば `http://example.com/practice/prefectures/read/<数字列>/` のような URL のパスの部分
    #                              -----------------------------------
    #    数字列は `2.` のメソッドの引数に `=id` と指定することで取得できる
    # 2. PrefectureV クラスの render_read メソッド
    # 3. HTMLテンプレートの中で {% url 'prefecture_read' %} のような形でURLを取得するのに使える

    # 都道府県の削除
    path('practice/prefectures/delete/<int:id>/',
         # ------------------------------------
         # 1
         PrefectureV.render_delete, name='prefecture_delete'),
    #    -------------------------        -----------------
    #    2                                3
    #
    # 1. 例えば `http://example.com/practice/prefectures/delete/<数字列>/` のような URL のパスの部分
    #                              -------------------------------------
    #    数字列は `2.` のメソッドの引数に `=id` と指定することで取得できる
    # 2. PrefectureV クラスの render_delete メソッド
    # 3. HTMLテンプレートの中で {% url 'prefecture_delete' %} のような形でURLを取得するのに使える

    # 都道府県の新規作成
    path('practice/prefecture/create/',
         # --------------------------
         # 1
         PrefectureV.render_upsert, name='prefecture_create'),
    #    -------------------------        -----------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/prefecture/create/` のような URL のパスの部分
    #                              ----------------------------
    # 2. PrefectureV クラスの render_upsert メソッド
    # 3. HTMLテンプレートの中で {% url 'prefecture_create' %} のような形でURLを取得するのに使える

    # 都道府県の更新
    path('practice/prefecture/update/<int:id>/',
         # -----------------------------------
         # 1
         PrefectureV.render_upsert, name='prefecture_update'),
    #    -------------------------        -----------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/prefecture/update/<数字列>/` のような URL のパスの部分
    #                              ------------------------------------
    #    数字列は `2.` のメソッドの引数に `=id` と指定することで取得できる
    # 2. PrefectureV クラスの render_upsert メソッド
    # 3. HTMLテンプレートの中で {% url 'prefecture_update' %} のような形でURLを取得するのに使える

    # ビューティファイでハロー
    path('practice/vuetify/hello1', VuetifyV.render_hello1, name='vuetify_hello1'),
    #     -----------------------   ----------------------        --------------
    #     1                         2                             3
    # 1. 例えば `http://example.com/practice/vuetify/hello1` のような URL のパスの部分
    #                              -----------------------
    # 2. VuetifyV クラスの render_hello1 メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_hello1' %} のような形でURLを取得するのに使える

    # ビューティファイでデータテーブル１
    path('practice/vuetify/data-table1',
         # ---------------------------
         # 1
         VuetifyV.render_data_table1, name='vuetify_data_table1'),
    #    ---------------------------        -------------------
    #    2                                  3
    # 1. 例えば `http://example.com/practice/vuetify/data-table1` のような URL のパスの部分
    #                              ----------------------------
    # 2. VuetifyV クラスの render_data_table1 メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_data_table1' %} のような形でURLを取得するのに使える

    # ビューティファイでバリデーション１
    path('practice/vuetify/validation1',
         # ---------------------------
         # 1
         VuetifyV.render_validation1, name='vuetify_validation1'),
    #    ---------------------------        -------------------
    #    2                                  3
    # 1. 例えば `http://example.com/practice/vuetify/validation1` のような URL のパスの部分
    #                              ----------------------------
    # 2. VuetifyV クラスの render_validation1 メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_validation1' %} のような形でURLを取得するのに使える

    # ビューティファイでデザート１
    path('practice/vuetify/desserts1',
         # -------------------------
         # 1
         VuetifyV.render_desserts1, name='vuetify_desserts1'),
    #    -------------------------        -----------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/vuetify/desserts1` のような URL のパスの部分
    #                              --------------------------
    # 2. VuetifyV クラスの render_desserts1 メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_desserts1' %} のような形でURLを取得するのに使える

    # ビューティファイでテキストエリア１
    path('practice/vuetify/textarea1',
         # -------------------------
         # 1
         VuetifyV.render_textarea1, name='vuetify_textarea1'),
    #    -------------------------        -----------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/vuetify/textarea1` のような URL のパスの部分
    #                              --------------------------
    # 2. VuetifyV クラスの render_textarea1 メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_textarea1' %} のような形でURLを取得するのに使える

    # ビューティファイでデザート１ . テキストエリア１から
    path('practice/vuetify/desserts1-from-textarea1',
         # ----------------------------------------
         # 1
         VuetifyV.render_desserts1_from_textarea1, name='vuetify_desserts1_from_textarea1'),
    #    ----------------------------------------        --------------------------------
    #    2                                               3
    # 1. 例えば `http://example.com/practice/vuetify/desserts1-from-textarea1` のような URL のパスの部分
    #                              -----------------------------------------
    # 2. VuetifyV クラスの render_desserts1_from_textarea1 メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_desserts1_from_textarea1' %} のような形でURLを取得するのに使える

    # ビューティファイでJSON形式のデザート１
    path('practice/vuetify/desserts1-as-json',
         # ---------------------------------
         # 1
         VuetifyV.render_desserts1_as_json, name='vuetify_desserts1_as_json'),
    #    ---------------------------------        -------------------------
    #    2                                        3
    # 1. 例えば `http://example.com/practice/vuetify/textarea1` のような URL のパスの部分
    #                              --------------------------
    # 2. VuetifyV クラスの render_desserts1_as_json メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_desserts1_as_json' %} のような形でURLを取得するのに使える

    # ビューティファイでテキストエリア１ . 保存用
    path('practice/vuetify/textarea1-to-model',
         # ----------------------------------
         # 1
         VuetifyV.render_textarea1_to_model, name='vuetify_textarea1_to_model'),
    #    ----------------------------------        --------------------------
    #    2                                         3
    # 1. 例えば `http://example.com/practice/vuetify/textarea1-to-model` のような URL のパスの部分
    #                              -----------------------------------
    # 2. VuetifyV クラスの render_textarea1_to_model メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_textarea1_to_model' %} のような形でURLを取得するのに使える

    # ビューティファイでデザート１ . テキストエリア１から . 保存付き
    path('practice/vuetify/save-desserts1-from-textarea1',
         # ---------------------------------------------
         # 1
         VuetifyV.render_save_result_of_desserts1_from_textarea1,
         # -----------------------------------------------------
         # 2
         name='vuetify_save_desserts1_from_textarea1'),
    #          -------------------------------------
    #          3
    # 1. 例えば `http://example.com/practice/vuetify/save-desserts1-from-textarea1` のような URL のパスの部分
    #                              ----------------------------------------------
    # 2. VuetifyV クラスの render_save_result_of_desserts1_from_textarea1 メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_save_desserts1_from_textarea1' %} のような形でURLを取得するのに使える

    # 対局部屋の一覧
    path('practice/rooms/', RoomV.render_list, name='practice_rooms_list'),
    #     ---------------   -----------------        -------------------
    #     1                 2                        3
    # 1. 例えば `http://example.com/practice/rooms/` のような URL のパスの部分
    #                              ---------------
    # 2. RoomV クラスの render_list メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_rooms_list' %} のような形でURLを取得するのに使える

    # 対局部屋の詳細
    path('rooms/read/<int:id>/', RoomV.render_read, name='practice_rooms_read'),
    #     --------------------   -----------------        -------------------
    #     1                      2                        3
    # 1. 例えば `http://example.com/rooms/read/<数字列>/` のような URL のパスの部分。
    #                              --------------------
    #    数字列は `2.` の関数の引数 id で取得できる
    # 2. RoomV クラスの render_read メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_rooms_read' %} のような形でURLを取得するのに使える

    # 対局部屋の削除
    path('rooms/delete/<int:id>/', RoomV.render_delete,
         # ---------------------   -------------------
         # 1                       2
         name='practice_rooms_delete'),
    #          ---------------------
    #          3
    # 1. 例えば `http://example.com/rooms/delete/<数字列>/` のような URL のパスの部分。
    #                              ----------------------
    #    数字列は `2.` の関数の引数 id で取得できる
    # 2. RoomV クラスの render_delete メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_rooms_delete' %} のような形でURLを取得するのに使える

    # 対局部屋の新規作成
    path('rooms/create/', RoomV.render_upsert,
         # ------------   -------------------
         # 1              2
         name='practice_rooms_create'),
    #          ---------------------
    #          3
    # 1. 例えば `http://example.com/rooms/create/` のような URL のパスの部分
    #                              -------------
    # 2. RoomV クラスの render_upsert メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_rooms_create' %} のような形でURLを取得するのに使える

    # 対局部屋の更新
    path('rooms/update/<int:id>/', RoomV.render_upsert,
         # ---------------------   -------------------
         # 1                       2
         name='practice_rooms_update'),
    #          ---------------------
    #          3
    # 1. 例えば `http://example.com/rooms/update/<数字列>/` のような URL のパスの部分。
    #                              ----------------------
    #    数字列は `2.` の関数の引数 id で取得できる
    # 2. RoomV クラスの render_upsert メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_rooms_update' %} のような形でURLを取得するのに使える

    # ロビー
    path('practice/lobby/', LobbyV.render_lobby, name='practice_lobby'),
    #     ---------------   -------------------  ---------------------
    #     1                 2                    3
    #
    # 1. 例えば `http://example.com/practice/lobby/` のような URL のパスの部分
    #                              ----------------
    #    数字列は `2.` の関数の引数 id で取得できる
    # 2. LobbyV クラスの render_lobby メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_lobby' %} のような形でURLを取得するのに使える

    # マイ ページ
    path('practice/my/', MyV.render_my, name='practice_my'),
    #     ------------   -------------        -----------
    #     1              2                    3
    #
    # 1. 例えば `http://example.com/practice/my/` のような URL のパスの部分
    #                              ------------
    # 2. MyV クラスの render_my メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_my' %} のような形でURLを取得するのに使える

    # 自動再読込
    path('practice/reloader/', ReloaderV.render_reloader,
         # -----------------   -------------------------
         # 1                            2
         name='practice_reloader'),
    #          -----------------
    #          3
    #
    # 1. 例えば `http://example.com/practice/reloader/` のような URL のパスの部分
    #                              ------------------
    # 2. ReloaderV クラスの render_reloader メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_reloader' %} のような形でURLを取得するのに使える

    # 自動リダイレクト
    path('practice/redirecter/', RedirecterV.render_redirect,
         # -------------------   ---------------------------
         # 1                     2
         name='practice_redirecter'),
    #          -------------------
    #          3
    #
    # 1. 例えば `http://example.com/practice/redirecter/` のような URL のパスの部分
    #                              --------------------
    # 2. RedirecterV クラスの render_redirect メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_redirecter' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3 対局申込中
    path('tic-tac-toe/v3/match-application/', TicTacToeV3o0o1MatchApplicationV.render,
         # --------------------------------   ---------------------------------------
         # 1                                  2
         name='tic_tac_toe_v3_match_application'),
    #          --------------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3/match-application/` のような URL のパスの部分
    #                              ---------------------------------
    # 2. TicTacToeV3o0o1MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3_match_application' %} のような形でURLを取得するのに使える


    # 〇×ゲーム v3 対局中
    path('tic-tac-toe/v3/playing/<str:kw_room_name>/', TicTacToeV3o0o1PlayingV.render,
         # -----------------------------------------   ------------------------------
         # 1                                           2
         name='tic_tac_toe_v3_playing'),
    #          ----------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3/playing/<部屋名>/` のような URL のパスの部分
    #                              --------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3o0o1PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3_playing' %} のような形でURLを取得するのに使える


    # 〇×ゲーム v3.0.3 対局申込中
    path('tic-tac-toe/v3o0o3/match-application/', TicTacToeV3o0o3MatchApplicationV.render,
         # ------------------------------------   ---------------------------------------
         # 1                                      2
         name='tic_tac_toe_v3o0o3_match_application'),
    #          ------------------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3o0o3/match-application/` のような URL のパスの部分
    #                              -------------------------------------
    # 2. TicTacToeV3o0o3MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3o0o3_match_application' %} のような形でURLを取得するのに使える


    # 〇×ゲーム v3.0.3 対局中
    path('tic-tac-toe/v3o0o3/playing/<str:kw_room_name>/', TicTacToeV3o0o3PlayingV.render,
         # ---------------------------------------------   ------------------------------
         # 1                                               2
         name='tic_tac_toe_v3o0o3_playing'),
    #          --------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3o0o3/playing/<部屋名>/` のような URL のパスの部分
    #                              ------------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3o0o3PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3o0o3_playing' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3.0.4 対局申込中
    path('tic-tac-toe/v3o0o4/match-application/', TicTacToeV3o0o4MatchApplicationV.render,
         # ------------------------------------   ---------------------------------------
         # 1                                      2
         name='tic_tac_toe_v3o0o4_match_application'),
    #          ------------------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3o0o4/match-application/` のような URL のパスの部分
    #                              -------------------------------------
    # 2. TicTacToeV3o0o4MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3o0o4_match_application' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3.0.4 対局中
    path('tic-tac-toe/v3o0o4/playing/<str:kw_room_name>/', TicTacToeV3o0o4PlayingV.render,
         # ---------------------------------------------   ------------------------------
         # 1                                               2
         name='tic_tac_toe_v3o0o4_playing'),
    #          --------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3o0o4/playing/<部屋名>/` のような URL のパスの部分
    #                              ------------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3o0o4PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3o0o4_playing' %} のような形でURLを取得するのに使える
]
