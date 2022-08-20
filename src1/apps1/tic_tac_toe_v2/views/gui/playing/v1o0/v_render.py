# BOF OA16o3o0gA14o0

from django.http import Http404
from django.shortcuts import render


def render_playing(request, kw_room_name, wsp_playing, playing_tp, on_update, expected_pieces):
    """OA16o3o0gA14o0 対局中 - 描画

    Parameters
    ----------
    wsp_playing : str
        Webソケットパス
    playing_tp : str
        Template path
    """

    my_turn = request.GET.get("myturn")
    if my_turn not in expected_pieces:
        raise Http404(f"My piece '{my_turn}' does not exists")

    on_update(request)

    # `dj_` は Djangoでレンダーするパラメーター名の目印
    context = {
        "dj_room_name": kw_room_name,
        "dj_my_turn": my_turn,
        "dj_path_of_ws_playing": wsp_playing,
    }
    return render(request, playing_tp, context)

# EOF OA16o3o0gA14o0
