from django.urls import path

# O3o1o0gA10o0 こんにちわページ
from apps1.practice_v1.views.page_the_hello.v1o0 import PageTheHello
#          -----------                      ----        ------------
#          11                               12          2
#    -------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# O8o2o0g4o0 ログイン必須ページ
from apps1.practice_v1.views.login_required.v1o0 import LoggingIn, LoggingOut
#          -----------                      ----        ---------------------
#          11                               12          2
#    -------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [

    # O3o1o0gA10o0 こんにちわページ
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

    # O8o2o0g4o0 ログイン中
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

    # O8o2o0g4o0 ログアウト中
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
]
