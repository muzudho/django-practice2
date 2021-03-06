class PlayingV():
    """対局中ビュー"""

    # 駒
    expected_pieces = ['X', 'O']

    # Webソケット v2
    path_of_ws_playing = "/tic-tac-toe/v2/playing/"
    #                                   ^two
    #                     ------------------------
    #                     1
    # 1. `ws://example.com:8000/tic-tac-toe/v2/playing/`
    #                          ------------------------

    # HTML
    path_of_html = "tic_tac_toe_v2/o1o0/gui/playing.html.txt"
    #                            ^two
    #               ----------------------------------------
    #               1
    # 1. `host1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/o1o0/gui/playing.html.txt`
    #                                          ----------------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_playing
        #    ---------        --------------
        #    1                2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o1o0/gui/playing/v_render.py`
        #                                                       --------
        # 2. `1.` に含まれる関数

        return render_playing(
            request,
            kw_room_name,
            PlayingV.path_of_ws_playing,
            PlayingV.path_of_html,
            PlayingV.on_update,
            PlayingV.expected_pieces)

    @staticmethod
    def on_update(request):
        """訪問後または送信後"""
        # 拡張したい挙動があれば、ここに書く
        pass
