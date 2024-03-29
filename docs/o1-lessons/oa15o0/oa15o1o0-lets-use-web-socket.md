# 目標

Webサーバーとクライアント間で双方向の非同期通信をしたい。だからする。  
その手法の１つの **Webソケット** ならできる  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| Key              | Value                                     |
| ---------------- | ----------------------------------------- |
| OS               | Windows10                                 |
| Container        | Docker                                    |
| Program Language | Python 3                                  |
| Auth             | allauth                                   |
| Frontend         | Vuetify                                   |
| Data format      | JSON                                      |
| Others           | (Socket), Web socket                      |
| Editor           | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 accounts_vol1o0    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   └── 📂 practice_vol1o0              # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       │   └── 📂 practice_vol1o0      # アプリケーションと同名
    │   │       │       └── 📂 data
    │   │       │           └── 📂 desserts1
    │   │       │               └── 📄 ver1o0.json
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_vol1o0      # アプリケーションと同名
    │   │       │       ├── 📂 prefecture
    │   │       │       └── 📂 vuetifies
    │   │       ├── 📂 views
    │   │       │   ├── 📂 prefecture
    │   │       │   └── 📂 vuetifies
    │   │       ├── 📄 __init__.py
    │   │       ├── 📄 admin.py
    │   │       ├── 📄 apps.py
    │   │       └── 📄 tests.py
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_accounts_vol1o0.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2                  # プロジェクト
    │   ├── 🐳 docker-compose-project2.yml
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📄 urls.py
    ├── 📂 src2_local                   # Djangoとは関係ないもの
    │    └── 📂 sockapp1
    │        ├── 📄 client.py
    │        ├── 📄 echo_server.py
    │        └── 📄 main_finally.py
    └── 📄 .gitignore
```

# 手順

## Step [OA15o1o0g1o0] Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step [OA15o1o0g2o0] Pythonパッケージ インストール指定 - requirements.txt ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1                   # あなたの開発用ディレクトリー。任意の名前
👉      └── 📄 requirements.txt
```

```shell
# ...略...


# 以下を追加
# For web socket
channels>=3.0
```

## Step [OA15o1o0g3o0] 設定の編集 - settings.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 project1                  # プロジェクト
👉      │   └── 📄 settings.py
        └── 📄 requirements.txt
```

```py
# ...略...


INSTALLED_APPS = [
    # ...略...


    # * 以下を追加
    # OA15o1o0g3o0 For web socket
    'channels',
]


# ...略...


# *
# ├── * 変更前
# │ // WSGI_APPLICATION = 'project1.wsgi.application'
# | // # * O2o1o0g9o1o2o_9o0 プロジェクト名の一般化
# │ // WSGI_APPLICATION = f'{PROJECT_NAME}.wsgi.application'
# │                         -------------------------------
# │                         1
# │ 1. DjangoのWSGI設定の大元となるグローバル変数。
# │    `src1/projectN/wsgi.py` ファイルの中の application 変数を指している
# │          -------------
# │
# └── * OA15o1o0g3o0 WSGI を ASGI にバージョンアップする
ASGI_APPLICATION = f"{PROJECT_NAME}.asgi.application"
#                    -------------------------------
#                    1
# 1. DjangoのASGI設定の大元となるグローバル変数。
#    `src1/projectN/asgi.py` ファイルの中の application 変数を指している
#          -------------

# * 続けて追加
# OA15o1o0g3o0 Webソケット使用
# See also: 📖 [Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)
CHANNEL_LAYERS = {
    'default': {
        # * Method 1: Via redis lab
        # 'BACKEND': 'channels_redis.core.RedisChannelLayer',
        # 'CONFIG': {
        #     "hosts": [
        #       'redis://h:<password>;@<redis Endpoint>:<port>'
        #     ],
        # },

        # * Method 2: Via local Redis
        # 'BACKEND': 'channels_redis.core.RedisChannelLayer',
        # 'CONFIG': {
        #      "hosts": [('127.0.0.1', 6379)],
        # },

        # Method 3: Via In-memory channel layer
        # Using this method.
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    },
}
```

👆 `WSGI` から `ASGI` に乗り換えた。 `ASGI` は `WSGI` を兼ねるようだ  

## Step [OA15o1o0g4o0] ASGI設定 - asgi.py ファイル＜その１＞

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 project1                  # プロジェクト
👉      │   ├── 📄 asgi.py
        │   └── 📄 settings.py
        └── 📄 requirements.txt
```

