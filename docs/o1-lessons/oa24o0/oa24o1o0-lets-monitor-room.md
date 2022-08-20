# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/tic-tac-toe/v3.3/match-application/)  

# 目標

ゲーム対局部屋をモニターしたい  

* 一手指す毎に
  * 盤面を、現盤面で上書きする
  * 棋譜に１手分追加する

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
| Database         | Postgresql, (Redis)                       |
| Program Language | Python 3                                  |
| Web framework    | Django                                    |
| Auth             | allauth                                   |
| Frontend         | Vuetify                                   |
| Data format      | JSON                                      |
| Others           | (Socket), Web socket                      |
| Editor           | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1                            # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 room
    │   │   │           └── 📄 v1o0.py
    │   │   ├── 📂 tic_tac_toe_v1           # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2           # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       ├── 📂 gui
    │   │       │       └── 📂 think
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       ├── 📂 gui
    │   │       │       └── 📂 think
    │   │       ├── 📂 views
    │   │       │   ├── 📂 gui
    │   │       │   └── 📂 think
    │   │       ├── 📄 __init__.py
    │   │       ├── 📄 admin.py
    │   │       ├── 📄 apps.py
    │   │       └── 📄 tests.py
    │   ├── 📂 data
    │   ├── 📂 project1                     # プロジェクト
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_accounts.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls_tic_tac_toe_v1.py
    │   │   ├── 📄 urls_tic_tac_toe_v2.py
    │   │   ├── 📄 urls.py
    │   │   ├── 📄 ws_urls_tic_tac_toe_v1.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2                     # プロジェクト
    │   ├── 🐳 docker-compose-project2.yml
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    ├── 📂 src2_local                      # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# 手順

## Step OA24o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA24o1o0g2o0 通信プロトコル作成 - message_converter/v1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3                 # アプリケーション
                └── 📂 websocks
                    └── 📂 message_converter
👉                      └── 📄 v1o0.py
```

```py
from asgiref.sync import sync_to_async

# 〇×ゲーム v2 メッセージコンバーター v1.0
from apps1.tic_tac_toe_v2.websocks.gui.message_converter.v1o0 import TicTacToeV2MessageConverter
#          --------------                                ----        ---------------------------
#          11                                            12          2
#    --------------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 部屋モデル
from apps1.practice_v1.models.room.v1o0 import Room
#          -----------             ----        ----
#          11                      12          2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


