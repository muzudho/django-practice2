# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# 〇×ゲームの練習 v3o1o0
from apps1.tic_tac_toe_v3.websocks.o1o0.consumer_custom import TicTacToeV3o1o0ConsumerCustom
#                       ^four                                              ^three
#    ----- -------------- ------------- ---------------        -----------------------------
#    1     2              3             4                      5
# 1,3 ディレクトリー名
# 1. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

# ...中略...

websocket_urlpatterns = [

    # ...中略...

    # 〇×ゲームの練習 v3o3o0
    url(r'^tic-tac-toe/v3o3o0/playing/(?P<kw_room_name>\w+)/$',
        #                 ^four
        # ---------------------------------------------------
        # 1
        TicTacToeV3o1o0ConsumerCustom.as_asgi()),
    #   ---------------------------------------
    #   2
    # 1. 例えば `ws://example.com/tic-tac-toe/v3o3o0/playing/Elephant/` のようなURLのパスの部分
    #                            ------------------------------------
    #    kw_room_name は変数として渡される
    # 2. クラス名とメソッド。 URL を ASGI形式にする
]
