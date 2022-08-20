# BOF OA21o1o0g6o0

from django.shortcuts import render


def render_auto_reload(request, auto_reload_tp):
    """OA21o1o0g6o0 描画 - 自動再読込

    Parameters
    ----------
    auto_reload_tp : str
        Template path
    """

    context = {}
    return render(request, auto_reload_tp, context)

# EOF OA21o1o0g6o0
