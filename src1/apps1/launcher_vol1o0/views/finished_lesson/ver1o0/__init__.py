# BOF O5o1o0gA10o0

from django.shortcuts import render


class Launcher():
    """O5o1o0gA10o0 練習1.0巻 ランチャー1.0版"""

    def render(request):
        """描画"""

        template_path = 'launcher_vol1o0/finished_lesson/ver1o0.html'
        #                -------------------------------------------
        #                1
        # 1. `src1/apps1/launcher_vol1o0/templates/launcher_vol1o0/finished_lesson/ver1o0.html` を取得
        #                                          -------------------------------------------

        context = {
            "dj_path_of_hello": "/practice/vol1.0/hello/ver1.0/",
            "dj_path_of_page_to_be_added_1": "/practice/vol1.0/page-to-be-added-1/ver1.0/",
            "dj_path_of_page_to_be_added_2": "/practice/vol1.0/page-to-be-added-2/ver1.0/",
        }

        return render(request, template_path, context)

# EOF O5o1o0gA10o0
