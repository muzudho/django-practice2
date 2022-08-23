# BOF OAAA1001o1o0ga14o0

from django.shortcuts import render


class BoardView():
    """OAAA1001o1o0ga14o0 盤"""

    @staticmethod
    def render(request):
        """描画"""

        template_path = 'lifegame_vol1o0/board/ver0o3o0.html.txt'
        #                ---------------------------------------
        #                1
        # 1. `src1/apps1/lifegame_vol1o0/templates/lifegame_vol1o0/board/ver0o3o0.html.txt` を取得
        #                                          ---------------------------------------

        context = {}
        return render(request, template_path, context)

# EOF OAAA1001o1o0ga14o0
