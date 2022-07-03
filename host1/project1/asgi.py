"""
ASGI config for project1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import project1.ws_urls1
#      -----------------
#      1
# 1. `host1/project1/ws_urls1.py`
#           -----------------

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')
#                                                -----------------
#                                                1
# 1. 設定モジュール名 `host1/project1/settings.py`
#                          -----------------
#    例えばレッスンの最初に project1 プロジェクトを作成した場合、
#    デフォルトでは project1 プロジェクトの設定モジュール名 `project1.settings` がハードコーディングされる
#                                                       -------- --------
#                                                       1.1      1.2
#    1.1 プロジェクト フォルダー名
#    1.2 settings.py ファイルの拡張子抜き

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            project1.ws_urls1.websocket_urlpatterns
        )
    ),
})
