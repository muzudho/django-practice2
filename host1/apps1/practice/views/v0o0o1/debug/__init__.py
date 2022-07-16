from django.http import HttpResponse

from apps1.practice.models_helper.mh_json import MhJson
#    ----- -------- ---------------------        ------
#    1     2        3                            4
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. クラス名

from apps1.practice.models.v0o0o1.m_prefecture import Prefecture
#          --------               ------------        ----------
#          1.1                    2                   3
#    ----------------------------
#    1
# 1. ディレクトリー
# 1.1 アプリケーション
# 2. Pythonファイル名 拡張子抜き
# 3. クラス名


class DebugV():
    """デバッグ ビュー"""

    @staticmethod
    def render_model_as_json(request):
        """描画 - モデルをダンプ出力する"""

        prefecture_resultset = Prefecture.objects.all()
        json_str = MhJson.from_model_to_json_str(prefecture_resultset)
        return HttpResponse(json_str)
