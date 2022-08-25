# BOF OA11o1o0g3o0

from django.shortcuts import render

# 都道府県モデル
from apps1.practice_vol1o0.models.prefecture.ver1o0 import Prefecture
#          ---------------                   ------        ----------
#          11                                12            2
#    ----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_list(request):
    """OA11o1o0g3o0 一覧画面の描画"""

    # Template path
    prefecture_list_tp = 'practice_vol1o0/prefecture/ver1o0/list.html'
    #                     -------------------------------------------
    #                     1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/prefecture/ver1o0/list.html` を取得
    #                                          -------------------------------------------

    context = {
        'prefectures': Prefecture.objects.all().order_by('pk'),  # pk順にメンバーを全部取得
    }
    return render(request, prefecture_list_tp, context)

# EOF OA11o1o0g3o0
