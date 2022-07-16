from django.contrib import admin

from .models.o1o0.m_prefecture import Prefecture
#    -------------------------        ----------
#    1                                2
#
# 1. このファイルと同じディレクトリにある `models/v0o0o1/m_prefecture.py` ファイルの拡張子抜き
#                                      --------------------------
# 2. クラス名

from .models.o1o0.m_dessert import Dessert
#    ----------------------        -------
#    1                             2
#
# 1. このファイルと同じディレクトリにある `models/v0o0o1/m_dessert.py` ファイルの拡張子抜き
#                                      --------------------------
# 2. クラス名

# Userの拡張
from .models.o1o0.m_user_profile import Profile
#    ---------------------------        -------
#    1                                  2
#
# 1. このファイルと同じディレクトリにある `models/v0o0o1/m_user_profile.py` ファイルの拡張子抜き
#                                      ----------------------------
# 2. クラス名

# 対局部屋
from .models.o1o0.m_room import Room
#    -------------------        ----
#    1                          2
#
# 1. このファイルと同じディレクトリにある `models/v0o0o1/m_room.py` ファイルの拡張子抜き
#                                      ---------------------
# 2. クラス名

# Register your models here.
#   └── * 管理画面にモデルが表示されるようになる
#       └── * `manage.py makemigrations` コマンドの実行対象になる
admin.site.register(Profile)
admin.site.register(Prefecture)
admin.site.register(Dessert)
admin.site.register(Room)
