from django.apps import AppConfig


class LifegameV1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    # name = 'lifegame_vol1o0'
    # * OAAA1001o1o0g5o0 変更後
    name = 'apps1.lifegame_vol1o0'
    #       ---------------------
    #       1
    # 1. `src1/apps1/lifegame_vol1o0/apps.py`
    #          ---------------------
