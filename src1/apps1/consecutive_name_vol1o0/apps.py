from django.apps import AppConfig


class NameOfConsecutiveVol1O0Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    # name = 'consecutive_name_vol1o0'
    # * [OAAA1001o2o0g5o0] 変更後
    name = 'apps1.consecutive_name_vol1o0'
    #       -----------------------------
    #       1
    # 1. `src1/apps1/consecutive_name_vol1o0/apps.py`
    #          -----------------------------
