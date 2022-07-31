from django.shortcuts import render


class PageTheHello():
    """O3o1o0g9o0 おはようページ"""

    @staticmethod
    def render(request):
        """描画"""

        # * `lp_` - Local path
        lp_this_page = 'practice_v1/o1o0/page_the_hello.html'
        #               ------------------------------------
        #               1
        # 1. src1/apps1/practice_v1/templates/practice_v1/o1o0/page_the_hello.html を取得
        #                                     ------------------------------------

        context = {}
        return render(request, lp_this_page, context)

        # テンプレートを使わず、HTMLをハードコーディングすることもできる
        # return HttpResponse("""Hello, world.<br/>
        #                    <a href="http://example.com/">ホーム</a>""")

        # 以下のような書き方もある
        # from django.http import HttpResponse
        # from django.template import loader
        # template = loader.get_template('this/is/a/local/path/example.html')
        # context = {}
        # HttpResponse(template.render(context, request))
