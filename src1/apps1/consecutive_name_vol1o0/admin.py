from django.contrib import admin

# [OAAA1001o2o1o0g4o0] 連続名1.0巻 催事種別1.0版
from .models.event.ver1o0 import Event
#    --------------------        -----
#    1                           2
# 1. このファイルと同じディレクトリにある `models/event/ver1o0.py` ファイルの拡張子抜き
#                                      ----------------------
# 2. クラス

# [OAAA1001o2o1o0g4o0] 連続名1.0巻 催事巻1.0版
from .models.event_volume.ver1o0 import EventVolume

# Register your models here.
#   └── * 管理画面にモデルが表示されるようになる
#       └── * `manage.py makemigrations` コマンドの実行対象になる

# [OAAA1001o2o1o0g4o0] 連続名1.0巻 催事種別1.0版
admin.site.register(Event)

# [OAAA1001o2o1o0g4o0] 連続名1.0巻 催事巻1.0版
admin.site.register(EventVolume)
