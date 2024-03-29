# BOF [OA16o1o0gA13o0]

class MatchApplicationView():
    """[OA16o1o0gA13o0] 対局申込ビュー"""

    playing_web_path = "/tic-tac-toe/vol1.0/playing/ver1.0/{0}/?&mypiece={1}"
    #                                   ^one
    #                   ----------------------------------------------------
    #                   1
    # 1. `http://example.com:8000/tic-tac-toe/vol1.0/playing/ver1.0/Elephant/?&mypiece=X`
    #                            -------------------------------------------------------

    template_path = "tic_tac_toe_vol1o0/match_application/ver1o0.html"
    #                               ^one
    #                ------------------------------------------------
    #                1
    # 1. src1/apps1/tic_tac_toe_vol1o0/templates/tic_tac_toe_vol1o0/match_application/ver1o0.html
    #                                            ------------------------------------------------

    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_match_application
        #    ---------        ------------------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_vol1o0/views/match_application/v1o0/v_render.py`
        #                                                                --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationView.playing_web_path,
            MatchApplicationView.template_path)

# EOF [OA16o1o0gA13o0]
