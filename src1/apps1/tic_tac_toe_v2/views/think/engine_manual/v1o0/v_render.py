# BOF OA16o2o0gA15o0

from django.shortcuts import render


def render_engine_manual(request, engine_manual_tp):
    """OA16o2o0gA15o0 描画 - エンジン手動

    Parameters
    ----------
    engine_manual_tp : str
        Template path
    """

    context = {}

    return render(request, engine_manual_tp, context)

# EOF OA16o2o0gA15o0
