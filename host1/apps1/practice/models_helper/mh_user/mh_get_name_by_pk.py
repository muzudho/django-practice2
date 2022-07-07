from django.contrib.auth.models import User


@staticmethod
def get_name_by_pk(id):
    """主キーを使って、ユーザーを絞りこみます"""

    try:
        user = User.objects.get(pk=id)
        return user.username

    except User.DoesNotExist:
        # ユーザーが存在しなかったときに代わりに出す文字列
        return "#unknown#"
