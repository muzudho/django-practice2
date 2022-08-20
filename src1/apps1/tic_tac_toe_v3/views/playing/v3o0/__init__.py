# BOF OA24o1o0g7o0

# 〇×ゲーム v2 対局中 v1.0
from apps1.tic_tac_toe_v2.views.gui.playing.v1o0 import PlayingV as PlayingVV2g1o0
#                       ^two
#          --------------                -------        --------    --------------
#          11                            12             2           3
#    -------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v2/views/gui/playing/v1o0/__init__.py`
#           -------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3 対局中 v1.0
from apps1.tic_tac_toe_v3.views.playing.v1o0 import PlayingV as PlayingVV3g1o0
#                       ^three
#          --------------               ----        --------    --------------
#          11                           12          2           3
#    ---------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v3/views/o1o0/playing/__init__.py`
#           ---------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名


class PlayingV():
    """OA24o1o0g7o0 対局中ビュー"""

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
        from apps1.tic_tac_toe_v2.views.gui.playing.v1o0.v_render import render_playing
        #                       ^two
        #    ----------------------------------------------------        --------------
        #    1                                                           2
        # 1. `src1/apps1/tic_tac_toe_v2/views/gui/playing/v1o0/v_render.py`
        #          ----------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            PlayingV.web_socket_path,
            PlayingVV3g1o0.template_path,
            PlayingVV3g1o0.on_update,
            PlayingVV2g1o0.expected_pieces)

# EOF OA24o1o0g7o0
