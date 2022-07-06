import json
from django.http import HttpResponse
from django.template import loader

from apps1.practice.models_helper.mh_user import MhUser
#    ----- -------- ---------------------        ------
#    1     2        3                            4
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 3. Python ファイル名。拡張子抜き
# 4. クラス名


def render_extends_user_list(request, path_of_this_page):
    """描画 - （拡張済）会員登録ユーザー一覧"""

    template = loader.get_template(path_of_this_page)

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        # Vue に渡すときは、 JSON オブジェクトではなく、 JSON 文字列です
        'dj_extends_user_str': json.dumps(MhUser.get_extends_user_dic()),
        #   --------                                 --------
    }

    return HttpResponse(template.render(context, request))
