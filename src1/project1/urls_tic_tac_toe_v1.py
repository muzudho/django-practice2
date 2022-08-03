from django.urls import path

# OA16o1o0gA17o0 対局申込
from apps1.tic_tac_toe_v1.views.match_application.v1o0 import MatchApplicationV
#          --------------                         ----        -----------------
#          11                                     12          2
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# OA16o1o0gA17o0 対局中
from apps1.tic_tac_toe_v1.views.playing.v1o0 import PlayingV
#          --------------               ----        --------
#          11                           12          2
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [

    # OA16o1o0gA17o0 対局申込
    path('tic-tac-toe/v1/match-application/',
         # --------------------------------
         # 1
         MatchApplicationV.render),
    #    ------------------------
    #    2
    # 1. 例えば `http://example.com/tic-tac-toe/v1/match-application/` のような URL のパスの部分
    #                              ---------------------------------
    # 2. MatchApplicationV クラスの render 静的メソッド

    # OA16o1o0gA17o0 対局中
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
