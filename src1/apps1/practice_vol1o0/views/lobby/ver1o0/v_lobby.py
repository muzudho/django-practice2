# BOF OA20o1o0g6o0

import json
from django.shortcuts import render

# 練習1.0巻 部屋モデルヘルパー1.0版
from apps1.practice_vol1o0.models_helper.room.ver1o0 import MhRoom
#          ---------------                    ------        ------
#          11                                 12            2
#    -----------------------------------------------
#    10
# 11, 12. ディレクトリー
# 10. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


# 練習1.0巻 セッション モデルヘルパー1.0版
from apps1.practice_vol1o0.models_helper.session.ver1o0 import MhSession
#          ---------------                       ------        ---------
#          11                                    12            2
#    --------------------------------------------------
#    10
# 11, 12. ディレクトリー
# 10. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_lobby(request, lobby_tp):
    """OA20o1o0g6o0 ロビー（待合室）

    Parameters
    ----------
    lobby_tp : str
        Template path
    """

    # 部屋の一覧
    room_dic = MhRoom.get_all_rooms_as_dic()

    # ユーザーの一覧
    user_dic = MhSession.get_all_logged_in_users()

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        'dj_room_dic': json.dumps(room_dic),
        'dj_user_dic': json.dumps(user_dic),
        # FIXME URL を urls.py で変更しても、こちらに反映されないが、どうするか？
        "dj_path_of_home": "/practice/vol1.0/my/ver1.0/",
        "dj_path_of_rooms_read": "/practice/ver1o0/rooms/read/",
    }

    return render(request, lobby_tp, context)

# EOF OA20o1o0g6o0
