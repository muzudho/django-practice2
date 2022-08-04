from django.shortcuts import render


def render_engine_manual(request, lp_engine_manual):
    """OA16o2o0gA15o0 描画 - エンジン手動

    Parameters
    ----------
    lp_engine_manual : str
        Local Path
    """

    context = {}

    return render(request, lp_engine_manual, context)
