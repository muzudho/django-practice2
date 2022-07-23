# 以前のバージョン
from apps1.tic_tac_toe_v2.views.o1o0.gui.playing import PlayingV as PlayingVV2o1o0
#                       ^two
#          --------------                -------        --------    --------------
#          11                            12             2           3
#    -------------------------------------------
#    10
# 10. `host1/apps1/tic_tac_toe_v2/views/o1o0/gui/playing/__init__.py`
#            -------------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名


class PlayingV():
    """対局中ビュー"""

    path_of_ws_playing = "/tic-tac-toe/v2o1/playing/"
    #                                   ^ two
    #                     --------------------------
    #                     1
    # 1. `ws://example.com:8000/tic-tac-toe/v2o1/playing/`
    #                          --------------------------

    path_of_html = "tic_tac_toe_v3/o1o0/playing.html.txt"
    #                            ^four
    #               --------------------------------------
    #               1
    # 1. `host1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/o1o0/playing.html.txt`
    #                                            --------------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o1o0.gui.playing.v_render import render_playing
        #                       ^two
        #    ----------------------------------------------------        --------------
        #    1                                                           2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o1o0/gui/playing/v_render.py`
        #           ----------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            PlayingV.path_of_ws_playing,
            PlayingV.path_of_html,
            PlayingV.on_update,
            PlayingVV2o1o0.expected_pieces)

    @staticmethod
    def on_update(request):
        """訪問後または送信後"""
        # 何もしません
        pass
