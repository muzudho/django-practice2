from django.http import HttpResponse
from django.template import loader


class Portal():
    """ポータル ページ"""

    def render(request):
        """描画"""

        template = loader.get_template('portal/v0o0o1/portal_base.html')
        #                               ------------------------------
        #                               1
        # 1. host1/apps1/practice/templates/portal/v0o0o1/portal_base.html を取得
        #                                   ------------------------------

        context = {
            "dj_path_of_page1": "/practice/page1",
            "dj_path_of_page2_patch1": "/practice/page2_patch1",
            "dj_path_of_page2_patch2": "/practice/page2_patch2",
        }

        return HttpResponse(template.render(context, request))
