import json
from django.http import JsonResponse


def render_desserts1_as_json(request):
    """JSON形式でデザート１描画"""

    with open('apps1/practice_v1/static/practice_v1/o1o0/data/desserts1.json', mode='r', encoding='utf-8') as f:
        #      -------------------------------------------------------------
        #      1
        # 1. `host1/apps1/practice_v1/static/practice_v1/o1o0/data/desserts1.json` を取得
        #           -------------------------------------------------------------
        doc = json.load(f)

    return JsonResponse(doc)
