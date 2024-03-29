from django.http import HttpResponse

# OA10o2o0g5o0 練習1.0巻 JSONモデルヘルパー1.0版
from apps1.practice_vol1o0.models_helper.json.ver1o0 import MhJson
#          ---------------                    ------        ------
#          11                                 12            2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# OA10o2o0g5o0 練習1.0巻 都道府県モデル1.0版
from apps1.practice_vol1o0.models.prefecture.ver1o0 import Prefecture
#          ---------------                   ------        ----------
#          11                                12            2
#    ----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


class DebugV():
    """OA10o2o0g5o0 デバッグ ビュー"""

    @staticmethod
    def render_model_as_json(request):
        """OA10o2o0g5o0 描画 - モデルをダンプ出力する"""

        prefecture_resultset = Prefecture.objects.all()

        # * これだと１行で表示されて見づらい
        # json_str = MhJson.from_model_to_json_str(prefecture_resultset)
        # return HttpResponse(json_str)

        # * インデントを付けて、<pre>タグで挟む
        # * Unicode文字 が数字になって見づらいという副作用はある
        json_str = MhJson.from_model_to_json_str_with_indent(
            prefecture_resultset)
        return HttpResponse(f"<pre>{json_str}</pre>")
