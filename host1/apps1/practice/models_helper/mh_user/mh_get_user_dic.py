import json
from django.contrib.auth import get_user_model  # カスタムした User
# from django.contrib.auth.models import User # デフォルトの User
from django.core import serializers


@staticmethod
def get_user_dic():
    """会員登録ユーザー一覧"""
    User = get_user_model()

    # 会員登録ユーザー一覧
    # ２段階変換: 問合せ結果（QuerySet） ----> JSON文字列 ----> オブジェクト
    user_table_qs = User.objects.all()  # QuerySet
    print(f"user_table_qs={user_table_qs}")
    user_table_json = serializers.serialize('json', user_table_qs)
    user_table_doc = json.loads(user_table_json)  # オブジェクト
    # print(f"user_table_doc={json.dumps(user_table_doc, indent=4)}")

    # 使いやすい形に変換します
    user_dic = dict()
    for user_rec in user_table_doc:
        user_dic[user_rec["pk"]] = {
            "pk": user_rec["pk"],
            "last_login": user_rec["fields"]["last_login"],
            "username": user_rec["fields"]["username"],
            "is_active": user_rec["fields"]["is_active"],
        }

    return user_dic
