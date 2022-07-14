# 目的

ゲーム対局部屋をモニターしたい  

* 一手指す毎に
  * 盤面を、現盤面で上書きする
  * 棋譜に１手分追加する

# はじめに

この記事は Lesson0 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key              | Value                                     |
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
    ├── 📂 host_local1                   # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    ├── 📂 host1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized    # アプリケーション
    │   │   ├── 📂 portal                # アプリケーション
    │   │   ├── 📂 practice              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 v0o0o1
    │   │   │           └── 📄 m_room.py
    │   │   ├── 📂 tic_tac_toe_v1        # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2        # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o0o1
    │   │       │           └── 📂 think
    │   │       │               ├── 📄 concepts.js
    │   │       │               ├── 📄 engine.js
    │   │       │               ├── 📄 judge_ctrl.js
    │   │       │               ├── 📄 position.js
    │   │       │               ├── 📄 things.js
    │   │       │               └── 📄 user_ctrl.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o0o1
    │   │       │           └── 📂 think
    │   │       │               └── 📄 engine_manual.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 v2o0o1
    │   │       │       └── 📂 think
    │   │       │           └── 📂 engine_manual
    │   │       │               ├── 📄 __init__.py
    │   │       │               └── 📄 v_render.py
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
    │   │   ├── 📄 urls_accounts.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls_tic_tac_toe_v1.py
    │   │   ├── 📄 urls_tic_tac_toe_v2.py
    │   │   ├── 📄 urls.py
    │   │   ├── 📄 ws_urls_tic_tac_toe_v1.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2                  # プロジェクト
    │   ├── 🐳 docker-compose-project2.yml
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

# Step 1. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. 通信プロトコル作成 - message_converter.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3                # アプリケーション
                └── 📂 websocks
                    └── 📂 o0o1
👉                      └── 📄 message_converter.py
```

```py
from asgiref.sync import sync_to_async

from apps1.tic_tac_toe_v2.websocks.v2o0o1.gui.message_converter import TicTacToeV2MessageConverter
#    ----- -------------- ------------------- -----------------        ---------------------------
#    1     2              3                   4                        5
# 1,3. ディレクトリー名
# 1. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

from apps1.practice.models.v0o0o1.m_room import Room
#    ----- -------- ------------- ------        ----
#    1     2        3             4             5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


class TicTacToeV3o1MessageConverter(TicTacToeV2MessageConverter):
    """サーバープロトコル"""

    def on_end(self, scope, doc_received):
        """対局終了時"""
        pass

    async def on_move(self, scope, doc_received):
        """駒を置いたとき"""

        # ログインしていなければ AnonymousUser
        user = scope["user"]
        print(
            f"[TicTacToeV3o1MessageConverter on_move] user=[{user}] doc_received={doc_received}")
        if user.is_anonymous:
            # ログインしていないユーザーの操作は記録しません
            return

        # 部屋名
        #
        # * URLのパスに含まれている
        room_name = scope["url_route"]["kwargs"]["kw_room_name"]
        # print(f"[TicTacToeV3o1MessageConverter on_move] scope={scope}")

        # `c2s_` は クライアントからサーバーへ送られてきた変数の目印
        event = doc_received.get("c2s_event", None)
        # 駒を置いたマス番号
        sq = doc_received.get("c2s_sq", None)
        # 駒を置いた方の X か O
        piece_moved = doc_received.get("c2s_pieceMoved", None)
        print(
            f"[TicTacToeV3o1MessageConverter on_move] クライアントからのメッセージを受信しました room_name=[{room_name}] event=[{event}] piece_moved=[{piece_moved}] sq=[{sq}]")
        # クライアントからのメッセージを受信しました room_name=[Elephant] event=[C2S_Moved] piece_moved=[X] sq=[2]

        # 部屋取得
        room = await get_room_by_name(room_name)

        # （デバッグ）現状を出力
        print(
            f"[TicTacToeV3o1MessageConverter on_move] room=[{room}]")
        print(
            f"[TicTacToeV3o1MessageConverter on_move] now room.name=[{room.name}] room.board=[{room.board}] room.record=[{room.record}]")

        # 駒を置きます
        #
        # * 盤が9マスになるように右を '.' で埋めます
        room.board = room.board.ljust(9, '.')
        print(
            f"[TicTacToeV3o1MessageConverter on_move] now2 room.board=[{room.board}]")

        room.board = f"{room.board[:sq]}{piece_moved}{room.board[sq+1:]}"
        print(
            f"[TicTacToeV3o1MessageConverter on_move] now3 room.board=[{room.board}]")

        # 棋譜を書きます
        #
        # * 相手が AnonymousUser なら、相手の指し手が記録されていないものになります
        # * 9文字を超えるようなら、切り捨てます

        print(
            f"[TicTacToeV3o1MessageConverter on_move] now4 room.record=[{room.record}]")
        room.record = f"{room.record}{sq}"[:9]
        print(
            f"[TicTacToeV3o1MessageConverter on_move] now5 room.record=[{room.record}]")

        # 部屋を上書きします
        await save_room(room)

        print(f"[TicTacToeV3o1MessageConverter on_move] saved")

    def on_start(self, scope, doc_received):
        """対局開始時"""

        print(
            f"[TicTacToeV3o1MessageConverter on_start] ignored. doc_received={doc_received}")
        pass


