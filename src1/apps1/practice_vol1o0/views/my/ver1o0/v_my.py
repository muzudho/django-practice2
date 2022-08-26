# BOF OA19o1o0g4o0

from django.shortcuts import render


def render_my(request, my_page_tp):
    """OA19o1o0g4o0 描画 - マイ ページ

    Parameters
    ----------
    my_page_tp : str
        Template path
    """

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        'dj_user': request.user,

        'dj_lobbyPath': '/practice/vol1.0/lobby/ver1.0/',
        #                ------------------------------
        #                1
        # 1. http://example.com/practice/vol1.0/lobby/ver1.0/
        #                      ------------------------------

        'dj_ticTacToePath': '/tic-tac-toe/vol2.0/match-application/ver1.0/',
        #                    ---------------------------------------------
        #                    1
        # 1. http://example.com/tic-tac-toe/vol2.0/match-application/ver1.0/
        #                      ---------------------------------------------

        'dj_loginPath': '/accounts/vol1.0/login/',
        #                -----------------------
        #                1
        # 1. http://example.com/accounts/vol1.0/login/
        #                      -----------------------

        'dj_logoutPath': '/accounts/vol1.0/logout/',
        #                 ------------------------
        #                 1
        # 1. http://example.com/accounts/vol1.0/logout/
        #                      ------------------------
    }

    return render(request, my_page_tp, context)

# EOF OA19o1o0g4o0
