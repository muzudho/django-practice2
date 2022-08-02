from django.shortcuts import render, get_object_or_404

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
    lp_prefecture_read = 'practice_v1/prefecture/v1o0/read.html'
    #                     -------------------------------------
    #                     1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/prefecture/v1o0/read.html` を取得
    #                                      -------------------------------------

    # GETストリングのidと、Prefectureテーブルのpkが一致するものを取得。無ければ 404エラー
    prefecture = get_object_or_404(Prefecture, pk=id)

    context = {
        'prefecture': prefecture,
    }
    return render(request, lp_prefecture_read, context)
