# EOF OA18o5o0g3o0

from django.forms import ModelForm

# 部屋モデル
from apps1.practice_vol1o0.models.room.ver1o0 import Room
#          ---------------             ------        ----
#          11                          12            2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


class RoomForm(ModelForm):
    """OA18o5o0g3o0 対局部屋フォーム"""

    class Meta:
        model = Room  # モデル指定
        fields = ('name', 'board', 'record',)  # フィールド指定

# BOF OA18o5o0g3o0
