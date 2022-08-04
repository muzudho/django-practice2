import json


class MatchApplicationV():
    """OA16o3o0gA11o0 対局申込ビュー"""

    # 対局申込 - 訪問後
    open_context = {
        # `dj_` は Djangoでレンダーするパラメーター名の目印
        # 入場者データ
        "dj_visitor_value": "X",
        # Python と JavaScript 間で配列データを渡すために JSON 文字列形式にします
        "dj_visitor_select": json.dumps([
            {"text": "X", "value": "X"},
            {"text": "O", "value": "O"},
        ]),
    }

    path_of_http_playing = "/tic-tac-toe/v2/playing/{0}/?&myturn={1}"
    #                                     ^ two
    #                       ----------------------------------------
    #                       1
    # 1. `http://example.com:8000/tic-tac-toe/v2/playing/Elephant/?&myturn=X`
    #                            -------------------------------------------

    path_of_local_html = "tic_tac_toe_v2/gui/match_application/v1o0.html"
    #                                  ^two
    #                     ----------------------------------------------
    #                     1
    # 1. src1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/gui/match_application/v1o0.html
    #                                        ----------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_match_application
        #    ---------        ------------------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_v2/views/gui/match_application/v1o0/v_render.py`
        #                                                                --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV.path_of_http_playing,
            MatchApplicationV.path_of_local_html,
            MatchApplicationV.on_sent,
            MatchApplicationV.open)

    @staticmethod
    def on_sent(request):
        """送信後"""
        pass

    @staticmethod
    def open(request):
        """訪問後"""
        return MatchApplicationV.open_context
