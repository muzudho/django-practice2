from django.http import HttpResponse
from django.template import loader

from apps1.practice.models.v0o0o1.m_room import Room
#    ----- -------- ------------- ------        ----
#    1     2        3             4             5
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


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
