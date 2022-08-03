import json
from django.shortcuts import render


def render_desserts1(request):
    """OA13o1o0g4o0 ビューティファイのデザート１"""

    # * `lp_` - Local path
    lp_desserts1 = 'practice_v1/o1o0/vuetify/desserts1.html'
    #               ---------------------------------------
    #               1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/o1o0/vuetify/desserts1.html` を取得
    #                                      ---------------------------------------

    with open('apps1/practice_v1/static/practice_v1/o1o0/data/desserts1.json', mode='r', encoding='utf-8') as f:
        #      -------------------------------------------------------------
        #      1
        # 1. `src1/apps1/practice_v1/static/practice_v1/o1o0/data/desserts1.json` を取得
        #          -------------------------------------------------------------
        doc = json.load(f)

    context = {
        'dessertsStr': json.dumps(doc)
    }
    return render(request, lp_desserts1, context)