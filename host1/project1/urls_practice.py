from django.urls import path

# おはようページ
from apps1.practice_v1.views.o1o0.page_the_hello import PageTheHello
#          -----------            --------------        ------------
#          11                     12                    2
#    -------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 練習ページ １回追加されたページ
from apps1.practice_v1.views.o2o0.page_to_be_added import PageToBeAdded as PageToBeAdded1
#          -----------            ----------------        -------------    --------------
#          11                     12                      2                3
#    ---------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 練習ページ ２回追加されたページ
from apps1.practice_v1.views.o3o0.page_to_be_added import PageToBeAdded as PageToBeAdded2
#                             ^three
#          -----------            ----------------        -------------    --------------
#          11                     12                      2                3
#    ---------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# ログイン必須ページ
from apps1.practice_v1.views.o1o0.login_required import LoggingIn, LoggingOut
#          -----------            --------------        ---------------------
#          11                     12                    2
#    -------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 会員用ボタン
from apps1.practice_v1.views.o1o0.button_for_member import ButtonForMember
#          -----------            -----------------        ---------------
#          11                     12                       2
#    ----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 会員一覧
from apps1.practice_v1.views.o1o0.user_list import UserListV
#          -----------            ---------        ---------
#          11                     12               2
#    --------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# （拡張済）会員一覧
from apps1.practice_v1.views.o1o0.extends_user_list import ExtendsUserListV
#          -----------            -----------------        ----------------
#          11                     12                       2
#    ----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# アクティブユーザー一覧
from apps1.practice_v1.views.o1o0.session import SessionV
#          -----------            -------        --------
#          11                     12             2
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 都道府県
from apps1.practice_v1.views.o1o0.prefecture import PrefectureV
#          -----------            ----------        -----------
#          11                     12                2
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# デバッグ用。モデルをダンプ出力
from apps1.practice_v1.views.o1o0.debug import DebugV
#          -----------            -----        ------
#          11                     12           2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 都道府県ビュー
from apps1.practice_v1.views.o1o0.vuetify import VuetifyV
#          -----------            -------        --------
#          11                     12             2
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 部屋ビュー
from apps1.practice_v1.views.o1o0.room import RoomV
#          -----------            ----        -----
#          11                     12          2
#    ---------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# ロビー ビュー
from apps1.practice_v1.views.o1o0.lobby import LobbyV
#          -----------            -----        ------
#          11                     12           2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# マイページ ビュー
from apps1.practice_v1.views.o1o0.my import MyV
#          -----------            --        ---
#          11                     12        2
#    -------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 自動リロード ビュー
from apps1.practice_v1.views.o1o0.auto_reload import AutoReloadV
#          -----------            -----------        -----------
#          11                     12                 2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 自動リダイレクト ビュー
from apps1.practice_v1.views.o2o0.auto_redirect import AutoRedirectV
#                             ^two
#          -----------            -------------        -------------
#          11                     12                   2
#    ------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 〇×ゲーム v3.1 対局申込中
from apps1.tic_tac_toe_v3.views.o1o0.match_application import MatchApplicationV as TicTacToeV3g1o0MatchApplicationV
#                       ^three   ^one
#          --------------            -----------------        -----------------    --------------------------------
#          11                        12                       2                    3
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3.1 対局中
from apps1.tic_tac_toe_v3.views.o1o0.playing import PlayingV as TicTacToeV3g1o0PlayingV
#                       ^three   ^one
#          --------------            -------        --------    -----------------------
#          11                        12             2           3
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3.2 対局申込中
from apps1.tic_tac_toe_v3.views.o2o0.match_application import MatchApplicationV as TicTacToeV3g2o0MatchApplicationV
#                       ^three   ^two
#          --------------            -----------------        -----------------    --------------------------------
#          11                        12                       2                    3
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3.3 対局申込中
from apps1.tic_tac_toe_v3.views.o3o0.match_application import MatchApplicationV as TicTacToeV3g3o0MatchApplicationV
#                       ^three   ^three
#          --------------            -----------------        -----------------    --------------------------------
#          11                        12                       2                    3
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3.3 対局中
from apps1.tic_tac_toe_v3.views.o3o0.playing import PlayingV as TicTacToeV3g3o0PlayingV
#                       ^three   ^three
#          ----------------          -------        --------    -----------------------
#          11                        12             2           3
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3.4 対局申込中
from apps1.tic_tac_toe_v3.views.o4o0.match_application import MatchApplicationV as TicTacToeV3g4o0MatchApplicationV
#                       ^three   ^four
#          --------------            -----------------        -----------------    --------------------------------
#          11                        12                       2                    3
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3.4 対局中
from apps1.tic_tac_toe_v3.views.o4o0.playing import PlayingV as TicTacToeV3g4o0PlayingV
#                       ^three   ^four
#          --------------            -------        --------    -----------------------
#          11                        12             2           3
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [

    # おはようページ
    path('practice/v1/page-the-hello',
         # -------------------------
         # 1
         PageTheHello.render, name='page_the_hello'),
    #    -------------------        --------------
    #    2                          3
    # 1. 例えば `http://example.com/practice/v1/page-the-hello` のようなURLのパスの部分
    #                              --------------------------
    # 2. PageTheHello クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page_the_hello' %} のような形でURLを取得するのに使える

    # 練習ページ２ １回追加されたページ
    path('practice/v1/page-to-be-added-1',
         # -----------------------------
         # 1
         PageToBeAdded1.render, name='page_to_be_added_1'),
    #    ---------------------        ------------------
    #    2                            3
    #
    # 1. 例えば `http://example.com/practice/v1/page-to-be-added-1` のようなURLのパスの部分
    #                              ------------------------------
    # 2. PageToBeAdded1 (別名)クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page_to_be_added_1' %} のような形でURLを取得するのに使える

    # 練習ページ２ ２回追加されたページ
    path('practice/v1/page-to-be-added-2',
         # -----------------------------
         # 1
         PageToBeAdded2.render, name='page_to_be_added_2'),
    #    ---------------------        ------------------
    #    2                            3
    #
    # 1. 例えば `http://example.com/practice/v1/page-to-be-added-2` のようなURLのパスの部分
    #                              ------------------------------
    # 2. PageToBeAdded2 (別名)クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page_to_be_added_2' %} のような形でURLを取得するのに使える

    # ログイン中
    path('practice/v1/login-required', LoggingIn.render,
         # -------------------------   ----------------
         # 1                           2
         name='practice_v1_login_required'),
    #          --------------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/login-required` のような URL のパスの部分
    #                              --------------------------
    # 2. LoggingIn クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_login_required' %} のような形でURLを取得するのに使える

    # ログアウト中
    path('practice/v1/logout', LoggingOut.render,
         # -----------------   -----------------
         # 1                   2
         name='practice_v1_logout'),
    #          ------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/logout` のような URL のパスの部分
    #                              ------------------
    # 2. LoggingOut クラスの render 静的メソッド
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
    path('practice/v1/prefectures/',
         # -----------------------
         # 1
         PrefectureV.render_list, name='practice_v1_prefectures'),
    #    -----------------------        -----------------------
    #    2                              3
    # 1. 例えば `http://example.com/practice/v1/prefectures/` のような URL のパスの部分
    #                              ------------------------
    # 2. PrefectureV クラスの render_list 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_prefectures' %} のような形でURLを取得するのに使える

    # 都道府県の詳細
    path('practice/v1/prefectures/read/<int:id>/',
         # -------------------------------------
         # 1
         PrefectureV.render_read, name='practice_v1_prefectures_read'),
    #    -----------------------        ----------------------------
    #    2                              3
    #
    # 1. 例えば `http://example.com/practice/v1/prefectures/read/<数字列>/` のような URL のパスの部分
    #                              --------------------------------------
    #    数字列は `2.` のメソッドの引数 id で取得できる
    # 2. PrefectureV クラスの render_read 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_prefectures_read' %} のような形でURLを取得するのに使える

    # 都道府県の削除
    path('practice/v1/prefectures/delete/<int:id>/',
         # ---------------------------------------
         # 1
         PrefectureV.render_delete, name='practice_v1_prefectures_delete'),
    #    -------------------------        ------------------------------
    #    2                                3
    #
    # 1. 例えば `http://example.com/practice/v1/prefectures/delete/<数字列>/` のような URL のパスの部分
    #                              ----------------------------------------
    #    数字列は `2.` のメソッドの引数 id で取得できる
    # 2. PrefectureV クラスの render_delete メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_prefectures_delete' %} のような形でURLを取得するのに使える

    # 都道府県の新規作成
    path('practice/v1/prefectures/create/',
         # ------------------------------
         # 1
         PrefectureV.render_upsert, name='practice_v1_prefectures_create'),
    #    -------------------------        ------------------------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/v1/prefectures/create/` のような URL のパスの部分
    #                              -------------------------------
    # 2. PrefectureV クラスの render_upsert 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_prefectures_create' %} のような形でURLを取得するのに使える

    # 都道府県の更新
    path('practice/v1/prefectures/update/<int:id>/',
         # ---------------------------------------
         # 1
         PrefectureV.render_upsert, name='practice_v1_refectures_update'),
    #    -------------------------        -----------------------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/v1/prefectures/update/<数字列>/` のような URL のパスの部分
    #                              ----------------------------------------
    #    数字列は `2.` のメソッドの引数 id で取得できる
    # 2. PrefectureV クラスの render_upsert 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_refectures_update' %} のような形でURLを取得するのに使える

    # ビューティファイでハロー
    path('practice/v1/vuetify/hello1', VuetifyV.render_hello1,
         # -------------------------   ----------------------
         # 1                           2
         name='practice_v1_vuetify_hello1'),
    #          --------------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/vuetify/hello1` のような URL のパスの部分
    #                              --------------------------
    # 2. VuetifyV クラスの render_hello1 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_hello1' %} のような形でURLを取得するのに使える

    # ビューティファイでデータテーブル１
    path('practice/v1/vuetify/data-table1',
         # ------------------------------
         # 1
         VuetifyV.render_data_table1, name='practice_v1_vuetify_data_table1'),
    #    ---------------------------        -------------------------------
    #    2                                  3
    # 1. 例えば `http://example.com/practice/v1/vuetify/data-table1` のような URL のパスの部分
    #                              -------------------------------
    # 2. VuetifyV クラスの render_data_table1 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_data_table1' %} のような形でURLを取得するのに使える

    # ビューティファイでバリデーション１
    path('practice/v1/vuetify/validation1',
         # ------------------------------
         # 1
         VuetifyV.render_validation1, name='practice_v1_vuetify_validation1'),
    #    ---------------------------        -------------------------------
    #    2                                  3
    # 1. 例えば `http://example.com/practice/v1/vuetify/validation1` のような URL のパスの部分
    #                              -------------------------------
    # 2. VuetifyV クラスの render_validation1 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_validation1' %} のような形でURLを取得するのに使える

    # ビューティファイでデザート１
    path('practice/v1/vuetify/desserts1',
         # ----------------------------
         # 1
         VuetifyV.render_desserts1, name='practice_v1_vuetify_desserts1'),
    #    -------------------------        -----------------------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/v1/vuetify/desserts1` のような URL のパスの部分
    #                              -----------------------------
    # 2. VuetifyV クラスの render_desserts1 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_desserts1' %} のような形でURLを取得するのに使える

    # ビューティファイでテキストエリア１
    path('practice/v1/vuetify/textarea1',
         # ----------------------------
         # 1
         VuetifyV.render_textarea1, name='practice_v1_vuetify_textarea1'),
    #    -------------------------        -----------------------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/v1/vuetify/textarea1` のような URL のパスの部分
    #                              -----------------------------
    # 2. VuetifyV クラスの render_textarea1 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_textarea1' %} のような形でURLを取得するのに使える

    # ビューティファイでデザート１ . テキストエリア１から
    path('practice/v1/vuetify/desserts1-from-textarea1',
         # -------------------------------------------
         # 1
         VuetifyV.render_desserts1_from_textarea1, name='practice_v1_vuetify_desserts1_from_textarea1'),
    #    ----------------------------------------        --------------------------------------------
    #    2                                               3
    # 1. 例えば `http://example.com/practice/v1/vuetify/desserts1-from-textarea1` のような URL のパスの部分
    #                              ---------------------------------------------
    # 2. VuetifyV クラスの render_desserts1_from_textarea1 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_desserts1_from_textarea1' %} のような形でURLを取得するのに使える

    # ビューティファイでJSON形式のデザート１
    path('practice/v1/vuetify/desserts1-as-json',
         # ------------------------------------
         # 1
         VuetifyV.render_desserts1_as_json, name='practice_v1_vuetify_desserts1_as_json'),
    #    ---------------------------------        -------------------------------------
    #    2                                        3
    # 1. 例えば `http://example.com/practice/v1/vuetify/desserts1-as-json` のような URL のパスの部分
    #                              -------------------------------------
    # 2. VuetifyV クラスの render_desserts1_as_json 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_desserts1_as_json' %} のような形でURLを取得するのに使える

    # ビューティファイでテキストエリア１ . 保存用
    path('practice/v1/vuetify/textarea1-to-model',
         # -------------------------------------
         # 1
         VuetifyV.render_textarea1_to_model, name='practice_v1_vuetify_textarea1_to_model'),
    #    ----------------------------------        --------------------------------------
    #    2                                         3
    # 1. 例えば `http://example.com/practice/v1/vuetify/textarea1-to-model` のような URL のパスの部分
    #                              --------------------------------------
    # 2. VuetifyV クラスの render_textarea1_to_model 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_textarea1_to_model' %} のような形でURLを取得するのに使える

    # ビューティファイでデザート１ . テキストエリア１から . 保存付き
    path('practice/v1/vuetify/save-desserts1-from-textarea1',
         # ------------------------------------------------
         # 1
         VuetifyV.render_save_result_of_desserts1_from_textarea1,
         # -----------------------------------------------------
         # 2
         name='vuetify_save_desserts1_from_textarea1'),
    #          -------------------------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/vuetify/save-desserts1-from-textarea1` のような URL のパスの部分
    #                              -------------------------------------------------
    # 2. VuetifyV クラスの render_save_result_of_desserts1_from_textarea1 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_save_desserts1_from_textarea1' %} のような形でURLを取得するのに使える

    # 対局部屋の一覧
    path('practice/v1/rooms/', RoomV.render_list, name='practice_v1_rooms'),
    #     ------------------   -----------------        -----------------
    #     1                    2                        3
    # 1. 例えば `http://example.com/practice/v1/rooms/` のような URL のパスの部分
    #                              ------------------
    # 2. RoomV クラスの render_list 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_rooms' %} のような形でURLを取得するのに使える

    # 対局部屋の詳細
    path('practice/v1/rooms/read/<int:id>/',
         # -------------------------------
         # 1
         RoomV.render_read, name='practice_v1_rooms_read'),
    #    -----------------        ----------------------
    #    2                        3
    # 1. 例えば `http://example.com/practice/v1/rooms/read/<数字列>/` のような URL のパスの部分。
    #                              --------------------------------
    #    数字列は `2.` の関数の引数 id で取得できる
    # 2. RoomV クラスの render_read 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_rooms_read' %} のような形でURLを取得するのに使える

    # 対局部屋の削除
    path('practice/v1/rooms/delete/<int:id>/', RoomV.render_delete,
         # ---------------------------------   -------------------
         # 1                                   2
         name='practice_v1_rooms_delete'),
    #          ------------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/rooms/delete/<数字列>/` のような URL のパスの部分。
    #                              ----------------------------------
    #    数字列は `2.` の関数の引数 id で取得できる
    # 2. RoomV クラスの render_delete 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_rooms_delete' %} のような形でURLを取得するのに使える

    # 対局部屋の新規作成
    path('practice/v1/rooms/upsert/', RoomV.render_upsert,
         # ------------------------   -------------------
         # 1                          2
         name='practice_v1_rooms_create'),
    #          ------------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/rooms/upsert/` のような URL のパスの部分
    #                              -------------------------
    # 2. RoomV クラスの render_upsert 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_rooms_create' %} のような形でURLを取得するのに使える

    # 対局部屋の更新
    path('practice/v1/rooms/upsert/<int:id>/', RoomV.render_upsert,
         # ---------------------------------   -------------------
         # 1                                   2
         name='practice_v1_rooms_update'),
    #          ------------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/rooms/upsert/<数字列>/` のような URL のパスの部分
    #                              ----------------------------------
    #    数字列は `2.` の関数の引数 id で取得できる
    # 2. RoomV クラスの render_upsert 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_rooms_update' %} のような形でURLを取得するのに使える

    # ロビー
    path('practice/v1/lobby/', LobbyV.render_lobby, name='practice_v1_lobby'),
    #     ------------------   -------------------        -----------------
    #     1                    2                          3
    # 1. 例えば `http://example.com/practice/v1/lobby/` のような URL のパスの部分
    #                              ------------------
    #    数字列は `2.` の関数の引数 id で取得できる
    # 2. LobbyV クラスの render_lobby 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_lobby' %} のような形でURLを取得するのに使える

    # マイ ページ
    path('practice/v1/my/', MyV.render_my, name='practice_v1_my'),
    #     ---------------   -------------        --------------
    #     1                 2                    3
    #
    # 1. 例えば `http://example.com/practice/v1/my/` のような URL のパスの部分
    #                              ---------------
    # 2. MyV クラスの render_my 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_my' %} のような形でURLを取得するのに使える

    # 自動再読込
    path('practice/v1/auto_reload/', AutoReloadV.render_auto_reload,
         # -----------------------   ------------------------------
         # 1                         2
         name='practice_v1_auto_reload'),
    #          -----------------------
    #          3
    #
    # 1. 例えば `http://example.com/practice/v1/auto_reload/` のような URL のパスの部分
    #                              ------------------------
    # 2. AutoReloadV クラスの render_auto_reload 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_auto_reload' %} のような形でURLを取得するのに使える

    # 自動リダイレクト
    path('practice/v1/auto_redirect/', AutoRedirectV.render_auto_redirect,
         # -------------------------   ----------------------------------
         # 1                           2
         name='practice_v1_auto_redirect'),
    #          -------------------------
    #          3
    #
    # 1. 例えば `http://example.com/practice/v1/auto_redirect/` のような URL のパスの部分
    #                              --------------------------
    # 2. AutoRedirectV クラスの render_auto_redirect メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_auto_redirect' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3.1 対局申込中
    path('tic-tac-toe/v3.1/match-application/', TicTacToeV3g1o0MatchApplicationV.render,
         # ----------------------------------   ---------------------------------------
         # 1                                    2
         name='tic_tac_toe_v3g1o0_match_application'),
    #          ------------------------------------
    #          3
    # 1. 例えば `http://example.com/tic-tac-toe/v3.1/match-application/` のような URL のパスの部分
    #                              -----------------------------------
    # 2. TicTacToeV3g1o0MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g1o0_match_application' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3.1 対局中
    path('tic-tac-toe/v3.1/playing/<str:kw_room_name>/', TicTacToeV3g1o0PlayingV.render,
         # -------------------------------------------   ------------------------------
         # 1                                             2
         name='tic_tac_toe_v3g1o0_playing'),
    #          --------------------------
    #          3
    # 1. 例えば `http://example.com/tic-tac-toe/v3.1/playing/<部屋名>/` のような URL のパスの部分
    #                              ----------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3g1o0PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g1o0_playing' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3.2 対局申込中
    path('tic-tac-toe/v3.2/match-application/', TicTacToeV3g2o0MatchApplicationV.render,
         # ----------------------------------   ---------------------------------------
         # 1                                    2
         name='tic_tac_toe_v3g2o0_match_application'),
    #          ------------------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3.2/match-application/` のような URL のパスの部分
    #                              -------------------------------------
    # 2. TicTacToeV3g2o0MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g2o0_match_application' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3.3 対局申込中
    path('tic-tac-toe/v3.3/match-application/', TicTacToeV3g3o0MatchApplicationV.render,
         # ----------------------------------   ---------------------------------------
         # 1                                    2
         name='tic_tac_toe_v3g3o0_match_application'),
    #          --------------------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3.3/match-application/` のような URL のパスの部分
    #                              -----------------------------------
    # 2. TicTacToeV3g3o0MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g3o0_match_application' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3.3 対局中
    path('tic-tac-toe/v3.3/playing/<str:kw_room_name>/', TicTacToeV3g3o0PlayingV.render,
         # -------------------------------------------   ------------------------------
         # 1                                             2
         name='tic_tac_toe_v3g3o0_playing'),
    #          ----------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3.3/playing/<部屋名>/` のような URL のパスの部分
    #                              ----------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3g3o0PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g3o0_playing' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3.4 対局申込中
    path('tic-tac-toe/v3.4/match-application/', TicTacToeV3g4o0MatchApplicationV.render,
         # ----------------------------------   ---------------------------------------
         # 1                                    2
         name='tic_tac_toe_v3g4o0_match_application'),
    #          --------------------------------------
    #          3
    # 1. 例えば `http://example.com/tic-tac-toe/v3.4/match-application/` のような URL のパスの部分
    #                              -----------------------------------
    # 2. TicTacToeV3g4o0MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g4o0_match_application' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3.4 対局中
    path('tic-tac-toe/v3.4/playing/<str:kw_room_name>/', TicTacToeV3g4o0PlayingV.render,
         # -------------------------------------------   ------------------------------
         # 1                                             2
         name='tic_tac_toe_v3g4o0_playing'),
    #          ----------------------------
    #          3
    # 1. 例えば `http://example.com/tic-tac-toe/v3.4/playing/<部屋名>/` のような URL のパスの部分
    #                              ----------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3g4o0PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g4o0_playing' %} のような形でURLを取得するのに使える
]
