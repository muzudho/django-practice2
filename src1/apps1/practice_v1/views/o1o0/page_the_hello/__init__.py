from django.http import HttpResponse
from django.template import loader


class PageTheHello():
    """おはようページ"""

    @staticmethod
    def render(request):
        """描画"""

        template = loader.get_template('practice_v1/o1o0/page_the_hello.html')
        #                               ------------------------------------
        #                               1
        # 1. src1/apps1/practice_v1/templates/practice_v1/o1o0/page_the_hello.html を取得
        #                                     ------------------------------------

        context = {}
        return HttpResponse(template.render(context, request))

        # テンプレートを使わず、HTMLをハードコーディングすることもできる
        # return HttpResponse("""Hello, world.<br/>
        #                    <a href="http://example.com/">ホーム</a>""")
