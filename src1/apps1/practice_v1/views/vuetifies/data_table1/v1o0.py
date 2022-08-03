from django.shortcuts import render


def render_data_table1(request):
    """OA12o2o0g3o0 描画 - データテーブル１"""

    # * `lp_` - Local path
    lp_data_table1 = 'practice_v1/vuetifies/data_table1/v1o0.html'
    #                 -------------------------------------------
    #                 1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/vuetifies/data_table1/v1o0.html` を取得
    #                                      -------------------------------------------

    context = {}
    return render(request, lp_data_table1, context)
