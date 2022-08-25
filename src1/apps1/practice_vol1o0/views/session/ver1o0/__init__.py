class SessionV():
    """O9o3o0g5o0 練習1.0巻 セッション1.0版"""

    # このページ
    _path_of_this_page = "practice_vol1o0/active_user_list/ver1o0.html"
    #                     --------------------------------------------
    #                     1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/active_user_list/ver1o0.html` を取得
    #                                          --------------------------------------------

    @staticmethod
    def render(request):
        """O9o3o0g5o0 練習1.0巻 セッション1.0版 - 描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_active_user_list
        #    ---------        -----------------------
        #    1                2
        # 1. `src1/apps1/practice_vol1o0/views/session/ver1o0/v_render.py`
        #                                                     --------
        # 2. `1.` に含まれる関数

        return render_active_user_list(request, SessionV._path_of_this_page)
