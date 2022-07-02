from django.http import HttpResponse
from django.template import loader

from apps1.practice.models.m_prefecture import Prefecture
#    ----- -------- ------ ------------        ----------
#    1     2        3      4                   5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


def render_read(request, id=id):
    """描画

    Parameters
    ----------
    request : object
        リクエスト
    id : str
        URLのGETストリングの ?id= の値
    """

    template = loader.get_template('practice/v0o0o1/prefecture/read.html')
    #                               ------------------------------------
    #                               1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/prefecture/read.html` を取得
    #                                    ------------------------------------

    context = {
        # GETストリングのidと、Prefectureテーブルのpkが一致するものを取得
        'prefecture': Prefecture.objects.get(pk=id),
    }
    return HttpResponse(template.render(context, request))
