from django.contrib.auth import get_user_model  # カスタムした User
# from django.contrib.auth.models import User   # デフォルトの User


def get_extends_user_dic():
    """O9o2o0g8o0 （拡張済）会員登録ユーザー一覧"""
    User = get_user_model()

    # 会員登録ユーザー一覧
    user_resultset = User.objects.all().select_related('profile')
    #                                  --------------------------
    #                                  1
    # 1. これを付けて何が起こっているか分からないが、サンプルでよく付けているのを見かけるので真似する。外しても動く。
    #    User クラスを拡張して作った Profile クラスの OneToOneField フィールドの名前を指している

    # 使いやすい形に変換する
    user_dic = dict()

    for user in user_resultset:

        user_dic[user.pk] = {
            "pk": user.pk,
            # 日付型はJSONに変換できないので、先に文字列に変換しておく
            "last_login": user.last_login.strftime("%Y-%m-%d %H:%M:%S"),
            "username": user.username,
            "is_active": user.is_active,
            "match_state": user.profile.match_state
        }

    return user_dic
