from django.apps import AppConfig


class TicTacToeV3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    # name = 'tic_tac_toe_v3'
    # * 変更後
    name = 'apps1.tic_tac_toe_v3'
    #       ------------
    #       1
    # 1. `host1/apps1/tic_tac_toe_v3/apps.py`
    #           --------------------
