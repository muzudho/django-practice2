class Playing():
    """対局"""

    _path_of_html = "tic_tac_toe_v1/o0o1/playing.html"
    #                                ^^^ zero.one
    #                --------------------------------
    #                1
    # 1. `host1/apps1/tic_tac_toe_v1/templates/tic_tac_toe_v1/o0o1/playing.html`
    #                                          --------------------------------

    def render(request, room_name):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_playing
        #    ---------        --------------
        #    1                2
        # 1. `host1/apps1/tic_tac_toe_v1/views/v1o0o1/playing/v_render.py`
        #                                                     --------
        # 2. `1.` に含まれる関数

        return render_playing(request, room_name, Playing._path_of_html)
