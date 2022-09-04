# BOF [OAAA1001o2o0g10o0]

import json
from django.shortcuts import render


class DataTableView():
    """[OAAA1001o2o0g10o0] データテーブル"""

    @staticmethod
    def render(request):
        """[OAAA1001o2o0g10o0] 描画"""

        # Template path
        data_table_tp = 'consecutive_name_vol1o0/data_table/ver1o0.html'
        #                ----------------------------------------------
        #                1
        # 1. `src1/apps1/consecutive_name_vol1o0/templates/consecutive_name_vol1o0/data_table/ver1o0.html` を取得
        #                                                  ----------------------------------------------

        with open('apps1/consecutive_name_vol1o0/static/consecutive_name_vol1o0/data/smoek_test/ver1o0.json', mode='r', encoding='utf-8') as f:
            #      ----------------------------------------------------------------------------------------
            #      1
            # 1. `src1/apps1/consecutive_name_vol1o0/static/consecutive_name_vol1o0/data/smoek_test/ver1o0.json` を取得
            #          ----------------------------------------------------------------------------------------
            jsObject = json.load(f)

        context = {
            # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
            'dj_dataTableJson': json.dumps(jsObject)
        }
        return render(request, data_table_tp, context)

# EOF [OAAA1001o2o0g10o0]
