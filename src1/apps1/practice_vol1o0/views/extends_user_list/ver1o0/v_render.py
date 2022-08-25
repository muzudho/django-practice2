# BOF O9o2o0gA11o0

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


def render_extends_user_list(request, extends_user_list_tp):
    """O9o2o0gA11o0 練習1.0巻 拡張済み会員登録ユーザー一覧1.0版 - 描画

    Parameters
    ----------
    extends_user_list_tp : str
        ローカルパス
    """

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        # Vue に渡すときは、 JSON オブジェクトではなく、 JSON 文字列です
        'dj_extends_user_str': json.dumps(MhUser.get_extends_user_dic()),
        #   --------                                 --------
    }

    return render(request, extends_user_list_tp, context)

# EOF O9o2o0gA11o0
