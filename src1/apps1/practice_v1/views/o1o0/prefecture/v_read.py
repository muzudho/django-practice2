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


def render_read(request, id=id):
    """OA11o2o0g3o0 詳細画面の描画

    Parameters
    ----------
    request : object
        リクエスト
    id : str
        URLのGETストリングの ?id= の値
    """

    # * `lp_` - Local path
    lp_prefecture_read = 'practice_v1/o1o0/prefecture/read.html'
    #                     -------------------------------------
    #                     1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/o1o0/prefecture/read.html` を取得
    #                                      -------------------------------------

    context = {
        # GETストリングのidと、Prefectureテーブルのpkが一致するものを取得
        'prefecture': Prefecture.objects.get(pk=id),
    }
    return render(request, lp_prefecture_read, context)
