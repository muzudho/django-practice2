class PlayingV():
    """対局中ビュー"""

    path_of_ws_playing = "/tic-tac-toe/v2o0o1/playing/"
    #                                   ^ two
    #                     ----------------------------
    #                     1
    # 1. `ws://example.com:8000/tic-tac-toe/v2o0o1/playing/`
    #                          ---------------------------

    path_of_html = "tic_tac_toe_v3/o0o1/playing.html.txt"
    #                            ^ three
    #               ------------------------------------
    #               1
    # 1. `host1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/o0o1/playing.html.txt`
    #                                          ------------------------------------

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
            PlayingV.path_of_html,
            PlayingV.on_update,
            playing_expected_pieces)

    @staticmethod
    def on_update(request):
        """訪問後または送信後"""
        # 拡張したい挙動があれば、ここに書く
        pass
