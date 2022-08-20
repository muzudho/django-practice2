# BOF O5o1o0gA10o0

from django.shortcuts import render


class Portal():
    """O5o1o0gA10o0 ポータル ページ"""

    def render(request):
        """描画"""

        template_path = 'portal_v1/v1o0.html'
        #                -------------------
        #                1
        # 1. src1/apps1/practice_v1/templates/portal_v1/v1o0.html を取得
        #                                     -------------------

        context = {
            "dj_path_of_page_the_hello": "/practice/v1/page-the-hello",
            "dj_path_of_page_to_be_added_1": "/practice/v1/page-to-be-added-1",
            "dj_path_of_page_to_be_added_2": "/practice/v1/page-to-be-added-2",
        }

        return render(request, template_path, context)

# EOF O5o1o0gA10o0
