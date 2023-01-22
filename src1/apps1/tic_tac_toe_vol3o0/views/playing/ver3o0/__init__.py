# BOF [OA24o1o0g7o0]

# 〇×ゲーム2.0巻 対局中1.0版
from apps1.tic_tac_toe_vol2o0.views.gui.playing.ver1o0 import PlayingView as ViewOfPlayingV2g1o0
#                         ^two
#          ------------------                   ------        -----------    -------------------
#          11                                   12            2              3
#    -------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_vol2o0/views/gui/playing/ver1o0/__init__.py`
#           -------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム3.0巻 対局中1.0版
from apps1.tic_tac_toe_vol3o0.views.playing.ver1o0 import PlayingView as ViewOfPlayingV3g1o0
#                         ^three
#          ------------------               ------        -----------    -------------------
#          11                               12            2              3
#    ---------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_vol3o0/views/playing/ver1o0/__init__.py`
#           ---------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名


class PlayingView():
    """[OA24o1o0g7o0] 対局中ビュー"""

    web_socket_path = "/tic-tac-toe/v3.3/playing/"
    #                                ^three
    #                  --------------------------
    #                  1
    # 1. `ws://example.com/tic-tac-toe/v3.3/playing/Elephant/`
    #                     --------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_vol2o0.views.gui.playing.ver1o0.v_render import render_playing
        #                         ^two
        #    ----------------------------------------------------------        --------------
        #    1                                                                 2
        # 1. `src1/apps1/tic_tac_toe_vol2o0/views/gui/playing/ver1o0/v_render.py`
        #          ----------------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            PlayingView.web_socket_path,
            ViewOfPlayingV3g1o0.template_path,
            ViewOfPlayingV3g1o0.on_update,
            ViewOfPlayingV2g1o0.expected_pieces)

# EOF [OA24o1o0g7o0]
