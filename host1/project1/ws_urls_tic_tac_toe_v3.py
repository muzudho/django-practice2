# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# 〇×ゲームの練習３．０．１
from apps1.tic_tac_toe_v3.websocks.o0o1.consumer_custom import TicTacToeV3o0o1ConsumerCustom
#                       ^three                                           ^^^^^ three.zero.one
#    ----- -------------- ------------- ---------------        -----------------------------
#    1     2              3             4                      5
# 1,3 ディレクトリー名
# 1. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

# ...中略...

websocket_urlpatterns = [

    # ...中略...

    # 〇×ゲームの練習３．０．３
    url(r'^tic-tac-toe/v3o0o3/playing/(?P<kw_room_name>\w+)/$',
        #               ^^^^^ three.zero.three
        # -------------------------------------------------
        # 1
        TicTacToeV3o0o1ConsumerCustom.as_asgi()),
    #             ^^^^^ three.zero.one
    #   ---------------------------------------
    #   2
    # 1. 例えば `ws://example.com/tic-tac-toe/v3o0o3/playing/Elephant/` のようなURLのパスの部分
    #                            ------------------------------------
    #    kw_room_name は変数として渡される
    # 2. クラス名とメソッド。 URL を ASGI形式にする
]