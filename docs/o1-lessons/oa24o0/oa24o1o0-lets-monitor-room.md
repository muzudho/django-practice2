# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/tic-tac-toe/vol3.0/match-application/ver3.0/)  

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
    │   │   ├── 📂 accounts_vol1o0    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_vol1o0              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 room
    │   │   │           └── 📄 ver1o0.py
    │   │   ├── 📂 tic_tac_toe_vol1o0           # アプリケーション
    │   │   └── 📂 tic_tac_toe_vol2o0           # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_vol2o0
    │   │       │       ├── 📂 gui
    │   │       │       └── 📂 think
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_vol2o0
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
    │   │   ├── 📄 urls_accounts_vol1o0.py
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
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📄 urls.py
    ├── 📂 src2_local                      # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# 実装手順

## Step [OA24o1o0g1o0] Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## ~~Step [OA24o1o0g2o0]~~

Merged to OA24o1o0g3o0  

## Step [OA24o1o0g3o_1o0] Moveメッセージ・ハンドラー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol3o0                 # アプリケーション
                └── 📂 websocks
                    └── 📂 gui
                        └── 📂 c2s_handlers
                            └── 📂 move
👉                              └── 📄 ver1o0.py
```

```py
# BOF [OA24o1o0g3o_1o0]

from asgiref.sync import sync_to_async

# 部屋モデル
from apps1.practice_vol1o0.models.room.ver1o0 import Room
#          ---------------             ------        ----
#          11                          12            2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# [OA16o3o_2o0g1o_2o0] Movedメッセージ
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.moved.ver1o0 import MovedS2cMessage


class MoveC2sHandler:
    """駒を置いたとき"""

    async def on_message_received(self, scope, doc_received):
        """メッセージ受信"""

        # ログインしていなければ AnonymousUser
        user = scope["user"]
        # print(
        #     f"[TicTacToeV3o1o0ConsumerCustom on_move 1] user=[{user}] doc_received={doc_received}")
        if user.is_anonymous:
            # ログインしていないユーザーの操作は記録しません
            # print(
            #    f"[TicTacToeV3o1o0ConsumerCustom on_move 1.5] ログインしていないので操作の記録を省きます")
            pass

        else:

            # print(f"[TicTacToeV3o1o0ConsumerCustom on_move 1.75] ログインしています")

            # 部屋名
            #
            # * URLのパスに含まれている
            room_name = scope["url_route"]["kwargs"]["kw_room_name"]
            # print(f"[TicTacToeV3o1o0ConsumerCustom on_move 2] scope={scope}")

            # イベント名 (Client to server)
            event = doc_received.get("event", None)
            # 駒を置いたマス番号
            sq = doc_received.get("sq", None)
            # 駒を置いた方の X か O
            piece_moved = doc_received.get("piece", None)
            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 3] クライアントからのメッセージを受信しました room_name=[{room_name}] event=[{event}] piece_moved=[{piece_moved}] sq=[{sq}]")
            # クライアントからのメッセージを受信しました room_name=[Elephant] event=[C2S_Moved] piece_moved=[X] sq=[2]

            # 部屋取得
            room = await get_room_by_name(room_name)

            # （デバッグ）現状を出力
            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 4] room=[{room}]")
            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 5] now room.name=[{room.name}] room.board=[{room.board}] room.record=[{room.record}]")

            # 駒を置きます
            #
            # * 盤が9マスになるように右を '.' で埋めます
            room.board = room.board.ljust(9, '.')
            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 6] now2 room.board=[{room.board}]")

            room.board = f"{room.board[:sq]}{piece_moved}{room.board[sq+1:]}"
            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 7] now3 room.board=[{room.board}]")

            # 棋譜を書きます
            #
            # * 相手が AnonymousUser なら、相手の指し手が記録されていないものになります
            # * 9文字を超えるようなら、切り捨てます

            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 8] now4 room.record=[{room.record}]")
            room.record = f"{room.record}{sq}"[:9]
            print(
                f"[TicTacToeV3o1o0ConsumerCustom on_move 9] now5 room.record=[{room.record}]")

            # 部屋を上書きします
            await save_room(room)

            print(f"[TicTacToeV3o1o0ConsumerCustom on_move 10] saved")

        # Client to server
        sq = doc_received.get("sq", None)
        piece_moved = doc_received.get("piece", None)
        # print(
        #     f"[TicTacToeV3o1o0ConsumerCustom on_move 11] C2S_Moved sq=[{sq}] piece_moved=[{piece_moved}]")

        args = {
            "sq1": sq,
            "piece1": piece_moved,
        }

        return MovedS2cMessage(args).asDict()


