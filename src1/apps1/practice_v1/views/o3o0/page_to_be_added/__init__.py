from django.shortcuts import render


class PageToBeAdded():
    """O3o3o0g3o0 追加されるページ"""

    def render(request):
        """描画"""

        # * `lp_` - Local path
        lp_this_page = 'practice_v1/o3o0/page_to_be_added.html.txt'
        #                            ^three
        #               ------------------------------------------
        #               1
        # 1. src1/apps1/practice_v1/templates/practice_v1/o3o0/page_to_be_added.html.txt を取得
        #                                     ------------------------------------------

        context = {}
        return render(request, lp_this_page, context)
