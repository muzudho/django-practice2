from django.shortcuts import render

# 都道府県モデル
from apps1.practice_v1.models.prefecture.v1o0 import Prefecture
#          -----------                   ----        ----------
#          11                            12          2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_list(request):
    """OA11o1o0g3o0 一覧画面の描画"""

    # * `lp_` - Local path
    lp_prefecture_list = 'practice_v1/o1o0/prefecture/list.html'
    #                     -------------------------------------
    #                     1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/o1o0/prefecture/list.html` を取得
    #                                      -------------------------------------

    context = {
        'prefectures': Prefecture.objects.all().order_by('pk'),  # pk順にメンバーを全部取得
    }
    return render(request, lp_prefecture_list, context)
