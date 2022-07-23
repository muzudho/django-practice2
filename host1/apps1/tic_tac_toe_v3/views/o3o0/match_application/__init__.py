# 以前のバージョン
from apps1.tic_tac_toe_v2.views.o1o0.gui.match_application import MatchApplicationV as MatchApplicationVV2g1o0
#                       ^two
#          --------------                -----------------        -----------------    -----------------------
#          11                            12                       2                    3
#    -----------------------------------------------------
#    10
# 1. `host1/apps1/tic_tac_toe_v2/views/o1o0/gui/match_application/__init__.py`
#           -----------------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o1o0.match_application import MatchApplicationV as MatchApplicationVV3g1o0
#                       ^three
#          --------------            -----------------        -----------------    -----------------------
#          11                        12                       2                    3
#    -------------------------------------------------
#    10
# 1. `host1/apps1/tic_tac_toe_v3/views/o1o0/match_application/__init__.py`
#           -------------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名


class MatchApplicationV():
    """対局申込ビュー"""

    path_of_http_playing = "/tic-tac-toe/v3.3/playing/{0}/?&myturn={1}"
    #                                       ^three
    #                       ------------------------------------------
    #                       1
    # 1. `http://example.com:8000/tic-tac-toe/v3.3/playing/Elephant/?&myturn=X`
    #                            ---------------------------------------------

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
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV.path_of_http_playing,
            MatchApplicationVV2g1o0.path_of_html,
            MatchApplicationVV3g1o0.on_sent,
            MatchApplicationVV2g1o0.open)
