# BOF [OA23o1o0g2o0]

# 〇×ゲーム2.0巻 対局申込1.0版
from apps1.tic_tac_toe_vol2o0.views.gui.match_application.ver1o0 import MatchApplicationView as ViewOfMatchApplicationV2g1o0
#                         ^two
#    -----------------------------------------------------------        --------------------    ----------------------------
#    1                                                                  2                       3
# 1. `src1/apps1/tic_tac_toe_vol2o0/views/gui/match_application/ver1o0/__init__.py`
#          -----------------------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名

# 〇×ゲーム3.0巻 対局申込1.0版
from apps1.tic_tac_toe_vol3o0.views.match_application.ver1o0 import MatchApplicationView as ViewOfMatchApplicationV3g1o0
#                         ^three                         ^one
#          ------------------                         ------        --------------------    ----------------------------
#          11                                         12            2                       3
#    -------------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_vol3o0/views/match_application/ver1o0/__init__.py`
#           -------------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class MatchApplicationView():
    """[OA23o1o0g2o0] 対局申込ビュー"""

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_vol2o0.views.gui.match_application.ver1o0.v_render import render_match_application
        #                         ^two
        #    --------------------------------------------------------------------        ------------------------
        #    1                                                                           2
        # 1. `src1/apps1/tic_tac_toe_vol2o0/views/gui/match_application/ver1o0/v_render.py`
        #          --------------------------------------------------------------------
        # 2. `1.` に含まれる静的関数

        return render_match_application(
            request,
            ViewOfMatchApplicationV3g1o0.playing_web_path,
            ViewOfMatchApplicationV2g1o0.template_path,
            MatchApplicationView.on_sent,
            MatchApplicationView.open)

    @staticmethod
    def on_sent(request):
        """送信後"""

        # 以下のファイルはあとで作ります
        from .v_on_sent import match_application_on_sent
        #    ----------        -------------------------
        #    1                 2
        # 1. `src1/apps1/tic_tac_toe_vol3o0/views/match_application/ver2o0/v_on_sent.py`
        #                                                                  ---------
        # 2. `1.` に含まれる関数

        return match_application_on_sent(request)

    @staticmethod
    def open(request):
        """訪問後"""
        return ViewOfMatchApplicationV2g1o0.open_context

# EOF [OA23o1o0g2o0]
