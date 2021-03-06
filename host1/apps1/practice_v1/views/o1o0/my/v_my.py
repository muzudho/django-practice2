from django.http import HttpResponse
from django.template import loader


def render_my(request, path_of_my_page):
    """描画 - マイ ページ"""
    template = loader.get_template(path_of_my_page)

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

    return HttpResponse(template.render(context, request))
