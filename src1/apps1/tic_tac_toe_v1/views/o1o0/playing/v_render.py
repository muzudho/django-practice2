from django.http import Http404
from django.shortcuts import render


def render_playing(request, room_name, lp_playing):
    """OA16o1o0gA16o0 描画 - 対局

    Parameters
    ----------
    lp_playing : str
        Local Path
    """

    myPiece = request.GET.get("mypiece")
    if myPiece not in ['X', 'O']:
        raise Http404(f"My piece '{myPiece}' does not exists")

    context = {
        "my_piece": myPiece,
        "room_name": room_name
    }
    return render(request, lp_playing, context)
