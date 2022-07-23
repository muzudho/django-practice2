from apps1.practice_v1.models.o1o0.m_room import Room
#          -----------             ------        ----
#          1.1                     1.2           2
#    ------------------------------------
#    1
# 1, 1.2 ディレクトリー
# 1.1 アプリケーション
# 2. `1.2` に含まれる __init__.py ファイルにさらに含まれるクラス


@staticmethod
def get_all_rooms_as_dic():
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