class TicTacToeV3g1o0MessageConverter(TicTacToeV2MessageConverter):
    """OA24o1o0g2o0 サーバープロトコル"""

    def on_end(self, scope, doc_received):
        """対局終了時"""
        pass

    async def on_move(self, scope, doc_received):
        """駒を置いたとき"""

        # ログインしていなければ AnonymousUser
        user = scope["user"]
        print(
            f"[TicTacToeV3g1o0MessageConverter on_move] user=[{user}] doc_received={doc_received}")
        if user.is_anonymous:
            # ログインしていないユーザーの操作は記録しません
            return

        # 部屋名
        #
        # * URLのパスに含まれている
        room_name = scope["url_route"]["kwargs"]["kw_room_name"]
        # print(f"[TicTacToeV3g1o0MessageConverter on_move] scope={scope}")

        # `c2s_` は クライアントからサーバーへ送られてきた変数の目印
        event = doc_received.get("c2s_event", None)
        # 駒を置いたマス番号
        sq = doc_received.get("c2s_sq", None)
        # 駒を置いた方の X か O
        piece_moved = doc_received.get("c2s_pieceMoved", None)
        print(
            f"[TicTacToeV3g1o0MessageConverter on_move] クライアントからのメッセージを受信しました room_name=[{room_name}] event=[{event}] piece_moved=[{piece_moved}] sq=[{sq}]")
        # クライアントからのメッセージを受信しました room_name=[Elephant] event=[C2S_Moved] piece_moved=[X] sq=[2]

        # 部屋取得
        room = await get_room_by_name(room_name)

        # （デバッグ）現状を出力
        print(
            f"[TicTacToeV3g1o0MessageConverter on_move] room=[{room}]")
        print(
            f"[TicTacToeV3g1o0MessageConverter on_move] now room.name=[{room.name}] room.board=[{room.board}] room.record=[{room.record}]")

        # 駒を置きます
        #
        # * 盤が9マスになるように右を '.' で埋めます
        room.board = room.board.ljust(9, '.')
        print(
            f"[TicTacToeV3g1o0MessageConverter on_move] now2 room.board=[{room.board}]")

        room.board = f"{room.board[:sq]}{piece_moved}{room.board[sq+1:]}"
        print(
            f"[TicTacToeV3g1o0MessageConverter on_move] now3 room.board=[{room.board}]")

        # 棋譜を書きます
        #
        # * 相手が AnonymousUser なら、相手の指し手が記録されていないものになります
        # * 9文字を超えるようなら、切り捨てます

        print(
            f"[TicTacToeV3g1o0MessageConverter on_move] now4 room.record=[{room.record}]")
        room.record = f"{room.record}{sq}"[:9]
        print(
            f"[TicTacToeV3g1o0MessageConverter on_move] now5 room.record=[{room.record}]")

        # 部屋を上書きします
        await save_room(room)

        print(f"[TicTacToeV3g1o0MessageConverter on_move] saved")

    def on_start(self, scope, doc_received):
        """対局開始時"""

        print(
            f"[TicTacToeV3g1o0MessageConverter on_start] ignored. doc_received={doc_received}")
        pass


@sync_to_async
def get_room_by_name(name):
    # FIXME 部屋名はIDではないので、先頭の要素を取得
    return Room.objects.filter(name=name)[0]


@sync_to_async
def save_room(room):
    room.save()
```

## Step OA24o1o0g3o0 Webソケットの通信プロトコル作成 - consumer_custom/v1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3                 # アプリケーション
                └── 📂 websocks
                    ├── 📂 consumer_custom
👉                  │   └── 📄 v1o0.py
                    └── 📂 message_converter
                        └── 📄 v1o0.py
```

```py
# 〇×ゲーム v2 コンシューマー v1.0
from apps1.tic_tac_toe_v2.websocks.gui.consumer.v1o0 import TicTacToeV2ConsumerBase
#                       ^two
#          --------------                       ----        -----------------------
#          11                                   12          2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれている __init__.py ファイルにさらに含まれるクラス

# 〇×ゲーム v3 メッセージコンバーター v1.0
from ..message_converter.v1o0 import TicTacToeV3g1o0MessageConverter
#                                             ^three
#    ------------------- ----        -------------------------------
#    1                   2           3
# 1. このファイルの隣のディレクトリー
# 2. Python ファイル。拡張子抜き
# 3. クラス


class TicTacToeV3o1o0ConsumerCustom(TicTacToeV2ConsumerBase):
    """OA24o1o0g3o0 Webソケット用コンシューマー"""

    def __init__(self):
        super().__init__()
        self._messageConverter = TicTacToeV3g1o0MessageConverter()
        #                                  ^three

    async def on_receive(self, doc_received):
        """クライアントからメッセージを受信したとき

        Returns
        -------
        response
        """

        return await self._messageConverter.on_receive(self.scope, doc_received)
```

## Step OA24o1o0g4o0 Webソケット用ルート新規作成 - ws_urls_tic_tac_toe_v3.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3               # アプリケーション
        │       └── 📂 websocks
        │           ├── 📂 consumer_custom
        │           │   └── 📄 v1o0.py
        │           └── 📂 message_converter
        │               └── 📄 v1o0.py
        └── 📂 project1                         # プロジェクト
