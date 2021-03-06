import json
from django.http import HttpResponse
from django.template import loader

# ユーザー モデルヘルパー
from apps1.practice_v1.models_helper.o1o0.mh_user import MhUser
#          -----------                    -------        ------
#          11                             12             2
#    --------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


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
