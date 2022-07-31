from django.shortcuts import render


def render_auto_reload(request, lp_auto_reload):
    """OA21o1o0g6o0 描画 - 自動再読込

    Parameters
    ----------
    lp_auto_reload : str
        ローカルパス
    """

    context = {}
    return render(request, lp_auto_reload, context)
