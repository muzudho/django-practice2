class RoomV():
    """OA18o2o0g5o0 対局部屋ビュー"""

    # OA18o2o0g5o0 一覧ページ
    _path_of_list_page = "practice_v1/room/list/v1o0.html"
    #                     -------------------------------
    #                     1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/room/list/v1o0.html` を取得
    #                                      -------------------------------

    # 詳細ページ
    _path_of_read_page = "practice_v1/room/read/v1o0.html"
    #                     -------------------------------
    #                     1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/room/read/v1o0.html` を取得
    #                                      -------------------------------

    # 削除ページ
    _path_of_delete_page = "practice_v1/room/delete/v1o0.html"
    #                       ---------------------------------
    #                       1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/room/delete/v1o0.html` を取得
    #                                      ---------------------------------

    # 新規作成または更新のページ
    _path_of_upsert_page = "practice_v1/room/upsert/v1o0.html"
    #                       ---------------------------------
    #                       1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/room/upsert/v1o0.html` を取得
    #                                      ---------------------------------

    @staticmethod
    def render_list(request):
        """OA18o2o0g5o0 描画 - 一覧"""

        # 以下のファイルはあとで作ります
        from ..list.v1o0 import render_list
        #    -----------        -----------
        #    1                  2
        # 1. `src1/apps1/practice_v1/views/room/list/v1o0.py`
        #                                       ---------
        # 2. `1.` に含まれる関数

        return render_list(request, RoomV._path_of_list_page)

    @staticmethod
    def render_read(request, id):
        """描画 - 詳細"""

        # 以下のファイルはあとで作ります
        from ..read.v1o0 import render_read
        #    -----------        -----------
        #    1                  2
        # 1. `src1/apps1/practice_v1/views/room/read/v1o0.py`
        #                                       ---------
        # 2. `1.` に含まれる関数

        return render_read(request, id, RoomV._path_of_read_page)

    @staticmethod
    def render_delete(request, id):
        """描画 - 削除"""

        # 以下のファイルはあとで作ります
        from ..delete.v1o0 import render_delete
        #    -------------        -------------
        #    1                    2
        # 1. `src1/apps1/practice_v1/views/room/delete/v1o0.py`
        #                                       -----------
        # 2. `1.` に含まれる関数

        return render_delete(request, id, RoomV._path_of_delete_page)

    @staticmethod
    def render_upsert(request, id=None):
        """新規作成または更新のページ"""

        # 以下のファイルはあとで作ります
        from ..upsert.v1o0 import render_upsert
        #    -------------        -------------
        #    1                    2
        # 1. `src1/apps1/practice_v1/views/room/upsert/v1o0.py`
        #                                       -----------
        # 2. `1.` に含まれる関数

        return render_upsert(request, id, RoomV._path_of_upsert_page)
