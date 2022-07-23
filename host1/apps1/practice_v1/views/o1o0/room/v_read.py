from django.shortcuts import render

from apps1.practice_v1.models.o1o0.m_room import Room
#          -----------             ------        ----
#          11                      12            2
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# ユーザー モデルヘルパー
from apps1.practice_v1.models_helper.o1o0.mh_user import MhUser
#          -----------                    -------        ------
#          11                             12             2
#    --------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


@staticmethod
def render_read(request, room_pk, path_of_read_page):
    """読取ページ"""

    # idを指定してメンバーを１人取得
    room_resultset = Room.objects.filter(pk=room_pk)

    # 使いやすい形に変換します
    if len(room_resultset) < 1:
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
        room = room_resultset[0]

        sente_id = room.sente_id
        gote_id = room.gote_id

        room_dic = {
            "pk": room.pk,
            "name": room.name,
            "sente_id": sente_id,
            "sente_name": MhUser.get_name_by_pk(sente_id),
            "gote_id": gote_id,
            "gote_name": MhUser.get_name_by_pk(gote_id),
            "board": room.board,
            "record": room.record,
        }

    context = {
        'room': room_dic,
    }
    return render(request, path_of_read_page, context)
