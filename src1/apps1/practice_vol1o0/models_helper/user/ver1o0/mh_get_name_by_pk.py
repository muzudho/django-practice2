from django.contrib.auth.models import User


def get_name_by_pk(id):
    """OA18o2o0g4o0 主キーを使って、ユーザーを絞りこみます"""

    try:
        user = User.objects.get(pk=id)
        return user.username

    except User.DoesNotExist:
        # ユーザーが存在しなかったときに代わりに出す文字列
        return "#unknown#"
