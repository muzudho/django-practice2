import json
from django.http import HttpResponse
from django.template import loader

# 部屋モデルヘルパー
from apps1.practice_v1.models_helper.o1o0.mh_room import MhRoom
#          -----------                    -------        ------
#          11                             12             2
#    --------------------------------------------
#    10
# 11, 12. ディレクトリー
# 10. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


# セッション モデルヘルパー
from apps1.practice_v1.models_helper.o1o0.mh_session import MhSession
#          -----------                    ----------        ---------
#          11                             12                2
#    -----------------------------------------------
#    10
# 11, 12. ディレクトリー
# 10. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


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
        "dj_path_of_home": "/practice/v1/my/",
        "dj_path_of_rooms_read": "/practice/v1/rooms/read/",
    }

    return HttpResponse(template.render(context, request))
