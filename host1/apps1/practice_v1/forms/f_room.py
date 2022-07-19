from django.forms import ModelForm

from apps1.practice_v1.models.o2o1.m_room import Room
#          -----------             ------        ----
#          1.1                     1.2           2
#    ------------------------------------
#    1
# 1, 1.2 ディレクトリー
# 1.1 アプリケーション
# 2. `1.2` に含まれる __init__.py ファイルにさらに含まれるクラス


class RoomForm(ModelForm):
    class Meta:
        model = Room  # モデル指定
        fields = ('name', 'board', 'record',)  # フィールド指定
