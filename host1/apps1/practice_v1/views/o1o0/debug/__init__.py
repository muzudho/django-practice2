from django.http import HttpResponse

# JSONモデルヘルパー
from apps1.practice_v1.models_helper.o1o0.mh_json import MhJson
#          -----------                    -------        ------
#          11                             12             2
#    --------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 都道府県モデル
from apps1.practice_v1.models.o1o0.m_prefecture import Prefecture
#          -----------             ------------        ----------
#          11                      12                  2
#    ------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


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
