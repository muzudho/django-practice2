# BOF OA12o1o0g3o0

from django.shortcuts import render


def render_hello1(request):
    """OA12o1o0g3o0 ハローの描画"""

    # Template path
    hello_tp = 'practice_v1/vuetifies/hello/v1o0.html'
    #           -------------------------------------
    #           1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/vuetifies/hello/v1o0.html` を取得
    #                                      -------------------------------------

    context = {}
    return render(request, hello_tp, context)

# EOF OA12o1o0g3o0
