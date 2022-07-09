from django.http import HttpResponse
from django.template import loader


class MyV():
    """マイ ページ ビュー"""

    # マイ ページ
    _path_of_my_page = "practice/v0o0o1/my.html"
    #                   ----------------------------
    #                   1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/my.html` を取得
    #                                    -----------------------

    @staticmethod
    def render_my(request):
        """描画 - マイ ページ"""

        # 以下のファイルはあとで作ります
        from .v_my import render_my
        #    -----        ---------
        #    1            2
        # 1. `host1/apps1/practice/views/v0o0o1/my/v_my.py`
        #                                          ----
        # 2. `1.` に含まれる関数

        return render_my(request, MyV._path_of_my_page)
