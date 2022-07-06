class SessionV():

    # そのページ
    _path_of_this_page = "practice/v0o0o1/active-user-list.html"
    #                     -------------------------------------
    #                     1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/active-user-list.html` を取得
    #                                    -------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_active_user_list
        #    ---------        ------------------------
        #    1                2
        # 1. `host1/apps1/practice/views/v0o0o1/session/v_render.py`
        #                                               --------
        # 2. `1.` に含まれる関数

        return render_active_user_list(request, SessionV._path_of_this_page)
