import json
from django.http import HttpResponse, JsonResponse
from django.template import loader

# デザート
from apps1.practice_v1.models.o1o0.m_dessert import Dessert
#          -----------             ---------        -------
#          11                      12               2
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_textarea1_to_model(request):
    """ビューティファイのテキストエリア１ to model"""

    template = loader.get_template(
        'practice_v1/o1o0/vuetify/textarea1_to_model.html.txt')
    #    ----------------------------------------------------
    #    1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o1o0/vuetify/textarea1_to_model.html.txt` を取得
    #                                       ----------------------------------------------------

    with open('apps1/practice_v1/static/practice_v1/o1o0/data/desserts1-placeholder.json', mode='r', encoding='utf-8') as f:
        #      -------------------------------------------------------------------------
        #      1
        # 1. `host1/apps1/practice_v1/static/practice_v1/o1o0/data/desserts1-placeholder.json` を取得
        #           -------------------------------------------------------------------------
        doc = json.load(f)

    context = {
        'dessertsStr': json.dumps(doc)
    }
    return HttpResponse(template.render(context, request))


def render_save_result_of_desserts1_from_textarea1(request):
    """ビューティファイのデザート１ . テキストエリア１から . 保存結果"""

    form1Textarea1 = request.POST["textarea1"]
    doc = json.loads(form1Textarea1)  # Dessert

    dessert = Dessert(
        name=doc["name"],
        calories=doc["calories"],
        fat=doc["fat"],
        carbs=doc["carbs"],
        protein=doc["protein"],
        iron=doc["iron"])
    dessert.save()

    doc2 = {
        'result': "Success"
    }
    return JsonResponse(doc2)
