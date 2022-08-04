from django.shortcuts import render

# 部屋モデル
from apps1.practice_v1.models.room.v1o0 import Room
#          -----------             ----        ----
#          11                      12          2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# ユーザー モデルヘルパー
from apps1.practice_v1.models_helper.user.v1o0 import MhUser
#          -----------                    ----        ------
#          11                             12          2
#    -----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_read(request, room_pk, lp_room_read):
    """OA18o3o0g4o0 読取ページ

    Parameters
    ----------
    lp_room_read : str
        ローカルパス
    """

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
    return render(request, lp_room_read, context)
