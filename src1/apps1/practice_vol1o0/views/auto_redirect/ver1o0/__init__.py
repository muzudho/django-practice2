class AutoRedirectV():
    """OA21o2o0g4o0 リダイレクト ビュー"""

    # 自動リダイレクト ページ
    _path_of_redirecter_page = "practice_v1/auto_reload/v1o1o0.html.txt"
    #                                                    ^^^one o one
    #                           ---------------------------------------
    #                           1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/auto_reload/o1o1o0.html.txt` を取得
    #                                      ---------------------------------------

    @staticmethod
    def render_auto_redirect(request):
        """描画 - 自動リダイレクト"""

        # 以下のファイルはあとで作ります
        from .v_redirect import render_auto_redirect
        #    -----------        --------------------
        #    1                  2
        # 1. `src1/apps1/practice_v1/views/auto_redirect/v1o0/v_redirect.py`
        #                                                     ----------
        # 2. `1.` に含まれる関数

        return render_auto_redirect(request, AutoRedirectV._path_of_redirecter_page)
