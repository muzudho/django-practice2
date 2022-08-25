# BOF O3o1o0g9o0

from django.shortcuts import render


class PageTheHello():
    """O3o1o0g9o0 こんにちわページ"""

    @staticmethod
    def render(request):
        """描画"""

        template_path = 'practice_vol1o0/page_the_hello/ver1o0.html'
        #                ------------------------------------------
        #                1
        # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/page_the_hello/ver1o0.html` を取得
        #                                          ------------------------------------------

        context = {}
        return render(request, template_path, context)

        # テンプレートを使わず、HTMLをハードコーディングすることもできる
        # return HttpResponse("""Hello, world.<br/>
        #                    <a href="http://example.com/">ホーム</a>""")

        # 以下のような書き方もある
        # from django.http import HttpResponse
        # from django.template import loader
        # template = loader.get_template('this/is/a/local/path/example.html')
        # context = {}
        # HttpResponse(template.render(context, request))

# EOF O3o1o0g9o0
