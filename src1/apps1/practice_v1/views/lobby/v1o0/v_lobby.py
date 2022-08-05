import json
from django.shortcuts import render

# 部屋モデルヘルパー
from apps1.practice_v1.models_helper.room.v1o0 import MhRoom
#          -----------                    ----        ------
#          11                             12          2
#    -----------------------------------------
#    10
# 11, 12. ディレクトリー
# 10. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


# セッション モデルヘルパー
from apps1.practice_v1.models_helper.session.v1o0 import MhSession
#          -----------                    -------        ---------
#          11                             12             2
#    --------------------------------------------
#    10
# 11, 12. ディレクトリー
# 10. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_lobby(request, lp_lobby):
    """OA20o1o0g6o0 ロビー（待合室）

    Parameters
    ----------
    lp_lobby : str
        ローカルパス
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
        "dj_path_of_home": "/practice/v1/my/",
        "dj_path_of_rooms_read": "/practice/v1/rooms/read/",
    }

    return render(request, lp_lobby, context)
