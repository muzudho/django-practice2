# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o1.playing import PlayingV as PlayingVV3o1
#    ----- -------------- ----------------        --------    ------------
#    1     2              3                       4           5
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. __init__.py ファイルに含まれるクラス名
# 5. '4.' の別名

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o3.playing import PlayingV as PlayingVV3o3
#    ----- -------------- ----------------        --------    ------------
#    1     2              3                       4           5
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. __init__.py ファイルに含まれるクラス名
# 5. '4.' の別名


# 対局中 - 駒
playing_expected_pieces = ['X', 'O', '_']


class PlayingV():

    path_of_html = "tic_tac_toe_v3/o4/playing.html.txt"
    #                            ^^^^three.four
    #               ----------------------------------
    #               1
    # 1. `host1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/o4/playing.html.txt`
    #                                          ----------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o1.gui.playing.v_render import render_playing
        #                       ^two
        #    --------------------------------------------------        --------------
        #    1                                                         2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o1/gui/playing/v_render.py`
        #           --------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            PlayingVV3o3.path_of_ws_playing,
            PlayingV.path_of_html,
            PlayingVV3o1.on_update,
            playing_expected_pieces)
        #   ^ Located in this file
