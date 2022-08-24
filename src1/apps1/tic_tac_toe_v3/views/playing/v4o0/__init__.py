# BOF OA25o1o0g4o0

# 〇×ゲーム v3 対局中 v1.0
from apps1.tic_tac_toe_v3.views.playing.v1o0 import PlayingV as PlayingVV3o1o0
#          --------------               ----        --------    --------------
#          11                           12          2           3
#    ---------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v3/views/playing/v1o0/__init__.py`
#           ---------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名

# 〇×ゲーム v3 対局中 v3.0
from apps1.tic_tac_toe_v3.views.playing.v3o0 import PlayingV as PlayingVV3o3o0
#          --------------               ----        --------    --------------
#          11                           12          2           3
#    ---------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v3/views/playing/v3o0/__init__.py`
#           ---------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class PlayingV():
    """OA25o1o0g4o0 対局中ビュー"""

    # 駒
    expected_pieces = ['X', 'O', '_']

    template_path = "tic_tac_toe_v3/playing/v4o0.html.txt"
    #                                        ^four
    #                ------------------------------------
    #                1
    # 1. `src1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/playing/v4o0.html.txt`
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
            PlayingVV3o3o0.web_socket_path,
            PlayingV.template_path,
            PlayingVV3o1o0.on_update,
            PlayingV.expected_pieces)

# EOF OA25o1o0g4o0
