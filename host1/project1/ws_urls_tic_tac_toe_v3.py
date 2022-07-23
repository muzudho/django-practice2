# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# 〇×ゲームの練習 v3.1
from apps1.tic_tac_toe_v3.websocks.o1o0.consumer_custom import TicTacToeV3o1o0ConsumerCustom
#                       ^three
#          --------------               ---------------        -----------------------------
#          11                           12                     2
#    --------------------------------------------------
#    10
# 10. ディレクトリー
# 11. アプリケーション
# 12. Python ファイル。拡張子抜き
# 2. クラス名


# ...略...


websocket_urlpatterns = [
    # ...略...


    # 〇×ゲームの練習 v3.3
    url(r'^tic-tac-toe/v3.3/playing/(?P<kw_room_name>\w+)/$',
        #                 ^three
        # -------------------------------------------------
        # 1
        TicTacToeV3o1o0ConsumerCustom.as_asgi()),
    #   ---------------------------------------
    #   2
    # 1. 例えば `ws://example.com/tic-tac-toe/v3.3/playing/Elephant/` のようなURLのパスの部分
    #                            ----------------------------------
    #    kw_room_name は変数として渡される
    # 2. クラス名とメソッド。 URL を ASGI形式にする
]
