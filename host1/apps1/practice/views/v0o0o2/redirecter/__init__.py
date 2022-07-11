class RedirecterV():
    """リダイレクト ビュー"""

    # 自動リダイレクト ページ
    _path_of_redirecter_page = "practice/v0o0o2/reloader_with_redirect.html.txt"
    #                                         ^two
    #                           -----------------------------------------------
    #                           1
    # 1. `host1/apps1/practice/templates/practice/v0o0o2/reloader_with_redirect.html.txt` を取得
    #                                    -----------------------------------------------

    @staticmethod
    def render_redirect(request):
        """描画 - 自動リダイレクト"""

        # 以下のファイルはあとで作ります
        from .v_redirect import render_redirect
        #    -----------        ---------------
        #    1                  2
        # 1. `host1/apps1/practice/views/v0o0o2/redirecter/v_redirect.py`
        #                                                  ----------
        # 2. `1.` に含まれる関数

        return render_redirect(request, RedirecterV._path_of_redirecter_page)
