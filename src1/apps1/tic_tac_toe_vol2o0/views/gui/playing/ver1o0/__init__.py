# BOF [OA16o3o0gA13o0]

class PlayingView():
    """[OA16o3o0gA13o0] 対局中ビュー"""

    # 駒
    expected_pieces = ['X', 'O']

    # 〇×ゲーム2.0巻 対局中 Webソケット
    web_socket_path = "/tic-tac-toe/v2/playing/"
    #                                ^two
    #                  ------------------------
    #                  1
    # 1. `ws://example.com:8000/tic-tac-toe/v2/playing/`
    #                          ------------------------

    # 〇×ゲーム2.0巻 対局中 HTML 1.1.0版
    template_path = "tic_tac_toe_vol2o0/gui/playing/ver1o1o0.html.txt"
    #                               ^two
    #                ------------------------------------------------
    #                1
    # 1. `src1/apps1/tic_tac_toe_vol2o0/templates/tic_tac_toe_vol2o0/gui/playing/ver1o1o0.html.txt`
    #                                             ------------------------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_playing
        #    ---------        --------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_vol2o0/views/gui/playing/ver1o0/v_render.py`
        #                                                            --------
        # 2. `1.` に含まれる関数

        return render_playing(
            request,
            kw_room_name,
            PlayingView.web_socket_path,
            PlayingView.template_path,
            PlayingView.on_update,
            PlayingView.expected_pieces)

    @staticmethod
    def on_update(request):
        """訪問後または送信後"""
        # 拡張したい挙動があれば、ここに書く
        pass

# EOF [OA16o3o0gA13o0]
