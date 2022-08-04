from django.urls import path

# OA16o2o0gA16o0 〇×ゲーム v2 思考エンジン
from apps1.tic_tac_toe_v2.views.think.engine_manual.v1o0 import EngineManual
#          --------------                           ----        ------------
#          11                                       12          2
#    ---------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 〇×ゲーム v2 対局申込ページ
from apps1.tic_tac_toe_v2.views.o1o0.gui.match_application import MatchApplicationV
#          --------------                  ---------------        -----------------
#          11                              12                     2
#    -----------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 〇×ゲーム v2 対局中ページ
from apps1.tic_tac_toe_v2.views.o1o0.gui.playing import PlayingV
#          --------------                -------        --------
#          11                            12             2
#    -------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [

    # OA16o2o0gA16o0 エンジン手動
    path('tic-tac-toe/v2/engine-manual/',
         # ----------------------------
         # 1
         EngineManual.render),
    #    -------------------
    #    2
    # 1. 例えば `http://example.com/tic-tac-toe/v2/engine-manual/` のような URL のパスの部分
    #                              -----------------------------
    # 2. EngineManual クラスの render 静的メソッド

    # 対局申込
    path('tic-tac-toe/v2/match-application/',
         # --------------------------------
         # 1
         MatchApplicationV.render),
    #    ------------------------
    #    2
    # 1. 例えば `http://example.com/tic-tac-toe/v2/match-application/` のような URL のパスの部分
    #                              ---------------------------------
    # 2. MatchApplicationV クラスの render 静的メソッド

    # 対局中
    path('tic-tac-toe/v2/playing/<str:kw_room_name>/',
         # -----------------------------------------
         # 1
         PlayingV.render),
    #    ---------------
    #    2
    # 1. 例えば `http://example.com/tic-tac-toe/v2/playing/<部屋名>/` のような URL のパスの部分。
    #                              --------------------------------
    #    <部屋名> に入った文字列は kw_room_name 変数に渡されます
    # 2. PlayingV クラスの render 静的メソッド
]
