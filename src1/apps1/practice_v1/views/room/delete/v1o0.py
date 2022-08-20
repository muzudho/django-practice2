# BOF OA18o4o0g4o0

from django.shortcuts import render, get_object_or_404

# 部屋モデル
from apps1.practice_v1.models.room.v1o0 import Room
#          -----------             ----        ----
#          11                      12          2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_delete(request, room_pk, room_delete_tp):
    """OA18o4o0g4o0 削除ページ

    Parameters
    ----------
    room_delete_tp : str
        Template path
    """

    room = get_object_or_404(Room, pk=room_pk)  # idを指定してメンバーを１人取得

    name = room.name  # 名前だけまだ使う
    room.delete()
    context = {
        'room': {
            'name': name
        }
    }
    return render(request, room_delete_tp, context)

# EOF OA18o4o0g4o0
