from django.forms import ModelForm

from apps1.practice.models.m_prefecture import Prefecture
#    ----- -------- ------ ------------        ----------
#    1     2        3      4                   5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


class PrefectureForm(ModelForm):
    class Meta:
        model = Prefecture  # モデル指定
        fields = ('seq', 'name',)  # フィールド指定
