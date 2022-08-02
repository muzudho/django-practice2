class SessionV():
    """O9o3o0g5o0 セッション ビュー"""

    # そのページ
    _path_of_this_page = "practice_v1/active_user_list/v1o0.html"
    #                     --------------------------------------
    #                     1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/active_user_list/v1o0.html` を取得
    #                                      --------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_active_user_list
        #    ---------        -----------------------
        #    1                2
        # 1. `src1/apps1/practice_v1/views/session/v1o0/v_render.py`
        #                                               --------
        # 2. `1.` に含まれる関数

        return render_active_user_list(request, SessionV._path_of_this_page)
