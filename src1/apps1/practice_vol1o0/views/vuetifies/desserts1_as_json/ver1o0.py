# BOF OA13o3o0g3o0

import json
from django.http import JsonResponse


def render_desserts1_as_json(request):
    """OA13o3o0g3o0 JSON形式でデザート１描画"""

    with open('apps1/practice_vol1o0/static/practice_vol1o0/data/desserts1/ver1o0.json', mode='r', encoding='utf-8') as f:
        #      -----------------------------------------------------------------------
        #      1
        # 1. `src1/apps1/practice_vol1o0/static/practice_vol1o0/data/desserts1/ver1o0.json` を取得
        #          -----------------------------------------------------------------------
        doc = json.load(f)

    return JsonResponse(doc)

# EOF OA13o3o0g3o0
