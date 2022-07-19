from django.forms import ModelForm

# 都道府県モデル
from apps1.practice_v1.models.o2o1.m_prefecture import Prefecture
#          -----------             ------------        ----------
#          1.1                     2                   3
#    ------------------------------------------
#    1
# 1. ディレクトリー
# 1.1 アプリケーション
# 2. Pythonファイル名 拡張子抜き
# 3. クラス名


class PrefectureForm(ModelForm):
    class Meta:
        model = Prefecture  # モデル指定
        fields = ('seq', 'name',)  # フィールド指定
