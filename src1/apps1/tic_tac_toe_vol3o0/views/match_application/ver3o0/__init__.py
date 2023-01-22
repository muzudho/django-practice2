# BOF [OA24o1o0g6o0]

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
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名

# 〇×ゲーム3.0巻 対局申込1.0版
from apps1.tic_tac_toe_vol3o0.views.match_application.ver1o0 import MatchApplicationView as ViewOfMatchApplicationV3g1o0
#                         ^three                         ^one
#          ------------------                         ------        --------------------    ----------------------------
#          11                                         12            2                       3
#    -------------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_vol3o0/views/match_application/v1o0/__init__.py`
#           -----------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class MatchApplicationView():
    """[OA24o1o0g6o0] 対局申込ビュー"""

    # 〇×ゲーム3.0巻 対局中3.0版
    playing_web_path = "/tic-tac-toe/vol3.0/playing/ver3.0/{0}/?&myturn={1}"
    #                                   ^three
    #                   ---------------------------------------------------
    #                   1
    # 1. `http://example.com:8000/tic-tac-toe/vol3.0/playing/ver3.0/Elephant/?&myturn=X`
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
        #          --------------------------------------------------------------------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationView.playing_web_path,
            ViewOfMatchApplicationV2g1o0.template_path,
            ViewOfMatchApplicationV3g1o0.on_sent,
            ViewOfMatchApplicationV2g1o0.open)

# EOF [OA24o1o0g6o0]
