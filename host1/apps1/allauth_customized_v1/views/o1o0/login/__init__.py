# See also: đ[Custom Signup View in django-allauth](https://tech.serhatteker.com/post/2020-06/custom-signup-view-in-django-allauth/)
from allauth.account.views import LoginView


class AccountsV1LoginView(LoginView):
    """django-allauth ăźă­ă°ă€ăł ăă„ăŒăă«ăčăżăă€ășăăŸă
    đ[views.py](https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py)
    """

    # ăăĄă€ă«ăăčïŒäœżăŁăŠăăćăăăȘăïŒ
    template_name = "allauth_customized_v1/templates/account/login.html"
    #                --------------------------------------------------
    #                1
    # 1. host1/apps1/allauth_customized_v1/templates/account/login.html ăććŸ
    #                --------------------------------------------------
