from django.shortcuts import render


def render_validation1(request):
    """OA12o3o0g3o0 バリデーション１の描画"""

    # * `lp_` - Local path
    lp_validation1 = 'practice_v1/vuetifies/validation1/v1o0.html'
    #                 -------------------------------------------
    #                 1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/vuetifies/validation1/v1o0.html` を取得
    #                                      -------------------------------------------

    context = {}
    return render(request, lp_validation1, context)
