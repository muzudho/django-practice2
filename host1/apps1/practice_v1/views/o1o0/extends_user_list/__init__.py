class ExtendsUserListV():
    """（拡張済）会員一覧ビュー"""

    # そのページ
    _path_of_this_page = "practice/v0o0o1/extends_user_list.html"
    #                     --------------------------------------
    #                     1
    # 1. `host1/apps1/portal/templates/practice/v0o0o1/extends_user_list.html` を取得
    #                                  --------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_extends_user_list
        #    ---------        ------------------------
        #    1                2
        # 1. `host1/apps1/portal/views/v0o0o1/extends_user_list/v_render.py`
        #                                                       --------
        # 2. `1.` に含まれる関数

        return render_extends_user_list(request, ExtendsUserListV._path_of_this_page)
