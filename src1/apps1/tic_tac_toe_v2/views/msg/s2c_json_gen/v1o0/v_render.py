# BOF OA16o3o_2o0g3o0

from django.shortcuts import render


def render_main(request, template_path):
    """OA16o3o_2o0g3o0 S2C JSON ジェネレーター - 描画

    Parameters
    ----------
    template_path : str
        Template path
    """

    context = {}

    return render(request, template_path, context)

# EOF OA16o3o_2o0g3o0
