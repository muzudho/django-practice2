import pandas as pd

from django.http import HttpResponse
from django.template import loader


class Portal():
    """ポータル ページ"""

    def render(request):
        """描画"""

        template = loader.get_template('portal/v0o0o2/portal_base.html')
        #                                           ^two
        #                               ------------------------------
        #                               1
        # 1. host1/apps1/practice_v1/templates/portal/v0o0o2/portal_base.html を取得
        #                                   ------------------------------

        df = pd.read_csv('apps1/portal_v1/data/finished-lessons.csv')
        #                 --------------------------------------
        #                 1
        # 1. `host1/apps1/portal_v1/data/finished-lessons.csv` を読取
        #           --------------------------------------

        print(df)
        #
        # Example
        # -------
        #                         path      label
        # 0         /practice/v1/page1     ページ１
        # 1  /practice/v1/page2_patch1  ページ２ パッチ１
        # 2  /practice/v1/page2_patch2  ページ２ パッチ２

        print(df.columns)
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

        for item in finished_lesson_list:
            print(f"{item['path']} , {item['label']}")
        #
        # Example
        # -------
        # /practice/v1/page1 , ページ１
        # /practice/v1/page2_patch1 , ページ２ パッチ１
        # /practice/v1/page2_patch2 , ページ２ パッチ２

        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        context = {
            "dj_finished_lesson_list": finished_lesson_list,
        }

        return HttpResponse(template.render(context, request))
