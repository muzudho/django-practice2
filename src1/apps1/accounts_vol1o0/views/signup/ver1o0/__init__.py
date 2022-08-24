# BOF O6o1o0gA11o0

# See also: 📖[Custom Signup View in django-allauth](https://tech.serhatteker.com/post/2020-06/custom-signup-view-in-django-allauth/)
from allauth.account.views import SignupView


class CustomizedSignupView(SignupView):
    """django-allauth のサインアップ ビューをカスタマイズします
    📖[views.py](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/views.py)
    """

    # ファイルパス（使っているか分からない）
    template_name = "account/signup.html"
    #                -------------------
    #                1
    # 1. Allauthのディレクトリー構成に合わせる
    #    `src1/apps1/accounts_vol1o0/templates/account/signup.html` を取得
    #                                          -------------------

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...

# EOF O6o1o0gA11o0
