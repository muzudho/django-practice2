import json

# 以前のバージョン
from apps1.tic_tac_toe_v2.views.o1.gui.match_application import MatchApplicationV as V2o0o1MatchApplicationV
#                       ^two
#    ---------------------------------------------------        -----------------    -----------------------
#    1                                                          2                    3
# 1. `host1/apps1/tic_tac_toe_v2/views/o1/gui/match_application/__init__.py`
#           ---------------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o1.match_application import MatchApplicationV as V3o0o1MatchApplicationV
#                       ^three
#    -----------------------------------------------        -----------------    -----------------------
#    1                                                      2                    3
# 1. `host1/apps1/tic_tac_toe_v3/views/o1/match_application/__init__.py`
#           -----------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名


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


class MatchApplicationV():
    """対局申込ビュー"""

    _path_of_http_playing = "/tic-tac-toe/v3o0o4/playing/{0}/?&myturn={1}"
    #                                      ^^^^^ three.zero.four
    #                        ------------------------------------------
    #                        1
    # 1. http://example.com:8000/tic-tac-toe/v3o0o4/playing/Elephant/?&myturn=X
    #                           -----------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o1.gui.match_application.v_render import render_match_application
        #                       ^two
        #    ------------------------------------------------------------        ------------------------
        #    1                                                                   2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o1/gui/match_application/v_render.py`
        #                                                               --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV._path_of_http_playing,
            V2o0o1MatchApplicationV.path_of_html,
            V3o0o1MatchApplicationV.on_sent,
            MatchApplicationV.open)

    @staticmethod
    def open(request):
        """訪問後"""
        # 拡張したい挙動があれば、ここに書く

        return match_application_open_context
        #      ^ Located in this file
