class RoomV():
    """対局部屋ビュー"""

    # 一覧ページ
    _path_of_list_page = "practice/v0o0o1/room/list.html"
    #                     ------------------------------
    #                     1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/room/list.html` を取得
    #                                    ------------------------------

    # 詳細ページ
    _path_of_read_page = "practice/v0o0o1/room/read.html"
    #                     ------------------------------
    #                     1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/room/read.html` を取得
    #                                    ------------------------------

    @staticmethod
    def render_list(request):
        """描画 - 一覧"""

        # 以下のファイルはあとで作ります
        from .v_list import render_list
        #    -------        -----------
        #    1              2
        # 1. `host1/apps1/practice/views/v0o0o1/room/v_list.py`
        #                                            ------
        # 2. `1.` に含まれる関数

        return render_list(request, RoomV._path_of_list_page)

    @staticmethod
    def render_read(request, id):
        """描画 - 詳細"""

        # 以下のファイルはあとで作ります
        from .v_read import render_read
        #    -------        -----------
        #    1              2
        # 1. `host1/apps1/practice/views/v0o0o1/room/v_read.py`
        #                                            ------
        # 2. `1.` に含まれる関数

        return render_read(request, id, RoomV._path_of_read_page)
