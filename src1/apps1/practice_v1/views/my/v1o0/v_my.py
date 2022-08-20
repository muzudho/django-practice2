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

        'dj_lobbyPath': '/practice/v1/lobby/',
        #                -------------------
        #                1
        # 1. http://example.com/practice/v1/lobby/
        #                      -------------------

        'dj_ticTacToePath': '/tic-tac-toe/v2/match-application/',
        #                    ----------------------------------
        #                    1
        # 1. http://example.com/tic-tac-toe/v2/match-application/
        #                      ----------------------------------

        'dj_loginPath': '/accounts/v1/login/',
        #                -------------------
        #                1
        # 1. http://example.com/accounts/v1/login/
        #                      -------------------

        'dj_logoutPath': '/accounts/v1/logout/',
        #                 --------------------
        #                 1
        # 1. http://example.com/accounts/v1/logout/
        #                      --------------------
    }

    return render(request, my_page_tp, context)

# EOF OA19o1o0g4o0