```py
import os

# * OA15o1o0g4o0 以下をコメントアウト
# from django.core.asgi import get_asgi_application

# vvvv OA15o1o0g4o0 ASGI設定
import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter
# ^^^^ OA15o1o0g4o0


# ...略... os.environ.setdefault( ... ) など


# * OA15o1o0g4o0 ASGI設定
django.setup()

# * OA15o1o0g4o0 以下を削除
# application = get_asgi_application()

# * OA15o1o0g4o0 ASGI設定
application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    # * IMPORTANT::Just HTTP for now. (We can add other protocols later.)
})
```

## Step [OA15o1o0g5o0] Visual Studio Code のエラー抑制 - pip コマンド

Python の channels パッケージは、 Dockerコンテナにインストールされていればよく、  
Dockerコンテナの外側のPCにインストールしている必要はないが、  
しかし あなたの Visual Studio Code は  
👇 以下のような PROBLEMS （エラーメッセージ）を出しているかもしれない  

```plaintext
Import "channels.http" could not be resolved
Import "channels.routing" could not be resolved
```

その Pythonソースは 外側のPCで実行するわけではないのだから無視して構わないが、気になるということはあるだろう。  
Dockerコンテナの外側のPCにも channels をインストールすれば（本末転倒だが）エラーメッセージは解消する。  
👇 もし望むなら、以下のコマンドを打鍵してほしい  

```shell
pip install channels
```

## Step [OA15o1o0g6o0] Dockerコンテナの停止～ビルド～起動

👇 以下のコマンドを打鍵してほしい  

```shell
# Dockerコンテナの停止
docker-compose down
# または Dockerマシンが走っているターミナルで `[Ctrl] + [C]` キーを打鍵
```

👇 以下のコマンドを打鍵してほしい  

```shell
# requirements.txtを変更したので、Pythonパッケージのインストールをやり直します
docker-compose build
```

👇 以下のコマンドを打鍵してほしい  

```shell
# Dockerコンテナの起動
docker-compose up
```

👆 これで Dockerコンテナに channels パッケージをインストールした  

## Step [OA15o1o0g7o0] Webソケット設定 - consumer.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_vol1o0              # アプリケーション
        │       └── 📂 websocks             # ただのフォルダー
        │           └── 📂 consumer         # ただのフォルダー
👉      │               └── 📄 ver1o0.py
        ├── 📂 project1                     # プロジェクト
        │   ├── 📄 asgi.py
        │   └── 📄 settings.py
        └── 📄 requirements.txt
```

```py
# See also:
#     📖 [Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)
#     📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
#     📖 [Channels - Channel Layers](https://channels.readthedocs.io/en/stable/topics/channel_layers.html)
from channels.generic.websocket import AsyncWebsocketConsumer


class WebsockPractice1V1Consumer(AsyncWebsocketConsumer):
    """OA15o1o0g7o0 非同期のWebソケットのコンシューマー"""

    async def connect(self):
        """接続時"""
        print("Connected")
        await self.accept()

    async def disconnect(self, close_code):
        """切断時"""
        print("Disconnected")

    async def receive(self, text_data):
        """メッセージ受信時
        Receive message from WebSocket.
        """
        print("Received")
        # Send message to WebSocket
        await self.send(text_data=f"Echo: {text_data}")

    async def send_message(self, res):
        """メッセージ送信時
        Receive message from room group
        """
        print("Sent message")
        # Send message to WebSocket
        await self.send(text_data=res)
```

## Step [OA15o1o0g8o0] ルート編集 - ws_urls_practice.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_vol1o0              # アプリケーション
        │       └── 📂 websocks
        │           └── 📂 consumer
        │               └── 📄 ver1o0.py
        ├── 📂 project1                     # プロジェクト
        │   ├── 📄 asgi.py
        │   ├── 📄 settings.py
👉      │   └── 📄 ws_urls_practice.py
        └── 📄 requirements.txt
```

```py
# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# OA15o1o0g8o0 練習1.0巻 Webソケットの練習１ 1.0版
from apps1.practice_vol1o0.websocks.consumer.ver1o0 import WebsockPractice1V1Consumer
#          ---------------                   ------        --------------------------
#          11                                12            2
#    ----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


websocket_urlpatterns = [

    # OA15o1o0g8o0 Webソケットの練習１
    url(r'^websock-practice1/v1/$', WebsockPractice1V1Consumer.as_asgi()),
    #     -----------------------   ------------------------------------
    #     1                         2
    # 1. 例えば `ws://example.com/websock-practice1/v1/` といったURLのパスの部分
    #                            ----------------------
    # 2. WebsockPractice1V1Consumer クラスの as_asgi 静的メソッドの返却値
]
```

## Step [OA15o1o0g9o0] ASGI設定 - asgi.py ファイル＜その２＞

👇以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_vol1o0              # アプリケーション
        │       └── 📂 websocks
        │           └── 📂 consumer
        │               └── 📄 ver1o0.py
        ├── 📂 project1                  # プロジェクト
👉      │   ├── 📄 asgi.py
        │   ├── 📄 settings.py
        │   └── 📄 ws_urls_practice.py
        └── 📄 requirements.txt
```

