# 以前のバージョン
from apps1.tic_tac_toe_v2.views.o1o0.gui.match_application import MatchApplicationV as MatchApplicationVV2g1o0
#                       ^two
#    -----------------------------------------------------        -----------------    -----------------------
#    1                                                            2                    3
# 1. `host1/apps1/tic_tac_toe_v2/views/o1o0/gui/match_application/__init__.py`
#           -----------------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o1o0.match_application import MatchApplicationV as MatchApplicationVV3g1o0
#                       ^three
#    ---------------------------------------------------      -----------------    -----------------------
#    1                                                        2                    3
# 1. `host1/apps1/tic_tac_toe_v3/views/o1o0/match_application/__init__.py`
#           -------------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名


class MatchApplicationV():
    """対局申込ビュー"""

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o1o0.gui.match_application.v_render import render_match_application
        #                       ^two
        #    --------------------------------------------------------------        ------------------------
        #    1                                                                     2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o1o0/gui/match_application/v_render.py`
        #                                                                 --------
        # 2. `1.` に含まれる静的関数

        return render_match_application(
            request,
            MatchApplicationVV3g1o0.path_of_http_playing,
            MatchApplicationVV2g1o0.path_of_html,
            MatchApplicationV.on_sent,
            MatchApplicationV.open)

    @staticmethod
    def on_sent(request):
        """送信後"""

        # 以下のファイルはあとで作ります
        from .v_on_sent import match_application_on_sent
        #    ----------        -------------------------
        #    1                 2
        # 1. `host1/apps1/tic_tac_toe_v3/views/o2o0/match_application/v_on_sent.py`
        #                                                             ---------
        # 2. `1.` に含まれる関数

        return match_application_on_sent(request)

    @staticmethod
    def open(request):
        """訪問後"""
        return MatchApplicationVV2g1o0.open_context
