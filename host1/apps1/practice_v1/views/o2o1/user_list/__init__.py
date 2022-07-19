class UserListV():
    """会員一覧ビュー"""

    # そのページ
    _path_of_this_page = "practice_v1/o2o1/user_list.html"
    #                     -------------------------------
    #                     1
    # 1. host1/apps1/practice_v1/templates/practice_v1/o2o1/user_list.html を取得
    #                                      -------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_user_list
        #    ---------        ----------------
        #    1                2
        # 1. `host1/apps1/practice_v1/views/o2o1/user_list/v_render.py`
        #                                                  --------
        # 2. `1.` に含まれる関数

        return render_user_list(request, UserListV._path_of_this_page)
