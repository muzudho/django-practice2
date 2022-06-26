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
]
