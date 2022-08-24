# BOF OA22o1o0g8o0

# 〇×ゲーム2.0巻 対局申込1.0版
from apps1.tic_tac_toe_vol2o0.views.gui.match_application.ver1o0 import MatchApplicationV as MatchApplicationVV2g1o0
#                       ^two
#    -----------------------------------------------------------        -----------------    -----------------------
#    1                                                                  2                    3
# 1. `src1/apps1/tic_tac_toe_vol2o0/views/gui/match_application/ver1o0/__init__.py`
#          -----------------------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名


class MatchApplicationV():
    """OA22o1o0g8o0 対局申込ビュー"""

    # 〇×ゲーム3.0巻 対局中3.1版
    playing_web_path = "/tic-tac-toe/vol3.0/playing/ver1.0/{0}/?&myturn={1}"
    #                                   ^three
    #                   ---------------------------------------------------
    #                   1
    # 1. `http://example.com:8000/tic-tac-toe/vol3.0/playing/ver1.0/Elephant/?&myturn=X`
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
            MatchApplicationV.playing_web_path,
            MatchApplicationVV2g1o0.template_path,
            MatchApplicationV.on_sent,
            MatchApplicationV.open)

    @staticmethod
    def on_sent(request):
        """送信後"""

        # 何もしません
        pass

    @staticmethod
    def open(request):
        """訪問後"""
        return MatchApplicationVV2g1o0.open_context

# EOF OA22o1o0g8o0
