from django.contrib.auth import get_user_model  # カスタムした User
# from django.contrib.auth.models import User # デフォルトの User


@staticmethod
def get_user_dic():
    """会員登録ユーザー一覧"""
    User = get_user_model()

    # 会員登録ユーザー一覧
    # ２段階変換: 問合せ結果（QuerySet） ----> JSON文字列 ----> オブジェクト
    user_resultset = User.objects.all()

    # 使いやすい形に変換します
    user_dic = dict()
    for user in user_resultset:
        user_dic[user.pk] = {
            "pk": user.pk,
            # 日付型はJSONに変換できないので、先に文字列に変換しておく
            "last_login": user.last_login.strftime("%Y-%m-%d %H:%M:%S"),
            "username": user.username,
            "is_active": user.is_active,
        }

    return user_dic
