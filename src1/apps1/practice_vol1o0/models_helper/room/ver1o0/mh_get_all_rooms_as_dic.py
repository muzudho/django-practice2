# BOF OA20o1o0g4o0

# 部屋モデル
from apps1.practice_vol1o0.models.room.ver1o0 import Room
#          ---------------             ------        ----
#          11                          12            2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def get_all_rooms_as_dic():
    """OA20o1o0g4o0 全ての対局部屋をディクショナリー構造で取得"""

    room_resultset = Room.objects.all().order_by('id')

    # 使いやすい形に変換します
    room_dic = dict()
    for room in room_resultset:

        # Example:
        # room: {'model': 'webapp1.room', 'pk': 2, 'fields': {'name': 'Elephant', 'board': 'XOXOXOXOX', 'record': '012345678'}}

        room_dic[room.pk] = {
            "pk": room.pk,
            "name": room.name,
            "board": room.board,
            "record": room.record,
        }

    return room_dic

# EOF OA20o1o0g4o0
