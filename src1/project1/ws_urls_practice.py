# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# OA15o1o0g8o0 Webソケットの練習１
from apps1.practice_v1.websocks.consumer.v1o0 import WebsockPractice1V1Consumer
#          -----------                   ----        --------------------------
#          11                            12          2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# Webソケットの練習２
from apps1.practice_v1.websocks.o1o0.consumer_as_json import WebsockPractice2V1Consumer
#                                                                         ^two
#    ------------------------------- ----------------        --------------------------
#    1                               2                       3
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き
# 3. クラス名


websocket_urlpatterns = [

    # OA15o1o0g8o0 Webソケットの練習１
    url(r'^websock-practice1/v1/$', WebsockPractice1V1Consumer.as_asgi()),
    #     -----------------------   ------------------------------------
    #     1                         2
    # 1. 例えば `ws://example.com/websock-practice1/v1/` といったURLのパスの部分
    #                            ----------------------
    # 2. WebsockPractice1V1Consumer クラスの as_asgi 静的メソッドの返却値

    # Webソケットの練習２
    url(r'^websock-practice2/v1/$', WebsockPractice2V1Consumer.as_asgi()),
    #                      ^two                    ^two
    #     -----------------------   ------------------------------------
    #     1                         2
    # 1. 例えば `ws://example.com/websock-practice2/v1/` といったURLのパスの部分
    #                            ----------------------
    # 2. WebsockPractice2V1Consumer クラスの as_asgi 静的メソッドの返却値
]
