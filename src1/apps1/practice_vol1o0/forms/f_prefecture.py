# BOF OA11o4o0g3o0

from django.forms import ModelForm

# 都道府県モデル
from apps1.practice_vol1o0.models.prefecture.ver1o0 import Prefecture
#          ---------------                   ------        ----------
#          11                                12            2
#    ----------------------------------------------
#    10
# 10. ディレクトリー
# 11 アプリケーション
# 12. Pythonファイル名 拡張子抜き
# 2. クラス


class PrefectureForm(ModelForm):
    """OA11o4o0g3o0 練習1.0巻 都道府県フォーム1.0版"""

    class Meta:
        model = Prefecture  # モデル指定
        fields = ('seq', 'name',)  # フィールド指定

# EOF OA11o4o0g3o0
