# See also: 📖[Custom Signup View in django-allauth](https://tech.serhatteker.com/post/2020-06/custom-signup-view-in-django-allauth/)
from allauth.account.views import LoginView


class AccountsV1LoginView(LoginView):
    """django-allauth のログイン ビューをカスタマイズします
    📖[views.py](https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py)
    """

    # ファイルパス
    template_name = "allauth-customized/v1/account/login.html"
    #                ----------------------------------------
    #                1
    # 1. host1/webapp1/templates/allauth-customized/v1/account/login.html を取得
    #                            ----------------------------------------


# グローバル変数
accounts_v1_login_view = AccountsV1LoginView.as_view()
