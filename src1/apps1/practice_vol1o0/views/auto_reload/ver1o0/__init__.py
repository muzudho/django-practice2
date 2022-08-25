# BOF OA21o1o0g5o0

class AutoReloadV():
    """OA21o1o0g5o0 自動再読込ビュー"""

    # 自動再読込ページ
    _path_of_auto_reload_page = "practice_vol1o0/auto_reload/ver1o0.html"
    #                            ---------------------------------------
    #                            1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/auto_reload/ver1o0.html` を取得
    #                                          ---------------------------------------

    @staticmethod
    def render_auto_reload(request):
        """描画 - 自動再読込"""

        # 以下のファイルはあとで作ります
        from .v_auto_reload import render_auto_reload
        #    --------------        ------------------
        #    1                     2
        # 1. `src1/apps1/practice_vol1o0/views/auto_reload/ver1o0/v_auto_reload.py`
        #                                                         -------------
        # 2. `1.` に含まれる関数

        return render_auto_reload(request, AutoReloadV._path_of_auto_reload_page)

# EOF OA21o1o0g5o0
