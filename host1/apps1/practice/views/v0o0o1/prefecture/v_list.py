from django.http import HttpResponse
from django.template import loader

from apps1.practice.models.m_prefecture import Prefecture
#    ----- -------- ------ ------------        ----------
#    1     2        3      4                   5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


def render_list(request):
    """一覧画面の描画"""

    template = loader.get_template('practice/v0o0o1/prefecture/list.html')
    #                               ------------------------------------
    #                               1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/prefecture/list.html` を取得
    #                                    ------------------------------------

    context = {
        'prefectures': Prefecture.objects.all().order_by('pk'),  # pk順にメンバーを全部取得
    }
    return HttpResponse(template.render(context, request))