@sync_to_async
def get_room_by_name(name):
    # FIXME 部屋名はIDではないので、先頭の要素を取得
    return Room.objects.filter(name=name)[0]


@sync_to_async
def save_room(room):
    room.save()
```

# Step 3. Webソケットの通信プロトコル作成 - consumer_custom.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3                # アプリケーション
                └── 📂 websocks
                    └── 📂 o0o1
👉                      ├── 📄 consumer_custom.py
                        └── 📄 message_converter.py
```

```py
from apps1.tic_tac_toe_v2.websocks.v2o0o1.gui.consumer_base import TicTacToeV2ConsumerBase
#                       ^ two                                                ^ two
#    ----- -------------- ------------------- -------------        -----------------------
#    1     2              3                   4                    5
# 1,3. ディレクトリー名
# 1. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

from .message_converter import TicTacToeV3o1MessageConverter
#                                        ^^^ three o one
#    ]-----------------        -----------------------------
#    12                        3
# 1. このファイルと同じディレクトリー
# 2. Python ファイル名。拡張子抜き
# 3. クラス名


class TicTacToeV3o0o1ConsumerCustom(TicTacToeV2ConsumerBase):
    """Webソケット用コンシューマー"""

    def __init__(self):
        super().__init__()
        self._messageConverter = TicTacToeV3o1MessageConverter()
        #                                  ^^^ three o one

    async def on_receive(self, doc_received):
        """クライアントからメッセージを受信したとき

        Returns
        -------
        response
        """

        return await self._messageConverter.on_receive(self.scope, doc_received)
```

# Step 4. Webソケット用ルート新規作成 - ws_urls_tic_tac_toe_v3.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                # アプリケーション
        │       └── 📂 websocks
        │           └── 📂 o0o1
        │               ├── 📄 consumer_custom.py
        │               └── 📄 message_converter.py
        └── 📂 project1                          # プロジェクト
👉          └── 📄 ws_urls_tic_tac_toe_v3.py     # Ver. Three
```

```py
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
```

# Step 5. Webソケット用総合ルート設定 - asgi.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                # アプリケーション
        │       └── 📂 websocks
        │           └── 📂 o0o1
        │               ├── 📄 consumer_custom.py
        │               └── 📄 message_converter.py
        └── 📂 project1                          # プロジェクト
👉          ├── 📄 asgi.py
            └── 📄 ws_urls_tic_tac_toe_v3.py     # Ver. Three
```

```py
# ...略...


# * 以下を追加
# 〇×ゲーム v3
import project1.ws_urls_tic_tac_toe_v3
#                                    ^three
#      -------------------------------
#      1
# 1. `host1/project1/ws_urls_tic_tac_toe_v3.py`
#           -------------------------------


# ...略...
# この辺に os.environ.setdefault(...)


# ...略...


# この辺に以下のような文
# > 複数のアプリケーションの websocket_urlpatterns をマージします
# > websocket_urlpatterns_merged = []


# ...略...


# * 以下を追加
# 〇×ゲーム v3
websocket_urlpatterns_merged.extend(
    project1.ws_urls_tic_tac_toe_v3.websocket_urlpatterns)
#                                 ^three
```

