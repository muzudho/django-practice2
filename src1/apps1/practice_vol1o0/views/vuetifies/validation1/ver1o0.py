# BOF OA12o3o0g3o0

from django.shortcuts import render


def render_validation1(request):
    """OA12o3o0g3o0 バリデーション１の描画"""

    # Template path
    validation1_tp = 'practice_vol1o0/vuetifies/validation1/ver1o0.html'
    #                 -------------------------------------------------
    #                 1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/vuetifies/validation1/ver1o0.html` を取得
    #                                          -------------------------------------------------

    context = {}
    return render(request, validation1_tp, context)

# EOF OA12o3o0g3o0
