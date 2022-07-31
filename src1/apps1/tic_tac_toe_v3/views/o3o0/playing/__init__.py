# 以前のバージョン
from apps1.tic_tac_toe_v2.views.o1o0.gui.playing import PlayingV as PlayingVV2g1o0
#                       ^two
#          --------------                -------        --------    --------------
#          11                            12             2           3
#    -------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v2/views/o1o0/gui/playing/__init__.py`
#           -------------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o1o0.playing import PlayingV as PlayingVV3o1o0
#                       ^three
#          --------------            -------        --------    --------------
#          11                        12             2           3
#    ---------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v3/views/o1o0/playing/__init__.py`
#           ---------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名


class PlayingV():
    """OA24o1o0g7o0 対局中ビュー"""

    path_of_web_socket = "/tic-tac-toe/v3.3/playing/"
    #                                     ^three
    #                     --------------------------
    #                     1
    # 1. `ws://example.com/tic-tac-toe/v3.3/playing/Elephant/`
    #                     --------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o1o0.gui.playing.v_render import render_playing
        #                       ^two
        #    ----------------------------------------------------        --------------
        #    1                                                           2
        # 1. `src1/apps1/tic_tac_toe_v2/views/o1o0/gui/playing/v_render.py`
        #          ----------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            PlayingV.path_of_web_socket,
            PlayingVV3o1o0.path_of_html,
            PlayingVV3o1o0.on_update,
            PlayingVV2g1o0.expected_pieces)
