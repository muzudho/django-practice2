from django.http import HttpResponse
from django.template import loader


class Page2Patch1():
    """ページ２ パッチ１"""

    def render(request):
        """描画"""

        template = loader.get_template(
            'practice_v1/o1/page2_patch1.html.txt')
        #    ------------------------------------
        #    1
        # 1. host1/apps1/practice_v1/templates/practice_v1/o1/page2_patch1.html.txt を取得
        #                                      ------------------------------------

        context = {}
        return HttpResponse(template.render(context, request))


class Page2Patch2():
    """ページ２ パッチ２"""

    def render(request):
        """描画"""

        template = loader.get_template(
            'practice_v1/o1/page2_patch2.html.txt')
        #                              ^two
        #    ------------------------------------
        #    1
        # 1. host1/apps1/practice_v1/templates/practice_v1/o1/page2_patch2.html.txt を取得
        #                                      ------------------------------------

        context = {}
        return HttpResponse(template.render(context, request))
