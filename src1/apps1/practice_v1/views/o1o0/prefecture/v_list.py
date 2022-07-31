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


def render_list(request):
    """一覧画面の描画"""

    template = loader.get_template('practice_v1/o1o0/prefecture/list.html')
    #                               -------------------------------------
    #                               1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/o1o0/prefecture/list.html` を取得
    #                                      -------------------------------------

    context = {
        'prefectures': Prefecture.objects.all().order_by('pk'),  # pk順にメンバーを全部取得
    }
    return HttpResponse(template.render(context, request))
