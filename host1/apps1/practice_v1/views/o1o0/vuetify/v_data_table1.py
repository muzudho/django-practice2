from django.http import HttpResponse
from django.template import loader


def render_data_table1(request):
    """描画 - データテーブル１"""

    template = loader.get_template(
        'practice_v1/o1o0/vuetify/data_table1.html')
    #    -----------------------------------------
    #    1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o1o0/vuetify/data_table1.html` を取得
    #                                       -----------------------------------------

    context = {
    }

    return HttpResponse(template.render(context, request))