# Step 6. 対局申込ビュー モジュール作成 - o0o3/match_application フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                # アプリケーション Ver Three
        │       ├── 📂 views
        │       │   └── 📂 o0o3                  # (Ver Three).Zero.Three
        │       │       └── 📂 match_application
👉      │       │           └── 📄 __init__.py
        │       └── 📂 websocks
        │           └── 📂 o0o1
        │               ├── 📄 consumer_custom.py
        │               └── 📄 message_converter.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 asgi.py
            └── 📄 ws_urls_tic_tac_toe_v3.py     # Ver. Three
```

```py
# 以前のバージョン
from apps1.tic_tac_toe_v2.views.v2o0o1.gui.match_application import MatchApplicationV as V2o0o1MatchApplicationV
#                       ^two
#    -------------------------------------------------------        -----------------    -----------------------
#    1                                                              2                    3
# 1. `host1/apps1/tic_tac_toe_v2/views/v2o0o1/gui/match_application/__init__.py`
#           -------------------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o0o1.match_application import MatchApplicationV as V3o0o1MatchApplicationV
#                       ^three
#    -------------------------------------------------        -----------------    -----------------------
#    1                                                        2                    3
# 1. `host1/apps1/tic_tac_toe_v3/views/o0o1/match_application/__init__.py`
#           -------------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名


class MatchApplicationV():
    """対局申込ビュー"""

    _path_of_http_playing = "/tic-tac-toe/v3o0o3/playing/{0}/?&myturn={1}"
    #                                      ^^^^^ three.zero.three
    #                        ------------------------------------------
    #                        1
    # 1. http://example.com:8000/tic-tac-toe/v3o0o3/playing/Elephant/?&myturn=X
    #                           -----------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.v2o0o1.gui.match_application.v_render import render_match_application
        #                       ^two
        #    ----------------------------------------------------------------        ------------------------
        #    1                                                                       2
        # 1. `host1/apps1/tic_tac_toe_v2/views/v2o0o1/gui/match_application/v_render.py`
        #                                                                   --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV._path_of_http_playing,
            V2o0o1MatchApplicationV.path_of_html,
            V3o0o1MatchApplicationV.on_sent,
            V2o0o1MatchApplicationV.open)
```

# Step 7. 対局申込ビュー モジュール作成 - o0o3/playing フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                # アプリケーション Ver Three
        │       ├── 📂 views
        │       │   └── 📂 o0o3                  # (Ver Three).Zero.Three
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 playing
👉      │       │           └── 📄 __init__.py
        │       └── 📂 websocks
        │           └── 📂 o0o1
        │               ├── 📄 consumer_custom.py
        │               └── 📄 message_converter.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 asgi.py
            └── 📄 ws_urls_tic_tac_toe_v3.py     # Ver. Three
```

```py
# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o0o1.playing import PlayingV as V3o0o1PlayingV
#    ----- -------------- ------------------        --------    --------------
#    1     2              3                         4           5
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. __init__.py ファイルに含まれるクラス名
# 5. '4.' の別名


class PlayingV():
    """対局中ビュー"""

    path_of_ws_playing = "/tic-tac-toe/v3o0o3/playing/"
    #                                   ^^^^^ three.zero.three
    #                     ----------------------------
    #                     1
    # 1. `ws://example.com/tic-tac-toe/v3o0o3/playing/Elephant/`
    #                     ----------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.v2o0o1.gui.playing import playing_expected_pieces
        #                       ^two
        #    ---------------------------------------------        -----------------------
        #    1                                                    2
        # 1. `host1/apps1/tic_tac_toe_v2/views/v2o0o1/gui/playing/__init__.py`
        #           ---------------------------------------------
        # 2. `1.` の `__init__.py` ファイルに含まれる playing_expected_pieces 変数

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.v2o0o1.gui.playing.v_render import render_playing
        #                       ^two
        #    ------------------------------------------------------        --------------
        #    1                                                             2
        # 1. `host1/apps1/tic_tac_toe_v2/views/v2o0o1/gui/playing/v_render.py`
        #           ------------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            PlayingV.path_of_ws_playing,
            V3o0o1PlayingV.path_of_html,
            V3o0o1PlayingV.on_update,
            playing_expected_pieces)