```py
import os

# * OA15o1o0g9o0 コメントアウトの解除
from django.core.asgi import get_asgi_application

# * 追加の取消ここから
# import django
# from channels.http import AsgiHandler
# * 追加の取消ここまで

# * 追加ここから
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# OA15o1o0g9o0 Webソケット練習１
from . import ws_urls_practice
#    -        ----------------
#    1        2
# 1. 同じディレクトリー
# 2. `src1/projectN/ws_urls_practice.py`
#                   ----------------
# * 追加ここまで


# ...略...
# この辺に os.environ.setdefault(...)


# * 追加の取消
# django.setup()


# ...略...


# * 以下を追加
# OA15o1o0g9o0 複数のアプリケーションの websocket_urlpatterns をマージします
websocket_urlpatterns_merged = []

# OA15o1o0g9o0 Webソケット練習１
websocket_urlpatterns_merged.extend(
    ws_urls_practice.websocket_urlpatterns)


# * 変更前
# | application = ProtocolTypeRouter({
# |     "http": AsgiHandler(),
# |     # * IMPORTANT::Just HTTP for now. (We can add other protocols later.)
# | })
# * OA15o1o0g9o0 変更後
application = ProtocolTypeRouter({
    # * 削除
    # "http": AsgiHandler(),
    # * 追加
    "http": get_asgi_application(),
    # * 追加
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns_merged
        )
    ),
})
```

## Step [OA15o1o0gA10o0] ローカルPCにPythonのパッケージ websocket-client をインストール

Step [OA15o1o0g1o0]～ 9. は Dockerコンテナの中のサーバーサイドだった。  
既に Djangoサーバー側では Webソケットで接続されるのを待っている  

Step [OA15o1o0g9o0] からは Dockerコンテナの外のクライアントサイドを説明する  

👇 Dockerコンテナの外側の あなたのPCでコマンドを打鍵してほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
# cd src1

pip install websocket-client
```

## Step [OA15o1o0gA11o0] 複製 - main_finally.py ファイル

👇 以下の記事で掲載した main_finally.py ファイルをコピー＆ペーストしてほしい  

* 📖 [ソケットを使おう！](https://qiita.com/muzudho1/items/7a6501f7dbafbaa9b96c)

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 practice_vol1o0              # アプリケーション
    │   │       └── 📂 websocks
    │   │           └── 📂 consumer
    │   │               └── 📄 ver1o0.py
    │   ├── 📂 project1                  # プロジェクト
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings.py
    │   │   └── 📄 ws_urls_practice.py
    │   └── 📄 requirements.txt
    └── 📂 src2_local
         ├── 📂 sockapp1
         │   ├── 📄 client.py
         │   ├── 📄 echo_server.py
👉       │   └── 📄 main_finally.py  # ここからコピー
         └── 📂 websockapp1
👉           └── 📄 main_finally.py  # ここへペースト
```

## Step [OA15o1o0gA12o0] Webソケット クライアント作成 - websock_client.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 practice_vol1o0              # アプリケーション
    │   │       └── 📂 websocks
    │   │           └── 📂 consumer
    │   │               └── 📄 ver1o0.py
    │   ├── 📂 project1                  # プロジェクト
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings.py
    │   │   └── 📄 ws_urls_practice.py
    │   └── 📄 requirements.txt
    └── 📂 src2_local
         ├── 📂 sockapp1
         │   ├── 📄 client.py
         │   ├── 📄 echo_server.py
         │   └── 📄 main_finally.py
         └── 📂 websockapp1
             ├── 📄 main_finally.py
👉           └── 📄 websock_client.py
```

```py
# See also:
#     📖 [Python WebSocket通信の仕方：クライアント編](https://www.raspberrypirulo.net/entry/websocket-client)
#     📖 [websocket-client - Examples](https://websocket-client.readthedocs.io/en/latest/examples.html)
#     📖 [GitHub - websocket-client](https://github.com/websocket-client/websocket-client)
import sys
import traceback
import websocket

