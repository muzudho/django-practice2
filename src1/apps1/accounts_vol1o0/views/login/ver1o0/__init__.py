# BOF O8o1o0g3o0

# See also: 📖[Custom Signup View in django-allauth](https://tech.serhatteker.com/post/2020-06/custom-signup-view-in-django-allauth/)
from allauth.account.views import LoginView


class CustomizedLoginView(LoginView):
    """django-allauth のログイン ビューをカスタマイズします
    📖[views.py](https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py)
    """

    # ファイルパス（使ってるか分からない）
    template_name = "accounts_vol1o0/templates/account/login.html"
    #                                          ------------------
    #                                          11
    #                --------------------------------------------
    #                1
    # 11. Allauthのディレクトリー構成に合わせる
    # 1. `src1/apps1/accounts_vol1o0/templates/accounts/login.html` を取得
    #                ---------------------------------------------

# EOF O8o1o0g3o0
