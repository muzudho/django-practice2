from django.urls import include, path  # include 追加
from django.views.generic import TemplateView  # 追加

from apps1.allauth_customized.views.v0o0o1 import v_accounts
#    -------------------------------------        ----------
#    1                                            2
# 1. アプリケーション フォルダー名
# 2. Pythonモジュール名（ディレクトリー名）
# 3. Python ファイル名。拡張子抜き


urlpatterns = [


    # ...中略...


    # +----
    # | 認証
    # | See also: https://sinyblog.com/django/django-allauth/

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
    path("accounts/v1/signup/", view=v_accounts.accounts_v1_signup_view,
         # ------------------        ----------------------------------
         # 1                        2
         name="signup"),
    #          ------
    #          3
    # 1. 例えば `http://example.com/accounts/v1/signup/` のような URL のパスの部分にマッチする
    #                              -------------------
    # 2. allauth の SignupView をカスタマイズしたオブジェクト
    # 3. HTMLテンプレートの中で {% url 'signup' %} のような形でURLを取得するのに使える

    # | 認証
    # +----
]
