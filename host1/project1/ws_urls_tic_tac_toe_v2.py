# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# 〇×ゲーム v2.0.1
from apps1.tic_tac_toe_v2.websocks.o1.gui.consumer_custom import TicTacToeV2ConsumerCustom
#    ----- -------------- --------------- ---------------        -------------------------
#    1     2              3               4                      5
#    ----------------------------------------------------
#    6
# 1. 開発者用ディレクトリーの一部
# 2. アプリケーション フォルダー名
# 3. ディレクトリー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名
# 6. モジュール名


websocket_urlpatterns = [

    # 〇×ゲーム v2.0.1
    url(r'^tic-tac-toe/v2o0o1/playing/(?P<kw_room_name>\w+)/$',
        # ---------------------------------------------------
        # 1
        TicTacToeV2ConsumerCustom.as_asgi()),
    #   -----------------------------------
    #   2
    # 1. 例えば `ws://example.com/tic-tac-toe/v2o0o1/playing/Elephant/` のようなURLのパスの部分
    #                            ------------------------------------
    #    kw_room_name は変数として渡される
    # 2. クラス名とメソッド。 URL を ASGI形式にする
]
