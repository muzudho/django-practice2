# 目的

観戦したい  

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
    ├── 📂host_local1                   # Djangoとは関係ないもの
    │    ├── 📂sockapp1
    │    └── 📂websockapp1
    ├── 📂host1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂apps1
    │   │   ├── 📂allauth_customized    # アプリケーション
    │   │   ├── 📂portal                # アプリケーション
    │   │   ├── 📂practice              # アプリケーション
    │   │   │   ├── 📂migrations
    │   │   │   └── 📂models
    │   │   │       └── 📂v0o0o1
    │   │   │           └── 📄m_room.py
    │   │   ├── 📂tic_tac_toe_v1        # アプリケーション
    │   │   └── 📂tic_tac_toe_v2        # アプリケーション
    │   │       ├── 📂migrations
    │   │       │   └── 📄__init__.py
    │   │       ├── 📂static
    │   │       │   └── 📂tic_tac_toe_v2
    │   │       │       └── 📂o0o1
    │   │       │           └── 📂think
    │   │       │               ├── 📄concepts.js
    │   │       │               ├── 📄engine.js
    │   │       │               ├── 📄judge_ctrl.js
    │   │       │               ├── 📄position.js
    │   │       │               ├── 📄things.js
    │   │       │               └── 📄user_ctrl.js
    │   │       ├── 📂templates
    │   │       │   └── 📂tic_tac_toe_v2
    │   │       │       └── 📂o0o1
    │   │       │           └── 📂think
    │   │       │               └── 📄engine_manual.html
    │   │       ├── 📂views
    │   │       │   └── 📂v2o0o1
    │   │       │       └── 📂think
    │   │       │           └── 📂engine_manual
    │   │       │               ├── 📄__init__.py
    │   │       │               └── 📄v_render.py
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
    │   │   ├── 📄urls_tic_tac_toe_v1.py
    │   │   ├── 📄urls_tic_tac_toe_v2.py
    │   │   ├── 📄urls.py
    │   │   ├── 📄ws_urls_tic_tac_toe_v1.py
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

# Step 2. 対局画面作成 - playing.html.txt ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂tic_tac_toe_v3                # アプリケーション Ver Three
                └── 📂templates
                    └── 📂tic_tac_toe_v3        # アプリケーションと同名
                        └── 📂o0o4
👉                          └── 📄playing.html.txt
```

```html
{% extends "tic_tac_toe_v3/o0o1/playing.html.txt" %}
{#                       ^^^^^^ three.zero.one
            ------------------------------------
            1
1. host1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/o0o1/playing.html.txt
                                        ------------------------------------

    自動フォーマットしないでください
    Do not auto fomatting
#}


{% block isYourTurn_patch1 %}
    // "X" か "O" かのどちらかのプレイヤーか
    isYourTurn = isYourTurn && (this.engine.position.turn.me == 'X' || this.engine.position.turn.me == 'O');
{% endblock isYourTurn_patch1 %}


{% block appendix_message %}
    xWon: "X won!",
    oWon: "O won!",
{% endblock appendix_message %}


{% block create_gameover_message %}
    // 観戦者のケース
    if (this.engine.position.turn.me == '_') {
        switch (this.engine.winner) {
            case PC_X_LABEL:
                return this.messages.xWon;
            case PC_O_LABEL:
                return this.messages.oWon;
            case PC_EMPTY_LABEL:
                return this.messages.draw;
            default:
                throw `unknown this.engine.winner = ${this.engine.winner}`;
        }
    }
{% endblock create_gameover_message %}
```

# Step 3. 対局申込ビュー モジュール作成 - o0o4/match_application フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂tic_tac_toe_v3                # アプリケーション Ver Three
                ├── 📂views
                │   └── 📂o0o4                  # (Ver Three).Zero.Four
                │       └── 📂match_application
👉              │           └── 📄__init__.py
                └── 📂templates
                    └── 📂tic_tac_toe_v3        # アプリケーションと同名
                        └── 📂o0o4
                            └── 📄playing.html.txt
```

```py
import json

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


# 以下、よく使う定型データ


# 対局申込 - 訪問後
match_application_open_context = {
    # `dj_` は Djangoでレンダーするパラメーター名の目印
    # 入場者データ
    "dj_visitor_value": "X",
    # Python と JavaScript 間で配列データを渡すために JSON 文字列形式にします
    "dj_visitor_select": json.dumps([
        {"text": "X", "value": "X"},
        {"text": "O", "value": "O"},
        {"text": "WatchingGame", "value": "_"},  # add
    ]),
}


# 対局中 - 駒
playing_expected_pieces = ['X', 'O', '_']


class MatchApplicationV():
    """対局申込ビュー"""

    _path_of_http_playing = "/tic-tac-toe/v3o0o4/playing/{0}/?&myturn={1}"
    #                                      ^^^^^ three.zero.four
    #                        ------------------------------------------
    #                        1
    # 1. http://example.com:8000/tic-tac-toe/v3o0o4/playing/Elephant/?&myturn=X
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
            MatchApplicationV.open)

    @staticmethod
    def open(request):
        """訪問後"""
        # 拡張したい挙動があれば、ここに書く

        return match_application_open_context
        #      ^ Located in this file
```

# Step 4. 対局申込ビュー モジュール作成 - o0o4/playing フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂tic_tac_toe_v3                # アプリケーション Ver Three
                ├── 📂views
                │   └── 📂o0o4                  # (Ver Three).Zero.Four
                │       ├── 📂match_application
                │       │   └── 📄__init__.py
                │       └── 📂playing
👉              │           └── 📄__init__.py
                └── 📂templates
                    └── 📂tic_tac_toe_v3        # アプリケーションと同名
                        └── 📂o0o4
                            └── 📄playing.html.txt
```

```py
import json

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o0o1.playing import PlayingV as V3o0o1PlayingV
#    ----- -------------- ------------------        --------    --------------
#    1     2              3                         4           5
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. __init__.py ファイルに含まれるクラス名
# 5. '4.' の別名


# 以下、よく使う定型データ


# 対局申込 - 訪問後
match_application_open_context = {
    # `dj_` は Djangoでレンダーするパラメーター名の目印
    # 入場者データ
    "dj_visitor_value": "X",
    # Python と JavaScript 間で配列データを渡すために JSON 文字列形式にします
    "dj_visitor_select": json.dumps([
        {"text": "X", "value": "X"},
        {"text": "O", "value": "O"},
        {"text": "WatchingGame", "value": "_"},  # add
    ]),
}


# 対局中 - 駒
playing_expected_pieces = ['X', 'O', '_']


class PlayingV():

    path_of_ws_playing = "/tic-tac-toe/v3o1/playing/"
    #                                   ^^^ three o one
    #                     --------------------------
    #                     1
    # 1. ws://example.com/tic-tac-toe/v3o1/playing/Elephant/
    #                    --------------------------

    path_of_html = "tic_tac_toe_v3/o0o4/playing.html.txt"
    #                            ^^^^^^ three.zero.four
    #               ------------------------------------
    #               1
    # 1. `host1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/o0o4/playing.html.txt`
    #                                          ------------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

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
            PlayingV.path_of_html,
            V3o0o1PlayingV.on_update,
            playing_expected_pieces)
        #   ^ Located in this file
