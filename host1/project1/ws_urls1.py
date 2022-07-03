# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# Webソケットの練習１
from apps1.practice.websocks.v0o0o1.consumer import WebsockPractice1V1Consumer
#    ------------------------------ --------        --------------------------
#    1                              2               3
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き
# 3. クラス名

# Webソケットの練習２
from apps1.practice.websocks.v0o0o1.consumer_as_json import WebsockPractice2V1Consumer
#                                                                          ^two
#    ------------------------------ ----------------        --------------------------
#    1                              2                       3
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き
# 3. クラス名


websocket_urlpatterns = [

    # Webソケットの練習１
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
