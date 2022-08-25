class UserListV():
    """O9o1o0g5o0 練習1.0巻 会員一覧1.0版"""

    # そのページ
    _path_of_this_page = "practice_vol1o0/user_list/ver1o0.html"
    #                     -------------------------------------
    #                     1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/user_list/ver1o0.html` を取得
    #                                          -------------------------------------

    @staticmethod
    def render(request):
        """O9o1o0g5o0 練習1.0巻 会員一覧1.0版 描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_user_list
        #    ---------        ----------------
        #    1                2
        # 1. `src1/apps1/practice_vol1o0/views/user_list/ver1o0/v_render.py`
        #                                                       --------
        # 2. `1.` に含まれる関数

        return render_user_list(request, UserListV._path_of_this_page)
