class AutoReloadV():
    """OA21o1o0g5o0 自動再読込ビュー"""

    # 自動再読込ページ
    _path_of_auto_reload_page = "practice_v1/auto_reload/v1o0.html"
    #                            ---------------------------------
    #                            1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/auto_reload/v1o0.html` を取得
    #                                      ---------------------------------

    @staticmethod
    def render_auto_reload(request):
        """描画 - 自動再読込"""

        # 以下のファイルはあとで作ります
        from .v_auto_reload import render_auto_reload
        #    --------------        ------------------
        #    1                     2
        # 1. `src1/apps1/practice_v1/views/auto_reload/v1o0/v_auto_reload.py`
        #                                                   -------------
        # 2. `1.` に含まれる関数

        return render_auto_reload(request, AutoReloadV._path_of_auto_reload_page)
