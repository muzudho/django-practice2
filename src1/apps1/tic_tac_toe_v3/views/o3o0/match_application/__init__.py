# 以前のバージョン
from apps1.tic_tac_toe_v2.views.gui.match_application.v1o0 import MatchApplicationV as MatchApplicationVV2g1o0
#                       ^two
#          --------------                -----------------        -----------------    -----------------------
#          11                            12                       2                    3
#    -----------------------------------------------------
#    10
# 1. `src1/apps1/tic_tac_toe_v2/views/gui/match_application/v1o0/__init__.py`
#          -----------------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名

# 〇×ゲーム v3.1
from apps1.tic_tac_toe_v3.views.match_application.v1o0 import MatchApplicationV as MatchApplicationVV3g1o0
#                       ^three                     ^one
#          --------------                         ----        -----------------    -----------------------
#          11                                     12          2                    3
#    -------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v3/views/match_application/v1o0/__init__.py`
#           -------------------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
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
        from apps1.tic_tac_toe_v2.views.gui.match_application.v1o0.v_render import render_match_application
        #                       ^two
        #    --------------------------------------------------------------        ------------------------
        #    1                                                                     2
        # 1. `src1/apps1/tic_tac_toe_v2/views/gui/match_application/v1o0/v_render.py`
        #                                                                --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV.path_of_http_playing,
            MatchApplicationVV2g1o0.path_of_local_html,
            MatchApplicationVV3g1o0.on_sent,
            MatchApplicationVV2g1o0.open)
