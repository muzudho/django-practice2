from django.http import Http404
from django.shortcuts import render


def render_playing(request, room_name, path_of_html):
    """描画 - 対局"""

    myPiece = request.GET.get("mypiece")
    if myPiece not in ['X', 'O']:
        raise Http404(f"My piece '{myPiece}' does not exists")

    context = {
        "my_piece": myPiece,
        "room_name": room_name
    }
    return render(request, path_of_html, context)
