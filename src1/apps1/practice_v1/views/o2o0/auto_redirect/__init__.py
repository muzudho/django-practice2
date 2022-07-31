class AutoRedirectV():
    """リダイレクト ビュー"""

    # 自動リダイレクト ページ
    _path_of_redirecter_page = "practice_v1/o2o0/auto_reload_with_redirect.html.txt"
    #                                        ^three
    #                           ---------------------------------------------------
    #                           1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/o2o0/auto_reload_with_redirect.html.txt` を取得
    #                                      ---------------------------------------------------

    @staticmethod
    def render_auto_redirect(request):
        """描画 - 自動リダイレクト"""

        # 以下のファイルはあとで作ります
        from .v_redirect import render_auto_redirect
        #    -----------        --------------------
        #    1                  2
        # 1. `src1/apps1/practice_v1/views/o2o0/auto_redirect/v_redirect.py`
        #                                                     ----------
        # 2. `1.` に含まれる関数

        return render_auto_redirect(request, AutoRedirectV._path_of_redirecter_page)
