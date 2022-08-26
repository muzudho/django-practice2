# BOF O5o2o0g7o0

import pandas as pd

from django.shortcuts import render


class Launcher():
    """O5o2o0g7o0 ランチャー1.0巻 2.0版"""

    def render(request):
        """描画"""

        template_path = 'launcher_vol1o0/ver2o0.html'
        #                                   ^two
        #                ---------------------------
        #                1
        # 1. src1/apps1/launcher_vol1o0/templates/launcher_vol1o0/ver2o0.html を取得
        #                                         ---------------------------

        df = pd.read_csv('apps1/launcher_vol1o0/data/finished-lessons.csv')
        #                 -----------------------------------------------
        #                 1
        # 1. `src1/apps1/launcher_vol1o0/data/finished-lessons.csv` を読取
        #          -----------------------------------------------

        # print(df)
        #
        # Example
        # -------
        #    path                                         label
        # 0  /practice/vol1.0/page-the-hello/ver1.0/      こんにちわページ
        # 1  /practice/vol1.0/page-to-be-added-1/ver1.0/  １回追加されたページ
        # 2  /practice/vol1.0/page-to-be-added-2/ver1.0/  ２回追加されたページ

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
