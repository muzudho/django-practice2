# BOF O5o2o0g7o0

import pandas as pd

from django.shortcuts import render


class Portal():
    """O5o2o0g7o0 ポータル ページ"""

    def render(request):
        """描画"""

        template_path = 'portal_v1/v2o0.html'
        #                           ^two
        #                -------------------
        #                1
        # 1. src1/apps1/portal_v1/templates/portal_v1/v2o0.html を取得
        #                                   -------------------

        df = pd.read_csv('apps1/portal_v1/data/finished-lessons.csv')
        #                 -----------------------------------------
        #                 1
        # 1. `src1/apps1/portal_v1/data/finished-lessons.csv` を読取
        #          -----------------------------------------

        # print(df)
        #
        # Example
        # -------
        #    path                             label
        # 0  /practice/v1/page-the-hello      こんにちわページ
        # 1  /practice/v1/page-to-be-added-1  １回追加されたページ
        # 2  /practice/v1/page-to-be-added-2  ２回追加されたページ

        # print(df.columns)
        #
        # Example
        # -------
        # Index(['path', 'label'], dtype='object')

        # 使いやすい構造に変換します
        finished_lesson_list = []
        df = df.reset_index()  # make sure indexes pair with number of rows
        for index, row in df.iterrows():
            finished_lesson_list.append({
                "path": row['path'],
                "label": row['label'],
            })

        # for item in finished_lesson_list:
        #    print(f"{item['path']} , {item['label']}")

        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        context = {
            "dj_finished_lesson_list": finished_lesson_list,
        }

        return render(request, template_path, context)

# EOF O5o2o0g7o0
