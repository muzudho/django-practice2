# BOF [OA16o3o0gA11o0]

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

    playing_web_path = "/tic-tac-toe/vol2.0/playing/ver1.0/{0}/?&myturn={1}"
    #                                   ^ two
    #                   ---------------------------------------------------
    #                   1
    # 1. `http://example.com:8000/tic-tac-toe/vol2.0/playing/ver1.0/Elephant/?&myturn=X`
    #                            ------------------------------------------------------

    template_path = "tic_tac_toe_vol2o0/gui/match_application/ver1o0.html"
    #                               ^two
    #                ----------------------------------------------------
    #                1
    # 1. src1/apps1/tic_tac_toe_vol2o0/templates/tic_tac_toe_vol2o0/gui/match_application/ver1o0.html
    #                                            ----------------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_match_application
        #    ---------        ------------------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_vol2o0/views/gui/match_application/ver1o0/v_render.py`
        #                                                                      --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV.playing_web_path,
            MatchApplicationV.template_path,
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

# EOF [OA16o3o0gA11o0]
