import json
from django.http import HttpResponse
from django.template import loader


def render_textarea1(request):
    """ビューティファイのテキストエリア１"""

    template = loader.get_template(
        'practice_v1/o1/vuetify/textarea1_base.html')
    #    ------------------------------------------
    #    1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o1/vuetify/textarea1_base.html` を取得
    #                                       ------------------------------------------

    with open('apps1/practice_v1/static/practice_v1/o1/data/desserts1.json', mode='r', encoding='utf-8') as f:
        #      -----------------------------------------------------------
        #      1
        # 1. `host1/apps1/practice_v1/static/practice_v1/o1/data/desserts1.json` を取得
        #           -----------------------------------------------------------
        doc = json.load(f)

    context = {
        'dessertsStr': json.dumps(doc)
    }
    return HttpResponse(template.render(context, request))


def render_desserts1_from_textarea1(request):
    """ビューティファイのデザート１ . テキストエリア１から"""

    form1Textarea1 = request.POST["textarea1"]

    template = loader.get_template(
        'practice_v1/o1/vuetify/desserts1.html')
    #    --------------------------------------
    #    1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o1/vuetify/desserts1.html` を取得
    #                                       -------------------------------------

    context = {
        'dessertsStr': form1Textarea1
    }
    return HttpResponse(template.render(context, request))
