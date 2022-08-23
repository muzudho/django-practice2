# BOF OA16o1o0gA16o0

from django.http import Http404
from django.shortcuts import render


def render_playing(request, room_name, playing_tp):
    """OA16o1o0gA16o0 描画 - 対局

    Parameters
    ----------
    playing_tp : str
        Template path
    """

    myPiece = request.GET.get("mypiece")
    if myPiece not in ['X', 'O']:
        raise Http404(f"My piece '{myPiece}' does not exists")

    context = {
        "my_piece": myPiece,
        "room_name": room_name
    }
    return render(request, playing_tp, context)

# EOF OA16o1o0gA16o0
