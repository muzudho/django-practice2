# BOF OA13o4o0gA11o0

import json
from django.http import JsonResponse
from django.shortcuts import render

# 練習1.0巻 デザート1.0版
from apps1.practice_vol1o0.models.dessert.ver1o0 import Dessert
#          ---------------                ------        -------
#          11                             12            2
#    -------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_textarea1_to_model(request):
    """OA13o4o0gA11o0 練習1.0巻 ビューティファイのテキストエリア１ 1.0版"""

    # Template path
    textarea1_to_model_tp = 'practice_vol1o0/vuetifies/textarea1_to_model/ver1o0.html.txt'
    #                        ------------------------------------------------------------
    #                        1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/vuetifies/textarea1_to_model/ver1o0.html.txt` を取得
    #                                          ------------------------------------------------------------

    with open('apps1/practice_vol1o0/static/practice_vol1o0/data/desserts1_placeholder/ver1o0.json', mode='r', encoding='utf-8') as f:
        #      -----------------------------------------------------------------------------------
        #      1
        # 1. `src1/apps1/practice_vol1o0/static/practice_vol1o0/data/desserts1_placeholder/ver1o0.json` を取得
        #          -----------------------------------------------------------------------------------
        doc = json.load(f)

    context = {
        'dessertsStr': json.dumps(doc)
    }
    return render(request, textarea1_to_model_tp, context)


def render_save_result_of_desserts1_from_textarea1(request):
    """OA13o4o0gA11o0 ビューティファイのデザート１ . テキストエリア１から . 保存結果"""

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

# EOF OA13o4o0gA11o0
