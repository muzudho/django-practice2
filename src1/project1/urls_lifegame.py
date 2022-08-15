from django.urls import path

# OAAA1001o1o0g9o0 盤
from apps1.lifegame_v1.views.board.v1o0 import BoardView as BoardViewV1o0
#          -----------             ----        ---------    -------------
#          11                      12          2            3
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


# OAAA1001o1o0ga12o_7o0 盤
from apps1.lifegame_v1.views.board.v1o1o0 import BoardView as BoardViewV1o1o0
#          -----------             ------        ---------    ---------------
#          11                      12            2            3
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [

    # OAAA1001o1o0ga10o0 ライフゲーム v1 の盤
    path('lifegame/v1/board',
         # ----------------
         # 1
         BoardViewV1o0.render, name='lifegame_v1_board'),
    #    --------------------        -----------------
    #    2                           3
    # 1. 例えば `http://example.com/lifegame/v1/board` のようなURLのパスの部分
    #                              -----------------
    # 2. BoardViewV1o0 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'lifegame_v1_board' %} のような形でURLを取得するのに使える


    # OAAA1001o1o0ga12o_7o0 ライフゲーム v1.1 の盤
    path('lifegame/v1.1/board',
         # ------------------
         # 1
         BoardViewV1o1o0.render, name='lifegame_v1o1_board'),
    #    ----------------------        -------------------
    #    2                             3
    # 1. 例えば `http://example.com/lifegame/v1.1/board` のようなURLのパスの部分
    #                              -------------------
    # 2. BoardViewV1o1o0 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'lifegame_v1o1_board' %} のような形でURLを取得するのに使える
]
