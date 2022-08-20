# BOF OA24o1o0g6o0

# 〇×ゲーム v2 対局申込 v1.0
from apps1.tic_tac_toe_v2.views.gui.match_application.v1o0 import MatchApplicationV as MatchApplicationVV2g1o0
#                       ^two
#          --------------                -----------------        -----------------    -----------------------
#          11                            12                       2                    3
#    -----------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v2/views/gui/match_application/v1o0/__init__.py`
#           -----------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名

# 〇×ゲーム v3.1 対局申込 v1.0
from apps1.tic_tac_toe_v3.views.match_application.v1o0 import MatchApplicationV as MatchApplicationVV3g1o0
#                       ^three                     ^one
#          --------------                         ----        -----------------    -----------------------
#          11                                     12          2                    3
#    -------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v3/views/match_application/v1o0/__init__.py`
#           -------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class MatchApplicationV():
    """OA24o1o0g6o0 対局申込ビュー"""

    playing_web_path = "/tic-tac-toe/v3.3/playing/{0}/?&myturn={1}"
    #                                 ^three
    #                   ------------------------------------------
    #                   1
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
            MatchApplicationV.playing_web_path,
            MatchApplicationVV2g1o0.template_path,
            MatchApplicationVV3g1o0.on_sent,
            MatchApplicationVV2g1o0.open)

# EOF OA24o1o0g6o0
