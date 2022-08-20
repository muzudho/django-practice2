# BOF O9o1o0g6o0

import json
from django.shortcuts import render

# ユーザー モデルヘルパー
from apps1.practice_v1.models_helper.user.v1o0 import MhUser
#          -----------                    ----        ------
#          11                             12          2
#    -----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_user_list(request, user_list_tp):
    """O9o1o0g6o0 描画 - 会員一覧

    Parameters
    ----------
    user_list_tp : str
        Template path
    """

    context = {
        # * `dj_` - 「Djangoがレンダーに埋め込む変数」 の目印
        # * Vue に渡すときは、 JSON オブジェクトではなく、 JSON 文字列
        'dj_user_dic': json.dumps(MhUser.get_user_dic())
    }

    return render(request, user_list_tp, context)

# EOF O9o1o0g6o0
