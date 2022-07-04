from django.urls import path

# 〇×ゲーム v2.0.1
from apps1.tic_tac_toe_v2.views.v2o0o1 import resources as tic_tac_toe_v2
#    ----- -------------- ------------        ---------    --------------
#    1     2              3                 4            5
#    -------------------------------
#    6
# 1. 開発者用ディレクトリーの一部
# 2. アプリケーション フォルダー名
# 3. ディレクトリー名
# 4. Python ファイル名。拡張子抜き
# 5. `4.` の別名
# 6. モジュール名


urlpatterns = [

    # エンジン手動
    path('tic-tac-toe/v2o0o1/engine-manual/',
         # --------------------------------
         # 1
         tic_tac_toe_v2.EngineManual.render),
    #    ----------------------------------
    #    2
    # 1. 例えば `http://example.com/tic-tac-toe/v2o0o1/engine-manual/` のような URL のパスの部分
    #                              --------------------------------
    # 2. tic_tac_toe_v2 (別名)ファイルの EngineManual クラスの render 静的メソッド
]
