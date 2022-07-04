"""〇×ゲーム v1.0.1"""
from django.http import Http404
from django.shortcuts import render, redirect


# 以下、リソース


class MatchApplication():
    """対局申込"""

    _path_of_http_playing = "/tic-tac-toe/v1o0o1/playing/{0}/?&mypiece={1}"
    #                                      ^^^ one.zero.one
    #                        ---------------------------------------------
    #                        1
    # 1. http://example.com:8000/tic-tac-toe/v1o0o1/playing/Elephant/?&mypiece=X
    #                           ------------------------------------------------

    _path_of_html = "tic_tac_toe_v1/o0o1/match_application.html"
    #                                ^^^zero.one
    #                -----------------------------------------
    #                1
    # 1. host1/apps1/tic_tac_toe_v1/templates/tic_tac_toe_v1/o0o1/match_application.html
    #                                         ------------------------------------------

    def render(request):
        """描画"""
        return render_match_application(request, MatchApplication._path_of_http_playing, MatchApplication._path_of_html)


class Playing():
    """対局"""

    _path_of_html = "tic_tac_toe_v1/o0o1/playing.html"
    #                                ^^^ zero.one
    #                --------------------------------
    #                1
    # 1. `host1/apps1/tic_tac_toe_v1/templates/tic_tac_toe_v1/o0o1/playing.html`
    #                                          --------------------------------

    def render(request, room_name):
        """描画"""
        return render_playing(request, room_name, Playing._path_of_html)


# 以下、関数


def render_match_application(request, path_of_http_playing, path_of_html):
    """対局申込 - 描画"""

    if request.method == "POST":
        # 送信後
        room_name = request.POST.get("room_name")
        myPiece = request.POST.get("my_piece")
        # TODO バリデーションチェックしたい
        return redirect(path_of_http_playing.format(room_name, myPiece))

    # 訪問後
    return render(request, path_of_html, {})


def render_playing(request, room_name, path_of_html):
    """対局 - 描画"""

    myPiece = request.GET.get("mypiece")
    if myPiece not in ['X', 'O']:
        raise Http404(f"My piece '{myPiece}' does not exists")

    context = {
        "my_piece": myPiece,
        "room_name": room_name
    }
    return render(request, path_of_html, context)
