# BOF OA13o1o0g4o0

import json
from django.shortcuts import render


def render_desserts1(request):
    """OA13o1o0g4o0 ビューティファイのデザート１"""

    # Template path
    desserts1_tp = 'practice_v1/vuetifies/desserts1/v1o0.html'
    #               -----------------------------------------
    #               1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/vuetifies/desserts1/v1o0.html` を取得
    #                                      -----------------------------------------

    with open('apps1/practice_v1/static/practice_v1/data/desserts1/v1o0.json', mode='r', encoding='utf-8') as f:
        #      -------------------------------------------------------------
        #      1
        # 1. `src1/apps1/practice_v1/static/practice_v1/data/desserts1/v1o0.json` を取得
        #          -------------------------------------------------------------
        doc = json.load(f)

    context = {
        'dessertsStr': json.dumps(doc)
    }
    return render(request, desserts1_tp, context)

# EOF OA13o1o0g4o0
