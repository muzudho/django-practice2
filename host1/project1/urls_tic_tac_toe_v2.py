from django.urls import path

# 〇×ゲーム v2.0.1
from apps1.tic_tac_toe_v2.views.o1o0.think.engine_manual import EngineManual
#    ----- -------------- ------------------------------        ------------
#    1     2              3                                     4
#    ---------------------------------------------------
#    5
# 1. 開発者用ディレクトリーの一部
# 2. アプリケーション フォルダー名
# 3. ディレクトリー名
# 4. クラス名
# 5. Pythonモジュール名

# 対局申込ページ v2.0.1
from apps1.tic_tac_toe_v2.views.o1o0.gui.match_application import MatchApplicationV
#          --------------                -----------------        -----------------
#          1.1                           1.2                      2
#    -----------------------------------------------------
#    1
# 1, 1.2 ディレクトリー
# 1.1 アプリケーション
# 2. `1.2` に含まれる __init__.py ファイルにさらに含まれるクラス

from apps1.tic_tac_toe_v2.views.o1o0.gui.playing import PlayingV


urlpatterns = [

    # エンジン手動
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
