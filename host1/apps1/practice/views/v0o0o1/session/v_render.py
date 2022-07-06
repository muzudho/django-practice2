import json
from django.http import HttpResponse
from django.template import loader

from apps1.practice.models_helper.mh_session import MhSession
#    ----- -------- ------------------------        ---------
#    1     2        3                               4
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. クラス名


def render_active_user_list(request, path_of_this_page):
    """描画 - アクティブ ユーザー一覧"""

    template = loader.get_template(path_of_this_page)

    context = {
        # * `dj_` - 「Djangoがレンダーに埋め込む変数」 の目印
        # * Vue に渡すときは、 JSON オブジェクトではなく、 JSON 文字列
        'dj_users': json.dumps(MhSession.get_all_logged_in_users())
    }

    return HttpResponse(template.render(context, request))
