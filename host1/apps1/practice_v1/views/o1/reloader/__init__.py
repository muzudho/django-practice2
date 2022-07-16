class ReloaderV():
    """自動再読込ビュー"""

    # 自動再読込ページ
    _path_of_reloader_page = "practice_v1/o1/reloader.html"
    #                                  -----------------------------
    #                                  1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o1/reloader.html` を取得
    #                                    -----------------------------

    @staticmethod
    def render_reloader(request):
        """描画 - 自動再読込"""

        # 以下のファイルはあとで作ります
        from .v_reloader import render_reloader
        #    -----------        ---------------
        #    1                  2
        # 1. `host1/apps1/practice_v1/views/o1/reloader/v_reloader.py`
        #                                               ----------
        # 2. `1.` に含まれる関数

        return render_reloader(request, ReloaderV._path_of_reloader_page)
