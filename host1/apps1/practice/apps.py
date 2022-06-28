from django.apps import AppConfig


class PracticeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    #name = 'practice'
    # * 変更後
    name = 'apps1.practice'
    #       --------------
    #       1
    # 1. `host1/apps1/practice/apps.py`
    #           --------------
