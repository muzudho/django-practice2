# BOF [OA16o1o0gA15o0]

class PlayingView():
    """[OA16o1o0gA15o0] 対局中ビュー"""

    template_path = "tic_tac_toe_vol1o0/playing/ver1o0.html"
    #                                              ^one
    #                --------------------------------------
    #                1
    # 1. `src1/apps1/tic_tac_toe_vol1o0/templates/tic_tac_toe_vol1o0/playing/ver1o0.html`
    #                                             --------------------------------------

    def render(request, room_name):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_playing
        #    ---------        --------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_vol1o0/views/playing/v1o0/v_render.py`
        #                                                      --------
        # 2. `1.` に含まれる関数

        return render_playing(request, room_name, PlayingView.template_path)

# EOF [OA16o1o0gA15o0]
