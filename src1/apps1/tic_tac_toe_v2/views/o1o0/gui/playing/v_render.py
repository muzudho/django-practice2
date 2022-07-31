from django.http import Http404
from django.shortcuts import render


def render_playing(request, kw_room_name, path_of_ws_playing, path_of_html, on_update, expected_pieces):
    """対局中 - 描画"""

    my_turn = request.GET.get("myturn")
    if my_turn not in expected_pieces:
        raise Http404(f"My piece '{my_turn}' does not exists")

    on_update(request)

    # `dj_` は Djangoでレンダーするパラメーター名の目印
    context = {
        "dj_room_name": kw_room_name,
        "dj_my_turn": my_turn,
        "dj_path_of_ws_playing": path_of_ws_playing,
    }
    return render(request, path_of_html, context)
