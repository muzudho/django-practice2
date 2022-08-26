# BOF OA18o2o0g6o0

import json
from django.shortcuts import render

# 練習1.0巻 部屋モデル1.0版
from apps1.practice_vol1o0.models.room.ver1o0 import Room
#          ---------------             ------        ----
#          11                          12            2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 練習1.0巻 ユーザー モデルヘルパー1.0版
from apps1.practice_vol1o0.models_helper.user.ver1o0 import MhUser
#          ---------------                    ------        ------
#          11                                 12            2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_list(request, room_list_tp):
    """OA18o2o0g6o0 一覧ページ

    Parameters
    ----------
    room_list_tp : str
        Template path
    """

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
        "dj_read_room_path": "/practice/vol1.0/rooms/read/ver1.0/",
    }
    return render(request, room_list_tp, context)

# EOF OA18o2o0g6o0
