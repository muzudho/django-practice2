from django.apps import AppConfig


class PracticeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    #name = 'practice_v1'
    # * O3o1o0g5o0 変更後
    name = 'apps1.practice_v1'
    #       -----------------
    #       1
    # 1. `src1/apps1/practice_v1/apps.py`
    #          -----------------