```

# Step 5. ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂tic_tac_toe_v3                # アプリケーション Ver Three
        │       ├── 📂views
        │       │   └── 📂o0o4                  # (Ver Three).Zero.Four
        │       │       ├── 📂match_application
        │       │       │   └── 📄__init__.py
        │       │       └── 📂playing
        │       │           └── 📄__init__.py
        │       └── 📂templates
        │           └── 📂tic_tac_toe_v3        # アプリケーションと同名
        │               └── 📂o0o4
        │                   └── 📄playing.html.txt
        └── 📂project1                          # プロジェクト
👉          └── 📄urls_practice.py
```

```py
# ...略...


# 〇×ゲーム v3.0.4 対局申込中
from apps1.tic_tac_toe_v3.views.o0o4.match_application import MatchApplicationV as TicTacToeV3o0o4MatchApplicationV
#                       ^three     ^four                                                     ^^^^^ three.zero.four
#    ----- -------------- ----------------------------        -----------------    --------------------------------
#    1     2              3                                   4                    5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. クラス名
# 5. '4.' の別名

# 〇×ゲーム v3.0.4 対局中
from apps1.tic_tac_toe_v3.views.o0o4.playing import PlayingV as TicTacToeV3o0o4PlayingV
#                       ^three     ^four                                  ^^^^^ three.zero.four
#    ----- -------------- ------------------        --------    -----------------------
#    1     2              3                         4           5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. クラス名
# 5. '4.' の別名


urlpatterns = [
    # ...略...


    # 〇×ゲーム v3.0.4 対局申込中
    path('tic-tac-toe/v3o0o4/match-application/', TicTacToeV3o0o4MatchApplicationV.render,
         # ------------------------------------   ---------------------------------------
         # 1                                      2
         name='tic_tac_toe_v3o0o4_match_application'),
    #          ------------------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3o0o4/match-application/` のような URL のパスの部分
    #                              -------------------------------------
    # 2. TicTacToeV3o0o4MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3o0o4_match_application' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3.0.4 対局中
    path('tic-tac-toe/v3o0o4/playing/<str:kw_room_name>/', TicTacToeV3o0o4PlayingV.render,
         # ---------------------------------------------   ------------------------------
         # 1                                               2
         name='tic_tac_toe_v3o0o4_playing'),
    #          --------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3o0o4/playing/<部屋名>/` のような URL のパスの部分
    #                              ------------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3o0o4PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3o0o4_playing' %} のような形でURLを取得するのに使える
]
```

# Step 6. Web画面へアクセス

* 観戦モードのテストをするので、Webページを３窓で開き、一方が X プレイヤー、もう一方が O プレイヤー、もう一方は WatchingGame を選んでください
* テストするためには `サインアップ` してアカウントを作ってから、 `ログイン` してください
* 最初のテストは　既存でない部屋名で、次のテストは　既存の部屋名　で行うといいかもしれません

📖 [http://localhost:8000/accounts/v1/signup/](http://localhost:8000/accounts/v1/signup/)  
📖 [http://localhost:8000/accounts/v1/login/](http://localhost:8000/accounts/v1/login/)  
📖 [http://localhost:8000/tic-tac-toe/v3o0o4/match-application/](http://localhost:8000/tic-tac-toe/v3o0o4/match-application/)  

部屋、ユーザーを確認するには、管理画面を使うのが確実です:  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

# Step 7. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   ├── 📂portal                        # アプリケーション
        │   │   └── 📂data
👉      │   │       └── 📄finished-lessons.csv
        │   └── 📂tic_tac_toe_v3                # アプリケーション Ver Three
        │       ├── 📂views
        │       │   └── 📂o0o4                  # (Ver Three).Zero.Four
        │       │       ├── 📂match_application
        │       │       │   └── 📄__init__.py
        │       │       └── 📂playing
        │       │           └── 📄__init__.py
        │       └── 📂templates
        │           └── 📂tic_tac_toe_v3        # アプリケーションと同名
        │               └── 📂o0o4
        │                   └── 📄playing.html.txt
        └── 📂project1                          # プロジェクト
            └── 📄urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/tic-tac-toe/v3o0o4/match-application/,〇×ゲーム v3.0.4 対局申込中
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  