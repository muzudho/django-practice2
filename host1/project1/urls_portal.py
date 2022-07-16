from django.urls import path

# * 変更前
# from apps1.portal_v1.views.o1.pages import Portal
# * 変更後
from apps1.portal_v1.views.o2.pages import Portal
#                           ^two
#    ------------------------ -----        ------
#    1                        2            3
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き
# 3. クラス名


urlpatterns = [

    # ポータル
    path('', Portal.render, name='page1'),
    #    --  -------------        -----
    #    1   2                    3
    # 1. 例えば `http://example.com/` のようなURLの直下
    # 2. Portal クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page1' %} のような形でURLを取得するのに使える
]
