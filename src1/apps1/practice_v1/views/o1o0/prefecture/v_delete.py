from django.http import HttpResponse
from django.template import loader

# 都道府県モデル
from apps1.practice_v1.models.o1o0.m_prefecture import Prefecture
#          -----------             ------------        ----------
#          11                      12                  2
#    ------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_delete(request, id=id):
    """削除画面の描画

    Parameters
    ----------
    request : object
        リクエスト
    id : str
        URLのGETストリングの ?id= の値
    """

    template = loader.get_template(
        'practice_v1/o1o0/prefecture/delete.html')
    #    ---------------------------------------
    #    1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/o1o0/prefecture/delete.html` を取得
    #                                      ---------------------------------------

    # GETストリングのidと、Prefectureテーブルのpkが一致するものを取得
    prefecture = Prefecture.objects.get(pk=id)
    name = prefecture.name  # 名前だけまだ使う
    prefecture.delete()
    # すでに削除されたデータを使うために以下のようにする
    context = {
        'prefecture': {
            'name': name
        }
    }
    return HttpResponse(template.render(context, request))
