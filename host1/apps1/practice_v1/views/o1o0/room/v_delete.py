from django.http import HttpResponse
from django.template import loader

from apps1.practice_v1.models.o1o0.m_room import Room
#          -----------             ------        ----
#          11                      12            2
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


@staticmethod
def render_delete(request, room_pk, path_of_delete_page):
    """削除ページ"""

    template = loader.get_template(path_of_delete_page)

    room = Room.objects.get(pk=room_pk)  # idを指定してメンバーを１人取得
    name = room.name  # 名前だけまだ使う
    room.delete()
    context = {
        'room': {
            'name': name
        }
    }
    return HttpResponse(template.render(context, request))
