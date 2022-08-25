# BOF O9o1o0g6o0

import json
from django.shortcuts import render

# 練習1.0巻 ユーザー モデルヘルパー1.0版
from apps1.practice_vol1o0.models_helper.user.ver1o0 import MhUser
#          ---------------                    ------        ------
#          11                                 12            2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_user_list(request, user_list_tp):
    """O9o1o0g6o0 練習1.0巻 会員一覧1.0版 - 描画

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