```

# Step 8. ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                # アプリケーション Ver Three
        │       ├── 📂 views
        │       │   └── 📂 o0o3                  # (Ver Three).Zero.Three
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 playing
        │       │           └── 📄 __init__.py
        │       └── 📂 websocks
        │           └── 📂 o0o1
        │               ├── 📄 consumer_custom.py
        │               └── 📄 message_converter.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 asgi.py
👉          ├── 📄 urls_practice.py
            └── 📄 ws_urls_tic_tac_toe_v3.py     # Ver. Three
```

```py
# ...略...


# 〇×ゲーム v3.0.3 対局申込中
from apps1.tic_tac_toe_v3.views.o0o3.match_application import MatchApplicationV as TicTacToeV3o0o3MatchApplicationV
#                       ^three     ^three                                                    ^^^^^ three.zero.three
#    ----- -------------- ----------------------------        -----------------    --------------------------------
#    1     2              3                                   4                    5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. クラス名
# 5. '4.' の別名

# 〇×ゲーム v3.0.3 対局中
from apps1.tic_tac_toe_v3.views.o0o3.playing import PlayingV as TicTacToeV3o0o3PlayingV
#                       ^three     ^three                                 ^^^^^ three.zero.three
#    ----- -------------- ------------------        --------    -----------------------
#    1     2              3                         4           5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. クラス名
# 5. '4.' の別名


urlpatterns = [
    # ...略...


    # 〇×ゲーム v3.0.3 対局申込中
    path('tic-tac-toe/v3o0o3/match-application/', TicTacToeV3o0o3MatchApplicationV.render,
         # ------------------------------------   ---------------------------------------
         # 1                                      2
         name='tic_tac_toe_v3o0o3_match_application'),
    #          ------------------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3o0o3/match-application/` のような URL のパスの部分
    #                              -------------------------------------
    # 2. TicTacToeV3o0o3MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3o0o3_match_application' %} のような形でURLを取得するのに使える


    # 〇×ゲーム v3.0.3 対局中
    path('tic-tac-toe/v3o0o3/playing/<str:kw_room_name>/', TicTacToeV3o0o3PlayingV.render,
         # ---------------------------------------------   ------------------------------
         # 1                                               2
         name='tic_tac_toe_v3o0o3_playing'),
    #          --------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3o0o3/playing/<部屋名>/` のような URL のパスの部分
    #                              ------------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3o0o3PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3o0o3_playing' %} のような形でURLを取得するのに使える
]
```

# Step 9. Web画面へアクセス

* このゲームは２人用なので、Webページを２窓で開き、片方が X プレイヤー、もう片方が O プレイヤーとして遊んでください
* テストするためには `サインアップ` してアカウントを作ってから、 `ログイン` してください
* 最初のテストは　既存でない部屋名で、次のテストは　既存の部屋名　で行うといいかもしれません

📖 [http://localhost:8000/accounts/v1/signup/](http://localhost:8000/accounts/v1/signup/)  
📖 [http://localhost:8000/accounts/v1/login/](http://localhost:8000/accounts/v1/login/)  
📖 [http://localhost:8000/tic-tac-toe/v3o0o3/match-application/](http://localhost:8000/tic-tac-toe/v3o0o3/match-application/)  

部屋、ユーザーを確認するには、管理画面を使うのが確実です:  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

# Step 10. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 tic_tac_toe_v3                # アプリケーション Ver Three
        │       ├── 📂 views
        │       │   └── 📂 o0o3                  # (Ver Three).Zero.Three
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 playing
        │       │           └── 📄 __init__.py
        │       └── 📂 websocks
        │           └── 📂 o0o1
        │               ├── 📄 consumer_custom.py
        │               └── 📄 message_converter.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 asgi.py
            ├── 📄 urls_practice.py
            └── 📄 ws_urls_tic_tac_toe_v3.py     # Ver. Three
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/tic-tac-toe/v3o0o3/match-application/,〇×ゲーム v3.0.3 対局申込中
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