@sync_to_async
def get_room_by_name(name):
    # FIXME 部屋名はIDではないので、先頭の要素を取得
    return Room.objects.filter(name=name)[0]


@sync_to_async
def save_room(room):
    room.save()

# EOF [OA24o1o0g3o_1o0]
```

## Step [OA24o1o0g3o0] Webソケットの通信プロトコル作成 - consumer_custom/v1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol3o0                 # アプリケーション
                └── 📂 websocks
                    └── 📂 consumer_custom
👉                      └── 📄 ver1o0.py
```

```py
# BOF [OA24o1o0g3o0]

# 〇×ゲーム2.0巻 ウェブソケットGUIコンシューマー1.0版
from apps1.tic_tac_toe_vol2o0.websocks.gui.consumer.ver1o0 import ConsumerBase
#                         ^two
#          ------------------                       ------        ------------
#          11                                       12            2
#    -----------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれている __init__.py ファイルにさらに含まれるクラス

# 〇×ゲーム2.0巻 ウェブソケットGUIメッセージ駆動1.0版
from apps1.tic_tac_toe_vol2o0.websocks.gui.message_manager.ver1o0 import MessageManager
#          ------------------                              ------        --------------
#          11                                              12            2
#    ------------------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス

# [OA16o3o0gA10o_1o0] 〇×ゲーム2.0巻 - WebソケットGUI Endメッセージハンドラー 1.0版
from apps1.tic_tac_toe_vol2o0.websocks.gui.c2s_handlers.end.ver1o0 import EndC2sHandler

# [OA24o1o0g3o_1o0] 〇×ゲーム3.0巻 - WebソケットGUI Moveメッセージハンドラー 1.0版
from apps1.tic_tac_toe_vol3o0.websocks.gui.c2s_handlers.move.ver1o0 import MoveC2sHandler
#                         ^

# [OA16o3o0gA10o_3o0] 〇×ゲーム2.0巻 - WebソケットGUI Startメッセージハンドラー 1.0版
from apps1.tic_tac_toe_vol2o0.websocks.gui.c2s_handlers.start.ver1o0 import StartC2sHandler


class TicTacToeV3o1o0ConsumerCustom(ConsumerBase):
    """OA24o1o0g3o0 Webソケット用コンシューマー"""

    def __init__(self):
        super().__init__()
        self._messageManager = MessageManager()
        self._messageManager.addMessageHandler('C2S_End', EndC2sHandler())
        self._messageManager.addMessageHandler('C2S_Moved', MoveC2sHandler())
        self._messageManager.addMessageHandler('C2S_Start', StartC2sHandler())

    async def on_receive(self, doc_received):
        """クライアントからメッセージを受信したとき

        Returns
        -------
        response
        """

        return await self._messageManager.execute(self.scope, doc_received)

# EOF [OA24o1o0g3o0]
```

## Step [OA24o1o0g4o0] Webソケット用ルート新規作成 - ws_urls_tic_tac_toe_v3.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol3o0               # アプリケーション
        │       └── 📂 websocks
        │           └── 📂 consumer_custom
        │               └── 📄 ver1o0.py
        └── 📂 project1                         # プロジェクト
👉          └── 📄 ws_urls_tic_tac_toe_v3.py    # Three
```

```py
# BOF OA24o1o0g4o0

# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# 〇×ゲームの練習 v3.1
from apps1.tic_tac_toe_vol3o0.websocks.consumer_custom.ver1o0 import TicTacToeV3o1o0ConsumerCustom
#                         ^three
#          ------------------                          ------        -----------------------------
#          11                                          12            2
#    -------------------------------------------------
#    10
# 10. ディレクトリー
# 11. アプリケーション
# 12. Python ファイル。拡張子抜き
# 2. クラス名


websocket_urlpatterns = [

    # OA24o1o0g4o0 〇×ゲームの練習3.0巻 3.3版
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

# EOF OA24o1o0g4o0
```

## Step [OA24o1o0g5o0] Webソケット用総合ルート編集 - asgi.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol3o0               # アプリケーション
        │       └── 📂 websocks
        │           └── 📂 consumer_custom
        │               └── 📄 ver1o0.py
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

## Step [OA24o1o0g6o0] 対局申込ビュー作成 - match_application/ver3o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol3o0                   # アプリケーション Three
        │       ├── 📂 views
        │       │   └── 📂 match_application
        │       │       └── 📂 ver3o0
👉      │       │           └── 📄 __init__.py
        │       └── 📂 websocks
        │           └── 📂 consumer_custom
        │               └── 📄 ver1o0.py
        └── 📂 project1                             # プロジェクト
            ├── 📄 asgi.py
            └── 📄 ws_urls_tic_tac_toe_v3.py        # Three
```

```py
# BOF [OA24o1o0g6o0]

# 〇×ゲーム2.0巻 対局申込1.0版
from apps1.tic_tac_toe_vol2o0.views.gui.match_application.ver1o0 import MatchApplicationView as ViewOfMatchApplicationV2g1o0
#                         ^two
#          ------------------                             ------        --------------------    ----------------------------
#          11                                             12            2                       3
#    -----------------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_vol2o0/views/gui/match_application/ver1o0/__init__.py`
#           -----------------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名

# 〇×ゲーム3.0巻 対局申込1.0版
from apps1.tic_tac_toe_vol3o0.views.match_application.ver1o0 import MatchApplicationView as ViewOfMatchApplicationV3g1o0
#                         ^three                         ^one
#          ------------------                         ------        --------------------    ----------------------------
#          11                                         12            2                       3
#    -------------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_vol3o0/views/match_application/v1o0/__init__.py`
#           -----------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class MatchApplicationView():
    """[OA24o1o0g6o0] 対局申込ビュー"""

    # 〇×ゲーム3.0巻 対局中3.0版
    playing_web_path = "/tic-tac-toe/vol3.0/playing/ver3.0/{0}/?&myturn={1}"
    #                                   ^three
    #                   ---------------------------------------------------
    #                   1
    # 1. `http://example.com:8000/tic-tac-toe/vol3.0/playing/ver3.0/Elephant/?&myturn=X`
    #                            ------------------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_vol2o0.views.gui.match_application.ver1o0.v_render import render_match_application
        #                         ^two
        #    --------------------------------------------------------------------        ------------------------
        #    1                                                                           2
        # 1. `src1/apps1/tic_tac_toe_vol2o0/views/gui/match_application/ver1o0/v_render.py`
        #          --------------------------------------------------------------------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationView.playing_web_path,
            ViewOfMatchApplicationV2g1o0.template_path,
            ViewOfMatchApplicationV3g1o0.on_sent,
            ViewOfMatchApplicationV2g1o0.open)

# EOF [OA24o1o0g6o0]
```

## Step [OA24o1o0g7o0] 対局申込ビュー作成 - playing/ver3o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol3o0                   # アプリケーション Three
        │       ├── 📂 views
        │       │   ├── 📂 match_application
        │       │   │   └── 📂 ver3o0
        │       │   │       └── 📄 __init__.py
        │       │   └── 📂 playing
        │       │       └── 📂 ver3o0
👉      │       │           └── 📄 __init__.py
        │       └── 📂 websocks
        │           └── 📂 consumer_custom
        │               └── 📄 ver1o0.py
        └── 📂 project1                             # プロジェクト
            ├── 📄 asgi.py
            └── 📄 ws_urls_tic_tac_toe_v3.py        # Three
```

