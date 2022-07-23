# See also: 📖[Custom Signup View in django-allauth](https://tech.serhatteker.com/post/2020-06/custom-signup-view-in-django-allauth/)
from allauth.account.views import LoginView


class AccountsV1LoginView(LoginView):
    """django-allauth のログイン ビューをカスタマイズします
    📖[views.py](https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py)
    """

    # ファイルパス（使ってるか分からない）
    template_name = "allauth_customized_v1/templates/account/login.html"
    #                --------------------------------------------------
    #                1
    # 1. host1/apps1/allauth_customized_v1/templates/account/login.html を取得
    #                --------------------------------------------------
