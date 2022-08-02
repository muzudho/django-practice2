from django.urls import include, path
#                       --------追加
from django.views.generic import TemplateView  # 追加

# O6o1o0gA12o0 サインアップ（会員登録）
from apps1.allauth_customized_v1.views.accounts.v1o0 import AccountsV1SignupView
#          ---------------------                ----        --------------------
#          11                                   12          2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. クラス

# O8o1o0g4o0 ログイン（ユーザー認証）
from apps1.allauth_customized_v1.views.login.v1o0 import AccountsV1LoginView
#          ---------------------            -----        -------------------
#          11                               12           2
#    --------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. クラス


urlpatterns = [
    # See also: https://sinyblog.com/django/django-allauth/

    # ログイン後に戻ってくるWebページの指定
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #    --  -----------------------------------------------        ----
    #    1   2                                                      3
    # 1. URL に パスを付けなかったときにマッチする
    # 2. 最初から用意されているビュー
    # 3. このパスを 'home' という名前で覚えておく

    # allauth の URLのパスのコピー
    path('accounts/v1/', include('allauth.urls')),
    #     ------------   -----------------------
    #     1
    # 1. 例えば `http://example.com/accounts/v1/` のような URLのパスの部分
    #                              ------------
    # 2. allauth アプリケーションに含まれる `allauth/urls.py` の urlpatterns 、
    #                                     ------------
    #    例えば `login/` のようなパスを (1.) のパスにぶら下げる形で全てコピーします

    # サインアップ（会員登録）
    path("accounts/v1/signup/", view=AccountsV1SignupView.as_view(),
         # ------------------        ------------------------------
         # 1                        2
         name="signup"),
    #          ------
    #          3
    # 1. 例えば `http://example.com/accounts/v1/signup/` のような URL のパスの部分にマッチする
    #                              -------------------
    # 2. allauth の SignupView をカスタマイズしたオブジェクト
    # 3. HTMLテンプレートの中で {% url 'signup' %} のような形でURLを取得するのに使える

    # ログイン（入場）
    path("accounts/v1/login/", view=AccountsV1LoginView.as_view(),
         # -----------------        -----------------------------
         # 1                        2
         name="login"),
    #          -----
    #          3
    # 1. 例えば `http://example.com/accounts/v1/login/` のような URL のパスの部分
    #                              -------------------
    # 2. allauth の LoginView をカスタマイズしたオブジェクト
    # 3. HTMLテンプレートの中で {% url 'login' %} のような形でURLを取得するのに使える
]
