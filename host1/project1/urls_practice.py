from django.urls import path

from apps1.practice.views.v0o0o1.pages import Page1
#    --------------------------- -----        -----
#    1                           2            3
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き
# 3. クラス名

from apps1.practice.views.v0o0o1.pages import Page2Patch1
#    --------------------------- -----        -----------
#    1                           2            3
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き
# 3. クラス名

from apps1.practice.views.v0o0o1.pages import Page2Patch2
#                                                       ^two
#    --------------------------- -----        -----------
#    1                           2            3
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き
# 3. クラス名

from apps1.practice.views.v0o0o1 import v_login_required
#    ---------------------------        ----------------
#    1                                  2
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き

from apps1.practice.views.v0o0o1.prefecture import PrefectureV
#    ----- -------- -----------------------        -----------
#    1     2        3                              4
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

from apps1.practice.views.v0o0o1.vuetify import VuetifyV
#    ----- -------- --------------------        --------
#    1     2        3                           4
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


urlpatterns = [

    path('practice/page1', Page1.render, name='page1'),
    #     --------------   ------------        -----
    #     1                2                   3
    # 1. 例えば `http://example.com/practice/page1` のようなURLのパスの部分
    #                              --------------
    # 2. Page1 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page1' %} のような形でURLを取得するのに使える

    # ページ２ パッチ１
    path('practice/page2_patch1', Page2Patch1.render, name='page2_patch1'),
    #     ---------------------   ------------------        ------------
    #     1                       2                         3
    #
    # 1. 例えば `http://example.com/practice/page2_patch1` のようなURLのパスの部分
    #                              ----------------------
    # 2. Page2Patch1 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page2_patch1' %} のような形でURLを取得するのに使える

    # ページ２ パッチ２
    path('practice/page2_patch2', Page2Patch2.render, name='page2_patch2'),
    #                         ^two          ^two                       ^two
    #     ---------------------   ------------------        ------------
    #     1                       2                         3
    #
    # 1. 例えば `http://example.com/practice/page2_patch2` のようなURLのパスの部分
    #                              ----------------------
    # 2. Page2Patch2 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page2_patch2' %} のような形でURLを取得するのに使える

    # ログイン中
    path('practice/login-required', v_login_required.LoggingIn.render,
         # ----------------------   ---------------------------------
         # 1                        2
         name='practiceLoginRequired'),
    #          ---------------------
    #          3
    # 1. 例えば `http://example.com/practice/login-required` のような URL のパスの部分
    #                              -----------------------
    # 2. v_login_required.py ファイルの LoggingIn クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practiceLoginRequired' %} のような形でURLを取得するのに使える

    # ログアウト中
    path('practice/logout', v_login_required.LoggingOut.render,
         # --------------   ----------------------------------
         # 1                2
         name='practiceLogout'),
    #          --------------
    #          3
    # 1. 例えば `http://example.com/practice/logout` のような URL のパスの部分
    #                              ---------------
    # 2. v_login_required.py ファイルの LoggingOut クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practiceLogout' %} のような形でURLを取得するのに使える

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
]
