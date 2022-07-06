import json
from django.contrib.auth import get_user_model  # カスタムした User
# from django.contrib.auth.models import User   # デフォルトの User
from django.core import serializers

from apps1.practice.models.v0o0o1.m_user_profile import Profile
#    ----- -------- ----------------------------        -------
#    1     2        3                                   4
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 3. Python ファイル名。拡張子抜き
# 4. クラス名


@staticmethod
def get_extends_user_dic():
    """（拡張済）会員登録ユーザー一覧"""
    User = get_user_model()

    # 会員登録ユーザー一覧
    # ２段階変換: 問合せ結果（QuerySet） ----> JSON文字列 ----> オブジェクト
    user_table_qs = User.objects.all().select_related('profile')  # QuerySet
    #                                 --------------------------
    #                                 1
    # 1. これを付けて何が起こっているか分からないが、サンプルでよく付けているのを見かけるので真似する。外しても動く。
    #    User クラスを拡張して作った Profile クラスの OneToOneField フィールドの名前を指しています
    # print(f"user_table_qs={user_table_qs}")
    #
    user_table_json = serializers.serialize('json', user_table_qs)
    user_table_doc = json.loads(user_table_json)
    # print(f"user_table_doc={json.dumps(user_table_doc, indent=4)}")

    # 使いやすい形に変換します
    user_dic = dict()
    # for user in user_table_doc:  # User Record
    # print(f"user={user}")
    #username = user["fields"]["username"]
    # print(f"user['fields']['username']={username}")
    #
    # ２段階変換: 問合せ結果（QuerySet） ----> JSON文字列 ----> オブジェクト
    # profile_table_qs = Profile.objects.filter(  # QuerySet
    #    #                             -------
    #    #                             1
    #    user__username=username)
    # 1. filter ならインスタンスが返ってくる。 get なら文字列表現が返ってくる
    #
    # QuerySet は中身が見えないので JSON にダンプするのが定番
    # print(f"Profile={profile_table_qs}")
    ##
    # profile_table_json = serializers.serialize(
    #    'json', profile_table_qs)
    # profile_table_doc = json.loads(profile_table_json)  # オブジェクト
    ## print(f"profile_table_doc={json.dumps(profile_table_doc, indent=4)}")

    # print(user.profile.match_state)
    for user in user_table_qs:

        user_dic[user.pk] = {
            "pk": user.pk,
            # 日付型はJSONに変換できないので、先に文字列に変換しておく
            "last_login": user.last_login.strftime("%Y-%m-%d %H:%M:%S"),
            "username": user.username,
            "is_active": user.is_active,

            # "match_state": profile_table_doc[0]["fields"]["match_state"],
            # ---
            # 1
            # 1. 先頭の1件を取っている

            "match_state": user.profile.match_state
        }

    return user_dic
