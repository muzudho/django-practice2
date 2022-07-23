from django.http import HttpResponse
from django.template import loader


class Portal():
    """ポータル ページ"""

    def render(request):
        """描画"""

        template = loader.get_template('portal_v1/o2o1/portal_base.html')
        #                               -------------------------------
        #                               1
        # 1. host1/apps1/practice_v1/templates/portal_v1/o2o1/portal_base.html を取得
        #                                      -------------------------------

        context = {
            "dj_path_of_page1": "/practice/v1.0/page1",
            "dj_path_of_page2_patch1": "/practice/v1.0/page2_patch1",
            "dj_path_of_page2_patch2": "/practice/v1.0/page2_patch2",
        }

        return HttpResponse(template.render(context, request))
