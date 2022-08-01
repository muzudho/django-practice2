from django.urls import path

# O5o1o0gA11o0 ポータルの練習
from apps1.portal_v1.views.portal.v1o0 import Portal as PortalO1o0
#          ---------              ----        ------    ----------
#          11                     12          2         3
#    ---------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# ポータル
from apps1.portal_v1.views.o2o0.portal import Portal as PortalO2o0
#                           ^two
#          ---------            ------        ------    ----------
#          11                   12            2         3
#    ---------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [

    # ポータルの練習
    path('practice/v1/portal',
         # -----------------
         # 1
         PortalO1o0.render, name='practice_v1_portal'),
    #    -----------------        ------------------
    #    2                        3
    # 1. 例えば `http://example.com/practice/v1/portal` のようなURLのパスの部分
    #                              -------------------
    # 2. PortalO1o0 (別名)クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_portal' %} のような形でURLを取得するのに使える

    # ポータル
    path('', PortalO2o0.render, name='portal'),
    #    --  -----------------        ------
    #    1   2                        3
    # 1. 例えば `http://example.com/` のようなURLの直下
    # 2. PortalO2o0 (別名)クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'portal' %} のような形でURLを取得するのに使える
]
