# BOF O3o3o0g3o0

from django.shortcuts import render


class PageToBeAdded():
    """O3o3o0g3o0 追加されるページ"""

    def render(request):
        """描画"""

        # * `lp_` - Local path
        template_path = 'practice_v1/page_to_be_added/v3o0.html.txt'
        #                                             ^three
        #               ------------------------------------------
        #               1
        # 1. src1/apps1/practice_v1/templates/practice_v1/page_to_be_added/v3o0.html.txt を取得
        #                                     ------------------------------------------

        context = {}
        return render(request, template_path, context)

# EOF O3o3o0g3o0
