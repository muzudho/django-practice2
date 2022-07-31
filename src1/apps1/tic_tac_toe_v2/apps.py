from django.apps import AppConfig


class TicTacToeV2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    # name = 'tic_tac_toe_v2'
    # * 変更後
    name = 'apps1.tic_tac_toe_v2'
    #       --------------------
    #       1
    # 1. `src1/apps1/tic_tac_toe_v2/apps.py`
    #          --------------------
