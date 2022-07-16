import datetime
from django.shortcuts import render


def render_auto_redirect(request, path_of_redirecter_page):
    """描画 - 自動リダイレクト ページ"""

    # 現在日時
    dt_now = datetime.datetime.now()

    # 今何分？
    dt_minute = dt_now.minute

    # 5 で割り切れる分なら、リダイレクト
    if dt_minute % 5 == 0:
        redirect_path = "/tic-tac-toe/v2/match-application/"
        #                ----------------------------------
        #                1
        # 1. `http://example.com/tic-tac-toe/v2/match-application/`
        #                       ----------------------------------
    else:
        # リダイレクトしたくないときは空文字列を送る、と取り決めておきます
        redirect_path = ""

    context = {
        # FIXME 相対パス。 URL を urls.py で変更したいとき、反映されないがどうするか？
        "dj_redirect_path": redirect_path,
    }

    return render(request, path_of_redirecter_page, context)
