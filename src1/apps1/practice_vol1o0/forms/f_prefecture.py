from django.forms import ModelForm

# 都道府県モデル
from apps1.practice_v1.models.prefecture.v1o0 import Prefecture
#          -----------                   ----        ----------
#          11                            12          2
#    ----------------------------------------
#    10
# 10. ディレクトリー
# 11 アプリケーション
# 12. Pythonファイル名 拡張子抜き
# 2. クラス


class PrefectureForm(ModelForm):
    """OA11o4o0g3o0 都道府県フォーム"""

    class Meta:
        model = Prefecture  # モデル指定
        fields = ('seq', 'name',)  # フィールド指定
