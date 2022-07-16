from django.http import HttpResponse

# JSONモデルヘルパー
from apps1.practice_v1.models_helper.o1.mh_json import MhJson
#    ----- ----------- ------------------------        ------
#    1     2           3                               4
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. クラス名

# 都道府県モデル
from apps1.practice_v1.models.o1.m_prefecture import Prefecture
#          -----------           ------------        ----------
#          1.1                   2                   3
#    ----------------------------------------
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

        # * これだと１行で表示されて見づらい
        # json_str = MhJson.from_model_to_json_str(prefecture_resultset)
        # return HttpResponse(json_str)

        # * インデントを付けて、<pre>タグで挟む
        # * Unicode文字 が数字になって見づらいという副作用はある
        json_str = MhJson.from_model_to_json_str_with_indent(
            prefecture_resultset)
        return HttpResponse(f"<pre>{json_str}</pre>")
