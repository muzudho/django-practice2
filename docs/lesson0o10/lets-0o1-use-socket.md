# 目的

Webサーバーとクライアント間で通知したい。  
その手法の１つに **Webソケット** があるが いきなり取り掛かるのは大変なので **ソケット** の説明をする  

この記事では Django は関係ない  

# はじめに

この記事は Lesson0 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key              | Value                                     |
| ---------------- | ----------------------------------------- |
| OS               | Windows10                                 |
| Container        | Docker                                    |
| Program Language | Python 3                                  |
| Auth             | allauth                                   |
| Frontend         | Vuetify                                   |
| Data format      | JSON                                      |
| Others           | Socket                                    |
| Editor           | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂host1
    │   ├── 📂apps1
    │   │   ├── 📂allauth_customized    # アプリケーション
    │   │   ├── 📂portal                # アプリケーション
    │   │   └── 📂practice              # アプリケーション
    │   │       ├── 📂management
    │   │       ├── 📂migrations
    │   │       ├── 📂models
    │   │       ├── 📂static
    │   │       │   └── 📂practice
    │   │       │       └── 📂v0o0o1
    │   │       │           └── 📂data
    │   │       │               └── 📄desserts1.json
    │   │       ├── 📂templates
    │   │       │   └── 📂practice          # アプリケーションと同名
    │   │       │       └── 📂v0o0o1
    │   │       │           ├── 📂prefecture
    │   │       │           └── 📂vuetify
    │   │       │               ├── 📄textarea1_base.html
    │   │       │               └── 📄desserts1.html
    │   │       ├── 📂views
    │   │       │   └── 📂v0o0o1
    │   │       │       ├── 📂prefecture
    │   │       │       └── 📂vuetify
    │   │       │           ├── 📄__init__.py
    │   │       │           └── 📄v_textarea1.py
    │   │       ├── 📄__init__.py
    │   │       ├── 📄admin.py
    │   │       ├── 📄apps.py
    │   │       └── 📄tests.py
    │   ├── 📂data
    │   ├── 📂project1                  # プロジェクト
    │   │   ├── 📄__init__.py
    │   │   ├── 📄asgi.py
    │   │   ├── 📄settings_secrets_example.txt
    │   │   ├── 📄settings.py
    │   │   ├── 📄urls_accounts.py
    │   │   ├── 📄urls_practice.py
    │   │   ├── 📄urls.py
    │   │   └── 📄wsgi.py
    │   ├── 📂project2                  # プロジェクト
    │   ├── 🐳docker-compose-project2.yml
    │   ├── 🐳docker-compose.yml
    │   ├── 🐳Dockerfile
    │   ├── 📄manage.py
    │   └── 📄requirements.txt
    └── 📄.gitignore
```

# Step 1. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. フォルダー作成

👇 ソケットの練習は Django とは関係ないので、別にフォルダーを作ってほしい  

```plaintext
    ├── 📂host_local1
👉  │    └── 📂sockapp1             # 新規作成
    └── 📂host1                     # 既存
```

# Step 3. 機能増強 - main_finally.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂host_local1
    │    └── 📂sockapp1
👉  │        └── 📄main_finally.py
    └── 📂host1
```

```py
import sys
import signal


class MainFinally:
    """アプリケーション終了時に、必ず終了処理を実行するための仕掛けです。
    See also: 📖 [Python で終了時に必ず何か実行したい](https://qiita.com/qualitia_cdev/items/f536002791671c6238e3)

    Examples
    --------
    import sys
    import traceback
    from .main_finally import MainFinally

    class Main1:
        def on_main(self):
            # ここで通常の処理
            return 0

        def on_except(self, e):
            # ここで例外キャッチ
            traceback.print_exc()

        def on_finally(self):
            # ここで終了処理
            return 1


    # このファイルを直接実行したときは、以下の関数を呼び出します
    if __name__ == "__main__":
        sys.exit(MainFinally.run(Main1()))
    """

    @staticmethod
    def run(target):
        """アプリケーション終了時に必ず on_finally()メソッドを呼び出します。
        通常の処理は on_main()メソッドに書いてください

        Parameters
        ----------
        target : class
            on_main(), on_except(), on_finally()メソッドが定義されたクラスです
        """
        def sigterm_handler(_signum, _frame) -> None:
            sys.exit(1)

        # 強制終了のシグナルを受け取ったら、強制終了するようにします
        signal.signal(signal.SIGTERM, sigterm_handler)

        try:
            # ここで何か処理
            return_code = target.on_main()

        except Exception as e:
            # ここで例外キャッチ
            target.on_except(e)

        finally:
            # 強制終了のシグナルを無視するようにしてから、クリーンアップ処理へ進みます
            signal.signal(signal.SIGTERM, signal.SIG_IGN)
            signal.signal(signal.SIGINT, signal.SIG_IGN)

            # ここで終了処理
            return_code = target.on_finally()

            # 強制終了のシグナルを有効に戻します
            signal.signal(signal.SIGTERM, signal.SIG_DFL)
            signal.signal(signal.SIGINT, signal.SIG_DFL)

        return return_code
```

