# 以前のバージョン
from apps1.tic_tac_toe_o4o1.views.o1o0.playing import PlayingV as PlayingVV3o1o0
#          ----------------            -------        --------    --------------
#          11                          12             2           3
#    -----------------------------------------
#    10
# 10. `host1/apps1/tic_tac_toe_o4o1/views/o1o0/playing/__init__.py`
#            -----------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名

# 以前のバージョン
from apps1.tic_tac_toe_o4o1.views.o4o1.playing import PlayingV as PlayingVV3o4o1
#          ----------------            -------        --------    --------------
#          11                          12             2           3
#    -----------------------------------------
#    10
# 10. `host1/apps1/tic_tac_toe_o4o1/views/o4o1/playing/__init__.py`
#            -----------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class PlayingV():
    """対局中ビュー"""

    # 駒
    expected_pieces = ['X', 'O', '_']

    path_of_html = "tic_tac_toe_o4o1/o5o1/playing.html.txt"
    #                                 ^five
    #               --------------------------------------
    #               1
    # 1. `host1/apps1/tic_tac_toe_o4o1/templates/tic_tac_toe_o4o1/o5o1/playing.html.txt`
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
            PlayingVV3o4o1.path_of_ws_playing,
            PlayingV.path_of_html,
            PlayingVV3o1o0.on_update,
            PlayingV.expected_pieces)
