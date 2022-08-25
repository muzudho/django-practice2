class RoomV():
    """OA18o2o0g5o0 対局部屋ビュー"""

    # OA18o2o0g5o0 練習1.0巻 一覧ページ1.0版
    _path_of_list_page = "practice_vol1o0/room/list/ver1o0.html"
    #                     -------------------------------------
    #                     1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/room/list/ver1o0.html` を取得
    #                                          -------------------------------------

    # OA18o3o0g3o0 練習1.0巻 詳細ページ1.0版
    _path_of_read_page = "practice_vol1o0/room/read/ver1o0.html"
    #                     -------------------------------------
    #                     1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/room/read/ver1o0.html` を取得
    #                                          -------------------------------------

    # OA18o4o0g3o0 練習1.0巻 削除1.0版
    _path_of_delete_page = "practice_vol1o0/room/delete/ver1o0.html"
    #                       ---------------------------------------
    #                       1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/room/delete/ver1o0.html` を取得
    #                                          ---------------------------------------

    # OA18o5o0g4o0 練習1.0巻 新規作成または更新1.0版
    _path_of_upsert_page = "practice_vol1o0/room/upsert/ver1o0.html"
    #                       ---------------------------------------
    #                       1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/room/upsert/ver1o0.html` を取得
    #                                          ---------------------------------------

    @staticmethod
    def render_list(request):
        """OA18o2o0g5o0 練習1.0巻 一覧ページ1.0版"""

        # 以下のファイルはあとで作ります
        from ..list.ver1o0 import render_list
        #    -------------        -----------
        #    1                    2
        # 1. `src1/apps1/practice_vol1o0/views/room/list/ver1o0.py`
        #                                           -----------
        # 2. `1.` に含まれる関数

        return render_list(request, RoomV._path_of_list_page)

    @staticmethod
    def render_read(request, id):
        """OA18o3o0g3o0 練習1.0巻 詳細ページ1.0版"""

        # 以下のファイルはあとで作ります
        from ..read.ver1o0 import render_read
        #    -------------        -----------
        #    1                    2
        # 1. `src1/apps1/practice_vol1o0/views/room/read/ver1o0.py`
        #                                           -----------
        # 2. `1.` に含まれる関数

        return render_read(request, id, RoomV._path_of_read_page)

    @staticmethod
    def render_delete(request, id):
        """OA18o4o0g3o0 練習1.0巻 削除1.0版"""

        # 以下のファイルはあとで作ります
        from ..delete.ver1o0 import render_delete
        #    ---------------        -------------
        #    1                      2
        # 1. `src1/apps1/practice_vol1o0/views/room/delete/ver1o0.py`
        #                                           -------------
        # 2. `1.` に含まれる関数

        return render_delete(request, id, RoomV._path_of_delete_page)

    @staticmethod
    def render_upsert(request, id=None):
        """OA18o5o0g4o0 練習1.0巻 新規作成または更新1.0版"""

        # 以下のファイルはあとで作ります
        from ..upsert.ver1o0 import render_upsert
        #    ---------------        -------------
        #    1                      2
        # 1. `src1/apps1/practice_vol1o0/views/room/upsert/ver1o0.py`
        #                                           -------------
        # 2. `1.` に含まれる関数

        return render_upsert(request, id, RoomV._path_of_upsert_page)
