# BOF OA11o3o0g3o0

from django.shortcuts import render, get_object_or_404

# 練習1.0巻 都道府県モデル1.0版
from apps1.practice_vol1o0.models.prefecture.ver1o0 import Prefecture
#          ---------------                   ------        ----------
#          11                                12            2
#    ----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_delete(request, id=id):
    """OA11o3o0g3o0 削除画面の描画

    Parameters
    ----------
    request : object
        リクエスト
    id : str
        URLのGETストリングの ?id= の値
    """

    # Template path
    prefecture_delete_tp = 'practice_vol1o0/prefecture/ver1o0/delete.html'
    #                       ---------------------------------------------
    #                       1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/prefecture/ver1o0/delete.html` を取得
    #                                          ---------------------------------------------

    # GETストリングのidと、Prefectureテーブルのpkが一致するものを取得。無ければ 404 画面へ飛ぶ
    prefecture = get_object_or_404(Prefecture, pk=id)

    name = prefecture.name  # 名前だけまだ使う
    prefecture.delete()
    # すでに削除されたデータを使うために以下のようにする
    context = {
        'prefecture': {
            'name': name
        }
    }
    return render(request, prefecture_delete_tp, context)

# EOF OA11o3o0g3o0
