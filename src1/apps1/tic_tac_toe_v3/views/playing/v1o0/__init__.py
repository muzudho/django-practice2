# BOF OA22o1o0g9o0

# 〇×ゲーム v2
from apps1.tic_tac_toe_vol2o0.views.gui.playing.ver1o0 import PlayingV as PlayingVV2g1o0
#                         ^two
#          ------------------                   ------        --------    --------------
#          11                                   12            2           3
#    -------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_vol2o0/views/gui/playing/ver1o0/__init__.py`
#           -------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名


class PlayingV():
    """OA22o1o0g9o0 対局中ビュー"""

    web_socket_path = "/tic-tac-toe/v2/playing/"
    #                                ^two
    #                  ------------------------
    #                  1
    # 1. `ws://example.com:8000/tic-tac-toe/v2/playing/`
    #                          ------------------------

    template_path = "tic_tac_toe_v3/playing/v1o0.html.txt"
    #                             ^three
    #                ------------------------------------
    #                1
    # 1. `src1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/playing/v1o0.html.txt`
    #                                         ------------------------------------

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
            PlayingV.web_socket_path,
            PlayingV.template_path,
            PlayingV.on_update,
            PlayingVV2g1o0.expected_pieces)

    @staticmethod
    def on_update(request):
        """訪問後または送信後"""
        # 何もしません
        pass

# EOF OA22o1o0g9o0
