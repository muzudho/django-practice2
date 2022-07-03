from django.contrib import admin

from .models.m_prefecture import Prefecture
#    --------------------        ----------
#    1                           2
#
# 1. このファイルと同じディレクトリにある `models/m_prefecture.py` ファイルの拡張子抜き
#                                      -------------------
# 2. クラス名

from .models.v0o0o1.m_dessert import Dessert
#    ------------------------        -------
#    1                               2
#
# 1. このファイルと同じディレクトリにある `models/v0o0o1/m_dessert.py` ファイルの拡張子抜き
#                                      --------------------------
# 2. クラス名

# Register your models here.
#   └── * 管理画面にモデルが表示されるようになる
#       └── * `manage.py makemigrations` コマンドの実行対象になる
admin.site.register(Prefecture)
admin.site.register(Dessert)
