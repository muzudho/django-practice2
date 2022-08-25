# BOF OA13o2o0g5o0

import json
from django.shortcuts import render


def render_textarea1(request):
    """OA13o2o0g5o0 ビューティファイのテキストエリア１"""

    # Template path
    textarea1_base_tp = 'practice_vol1o0/vuetifies/textarea1/ver1o0.html'
    #                    -----------------------------------------------
    #                    1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/vuetifies/textarea1/ver1o0.html` を取得
    #                                          -----------------------------------------------

    with open('apps1/practice_vol1o0/static/practice_vol1o0/data/desserts1/ver1o0.json', mode='r', encoding='utf-8') as f:
        #      -----------------------------------------------------------------------
        #      1
        # 1. `src1/apps1/practice_vol1o0/static/practice_vol1o0/data/desserts1/ver1o0.json` を取得
        #          -----------------------------------------------------------------------
        doc = json.load(f)

    context = {
        'dessertsStr': json.dumps(doc)
    }
    return render(request, textarea1_base_tp, context)


def render_desserts1_from_textarea1(request):
    """OA13o2o0g5o0 ビューティファイのデザート１ . テキストエリア１から"""

    form1Textarea1 = request.POST["textarea1"]

    # Template path
    desserts1_tp = 'practice_vol1o0/vuetifies/desserts1/ver1o0.html'
    #               -----------------------------------------------
    #               1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/vuetifies/desserts1/ver1o0.html` を取得
    #                                          -----------------------------------------------

    context = {
        'dessertsStr': form1Textarea1
    }
    return render(request, desserts1_tp, context)

# EOF OA13o2o0g5o0
