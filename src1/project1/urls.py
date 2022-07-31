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

# O3o1o0gA11o0 総合ルート編集
from .settings import PROJECT_NAME
#    ]--------        ------------
#    12               3
# 1. 同じディレクトリー
# 2. `src1/projectN/settings.py`
#                   --------
# 3. 変数

urlpatterns = [
    # 最初から Django の管理画面は用意されている
    path('admin/', admin.site.urls),
    #     ------   ---------------
    #     1        2
    # 1. 例えば `http://example.com/admin/` のような URLのパスの部分
    #                              -------
    # 2. 例えば `http://example.com/admin/login/?next=/admin/` のように admin.site.urls モジュールに含まれる urlpatterns を `1.` にぶら下げる
    #                                    --------------------
    #
    # もしあなたが、あとで Django アプリケーションを作ったなら、以下のように追加することになるだろう
    # path('', include('app1.urls')),
    #      --           ---------
    #      1            2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `src1/app1/urls.py` の urlpatterns を `1.` にぶら下げる
    #          ---------

    # O3o1o0gA11o0 練習
    path('', include(f'{PROJECT_NAME}.urls_practice')),
    #    --            ----------------------------
    #    1             2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `src1/projectN/urls_practice.py` の urlpatterns を `1.` にぶら下げる
    #          ----------------------


    # O5o1o0gA12o0 ポータル
    path('', include(f'{PROJECT_NAME}.urls_portal')),
    #    --            --------------------------
    #    1             2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `src1/projectN/urls_portal.py` の urlpatterns を `1.` にぶら下げる
    #          --------------------

    # O6o1o0gA13o0 ユーザー認証
    path('', include(f'{PROJECT_NAME}.urls_accounts')),
    #    --            ----------------------------
    #    1             2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `src1/projectN/urls_accounts.py` の urlpatterns を `1.` にぶら下げる
    #          ----------------------

    # OA16o1o0gA18o0 〇×ゲーム v1
    path('', include(f'{PROJECT_NAME}.urls_tic_tac_toe_v1')),
    #    --            ----------------------------------
    #    1             2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `src1/projectN/urls_tic_tac_toe_v1.py` の urlpatterns を `1.` にぶら下げる
    #          ----------------------------

    # OA16o2o0gA17o0 〇×ゲーム v2
    path('', include(f'{PROJECT_NAME}.urls_tic_tac_toe_v2')),
    #    --            ----------------------------------
    #    1             2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `src1/project1/urls_tic_tac_toe_v2.py` の urlpatterns を `1.` にぶら下げる
    #          ----------------------------
]
