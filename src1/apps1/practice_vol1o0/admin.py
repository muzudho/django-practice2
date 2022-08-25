from django.contrib import admin

# O9o2o0gA13o0 練習1.0巻 User拡張1.0版
from .models.user_profile.ver1o0 import Profile
#    ---------------------------        -------
#    1                                  2
# 1. このファイルと同じディレクトリにある `models/user_profile/ver1o0.py` ファイルの拡張子抜き
#                                      --------------------------
# 2. クラス

# OA10o1o0g3o0 都道府県
from .models.prefecture.v1o0 import Prefecture
#    -----------------------        ----------
#    1                              2
# 1. このファイルと同じディレクトリにある `models/prefecture/v1o0.py` ファイルの拡張子抜き
#                                      ----------------------
# 2. クラス

# OA13o4o0g3o0 デザート
from .models.dessert.v1o0 import Dessert
#    --------------------        -------
#    1                           2
# 1. このファイルと同じディレクトリにある `models/dessert/v1o0.py` ファイルの拡張子抜き
#                                      ----------------------
# 2. クラス

# OA18o1o0g3o0 対局部屋
from .models.room.v1o0 import Room
#    -----------------        ----
#    1                        2
# 1. このファイルと同じディレクトリにある `models/room/v1o0.py` ファイルの拡張子抜き
#                                      ----------------
# 2. クラス

# Register your models here.
#   └── * 管理画面にモデルが表示されるようになる
#       └── * `manage.py makemigrations` コマンドの実行対象になる

# O9o2o0gA13o0 Userの拡張
admin.site.register(Profile)

# OA10o1o0g3o0 都道府県
admin.site.register(Prefecture)

# OA13o4o0g3o0 デザート
admin.site.register(Dessert)

# OA18o1o0g3o0 対局部屋
admin.site.register(Room)
