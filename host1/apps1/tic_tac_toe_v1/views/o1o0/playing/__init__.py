class PlayingV():
    """対局中ビュー"""

    path_of_html = "tic_tac_toe_v1/o1o0/playing.html"
    #                               ^two
    #               --------------------------------
    #               1
    # 1. `host1/apps1/tic_tac_toe_v1/templates/tic_tac_toe_v1/o1o0/playing.html`
    #                                          --------------------------------

    def render(request, room_name):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_playing
        #    ---------        --------------
        #    1                2
        # 1. `host1/apps1/tic_tac_toe_v1/views/o1o0/playing/v_render.py`
        #                                                   --------
        # 2. `1.` に含まれる関数

        return render_playing(request, room_name, PlayingV.path_of_html)