```py
# BOF [OA24o1o0g7o0]

# 〇×ゲーム2.0巻 対局中1.0版
from apps1.tic_tac_toe_vol2o0.views.gui.playing.ver1o0 import PlayingView as ViewOfPlayingV2g1o0
#                         ^two
#          ------------------                   ------        -----------    -------------------
#          11                                   12            2              3
#    -------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_vol2o0/views/gui/playing/ver1o0/__init__.py`
#           -------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム3.0巻 対局中1.0版
from apps1.tic_tac_toe_vol3o0.views.playing.ver1o0 import PlayingView as ViewOfPlayingV3g1o0
#                         ^three
#          ------------------               ------        -----------    -------------------
#          11                               12            2              3
#    ---------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_vol3o0/views/playing/ver1o0/__init__.py`
#           ---------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名


class PlayingView():
    """[OA24o1o0g7o0] 対局中ビュー"""

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
        from apps1.tic_tac_toe_vol2o0.views.gui.playing.ver1o0.v_render import render_playing
        #                         ^two
        #    ----------------------------------------------------------        --------------
        #    1                                                                 2
        # 1. `src1/apps1/tic_tac_toe_vol2o0/views/gui/playing/ver1o0/v_render.py`
        #          ----------------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            PlayingView.web_socket_path,
            ViewOfPlayingV3g1o0.template_path,
            ViewOfPlayingV3g1o0.on_update,
            ViewOfPlayingV2g1o0.expected_pieces)

# EOF [OA24o1o0g7o0]
```

## ~~Step [OA24o1o0g8o0]~~

Marged to OA24o1o0g8o1o0  

## Step [OA24o1o0g8o1o0] ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 tic_tac_toe_vol3o0                   # アプリケーション Three
    │   │       ├── 📂 views
    │   │       │   └── 📂 o3o0                     # Three
    │   │       │       ├── 📂 match_application
    │   │       │       │   └── 📄 __init__.py
    │   │       │       └── 📂 playing
    │   │       │           └── 📄 __init__.py
    │   │       └── 📂 websocks
    │   │           └── 📂 consumer_custom
    │   │               └── 📄 ver1o0.py
    │   └── 📂 project1                             # プロジェクト
    │       ├── 📄 asgi.py
    │       └── 📄 ws_urls_tic_tac_toe_v3.py        # Three
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_tic_tac_toe_vol3o0_autogen.py,tic-tac-toe/vol3.0/match-application/ver3.0/,,"OA24o1o0g8o1o0 〇×ゲーム3.0巻 対局申込中3.0版",apps1.tic_tac_toe_vol3o0.views.match_application.ver3o0,MatchApplicationView,TicTacToe3o0MatchApplicationView3o0,render
../src1/project1/urls_tic_tac_toe_vol3o0_autogen.py,tic-tac-toe/vol3.0/playing/ver3.0/<str:kw_room_name>/,,"OA24o1o0g8o1o0 〇×ゲーム3.0巻 対局中3.0版",apps1.tic_tac_toe_vol3o0.views.playing.ver3o0,PlayingView,TicTacToe3o0PlayingView3o0,render
```

## Step [OA24o1o0g8o2o0] ルート編集 - コマンド打鍵

👇 以下のコマンドを打鍵してほしい  

```shell
cd ../src1_meta
python -m scripts.auto_generators.urls
cd ../src1
docker-compose restart
```

* ディレクトリーは、がんばって移動してほしい
* スクリプトについて See also: O3o2o_1o0g2o0
* 設定ファイルを変更したら、サーバーの再起動が必要

# テスト手順

## Step [OA24o1o0g9o0] Web画面へアクセス

