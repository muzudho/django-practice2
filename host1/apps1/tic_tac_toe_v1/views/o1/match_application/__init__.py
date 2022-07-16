class MatchApplicationV():
    """対局申込ビュー"""

    _path_of_http_playing = "/tic-tac-toe/v1/playing/{0}/?&mypiece={1}"
    #                                      ^one
    #                        -----------------------------------------
    #                        1
    # 1. http://example.com:8000/tic-tac-toe/v1/playing/Elephant/?&mypiece=X
    #                           --------------------------------------------

    path_of_html = "tic_tac_toe_v1/o1/match_application.html"
    #                            ^one
    #               ----------------------------------------
    #               1
    # 1. host1/apps1/tic_tac_toe_v1/templates/tic_tac_toe_v1/o1/match_application.html
    #                                         ----------------------------------------

    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_match_application
        #    ---------        ------------------------
        #    1                2
        # 1. `host1/apps1/tic_tac_toe_v1/views/o1/match_application/v_render.py`
        #                                                           --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV._path_of_http_playing,
            MatchApplicationV.path_of_html)
