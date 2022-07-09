import json
from django.core import serializers
from django.shortcuts import render

from apps1.practice.models.v0o0o1.m_room import Room
#    ----- -------- ------------- ------        ----
#    1     2        3             4             5
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

from apps1.practice.models_helper.mh_user import MhUser
#    ----- -------- ------------- -------        ------
#    1     2        3             4              5
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


@staticmethod
def render_read(request, room_pk, path_of_read_page):
    """読取ページ"""

    # ２段階変換: 問合せ結果（QuerySet） ----> JSON文字列 ----> オブジェクト
    # idを指定してメンバーを１人取得
    room_table_qs = Room.objects.filter(pk=room_pk)  # QuerySet
    room_table_json = serializers.serialize('json', room_table_qs)
    room_table_doc = json.loads(room_table_json)  # オブジェクト

    # 使いやすい形に変換します
    if len(room_table_doc) < 1:
        room_dic = {
            "pk": room_pk,
            "name": "",
            "sente_id": "",
            "sente_name": "",
            "gote_id": "",
            "gote_name": "",
            "board": "",
            "record": "",
        }
    else:
        # 先頭の１件
        room_rec = room_table_doc[0]

        sente_id = room_rec["fields"]["sente_id"]
        gote_id = room_rec["fields"]["gote_id"]

        room_dic = {
            "pk": room_rec["pk"],
            "name": room_rec["fields"]["name"],
            "sente_id": sente_id,
            "sente_name": MhUser.get_name_by_pk(sente_id),
            "gote_id": gote_id,
            "gote_name": MhUser.get_name_by_pk(gote_id),
            "board": room_rec["fields"]["board"],
            "record": room_rec["fields"]["record"],
        }

    context = {
        'room': room_dic,  # room_table_qs,
    }
    return render(request, path_of_read_page, context)
