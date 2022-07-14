import json

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o0o1.playing import PlayingV as V3o0o1PlayingV
#    ----- -------------- ------------------        --------    --------------
#    1     2              3                         4           5
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. __init__.py ファイルに含まれるクラス名
# 5. '4.' の別名

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o0o3.playing import PlayingV as V3o0o3PlayingV
#    ----- -------------- ------------------        --------    --------------
#    1     2              3                         4           5
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. __init__.py ファイルに含まれるクラス名
# 5. '4.' の別名


# 以下、よく使う定型データ


# 対局申込 - 訪問後
match_application_open_context = {
    # `dj_` は Djangoでレンダーするパラメーター名の目印
    # 入場者データ
    "dj_visitor_value": "X",
    # Python と JavaScript 間で配列データを渡すために JSON 文字列形式にします
    "dj_visitor_select": json.dumps([
        {"text": "X", "value": "X"},
        {"text": "O", "value": "O"},
        {"text": "WatchingGame", "value": "_"},  # add
    ]),
}


# 対局中 - 駒
playing_expected_pieces = ['X', 'O', '_']


class PlayingV():

    path_of_html = "tic_tac_toe_v3/o0o4/playing.html.txt"
    #                            ^^^^^^ three.zero.four
    #               ------------------------------------
    #               1
    # 1. `host1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/o0o4/playing.html.txt`
    #                                          ------------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.v2o0o1.gui.playing.v_render import render_playing
        #                       ^two
        #    ------------------------------------------------------        --------------
        #    1                                                             2
        # 1. `host1/apps1/tic_tac_toe_v2/views/v2o0o1/gui/playing/v_render.py`
        #           ------------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            V3o0o3PlayingV.path_of_ws_playing,
            PlayingV.path_of_html,
            V3o0o1PlayingV.on_update,
            playing_expected_pieces)
        #   ^ Located in this file
