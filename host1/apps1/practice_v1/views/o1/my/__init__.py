class MyV():
    """マイ ページ ビュー"""

    # マイ ページ
    _path_of_my_page = "practice_v1/o1/my.html"
    #                   ----------------------
    #                   1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o1/my.html` を取得
    #                                       ----------------------

    @staticmethod
    def render_my(request):
        """描画 - マイ ページ"""

        # 以下のファイルはあとで作ります
        from .v_my import render_my
        #    -----        ---------
        #    1            2
        # 1. `host1/apps1/practice_v1/views/o1/my/v_my.py`
        #                                         ----
        # 2. `1.` に含まれる関数

        return render_my(request, MyV._path_of_my_page)
