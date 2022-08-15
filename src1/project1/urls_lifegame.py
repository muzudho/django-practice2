from django.urls import path

# OAAA1001o1o0g9o0 ライフゲーム v0.1 の盤
from apps1.lifegame_v1.views.board.v0o1o0 import BoardView as BoardViewV0o1o0
#          -----------             ------        ---------    ---------------
#          11                      12            2            3
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


# OAAA1001o1o0ga12o_7o0 ライフゲーム v0.2 の盤
from apps1.lifegame_v1.views.board.v0o2o0 import BoardView as BoardViewV0o2o0
#          -----------             ------        ---------    ---------------
#          11                      12            2            3
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [

    # OAAA1001o1o0ga10o0 ライフゲーム v0.1 の盤
    path('lifegame/v0.1/board',
         # ------------------
         # 1
         BoardViewV0o1o0.render, name='lifegame_v0o1o0_board'),
    #    ----------------------        ---------------------
    #    2                             3
    # 1. 例えば `http://example.com/lifegame/v0.1/board` のようなURLのパスの部分
    #                              -------------------
    # 2. BoardViewV0o1o0 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'lifegame_v0o1o0_board' %} のような形でURLを取得するのに使える


    # OAAA1001o1o0ga12o_7o0 ライフゲーム v0.2 の盤
    path('lifegame/v0.2/board',
         # ------------------
         # 1
         BoardViewV0o2o0.render, name='lifegame_v0o2o0_board'),
    #    ----------------------        ---------------------
    #    2                             3
    # 1. 例えば `http://example.com/lifegame/v0.2/board` のようなURLのパスの部分
    #                              -------------------
    # 2. BoardViewV1o1o0 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'lifegame_v0o2o0_board' %} のような形でURLを取得するのに使える
]
