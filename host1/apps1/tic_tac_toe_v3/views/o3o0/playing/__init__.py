# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o1o0.playing import PlayingV as V3o0o1PlayingV
#    ----- -------------- ------------------        --------    --------------
#    1     2              3                         4           5
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. __init__.py ファイルに含まれるクラス名
# 5. '4.' の別名


class PlayingV():
    """対局中ビュー"""

    path_of_ws_playing = "/tic-tac-toe/v3o0o3/playing/"
    #                                   ^^^^^ three.zero.three
    #                     ----------------------------
    #                     1
    # 1. `ws://example.com/tic-tac-toe/v3o0o3/playing/Elephant/`
    #                     ----------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o1o0.gui.playing import playing_expected_pieces
        #                       ^two
        #    -------------------------------------------        -----------------------
        #    1                                                  2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o1o0/gui/playing/__init__.py`
        #           -------------------------------------------
        # 2. `1.` の `__init__.py` ファイルに含まれる playing_expected_pieces 変数

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
            V3o0o1PlayingV.path_of_html,
            V3o0o1PlayingV.on_update,
            playing_expected_pieces)
