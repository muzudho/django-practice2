from django.urls import path

from apps1.tic_tac_toe_v1.views.o2o1.match_application import MatchApplicationV
#    ----- -------------- ----------------------------        -----------------
#    1     2              3                                   4
#    -------------------------------------------------
#    5
# 1. 開発者用ディレクトリーの一部
# 2. アプリケーション フォルダー名
# 3. ディレクトリー名
# 4. クラス名
# 5. Pythonモジュール名

from apps1.tic_tac_toe_v1.views.o2o1.playing import PlayingV


urlpatterns = [

    # 対局申込
    path('tic-tac-toe/v1/match-application/',
         # --------------------------------
         # 1
         MatchApplicationV.render),
    #    ------------------------
    #    2
    # 1. 例えば `http://example.com/tic-tac-toe/v1/match-application/` のような URL のパスの部分
    #                              ---------------------------------
    # 2. MatchApplicationV クラスの render 静的メソッド

    # 対局中
    path('tic-tac-toe/v1/playing/<str:room_name>/',
         # --------------------------------------
         # 1
         PlayingV.render),
    #    ---------------
    #    2
    # 1. 例えば `http://example.com/tic-tac-toe/v1/playing/<部屋名>/` のような URL のパスの部分。
    #                              --------------------------------
    #    <部屋名> に入った文字列は room_name 変数に渡されます
    # 2. PlayingV クラスの render 静的メソッド
]
