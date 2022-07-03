import json
from django.http import HttpResponse
from django.template import loader


def render_desserts1(request):
    """ビューティファイのデザート１"""

    template = loader.get_template(
        'practice/v0o0o1/vuetify/desserts1.html')
    #    --------------------------------------
    #    1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/vuetify/desserts1.html` を取得
    #                                    --------------------------------------

    with open('apps1/practice/static/practice/v0o0o1/data/desserts1.json', mode='r', encoding='utf-8') as f:
        #      ---------------------------------------------------------
        #      1
        # 1. `host1/apps1/practice/static/practice/v0o0o1/data/desserts1.json` を取得
        #           ---------------------------------------------------------
        doc = json.load(f)

    context = {
        'dessertsStr': json.dumps(doc)
    }
    return HttpResponse(template.render(context, request))
