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

from apps1.practice.views.v0o0o1.prefecture.v_list import PrefectureListV
#    ----- -------- ----------------------- ------        ---------------
#    1     2        3                       4             5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

from apps1.practice.views.v0o0o1.prefecture.v_read import PrefectureReadV
#    ----- -------- ----------------------- ------        ---------------
#    1     2        3                       4             5
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

    # 都道府県一覧
    path('practice/prefectures/', PrefectureListV.render, name='prefecture_list'),
    #     ---------------------   ----------------------        ---------------
    #     1                       2                             3
    # 1. 例えば `http://example.com/practice/prefectures/` のような URL のパスの部分
    #                              ----------------------
    # 2. PrefectureListV クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'prefecture_list' %} のような形でURLを取得するのに使える

    # 都道府県詳細
    path('practice/prefectures/read/<int:id>/',
         # ----------------------------------
         # 1
         PrefectureReadV.render, name='prefecture_read'),
    #    ----------------------        ---------------
    #    2                             3
    #
    # 1. 例えば `http://example.com/practice/prefectures/read/<数字列>/` のような URL のパスの部分
    #                              -----------------------------------
    #    数字列は `2.` のメソッドの引数に `=id` と指定することで取得できる
    # 2. PrefectureReadV クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'prefecture_read' %} のような形でURLを取得するのに使える
]
