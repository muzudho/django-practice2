import json
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
def render_list(request, path_of_list_page):
    """一覧ページ"""

    # ２段階変換: roomテーブルid順 ----> JSON文字列 ----> オブジェクト
    room_resultset = Room.objects.all().order_by('id')
    # print(f"room_table_doc={json.dumps(room_table_doc, indent=4)}")
    """
    # Example
    room_table_doc=
    [
        {
            "model": "webapp1.room",
            "pk": 2,
            "fields": {
                "name": "Elephant",
                "sente_id": 1,
                "gote_id": 2,
                "board": "XOXOXOXOX",
                "record": "012345678"
            }
        },
        ...中略...
    ]
    """

    # 使いやすい形に変換します
    room_list = []

    for room in room_resultset:
        sente_id = room.sente_id
        gote_id = room.gote_id

        room_list.append(
            {
                "id": room.pk,
                "name": room.name,
                "sente_id": sente_id,
                "sente_name": MhUser.get_name_by_pk(sente_id),
                "gote_id": gote_id,
                "gote_name": MhUser.get_name_by_pk(gote_id),
                "board": room.board,
                "record": room.record,
            }
        )

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        # Vue には、 JSONオブジェクト を渡すのではなく、 JSON文字列 を渡します
        "dj_room_array": json.dumps(room_list),
        # FIXME URL を urls.py で変更しても、こちらに反映されないが、どうするか？
        "dj_read_room_path": "/rooms/read/",
    }
    # print(f"context={context}")

    return render(request, path_of_list_page, context)
