from django.shortcuts import render


class BoardView():
    """OAAA1001o1o0ga12o_6o0 盤"""

    @staticmethod
    def render(request):
        """描画"""

        # * `_lp` - Local path
        this_page_lp = 'lifegame_v1/board/v1o1o0.html.txt'
        #               ---------------------------------
        #               1
        # 1. `src1/apps1/lifegame_v1/templates/lifegame_v1/board/v1o1o0.html.txt` を取得
        #                                      ---------------------------------

        context = {}
        return render(request, this_page_lp, context)
