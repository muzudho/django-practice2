# BOF OA16o3o_1o0g3o0

import json


class TesterV():
    """OA16o3o_1o0g3o0 テスター ビュー"""

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

    template_path = "tic_tac_toe_v2/msg/tester/v1o0.html"
    #                             ^two
    #                -----------------------------------
    #                1
    # 1. src1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/msg/tester/v1o0.html
    #                                        -----------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_tester
        #    ---------        -------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_v2/views/msg/tester/v1o0/v_render.py`
        #                                                     --------
        # 2. `1.` に含まれる関数

        return render_tester(
            request,
            kw_room_name,
            TesterV.template_path,
            TesterV.on_open,
            TesterV.on_sent)

    @staticmethod
    def on_open(request):
        """訪問後

        Returns
        -------
        context : dict
            context
        """
        return TesterV.open_context

    @staticmethod
    def on_sent(request):
        """送信後"""
        pass

# EOF OA16o3o_1o0g3o0