👉          └── 📄 ws_urls_tic_tac_toe_v3.py    # Three
```

```py
# OA24o1o0g4o0
# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# 〇×ゲームの練習 v3.1
from apps1.tic_tac_toe_v3.websocks.consumer_custom.v1o0 import TicTacToeV3o1o0ConsumerCustom
#                       ^three
#          --------------                          ----        -----------------------------
#          11                                      12          2
#    ----------------------------------------------
#    10
# 10. ディレクトリー
# 11. アプリケーション
# 12. Python ファイル。拡張子抜き
# 2. クラス名


websocket_urlpatterns = [

    # OA24o1o0g4o0 〇×ゲームの練習 v3.3
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
```

## Step OA24o1o0g5o0 Webソケット用総合ルート設定 - asgi.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3               # アプリケーション
        │       └── 📂 websocks
        │           ├── 📂 consumer_custom
        │           │   └── 📄 v1o0.py
        │           └── 📂 message_converter
        │               └── 📄 v1o0.py
        └── 📂 project1                         # プロジェクト
👉          ├── 📄 asgi.py
            └── 📄 ws_urls_tic_tac_toe_v3.py    # Three
```

```py
# ...略...


# * 以下を追加
# OA24o1o0g5o0 〇×ゲーム v3
from . import ws_urls_tic_tac_toe_v3
#                                  ^three
#    -        ----------------------
#    1        2
# 1. 同じディレクトリー
# 2. `src1/projectN/ws_urls_tic_tac_toe_v3.py`
#                   ----------------------


# ...略...
# この辺に os.environ.setdefault(...)


# ...略...


# この辺に以下のような文
# > 複数のアプリケーションの websocket_urlpatterns をマージします
# > websocket_urlpatterns_merged = []


# ...略...


# * 以下を追加
# OA24o1o0g5o0 〇×ゲーム v3
websocket_urlpatterns_merged.extend(
    ws_urls_tic_tac_toe_v3.websocket_urlpatterns)
#                        ^three
```

## Step OA24o1o0g6o0 対局申込ビュー作成 - match_application/v3o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                   # アプリケーション Three
        │       ├── 📂 views
        │       │   └── 📂 match_application
        │       │       └── 📂 v3o0
👉      │       │           └── 📄 __init__.py
        │       └── 📂 websocks
        │           ├── 📂 consumer_custom
        │           │   └── 📄 v1o0.py
        │           └── 📂 message_converter
        │               └── 📄 v1o0.py
        └── 📂 project1                             # プロジェクト
            ├── 📄 asgi.py
            └── 📄 ws_urls_tic_tac_toe_v3.py        # Three
```

```py
# BOF OA24o1o0g6o0

# 〇×ゲーム v2 対局申込 v1.0
from apps1.tic_tac_toe_v2.views.gui.match_application.v1o0 import MatchApplicationV as MatchApplicationVV2g1o0
#                       ^two
#          --------------                -----------------        -----------------    -----------------------
#          11                            12                       2                    3
#    -----------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v2/views/gui/match_application/v1o0/__init__.py`
#           -----------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名

# 〇×ゲーム v3.1 対局申込 v1.0
from apps1.tic_tac_toe_v3.views.match_application.v1o0 import MatchApplicationV as MatchApplicationVV3g1o0
#                       ^three                     ^one
#          --------------                         ----        -----------------    -----------------------
#          11                                     12          2                    3
#    -------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v3/views/match_application/v1o0/__init__.py`
#           -------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class MatchApplicationV():
    """OA24o1o0g6o0 対局申込ビュー"""

    playing_web_path = "/tic-tac-toe/v3.3/playing/{0}/?&myturn={1}"
    #                                 ^three
    #                   ------------------------------------------
    #                   1
    # 1. `http://example.com:8000/tic-tac-toe/v3.3/playing/Elephant/?&myturn=X`
    #                            ---------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.gui.match_application.v1o0.v_render import render_match_application
        #                       ^two
        #    --------------------------------------------------------------        ------------------------
        #    1                                                                     2
        # 1. `src1/apps1/tic_tac_toe_v2/views/gui/match_application/v1o0/v_render.py`
        #                                                                --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV.playing_web_path,
            MatchApplicationVV2g1o0.template_path,
            MatchApplicationVV3g1o0.on_sent,
            MatchApplicationVV2g1o0.open)

