from django.urls import path

# O5o2o0g8o0 ポータル
from apps1.portal_v1.views.portal.v2o0 import Portal as PortalO2o0
#                                  ^two
#          ---------            ------        ------    ----------
#          11                   12            2         3
#    ---------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [

    # ポータル
    path('', PortalO2o0.render, name='portal'),
    #    --  -----------------        ------
    #    1   2                        3
    # 1. 例えば `http://example.com/` のようなURLの直下
    # 2. PortalO2o0 (別名)クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'portal' %} のような形でURLを取得するのに使える
]
