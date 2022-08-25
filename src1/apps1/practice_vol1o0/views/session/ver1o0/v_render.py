import json
from django.shortcuts import render

# セッション モデルヘルパー
from apps1.practice_v1.models_helper.session.v1o0 import MhSession
#          -----------                       ----        ---------
#          11                                12          2
#    --------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. クラス


def render_active_user_list(request, path_of_this_page):
    """O9o3o0g6o0 描画 - アクティブ ユーザー一覧"""

    context = {
        # * `dj_` - 「Djangoがレンダーに埋め込む変数」 の目印
        # * Vue に渡すときは、 JSON オブジェクトではなく、 JSON 文字列
        'dj_users': json.dumps(MhSession.get_all_logged_in_users())
    }

    return render(request, path_of_this_page, context)