# EOF OA24o1o0g6o0
```

## Step OA24o1o0g7o0 対局申込ビュー作成 - playing/v3o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                   # アプリケーション Three
        │       ├── 📂 views
        │       │   ├── 📂 match_application
        │       │   │   └── 📂 v3o0
        │       │   │       └── 📄 __init__.py
        │       │   └── 📂 playing
        │       │       └── 📂 v3o0
👉      │       │           └── 📄 __init__.py
        │       └── 📂 websocks
        │           ├── 📂 consumer_custom
        │           │   └── 📄 v1o0.py
        │           └── 📂 message_converter
        │               └── 📄 v1o0.py
        └── 📂 project1                             # プロジェクト
            ├── 📄 asgi.py
            └── 📄 ws_urls_tic_tac_toe_v3.py        # Three
```

```py
# BOF OA24o1o0g7o0

# 〇×ゲーム v2 対局中 v1.0
from apps1.tic_tac_toe_v2.views.gui.playing.v1o0 import PlayingV as PlayingVV2g1o0
#                       ^two
#          --------------                -------        --------    --------------
#          11                            12             2           3
#    -------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v2/views/gui/playing/v1o0/__init__.py`
#           -------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3 対局中 v1.0
from apps1.tic_tac_toe_v3.views.playing.v1o0 import PlayingV as PlayingVV3g1o0
#                       ^three
#          --------------               ----        --------    --------------
#          11                           12          2           3
#    ---------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v3/views/o1o0/playing/__init__.py`
#           ---------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名


class PlayingV():
    """OA24o1o0g7o0 対局中ビュー"""

    web_socket_path = "/tic-tac-toe/v3.3/playing/"
    #                                ^three
    #                  --------------------------
    #                  1
    # 1. `ws://example.com/tic-tac-toe/v3.3/playing/Elephant/`
    #                     --------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.gui.playing.v1o0.v_render import render_playing
        #                       ^two
        #    ----------------------------------------------------        --------------
        #    1                                                           2
        # 1. `src1/apps1/tic_tac_toe_v2/views/gui/playing/v1o0/v_render.py`
        #          ----------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            PlayingV.web_socket_path,
            PlayingVV3g1o0.template_path,
            PlayingVV3g1o0.on_update,
            PlayingVV2g1o0.expected_pieces)

# EOF OA24o1o0g7o0
```

## Step OA24o1o0g8o0 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                   # アプリケーション Three
        │       ├── 📂 views
        │       │   └── 📂 o3o0                     # Three
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 playing
        │       │           └── 📄 __init__.py
        │       └── 📂 websocks
        │           ├── 📂 consumer_custom
        │           │   └── 📄 v1o0.py
        │           └── 📂 message_converter
        │               └── 📄 v1o0.py
        └── 📂 project1                             # プロジェクト
            ├── 📄 asgi.py
👉          ├── 📄 urls_practice.py
            └── 📄 ws_urls_tic_tac_toe_v3.py        # Three
```

