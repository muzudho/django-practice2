class MyV():
    """OA19o1o0g3o0 マイ ページ ビュー"""

    # マイ ページ
    _path_of_my_page = "practice_v1/my/v1o0.html"
    #                   ------------------------
    #                   1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/my/v1o0.html` を取得
    #                                      ------------------------

    @staticmethod
    def render_my(request):
        """OA19o1o0g3o0 描画 - マイ ページ"""

        # 以下のファイルはあとで作ります
        from .v_my import render_my
        #    -----        ---------
        #    1            2
        # 1. `src1/apps1/practice_v1/views/my/v1o0/v_my.py`
        #                                          ----
        # 2. `1.` に含まれる関数

        return render_my(request, MyV._path_of_my_page)