* このゲームは２人用なので、Webページを２窓で開き、片方が X プレイヤー、もう片方が O プレイヤーとして遊んでください
* テスト用のアカウント `test1` は、もう作ってあるものとします
* 最初のテストは　既存でない部屋名で、次のテストは　既存の部屋名　で行うといいかもしれません

👇 （既にログインしているかもしれないので）ログアウトを試す

📖 [http://localhost:8000/accounts/vol1.0/logout/](http://localhost:8000/accounts/vol1.0/logout/)  

👇 以下の URL を開いて、 `test1` ユーザーでアクセスしてほしい  

```plaintext
ユーザー名: test1
E-mail: (あなたに届く、あなたの２個目のEメールアドレス)
パスワード: test1example
パスワード（再入力） test1example
```

📖 [http://localhost:8000/accounts/vol1.0/login/](http://localhost:8000/accounts/vol1.0/login/)  

👇 そして 以下の URL を開いて、 `TestOA24o1o0g9o0` 部屋に `X` 番として入ってほしい  

📖 [http://localhost:8000/tic-tac-toe/vol3.0/match-application/ver3.0/](http://localhost:8000/tic-tac-toe/vol3.0/match-application/ver3.0/)  

ここで、ログアウトしたなら対局部屋を追い出されるべきだが、まだそこまで作っていない。  

👇 それをいいことに、対局部屋のブラウザ画面を残したまま 今のユーザーをログアウトしてほしい  

📖 [http://localhost:8000/accounts/vol1.0/logout/](http://localhost:8000/accounts/vol1.0/logout/)  

👇 以下の URL を開いて、スーパーユーザー でログインしなおしてほしい（既に作っているはずだ）  

📖 [http://localhost:8000/accounts/vol1.0/login/](http://localhost:8000/accounts/vol1.0/login/)  

👇 そして 以下の URL を開いて、 `TestOA24o1o0g9o0` 部屋に `O` 番として入ってほしい  

📖 [http://localhost:8000/tic-tac-toe/vol3.0/match-application/ver3.0/](http://localhost:8000/tic-tac-toe/vol3.0/match-application/ver3.0/)  

👇 部屋、ユーザーを確認するには、管理画面を使うのが確実だ。  
スーパーユーザーのまま、 以下の URL を開いて、管理画面に入っていてほしい  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

サイドメニューから、 `Rooms` モデルを開いてほしい  
`TestOA24o1o0g9o0 room` があるはずなので、開いてほしい  

部屋に入っているユーザーの主キーが記録されていることを確認してほしい  

例：  

```plaintext
部屋名: TestOA24o1o0g9o0
対局者_先手Id: 2
対局者_後手Id: 1
盤面:
棋譜:
```

以下、３手ほど　○×ゲームを進めてほしい。  
そのあと、もう一度　サイドメニューから `Rooms` モデルの中の `TestOA24o1o0g9o0 room` を開いてほしい。  
盤面と、棋譜にテキストが入っていれば OK だ  

例：  

```plaintext
部屋名: TestOA24o1o0g9o0
対局者_先手Id: 2
対局者_後手Id: 1
盤面: .XX.....O
棋譜: 281
```

# 後処理

## Step [OA24o1o0gA10o0] ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 tic_tac_toe_vol3o0                   # アプリケーション Three
        │       ├── 📂 views
        │       │   └── 📂 o3o0                     # Three
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 playing
        │       │           └── 📄 __init__.py
        │       └── 📂 websocks
        │           └── 📂 consumer_custom
        │               └── 📄 ver1o0.py
        └── 📂 project1                             # プロジェクト
            ├── 📄 asgi.py
            ├── 📄 urls_practice.py
            └── 📄 ws_urls_tic_tac_toe_v3.py        # Three
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/tic-tac-toe/vol3.0/match-application/ver3.0/,OA24o1o0gA10o0 〇×ゲーム3.0巻 対局申込中3.0版
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

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