```py
# ...略...


# OA24o1o0g8o0 〇×ゲーム v3.3 対局申込中
from apps1.tic_tac_toe_v3.views.match_application.v3o0 import MatchApplicationV as TicTacToeV3g3o0MatchApplicationV
#                       ^three                     ^three
#          --------------                         ----        -----------------    --------------------------------
#          11                                     12          2                    3
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# OA24o1o0g8o0 〇×ゲーム v3.3 対局中
from apps1.tic_tac_toe_v3.views.playing.v3o0 import PlayingV as TicTacToeV3g3o0PlayingV
#                       ^three           ^three
#          ----------------             ----        --------    -----------------------
#          11                           12          2           3
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [
    # ...略...


    # OA24o1o0g8o0 〇×ゲーム v3.3 対局申込中
    path('tic-tac-toe/v3.3/match-application/', TicTacToeV3g3o0MatchApplicationV.render,
         # ----------------------------------   ---------------------------------------
         # 1                                    2
         name='tic_tac_toe_v3g3o0_match_application'),
    #          ------------------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3.3/match-application/` のような URL のパスの部分
    #                              -----------------------------------
    # 2. TicTacToeV3g3o0MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g3o0_match_application' %} のような形でURLを取得するのに使える

    # OA24o1o0g8o0 〇×ゲーム v3.3 対局中
    path('tic-tac-toe/v3.3/playing/<str:kw_room_name>/', TicTacToeV3g3o0PlayingV.render,
         # -------------------------------------------   ------------------------------
         # 1                                             2
         name='tic_tac_toe_v3g3o0_playing'),
    #          --------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3.3/playing/<部屋名>/` のような URL のパスの部分
    #                              ----------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3g3o0PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g3o0_playing' %} のような形でURLを取得するのに使える
]
```

## Step OA24o1o0g9o0 Web画面へアクセス

* このゲームは２人用なので、Webページを２窓で開き、片方が X プレイヤー、もう片方が O プレイヤーとして遊んでください
* テストするためには `サインアップ` してアカウントを作ってから、 `ログイン` してください
* 最初のテストは　既存でない部屋名で、次のテストは　既存の部屋名　で行うといいかもしれません

📖 [http://localhost:8000/accounts/v1/signup/](http://localhost:8000/accounts/v1/signup/)  
📖 [http://localhost:8000/accounts/v1/login/](http://localhost:8000/accounts/v1/login/)  
📖 [http://localhost:8000/tic-tac-toe/v3.3/match-application/](http://localhost:8000/tic-tac-toe/v3.3/match-application/)  

部屋、ユーザーを確認するには、管理画面を使うのが確実です:  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

## Step OA24o1o0gA10o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 tic_tac_toe_v3                   # アプリケーション Three
        │       ├── 📂 views
        │       │   └── 📂 o3o0                     # Three
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 playing
        │       │           └── 📄 __init__.py
        │       └── 📂 websocks
        │           ├── 📂 consumer_custom
        │           │   └── 📄 v1o0.py
        │           └── 📂 message_converter
        │               └── 📄 v1o0.py
        └── 📂 project1                             # プロジェクト
            ├── 📄 asgi.py
            ├── 📄 urls_practice.py
            └── 📄 ws_urls_tic_tac_toe_v3.py        # Three
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/tic-tac-toe/v3.3/match-application/,〇×ゲーム v3.3 対局申込中
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoで観戦モードを作ろう！](https://qiita.com/muzudho1/items/9e4a7dd1ccfac6ac8d66)  

# 参考にした記事

## 非同期処理，スレッド関連

📖 [Django: SynchronousOnlyOperation: You cannot call this from an async context - use a thread or sync_to_async](https://stackoverflow.com/questions/61926359/django-synchronousonlyoperation-you-cannot-call-this-from-an-async-context-u)  
📖 [Asynchronous support](https://docs.djangoproject.com/en/4.0/topics/async/)  
📖 [How to correct " 'coroutine' object has no attribute 'data'" Error when using Telethon for Telegram?](https://stackoverflow.com/questions/57147419/how-to-correct-coroutine-object-has-no-attribute-data-error-when-using-te)  
📖 [python3 の async/awaitを理解する](https://qiita.com/maueki/items/8f1e190681682ea11c98)  
📖 [Getting values from functions that run as asyncio tasks](https://stackoverflow.com/questions/32456881/getting-values-from-functions-that-run-as-asyncio-tasks)  

## 文字列関連

📖 [Python で文字列の一文字だけを変換](https://iatlex.com/python/string_change_1str)  
