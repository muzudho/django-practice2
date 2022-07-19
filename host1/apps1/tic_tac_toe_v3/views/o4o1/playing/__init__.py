# 以前のバージョン
from apps1.tic_tac_toe_v2.views.o2o1.gui.playing import PlayingV as PlayingVV2o2o1
#                       ^two
#          --------------                -------        --------    --------------
#          11                            12             2           3
#    -------------------------------------------
#    10
# 10. `host1/apps1/tic_tac_toe_v2/views/o2o1/gui/playing/__init__.py`
#            -------------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o2o1.playing import PlayingV as PlayingVV3o2o1
#                       ^three
#          --------------            -------        --------    --------------
#          11                        12             2           3
#    ---------------------------------------
#    10
# 10. `host1/apps1/tic_tac_toe_v3/views/o2o1/playing/__init__.py`
#            ---------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名


class PlayingV():
    """対局中ビュー"""

    path_of_ws_playing = "/tic-tac-toe/v3o4o1/playing/"
    #                                     ^four
    #                     ----------------------------
    #                     1
    # 1. `ws://example.com/tic-tac-toe/v3o4o1/playing/Elephant/`
    #                     ----------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o2o1.gui.playing.v_render import render_playing
        #                       ^two
        #    ----------------------------------------------------        --------------
        #    1                                                           2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o2o1/gui/playing/v_render.py`
        #           ----------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            PlayingV.path_of_ws_playing,
            PlayingVV3o2o1.path_of_html,
            PlayingVV3o2o1.on_update,
            PlayingVV2o2o1.expected_pieces)
