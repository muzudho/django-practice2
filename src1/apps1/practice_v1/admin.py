from django.contrib import admin

# O9o2o0gA13o0 Userの拡張
from .models.user_profile.v1o0 import Profile
#    -------------------------        -------
#    1                                2
# 1. このファイルと同じディレクトリにある `models/user_profile/v1o0.py` ファイルの拡張子抜き
#                                      ------------------------
# 2. クラス

# OA10o1o0g3o0 都道府県
from .models.prefecture.v1o0 import Prefecture
#    -----------------------        ----------
#    1                              2
# 1. このファイルと同じディレクトリにある `models/prefecture/v1o0.py` ファイルの拡張子抜き
#                                      ----------------------
# 2. クラス

from .models.o1o0.m_dessert import Dessert
#    ----------------------        -------
#    1                             2
# 1. このファイルと同じディレクトリにある `models/o1o0/m_dessert.py` ファイルの拡張子抜き
#                                      ----------------------
# 2. クラス

# 対局部屋
from .models.o1o0.m_room import Room
#    -------------------        ----
#    1                          2
# 1. このファイルと同じディレクトリにある `models/o1o0/m_room.py` ファイルの拡張子抜き
#                                      ------------------
# 2. クラス

# Register your models here.
#   └── * 管理画面にモデルが表示されるようになる
#       └── * `manage.py makemigrations` コマンドの実行対象になる

# O9o2o0gA13o0 Userの拡張
admin.site.register(Profile)

# OA10o1o0g3o0 都道府県
admin.site.register(Prefecture)

admin.site.register(Dessert)

admin.site.register(Room)
