import json

# 以前のバージョン
from apps1.tic_tac_toe_v2.views.o1o0.gui.match_application import MatchApplicationV as MatchApplicationVV2g1o0
#                       ^two
#          --------------                -----------------        -----------------    -----------------------
#          11                            12                       2                    3
#    -----------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v2/views/o1o0/gui/match_application/__init__.py`
#           -----------------------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o1o0.match_application import MatchApplicationV as MatchApplicationVV3g1o0
#                       ^three
#          --------------            -----------------        -----------------    -----------------------
#          11                        12                       2                    3
#    -------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v3/views/o1o0/match_application/__init__.py`
#           -------------------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class MatchApplicationV():
    """対局申込ビュー"""

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

    path_of_http_playing = "/tic-tac-toe/v3.4/playing/{0}/?&myturn={1}"
    #                                    ^^^^
    #                       ------------------------------------------
    #                       1
    # 1. `http://example.com:8000/tic-tac-toe/v3.4/playing/Elephant/?&myturn=X`
    #                            ---------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o1o0.gui.match_application.v_render import render_match_application
        #                       ^two
        #    --------------------------------------------------------------        ------------------------
        #    1                                                                     2
        # 1. `src1/apps1/tic_tac_toe_v2/views/o1o0/gui/match_application/v_render.py`
        #                                                                --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV.path_of_http_playing,
            MatchApplicationVV2g1o0.path_of_local_html,
            MatchApplicationVV3g1o0.on_sent,
            MatchApplicationV.open)

    @staticmethod
    def open(request):
        """訪問後"""
        return MatchApplicationV.open_context
