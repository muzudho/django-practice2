from django.contrib.auth import get_user_model  # カスタムした User
# from django.contrib.auth.models import User # デフォルトの User


def get_user_dic():
    """O9o1o0g4o0 会員登録ユーザー一覧"""
    User = get_user_model()

    # 会員登録ユーザー一覧
    user_resultset = User.objects.all()

    # 使いやすい形に変換します
    user_dic = dict()
    for user in user_resultset:

        if user.last_login is None:
            # まだ一度もログインしていないとき
            last_login1 = ""
        else:
            # 日付型はJSONに変換できないので、先に文字列に変換しておく
            last_login1 = user.last_login.strftime("%Y-%m-%d %H:%M:%S")

        user_dic[user.pk] = {
            "pk": user.pk,
            "last_login": last_login1,
            "username": user.username,
            "is_active": user.is_active,
        }

    return user_dic
