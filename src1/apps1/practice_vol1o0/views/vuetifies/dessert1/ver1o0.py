# BOF OA13o1o0g4o0

import json
from django.shortcuts import render


def render_desserts1(request):
    """OA13o1o0g4o0 ビューティファイのデザート１"""

    # Template path
    desserts1_tp = 'practice_vol1o0/vuetifies/desserts1/ver1o0.html'
    #               -----------------------------------------------
    #               1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/vuetifies/desserts1/ver1o0.html` を取得
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
    return render(request, desserts1_tp, context)

# EOF OA13o1o0g4o0
