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

# O3o2o_1o0g5o0 自動生成されたURL設定
from .urls_autogen import urlpatterns as urlpatterns_autogen
#    ]------------        -----------    -------------------
#    12                   3              4
# 1. 同じディレクトリー
# 2. `src1/projectN/urls_autogen.py`
#                   ------------
# 3. `2.` に含まれる変数
# 4. `3.` の別名

# O5o2o0g8o1o0 ランチャー1.0巻 2.0版
from apps1.launcher_vol1o0.views.launcher.ver2o0 import Launcher as LauncherView1o0g2o0
#                                            ^two
#          ---------------                ------        --------    -------------------
#          11                             12            2           3
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

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

    # O5o2o0g8o1o0 ランチャー1.0巻 2.0版
    # あとで allauth のURLをインクルードしたとき、そちらのルートパスのURL と衝突するようだから、
    # それより先に並べる必要がある
    path('', LauncherView1o0g2o0.render, name='home'),
    #    --  --------------------------        ----
    #    1   2                                 3
    # 1. 例えば `http://example.com/` のようなURLの直下
    # 2. LauncherView1o0g2o0 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'home' %} のような形でURLを取得するのに使える

    # O6o1o0gA13o0 ユーザー認証
    path('', include(f'{PROJECT_NAME}.urls_accounts')),
    #    --            ----------------------------
    #    1             2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `src1/projectN/urls_accounts.py` の urlpatterns を `1.` にぶら下げる
    #          ----------------------
]

# O3o2o_1o0g5o0 自動生成されたURL設定
urlpatterns.extend(urlpatterns_autogen)
