from django.shortcuts import render

from apps1.practice_v1.models.o1o0.m_room import Room
#          -----------             ------        ----
#          11                      12            2
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_delete(request, room_pk, lp_room_delete):
    """OA18o4o0g4o0 削除ページ

    Parameters
    ----------
    lp_room_delete : str
        ローカルパス
    """

    room = Room.objects.get(pk=room_pk)  # idを指定してメンバーを１人取得
    name = room.name  # 名前だけまだ使う
    room.delete()
    context = {
        'room': {
            'name': name
        }
    }
    return render(request, lp_room_delete, context)
