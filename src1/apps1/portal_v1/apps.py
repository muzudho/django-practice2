from django.apps import AppConfig


class PortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # 変更前
    #name = 'portal_v1'
    # 変更後
    name = 'apps1.portal_v1'
    #       ---------------
    #       1
    # 1. `src1/apps1/portal_v1/apps.py`
    #          ---------------