try:
    import thread  # 見つからない
except ImportError:
    import _thread as thread  # websocket-client の GitHub ではこっちが使われている

import time
import argparse
from main_finally import MainFinally


class Websocket_Client():
    """OA15o1o0gA12o0 Webソケット クライアント"""

    def __init__(self, url):

        # デバックログの表示/非表示設定
        websocket.enableTrace(True)

        # WebSocketAppクラスを生成
        self.websockApp = websocket.WebSocketApp(url,
                                                 on_open=lambda ws: self.on_open(
                                                     ws),
                                                 on_close=lambda ws, close_status_code, close_msg: self.on_close(
                                                     ws, close_status_code, close_msg),
                                                 on_message=lambda ws, msg: self.on_message(
                                                     ws, msg),
                                                 on_error=lambda ws, msg: self.on_error(ws, msg))

    def on_message(self, ws, message):
        """メッセージ受信に呼ばれる関数"""
        print("receive : {}".format(message))

    def on_error(self, ws, error):
        """エラー時に呼ばれる関数"""
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        """サーバーから切断時に呼ばれる関数"""
        print("### closed ###")

    def on_open(self, ws):
        """サーバーから接続時に呼ばれる関数"""
        thread.start_new_thread(self.run_worker, ())

    def run_worker(self, *args):
        """サーバーから接続時にスレッドで起動する関数"""
        while True:
            time.sleep(0.1)
            input_data = input("send data:")
            self.websockApp.send(input_data)

    def clean_up(self):
        self.websockApp.close()
        print("thread terminating...")

    def run_forever(self):
        """websocketクライアント起動"""
        self.websockApp.run_forever()


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":

    class Main1:
        def __init__(self):
            self._client = None

        def on_main(self):
            parser = argparse.ArgumentParser(
                description='サーバーのアドレスとポートを指定して、テキストを送信します')
            parser.add_argument('--host', default="127.0.0.1",
                                help='サーバーのホスト。規定値:127.0.0.1')
            parser.add_argument('--port', type=int,
                                default=8000, help='サーバーのポート。規定値:8000')
            args = parser.parse_args()

            # FIXME このURLの埋め込みを外に出せないか？
            url = f"ws://{args.host}:{args.port}/websock-practice1/v1/"
            self._client = Websocket_Client(url)
            self._client.run_forever()
            return 0

        def on_except(self, e):
            """ここで例外キャッチ"""
            traceback.print_exc()

        def on_finally(self):
            if self._client:
                self._client.clean_up()

            print("★これで終わり")
            return 1

    sys.exit(MainFinally.run(Main1()))
```

## Step [OA15o1o0gA13o0] Webソケット通信 - コマンド実行

👇 以下のコマンドを打鍵してほしい  

```shell
# がんばって `src2_local/websockapp1` へ、カレントディレクトリを移動してほしい
# cd src2_local/websockapp1

python.exe -m websock_client
```

これで サーバー側とつながったはずだ。  
適当な文字列 `hello` でも打鍵してほしい。  
`receive : Echo: hello` と返ってくれば成功だ

クライアント側は `[ctrl] + [C]` キーで終了してほしい  

サーバー側で `[ctrl] + [C]` キーを打鍵するとサーバーが落ちるので注意してほしい  

# 次の記事

📖 [DjangoのWebサーバーとクライアント側のアプリ間でJSON形式のテキストを通信しよう！](https://qiita.com/muzudho1/items/a3870c78f609a65debe0)

# 参考にした記事

📖 [Python WebSocket通信の仕方：クライアント編](https://www.raspberrypirulo.net/entry/websocket-client)  
📖 [websocket-client - Examples](https://websocket-client.readthedocs.io/en/latest/examples.html)  
📖 [GitHub - websocket-client](https://github.com/websocket-client/websocket-client)  
📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)  
📖 [Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)  
📖 [Python で終了時に必ず何か実行したい](https://qiita.com/qualitia_cdev/items/f536002791671c6238e3)  
📖 [Django を WebSocket サーバにする](https://qiita.com/ekzemplaro/items/a6b81bd1d181fdd0cc24)  
📖 [django-channels を使った websocket を用いたチャットアプリの作成](https://zenn.dev/y_k/articles/e8878460fff3d5aa1d1d)  
📖 [Django ChannelsでできるリアルタイムWeb](https://qiita.com/massa142/items/cbd508efe0c45b618b34)  
