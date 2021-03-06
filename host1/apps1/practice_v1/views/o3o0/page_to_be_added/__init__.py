from django.http import HttpResponse
from django.template import loader


class PageToBeAdded():
    """追加されるページ"""

    def render(request):
        """描画"""

        template = loader.get_template(
            'practice_v1/o3o0/page_to_be_added.html.txt')
        #                 ^three
        #    ------------------------------------------
        #    1
        # 1. host1/apps1/practice_v1/templates/practice_v1/o3o0/page_to_be_added.html.txt を取得
        #                                      ------------------------------------------

        context = {}
        return HttpResponse(template.render(context, request))
