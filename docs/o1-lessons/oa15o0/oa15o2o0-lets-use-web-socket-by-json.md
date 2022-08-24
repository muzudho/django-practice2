# 目標

Webサーバーとクライアント間でテキストを双方向の非同期通信するのは前にやった。  
今回は送受信するデータが JSON形式 しかないと割り切ってみる  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is          | This is                                   |
| ---------------- | ----------------------------------------- |
| OS               | Windows10                                 |
| Container        | Docker                                    |
| Program Language | Python 3                                  |
| Web framework    | Django                                    |
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
    │   │   └── 📂 practice_v1              # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       │   └── 📂 practice_v1
    │   │       │       └── 📂 data
    │   │       │           └── 📂 desserts1
    │   │       │               └── 📄 v1o0.json
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1          # アプリケーションと同名
    │   │       │       ├── 📂 prefecture
    │   │       │       └── 📂 vuetifies
    │   │       ├── 📂 views
    │   │       │   ├── 📂 prefecture
    │   │       │   └── 📂 vuetifies
    │   │       ├── 📂 websocks
    │   │       │   └── 📂 consumer
    │   │       │       └── 📄 v1o0.py
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
    │    ├── 📂 sockapp1
    │    │   ├── 📄 client.py
    │    │   ├── 📄 echo_server.py
    │    │   └── 📄 main_finally.py
    │    └── 📂 websockapp1
    │        ├── 📄 main_finally.py
    │        └── 📄 websock_client.py
    └── 📄 .gitignore
```

# 手順

## Step OA15o2o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA15o2o0g2o0 ASGI設定 - asgi.py ファイル

これは 前回の記事で行った。 WSGI を ASGI にバージョンアップしておくことは必要だ  

## Step OA15o2o0g3o0 Webソケット設定 - consumer_as_json/v1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1              # アプリケーション
                └── 📂 websocks
                    └── 📂 consumer_as_json
👉                      └── 📄 v1o0.py
```

```py
# See also:
#     📖 [Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)
#     📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
#     📖 [Channels - Channel Layers](https://channels.readthedocs.io/en/stable/topics/channel_layers.html)
from channels.generic.websocket import AsyncJsonWebsocketConsumer
#                                           ----
#                                           1
# 1. Json を使うものに変更


class WebsockPractice2V1Consumer(AsyncJsonWebsocketConsumer):
    """OA15o2o0g3o0 非同期のWebソケットのコンシューマー"""

    async def connect(self):
        """Called when the websocket is handshaking as part of initial connection."""
        print("Connected")
        await self.accept()

    async def disconnect(self, close_code):
        """Called when the WebSocket closes for any reason."""
        print("Disconnected")

    async def receive_json(self, doc):
        """
        Called when we get a text frame. Channels will JSON-decode the payload
        for us and pass it as the first argument.
        """
        print("Received JSON")
        # Send message to WebSocket
        await self.send(text_data=f"Echo: {doc}")

    async def send_message(self, res):
        """ Receive message from room group """
        print("Sent message")
        # Send message to WebSocket
        await self.send(text_data=res)
```

## Step OA15o2o0g4o0 ルート編集 - ws_urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1              # アプリケーション
        │       └── 📂 websocks
        │           └── 📂 consumer_as_json
        │               └── 📄 v1o0.py
        └── 📂 project1                  # プロジェクト
👉          └── 📄 ws_urls_practice.py
```

```py
# ...略...


# * 以下を追加
# OA15o2o0g4o0 Webソケットの練習２
from apps1.practice_v1.websocks.consumer_as_json.v1o0 import WebsockPractice2V1Consumer
#                                                                           ^two
#          -----------                           ----        --------------------------
#          11                                    12          2
#    ------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


websocket_urlpatterns = [
    # ...略...


    # * 以下を追加
    # OA15o2o0g4o0 Webソケットの練習２
    url(r'^websock-practice2/v1/$', WebsockPractice2V1Consumer.as_asgi()),
    #                      ^two                    ^two
    #     -----------------------   ------------------------------------
    #     1                         2
    # 1. 例えば `ws://example.com/websock-practice2/v1/` といったURLのパスの部分
    #                            ----------------------
    # 2. WebsockPractice2V1Consumer クラスの as_asgi 静的メソッドの返却値
]
```

## Step OA15o2o0g5o0 ローカルPCにPythonのパッケージ websocket-client をインストール

Step OA15o2o0g1o0～ 4. は サーバーサイドだった。  
Step OA15o2o0g5o0 からは クライアントサイドを説明する  

websocket-client パッケージは以前の記事で既にインストールしてある  

## Step OA15o2o0g6o0 Webクライアントソケット設定 - client_as_json.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 practice_v1              # アプリケーション
    │   │       └── 📂 websocks
    │   │           └── 📂 consumer_as_json
    │   │               └── 📄 v1o0.py
    │   └── 📂 project1                  # プロジェクト
    │       └── 📄 ws_urls_practice.py
    └── 📂 src2_local
         └── 📂 websockapp1
👉           └── 📄 client_as_json.py
```

```py
# See also:
#     📖 [GitHub andrewgodwin/channels-examples/multichat/chat/consumers.py](https://github.com/andrewgodwin/channels-examples/blob/master/multichat/chat/consumers.py)
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


class ClientAsJson():
    """OA15o2o0g6o0 Webソケット クライアント JSON使用"""

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
        print("### error ###")
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
            input_data = input("send JSON:")
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
            url = f"ws://{args.host}:{args.port}/websock-practice2/v1/"
            #                                    ---------------------
            #                                    1
            # 1. URLを合わせるように注意
            self._client = ClientAsJson(url)
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

## Step OA15o2o0g7o0 Webソケット クライアント起動 - コマンド実行

👇 以下のコマンドを打鍵してほしい

```shell
# がんばって `src2_local/websockapp1` へ、カレントディレクトリを移動してほしい
# cd src2_local/websockapp1

python.exe -m client_as_json
#             --------------
#             1
# 1. Pythonファイル名。拡張子抜き
```

これで サーバー側とつながったはずだ。  
適当なJSON形式の文字列 `{"x":1}` でも打鍵してほしい。  
JSON形式として ふさわしくない文字列を送信するとサーバーが止まってしまう。  
クライアント側は `[ctrl] + [C]` キーで終了してほしい  

サーバー側で `[ctrl] + [C]` キーを打鍵するとサーバーが落ちるので注意してほしい  

# 次の記事

📖 [Djangoを介してWebブラウザ越しに２人対戦できる〇×ゲームを作ろう！](https://qiita.com/muzudho1/items/3bd5e55fbea2c0598e8b)  

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
📖 [GitHub andrewgodwin/channels-examples/multichat/chat/consumers.py](https://github.com/andrewgodwin/channels-examples/blob/master/multichat/chat/consumers.py)  
