"""
ASGI config for project1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from .settings import PROJECT_NAME
#    ]--------        ------------
#    12               3
# 1. 同じディレクトリー
# 2. `host1/projectN/settings.py`
#                    --------
# 3. 変数

# Webソケット練習
from . import ws_urls_practice
#    -        ----------------
#    1        2
# 1. 同じディレクトリー
# 2. `host1/projectN/ws_urls_practice.py`
#                    ----------------

# 〇×ゲーム v1
from . import ws_urls_tic_tac_toe_v1
#    -        ----------------------
#    1        2
# 1. 同じディレクトリー
# 2. `host1/projectN/ws_urls_tic_tac_toe_v1.py`
#                    ----------------------

# 〇×ゲーム v2
from . import ws_urls_tic_tac_toe_v2
#                                  ^two
#    -        ----------------------
#    1        2
# 1. 同じディレクトリー
# 2. `host1/projectN/ws_urls_tic_tac_toe_v2.py`
#                    ----------------------

# 〇×ゲーム v3
from . import ws_urls_tic_tac_toe_v3
#                                  ^three
#    -        ----------------------
#    1        2
# 1. 同じディレクトリー
# 2. `host1/projectN/ws_urls_tic_tac_toe_v3.py`
#                    ----------------------

# * 変更前
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')
# * 変更後
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{PROJECT_NAME}.settings')
#                                                 -----------------------
#                                                 1
# 1. 設定モジュール名 `host1/projectN/settings.py`
#                          -----------------


# 複数のアプリケーションの websocket_urlpatterns をマージします
websocket_urlpatterns_merged = []

# Webソケット練習
websocket_urlpatterns_merged.extend(
    ws_urls_practice.websocket_urlpatterns)

# 〇×ゲーム v1
websocket_urlpatterns_merged.extend(
    ws_urls_tic_tac_toe_v1.websocket_urlpatterns)

# 〇×ゲーム v2
websocket_urlpatterns_merged.extend(
    ws_urls_tic_tac_toe_v2.websocket_urlpatterns)
#                        ^two

# 〇×ゲーム v3
websocket_urlpatterns_merged.extend(
    ws_urls_tic_tac_toe_v3.websocket_urlpatterns)
#                        ^three


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns_merged
        )
    ),
})
