# BOF OA16o3o_1o0g2o0

from django.shortcuts import render


def render_main(request, template_path):
    """OA16o3o_1o0g2o0 C2S JSON ジェネレーター - 描画

    Parameters
    ----------
    template_path : str
        Template path
    """

    context = {}

    return render(request, template_path, context)

# EOF OA16o3o_1o0g2o0