# Step 4. 練習用通信サーバー作成 - echo_server.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂host_local1
    │    └── 📂sockapp1
👉  │        ├── 📄echo_server.py
    │        └── 📄main_finally.py
    └── 📂host1
```

```py
# See also: 📖 [How to Make a Chat Application in Python](https://www.thepythoncode.com/article/make-a-chat-room-application-in-python)
import sys
import traceback
import socket
from threading import Thread
from main_finally import MainFinally


class EchoServer():
    def __init__(self, host="0.0.0.0", port=5002, message_size=1024):
        """初期化

        Parameters
        ----------
        host : str
            サーバーのIPアドレス。 規定値 "0.0.0.0"

        port : int
            サーバー側のポート番号。 規定値 5002

        message_size : int
            １回の通信で送れるバイト長。 規定値 1024
        """
        self._host = host
        self._port = port
        self._message_size = message_size

        # (Server socket) このサーバーのTCPソケットです
        self._s_sock = None

        # (Client socket set) このサーバーに接続してきたクライアントのソケットの集まりです
        self._c_sock_set = None

    def run(self):
        def client_worker(c_sock):
            """クライアントから送信されてくるバイナリデータに対応します

            Parameters
            ----------
            c_sock : socket
                接続しているクライアントのソケット
            """
            while True:
                try:
                    # クライアントから受信したバイナリデータをテキストに変換します
                    message = c_sock.recv(self._message_size).decode()

                    # とりあえず "Echo: " と頭に付けてバイナリデータに変換して送り返します
                    message = f"Echo: {message}"
                    c_sock.send(message.encode())

                except Exception as e:
                    # client no longer connected
                    # remove it from the set
                    print(f"[!] Error: {e}")

                    print(f"Remove a socket")
                    self._c_sock_set.remove(c_sock)
                    break

        self._c_sock_set = set()  # 初期化

        s_sock = socket.socket()  # このサーバーのTCPソケットの設定を行っていきます

        # make the port as reusable port
        s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # ホストとポート番号を設定します
        s_sock.bind((self._host, self._port))

        # クライアントの同時接続数上限
        s_sock.listen(5)
        self._s_sock = s_sock

        print(f"[*] Listening as {self._host}:{self._port}")

        # クライアントからの接続を待ち続けるループです
        while True:
            print(f"Wait a connection")
            # クライアントからの接続があるまで、ここでブロックします
            # 'c_sock' - Client socket
            # 'c_addr' - Client address
            c_sock, c_addr = self._s_sock.accept()
            print(f"[+] {c_addr} connected.")

            # クライアントの接続を覚えておきます
            self._c_sock_set.add(c_sock)

            # 別スレッドを開始します
            thr = Thread(target=client_worker, args=(c_sock,))

            # make the thread daemon so it ends whenever the main thread ends
            thr.daemon = True

            # start the thread
            thr.start()

    def clean_up(self):
        # クライアントのソケットを閉じます
        print("Clean up")
        if not (self._c_sock_set is None):
            for c_sock in self._c_sock_set:
                c_sock.close()

        # サーバーのソケットも閉じます
        if not (self._s_sock is None):
            self._s_sock.close()

# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":

    class Main1:
        def __init__(self):
            self._echo_server = None

        def on_main(self):
            self._echo_server = EchoServer(host="0.0.0.0", port=5002)
            self._echo_server.run()
            return 0

        def on_except(self, e):
            """ここで例外キャッチ"""
            traceback.print_exc()

        def on_finally(self):
            # [Ctrl] + [C] を受け付けないから、ここにくるのは難しい
            if self._echo_server:
                self._echo_server.clean_up()

            print("★これで終わり")
            return 1

    sys.exit(MainFinally.run(Main1()))

```

# Step 5. 練習用通信クライアント作成 - client.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂host_local1
    │    └── 📂sockapp1
👉  │        ├── 📄client.py
    │        ├── 📄echo_server.py
    │        └── 📄main_finally.py
    └── 📂host1
```

