# BOF OAAA1001o1o0ga12o_6o0

from django.shortcuts import render


class BoardView():
    """OAAA1001o1o0ga12o_6o0 盤"""

    @staticmethod
    def render(request):
        """描画"""

        # Template path
        this_page_tp = 'lifegame_v1/board/v0o2o0.html.txt'
        #               ---------------------------------
        #               1
        # 1. `src1/apps1/lifegame_v1/templates/lifegame_v1/board/v0o2o0.html.txt` を取得
        #                                      ---------------------------------

        context = {}
        return render(request, this_page_tp, context)

# EOF OAAA1001o1o0ga12o_6o0
