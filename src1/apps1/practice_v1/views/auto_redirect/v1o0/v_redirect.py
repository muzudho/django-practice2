# BOF OA21o2o0g5o0

import datetime
from django.shortcuts import render


def render_auto_redirect(request, auto_redirect_tp):
    """OA21o2o0g5o0 描画 - 自動リダイレクト ページ

    Parameters
    ----------
    auto_redirect_tp : str
        Template path
    """

    # 現在日時
    dt_now = datetime.datetime.now()

    # 今何分？
    dt_minute = dt_now.minute

    # 5 で割り切れる分なら、リダイレクト
    if dt_minute % 5 == 0:
        redirect_path = "/tic-tac-toe/vol2.0/ver1.0/match-application/"
        #                ---------------------------------------------
        #                1
        # 1. `http://example.com/tic-tac-toe/vol2.0/ver1.0/match-application/`
        #                       ---------------------------------------------
    else:
        # リダイレクトしたくないときは空文字列を送る、と取り決めておきます
        redirect_path = ""

    context = {
        # FIXME 相対パス。 URL を urls.py で変更したいとき、反映されないがどうするか？
        "dj_redirect_path": redirect_path,
    }

    return render(request, auto_redirect_tp, context)

# EOF OA21o2o0g5o0