```py
import sys
import traceback
import socket
import argparse
from threading import Thread
from main_finally import MainFinally


class Client:
    def __init__(self, server_host="127.0.0.1", server_port=5002, message_size=1024):
        """クライアントです。

        Parameters
        ----------
        server_host : str
            接続先サーバーのホスト名、またはIPアドレスです。 規定値 "127.0.0.1"

        server_port : int
            接続先サーバーのポート番号です。 規定値 5002

        message_size : int
            １回の通信で送れるバイト長。 規定値 1024
        """
        self._s_host = server_host
        self._s_port = server_port
        self._message_size = message_size

        # (Server socket) 接続先サーバーのソケットです
        self._s_sock = None

        # (Server thread) サーバーからのメッセージを受信するスレッド
        self._s_thr = None

        # サーバースレッドが終了したら、メインスレッドも終了させるのに使います
        self._is_terminate_server_thread = False

    def clean_up(self):
        # サーバーのソケットを閉じます
        self._s_sock.close()

        # 実行中のスレッドがあれば終了するまで待機するのがクリーンです
        if not (self._s_thr is None) and self._s_thr.is_alive():
            print("[CleanUp] Before join")
            self._s_thr.join()
            print("[CleanUp] After join")
            self._s_thr = None

    def run(self):
        def server_worker():
            while True:
                try:
                    message = self._s_sock.recv(self._message_size).decode()
                    print("\n" + message)

                    if message == "quit":
                        # サーバーから quit が送られてきたら終了することにします
                        # サーバーから強制的に切断しても同じですが、エラーメッセージが出ないという違いがあります
                        # TODO ただし、このワーカースレッドが止まっても、標準入力の待機からは自動的には抜けません
                        print(f"""[-] Disconnected by server.""")
                        self._is_terminate_server_thread = True
                        return

                except Exception as e:
                    # client no longer connected
                    # remove it from the set
                    print(f"[!] Error: {e}")

                    print(
                        f"""Finished listening to the server.
Please push q key to quit."""
                    )
                    self._is_terminate_server_thread = True
                    return

        # initialize TCP socket
        self._s_sock = socket.socket()
        # connect to the server
        print(f"[*] Connecting to {self._s_host}:{self._s_port}...")
        self._s_sock.connect((self._s_host, self._s_port))
        print("[+] Connected.")

        # make a thread that listens for messages to this client & print them
        self._s_thr = Thread(target=server_worker)
        # make the thread daemon so it ends whenever the main thread ends
        self._s_thr.daemon = True
        # start the thread
        self._s_thr.start()

        while not self._is_terminate_server_thread:
            # input message we want to send to the server
            to_send = input()  # ここでブロックします。このブロックをプログラムから解除する簡単な方法はありません

            # a way to exit the program
            if to_send.lower() == "q":
                break

            to_send = f"{to_send}"
            # finally, send the message
            self._s_sock.send(to_send.encode())

# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":

    class Main1:
        def __init__(self):
            self._client = None

        def on_main(self):
            parser = argparse.ArgumentParser(
                description='サーバーのアドレスとポートを指定して、テキストを送信します')
            parser.add_argument('--host', default="127.0.0.1", help='サーバーのホスト。規定値:127.0.0.1')
            parser.add_argument('--port', type=int, default=5002, help='サーバーのポート。規定値:5002')
            args = parser.parse_args()

            self._client = Client(server_host=args.host, server_port=args.port)
            self._client.run()
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

# Step 6. エコーサーバー起動 - コマンド実行

```shell
cd host_local1/sockapp1

python.exe -m echo_server
```

# Step 7. クライアント起動～停止 - コマンド実行

エコーサーバーとは別ターミナルで:  

```shell
cd host_local1/sockapp1

python.exe -m client
```

続けて `hello` と打鍵してほしい  

```plaintext
Echo: hello
```

👆 と返ってくれば成功だ  

続けて `q` と打鍵してほしい  

これで クライアントを強制終了する  

# Step 8. エコーサーバー停止

サーバーは良い止め方がないので、ターミナルごと終了させてほしい  

# 次の記事

📖 [DjangoのWebサーバーとクライアント側のアプリで通信しよう！](https://qiita.com/muzudho1/items/9bad88a4092bf83a0f12)  

# 参考にした記事

📖 [Python で終了時に必ず何か実行したい](https://qiita.com/qualitia_cdev/items/f536002791671c6238e3)  
📖 [How to Make a Chat Application in Python](https://www.thepythoncode.com/article/make-a-chat-room-application-in-python)  
