"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # 最初から Django の管理画面は用意されている
    path('admin/', admin.site.urls),
    #     ------   ---------------
    #     1        2
    # 1. 例えば `http://example.com/admin/` のような URLのパスの部分
    #                              -------
    # 2. 例えば `http://example.com/admin/login/?next=/admin/` のように admin.site.urls モジュールに含まれる urlpatterns を (1.) にぶら下げる
    #                                    --------------------
    #
    # もしあなたが、あとで Django アプリケーションを作ったなら、以下のように追加することになるだろう
    # path('', include('app1.urls')),
    #      --           ---------
    #      1            2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `host1/app1/urls.py` の urlpatterns を (1.) にぶら下げる
    #           ---------

    # 練習
    path('', include('project1.urls_practice')),
    #    --           ----------------------
    #      1          2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `host1/project1/urls_practice.py` の urlpatterns を (1.) にぶら下げる
    #           ----------------------


    # ポータル
    path('', include('project1.urls_portal')),
    #    --           --------------------
    #      1          2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `host1/project1/urls_portal.py` の urlpatterns を (1.) にぶら下げる
    #           --------------------


    # 認証
    path('', include('project1.urls_accounts')),
    #    --           ----------------------
    #      1          2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `host1/project1/urls_accounts.py` の urlpatterns を (1.) にぶら下げる
    #           ----------------------

    # 〇×ゲーム v1.0.1
    path('', include('project1.urls_tic_tac_toe_v1')),
    #    --           ----------------------------
    #      1          2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `host1/project1/urls_tic_tac_toe_v1.py` の urlpatterns を (1.) にぶら下げる
    #           ----------------------------
]
