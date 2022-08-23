# BOF OA16o1o0gA20o0

# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# OA16o1o0gA20o0 〇×ゲーム1.0巻 1.0版
from apps1.tic_tac_toe_vol1o0.websocks.consumer.ver1o0 import TicTacToeV1Consumer
#          ------------------                   ------        -------------------
#          11                                   12            2
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


websocket_urlpatterns = [

    # OA16o1o0gA20o0 〇×ゲーム1.0巻 1.0版
    url(r'^tic-tac-toe/v1/playing/(?P<room_name>\w+)/$',
        # --------------------------------------------
        # 1
        TicTacToeV1Consumer.as_asgi()),
    #   -----------------------------
    #   2
    # 1. 例えば `ws://example.com/tic-tac-toe/v1/playing/Elephant/` のようなURLのパスの部分
    #                            --------------------------------
    #    room_name は変数として渡される
    # 2. クラス名とメソッド。 URL を ASGI形式にする
]

# EOF OA16o1o0gA20o0
