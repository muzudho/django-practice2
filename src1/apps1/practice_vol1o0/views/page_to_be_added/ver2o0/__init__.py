# BOF O3o2o0g4o0

from django.shortcuts import render


class PageToBeAdded():
    """O3o2o0g4o0 練習1.0巻 追加されるページ2.0版"""

    def render(request):
        """描画"""

        template_path = 'practice_vol1o0/page_to_be_added/ver2o0.html.txt'
        #                                                    ^two
        #                ------------------------------------------------
        #                1
        # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/page_to_be_added/ver2o0.html.txt` を取得
        #                                          ------------------------------------------------

        context = {}
        return render(request, template_path, context)

# EOF O3o2o0g4o0
