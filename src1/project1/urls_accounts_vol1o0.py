# BOF O6o1o0gA12o0

from django.urls import include, path
#                       --------追加
# from django.views.generic import TemplateView  # 追加

# O6o1o0gA12o0 アカウント1.0巻 サインアップ（会員登録）1.0版
from apps1.accounts_vol1o0.views.signup.ver1o0 import CustomizedSignupView as Accounts1o0SignupView1o0
#          ---------------              ------        --------------------    ------------------------
#          11                           12            2                       3
#    -----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. クラス
# 3. `2.` の別名

# O8o1o0g4o0 アカウント1.0巻 ログイン（ユーザー認証）1.0版
from apps1.accounts_vol1o0.views.login.ver1o0 import CustomizedLoginView as Accounts1o0LoginView1o0
#          ---------------             ------        -------------------    -----------------------
#          11                          12            2                      3
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. クラス
# 3. `2.` の別名


urlpatterns = [
    # See also: https://sinyblog.com/django/django-allauth/

    # # ログイン後に戻ってくるWebページの指定
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # #    --  -----------------------------------------------        ----
    # #    1   2                                                      3
    # # 1. URL に パスを付けなかったときにマッチする
    # # 2. 最初から用意されているビュー
    # # 3. このパスを 'home' という名前で覚えておく

    # AllauthのURLのパスをぶらさげる
    path('accounts/vol1.0/', include('allauth.urls')),
    #     ----------------   -----------------------
    #     1
    # 1. 例えば `http://example.com/accounts/vol1.0/` のような URLのパスの部分
    #                              -----------------
    # 2. allauth アプリケーションに含まれる `allauth/urls.py` の urlpatterns 、
    #                                     ------------
    #    例えば `login/` のようなパスを (1.) のパスにぶら下げる形で全てコピーします

    # サインアップ（会員登録）
    path("accounts/vol1.0/signup/", view=Accounts1o0SignupView1o0.as_view(),
         # ----------------------        ----------------------------------
         # 1                             2
         name="signup"),
    #          ------
    #          3
    # 1. 例えば `http://example.com/accounts/vol1.0/signup/` のような URL のパスの部分にマッチする
    #                              ------------------------
    # 2. allauth の SignupView をカスタマイズしたオブジェクト
    # 3. HTMLテンプレートの中で {% url 'signup' %} のような形でURLを取得するのに使える

    # O8o1o0g4o0 ログイン（ユーザー認証）
    path("accounts/vol1.0/login/", view=Accounts1o0LoginView1o0.as_view(),
         # ---------------------        ---------------------------------
         # 1                            2
         name="login"),
    #          -----
    #          3
    # 1. 例えば `http://example.com/accounts/vol1.0/login/` のような URL のパスの部分
    #                              -----------------------
    # 2. allauth の LoginView をカスタマイズしたオブジェクト
    # 3. HTMLテンプレートの中で {% url 'login' %} のような形でURLを取得するのに使える
]

# EOF O6o1o0gA12o0
