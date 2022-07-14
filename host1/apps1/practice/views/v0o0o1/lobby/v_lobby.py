import json
from django.http import HttpResponse
from django.template import loader

from apps1.practice.models_helper.mh_room import MhRoom
#    ----- -------- ---------------------        ------
#    1     2        3                            4
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. クラス名


from apps1.practice.models_helper.mh_session import MhSession
#    ----- -------- ------------------------        ---------
#    1     2        3                               4
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. クラス名


def render_lobby(request, path_of_lobby_page):
    """ロビー（待合室）"""
    template = loader.get_template(path_of_lobby_page)

    # 部屋の一覧
    room_dic = MhRoom.get_all_rooms_as_dic()

    # ユーザーの一覧
    user_dic = MhSession.get_all_logged_in_users()

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        'dj_room_dic': json.dumps(room_dic),
        'dj_user_dic': json.dumps(user_dic),
        # FIXME URL を urls.py で変更しても、こちらに反映されないが、どうするか？
        "dj_path_of_home": "/home/v1/",
        "dj_path_of_rooms_read": "/rooms/read/",
    }

    return HttpResponse(template.render(context, request))