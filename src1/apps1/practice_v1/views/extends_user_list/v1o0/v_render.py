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


def render_extends_user_list(request, lp_extends_user_list):
    """O9o2o0gA11o0 描画 - （拡張済）会員登録ユーザー一覧

    Parameters
    ----------
    lp_extends_user_list : str
        ローカルパス
    """

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        # Vue に渡すときは、 JSON オブジェクトではなく、 JSON 文字列です
        'dj_extends_user_str': json.dumps(MhUser.get_extends_user_dic()),
        #   --------                                 --------
    }

    return render(request, lp_extends_user_list, context)
