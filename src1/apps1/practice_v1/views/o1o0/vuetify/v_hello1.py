from django.shortcuts import render


def render_hello1(request):
    """OA12o1o0g3o0 ハローの描画"""

    # * `lp_` - Local path
    lp_hello = 'practice_v1/o1o0/vuetify/hello1.html'
    #           ------------------------------------
    #           1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/o1o0/vuetify/hello1.html` を取得
    #                                      ------------------------------------

    context = {}
    return render(request, lp_hello, context)
