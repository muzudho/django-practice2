# BOF OA12o2o0g3o0

from django.shortcuts import render


def render_data_table1(request):
    """OA12o2o0g3o0 描画 - データテーブル１"""

    # Template path
    data_table1_tp = 'practice_vol1o0/vuetifies/data_table1/ver1o0.html'
    #                 -------------------------------------------------
    #                 1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/vuetifies/data_table1/ver1o0.html` を取得
    #                                          -------------------------------------------------

    context = {}
    return render(request, data_table1_tp, context)

# EOF OA12o2o0g3o0
