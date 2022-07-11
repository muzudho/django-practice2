# 以下、よく使う定型データ


# 対局中 - 駒
playing_expected_pieces = ['X', 'O']


# 以下、ロジック


class Playing():
    """対局中"""

    _path_of_ws_playing = "/tic-tac-toe/v2o0o1/playing/"
    #                                    ^ two
    #                      ----------------------------
    #                      1
    # 1. `ws://example.com:8000/tic-tac-toe/v2o0o1/playing/`
    #                          ---------------------------

    _path_of_html = "tic_tac_toe_v2/o0o1/gui/playing.html.txt"
    #                             ^ two
    #                ----------------------------------------
    #                1
    # 1. `host1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/o0o1/gui/playing.html.txt`
    #                                          ----------------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_playing
        #    ---------        --------------
        #    1                2
        # 1. `host1/apps1/tic_tac_toe_v2/views/v2o0o1/gui/playing/v_render.py`
        #                                                         --------
        # 2. `1.` に含まれる関数

        return render_playing(
            request,
            kw_room_name,
            Playing._path_of_ws_playing,
            Playing._path_of_html,
            Playing.on_update,
            playing_expected_pieces)

    @staticmethod
    def on_update(request):
        """訪問後または送信後"""
        # 拡張したい挙動があれば、ここに書く
        pass
