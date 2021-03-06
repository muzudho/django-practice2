# See also: đ[Custom Signup View in django-allauth](https://tech.serhatteker.com/post/2020-06/custom-signup-view-in-django-allauth/)
from allauth.account.views import SignupView


class AccountsV1SignupView(SignupView):
    """django-allauth ăźă”ă€ăłăąăă ăă„ăŒăă«ăčăżăă€ășăăŸă
    đ[views.py](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/views.py)
    """

    # ăăĄă€ă«ăăč
    template_name = "account/signup.html"
    #                -------------------
    #                1
    # 1. `host1/apps1/allauth_customized_v1/templates/account/signup.html` ăććŸ
    #                                                 -------------------

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...
