# BOF [OA25o1o0g3o0]

import json

# 〇×ゲーム2.0巻 対局申込1.0版
from apps1.tic_tac_toe_vol2o0.views.gui.match_application.ver1o0 import MatchApplicationView as ViewOfMatchApplicationV2g1o0
#                         ^two
#          ------------------                             ------        --------------------    ----------------------------
#          11                                             12            2                       3
#    -----------------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_vol2o0/views/gui/match_application/ver1o0/__init__.py`
#           -----------------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名

# 〇×ゲーム3.0巻 対局申込2.0版
from apps1.tic_tac_toe_vol3o0.views.match_application.ver2o0 import MatchApplicationView as ViewOfMatchApplicationV3g2o0
#                       ^three                           ^two
#          ------------------                         ------        --------------------    ----------------------------
#          11                                         12            2                       3
#    -------------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_vol3o0/views/match_application/ver1o0/__init__.py`
#           -------------------------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class MatchApplicationView():
    """[OA25o1o0g3o0] 対局申込ビュー"""

    # 対局申込 - 訪問後
    open_context = {
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

    playing_web_path = "/tic-tac-toe/vol3.0/playing/ver4.0/{0}/?&myturn={1}"
    #                                                  ^four
    #                   ---------------------------------------------------
    #                   1
    # 1. `http://example.com:8000/tic-tac-toe/vol3.0/playing/ver4.0/Elephant/?&myturn=X`
    #                            ------------------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_vol2o0.views.gui.match_application.ver1o0.v_render import render_match_application
        #                         ^two
        #    --------------------------------------------------------------------        ------------------------
        #    1                                                                           2
        # 1. `src1/apps1/tic_tac_toe_vol2o0/views/gui/match_application/ver1o0/v_render.py`
        #                                                                      --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationView.playing_web_path,
            ViewOfMatchApplicationV2g1o0.template_path,
            ViewOfMatchApplicationV3g2o0.on_sent,
            MatchApplicationView.open)

    @staticmethod
    def open(request):
        """訪問後"""
        return MatchApplicationView.open_context

# EOF [OA25o1o0g3o0]
