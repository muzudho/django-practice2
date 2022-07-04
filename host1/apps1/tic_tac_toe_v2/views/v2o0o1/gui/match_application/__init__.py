import json


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
    ]),
}


class MatchApplication():
    """対局申込"""

    _path_of_http_playing = "/tic-tac-toe/v2/playing/{0}/?&myturn={1}"
    #                                      ^ two
    #                        ----------------------------------------
    #                        1
    # 1. http://example.com:8000/tic-tac-toe/v2/playing/Elephant/?&myturn=X
    #                           -------------------------------------------

    _path_of_html = "tic_tac_toe_v2/o0o1/gui/match_application.html"
    #                             ^ two
    #                ---------------------------------------------
    #                1
    # 1. host1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/o0o1/gui/match_application.html
    #                                         ----------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_match_application
        #    ---------        ------------------------
        #    1                2
        # 1. `host1/apps1/tic_tac_toe_v2/views/v2o0o1/gui/match_application/v_render.py`
        #                                                                   --------
        # 2. `1.` に含まれる関数

        return render_match_application(request, MatchApplication._path_of_http_playing, MatchApplication._path_of_html, MatchApplication.on_sent, MatchApplication.open)

    @staticmethod
    def on_sent(request):
        """送信後"""
        # 拡張したい挙動があれば、ここに書く
        pass

    @staticmethod
    def open(request):
        """訪問後"""
        # 拡張したい挙動があれば、ここに書く

        return match_application_open_context
