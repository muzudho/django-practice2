class PlayingV():
    """OA16o3o0gA13o0 対局中ビュー"""

    # 駒
    expected_pieces = ['X', 'O']

    # Webソケット v2
    path_of_web_socket = "/tic-tac-toe/v2/playing/"
    #                                   ^two
    #                     ------------------------
    #                     1
    # 1. `ws://example.com:8000/tic-tac-toe/v2/playing/`
    #                          ------------------------

    # HTML
    path_of_local_html = "tic_tac_toe_v2/gui/playing/v1o1o0.html.txt"
    #                                  ^two
    #                     ------------------------------------------
    #                     1
    # 1. `src1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/gui/playing/v1o1o0.html.txt`
    #                                         ------------------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_playing
        #    ---------        --------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_v2/views/gui/playing/v1o0/v_render.py`
        #                                                      --------
        # 2. `1.` に含まれる関数

        return render_playing(
            request,
            kw_room_name,
            PlayingV.path_of_web_socket,
            PlayingV.path_of_local_html,
            PlayingV.on_update,
            PlayingV.expected_pieces)

    @staticmethod
    def on_update(request):
        """訪問後または送信後"""
        # 拡張したい挙動があれば、ここに書く
        pass
