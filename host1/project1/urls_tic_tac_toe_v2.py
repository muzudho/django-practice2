from django.urls import path

# 〇×ゲーム v2.0.1
from apps1.tic_tac_toe_v2.views.v2o0o1.engine_manual import EngineManual
#    ----- -------------- --------------------------        ------------
#    1     2              3                                 4
#    -----------------------------------------------
#    5
# 1. 開発者用ディレクトリーの一部
# 2. アプリケーション フォルダー名
# 3. ディレクトリー名
# 4. クラス名
# 5. Pythonモジュール名


urlpatterns = [

    # エンジン手動
    path('tic-tac-toe/v2o0o1/engine-manual/',
         # --------------------------------
         # 1
         EngineManual.render),
    #    -------------------
    #    2
    # 1. 例えば `http://example.com/tic-tac-toe/v2o0o1/engine-manual/` のような URL のパスの部分
    #                              --------------------------------
    # 2. EngineManual クラスの render 静的メソッド
]
