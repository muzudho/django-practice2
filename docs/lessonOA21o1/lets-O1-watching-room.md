# 目的

観戦したい  

# はじめに

この記事は LessonO2o1 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 o1
    │   │   │           └── 📄 m_room.py
    │   │   ├── 📂 tic_tac_toe_v1        # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2        # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o1
    │   │       │           └── 📂 think
    │   │       │               ├── 📄 concepts.js
    │   │       │               ├── 📄 engine.js
    │   │       │               ├── 📄 judge_ctrl.js
    │   │       │               ├── 📄 position.js
    │   │       │               ├── 📄 things.js
    │   │       │               └── 📄 user_ctrl.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o1
    │   │       │           └── 📂 think
    │   │       │               └── 📄 engine_manual.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 o1
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

# Step O1 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step O2o1 対局画面作成 - playing.html.txt ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3                # アプリケーション Three
                └── 📂 templates
                    └── 📂 tic_tac_toe_v3        # アプリケーションと同名
                        └── 📂 o5o1
👉                          └── 📄 playing.html.txt
```

```html
{% extends "tic_tac_toe_v3/o1/playing.html.txt" %}
{#                       ^^^^three.one
            ------------------------------------
            1
1. host1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/o1/playing.html.txt
                                        ----------------------------------

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

# Step O3o1 対局申込ビュー モジュール作成 - o5o1/match_application フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3                # アプリケーション Three
                ├── 📂 views
                │   └── 📂 o5o1                  # .Five.One
                │       └── 📂 match_application
👉              │           └── 📄 __init__.py
                └── 📂 templates
                    └── 📂 tic_tac_toe_v3        # アプリケーションと同名
                        └── 📂 o5o1
                            └── 📄 playing.html.txt
```

```py
import json

# 以前のバージョン
from apps1.tic_tac_toe_v2.views.o1.gui.match_application import MatchApplicationV as MatchApplicationVV2o1
#                       ^two
#          --------------              -----------------        -----------------    ---------------------
#          11                          12                       2                    3
#    ---------------------------------------------------
#    10
# 10. `host1/apps1/tic_tac_toe_v2/views/o1/gui/match_application/__init__.py`
#            ---------------------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o1.match_application import MatchApplicationV as MatchApplicationVV3o1
#                       ^three
#          --------------          -----------------        -----------------    ---------------------
#          11                      12                       2                    3
#    -----------------------------------------------
#    10
# 10. `host1/apps1/tic_tac_toe_v3/views/o1/match_application/__init__.py`
#            -----------------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class MatchApplicationV():
    """対局申込ビュー"""

    # 対局申込 - 訪問後
    open_context = {
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

    path_of_http_playing = "/tic-tac-toe/v3o5o1/playing/{0}/?&myturn={1}"
    #                                       ^five
    #                       --------------------------------------------
    #                       1
    # 1. `http://example.com:8000/tic-tac-toe/v3o5o1/playing/Elephant/?&myturn=X`
    #                            -----------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o1.gui.match_application.v_render import render_match_application
        #                       ^two
        #    ------------------------------------------------------------        ------------------------
        #    1                                                                   2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o1/gui/match_application/v_render.py`
        #                                                               --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV.path_of_http_playing,
            MatchApplicationVV2o1.path_of_html,
            MatchApplicationVV3o1.on_sent,
            MatchApplicationV.open)

    @staticmethod
    def open(request):
        """訪問後"""
        return MatchApplicationV.open_context
```

# Step O4o1 対局申込ビュー モジュール作成 - o5o1/playing フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3                   # アプリケーション Three
                ├── 📂 views
                │   └── 📂 o5o1
                │       ├── 📂 match_application
                │       │   └── 📄 __init__.py
                │       └── 📂 playing
👉              │           └── 📄 __init__.py
                └── 📂 templates
                    └── 📂 tic_tac_toe_v3
                        └── 📂 o5o1
                            └── 📄 playing.html.txt
```

```py
# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o1.playing import PlayingV as PlayingVV3o1
#          --------------          -------        --------    ------------
#          11                      12             2           3
#    -------------------------------------
#    10
# 10. `host1/apps1/tic_tac_toe_v3/views/o1/playing/__init__.py`
#            -------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名

# 以前のバージョン
from apps1.tic_tac_toe_v3.views.o3.playing import PlayingV as PlayingVV3o3
#          --------------          -------        --------    ------------
#          11                      12             2           3
#    -------------------------------------
#    10
# 10. `host1/apps1/tic_tac_toe_v3/views/o3/playing/__init__.py`
#            -------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class PlayingV():
    """対局中ビュー"""

    # 駒
    expected_pieces = ['X', 'O', '_']

    path_of_html = "tic_tac_toe_v3/o5o1/playing.html.txt"
    #                               ^five
    #               ------------------------------------
    #               1
    # 1. `host1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/o5o1/playing.html.txt`
    #                                          ------------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o1.gui.playing.v_render import render_playing
        #                       ^two
        #    --------------------------------------------------        --------------
        #    1                                                         2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o1/gui/playing/v_render.py`
        #           --------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            PlayingVV3o3.path_of_ws_playing,
            PlayingV.path_of_html,
            PlayingVV3o1.on_update,
            PlayingV.expected_pieces)
```

# Step O5o1 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                   # アプリケーション Three
        │       ├── 📂 views
        │       │   └── 📂 o5o1
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 playing
        │       │           └── 📄 __init__.py
        │       └── 📂 templates
        │           └── 📂 tic_tac_toe_v3
        │               └── 📂 o5o1
        │                   └── 📄 playing.html.txt
        └── 📂 project1                             # プロジェクト
👉          └── 📄 urls_practice.py
```

```py
# ...略...


# 〇×ゲーム v3o5o1 対局申込中
from apps1.tic_tac_toe_v3.views.o5o1.match_application import MatchApplicationV as TicTacToeV3o5o1MatchApplicationV
#                                ^.five                                                        ^five
#          --------------            -----------------        -----------------    --------------------------------
#          11                        12                       2                    3
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3o5o1 対局中
from apps1.tic_tac_toe_v3.views.o5o1.playing import PlayingV as TicTacToeV3o5o1PlayingV
#                                ^five                                      ^five
#          --------------            -------        --------    -----------------------
#          11                        12             2           3
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [
    # ...略...


    # 〇×ゲーム v3o5o1 対局申込中
    path('tic-tac-toe/v3o5o1/match-application/', TicTacToeV3o5o1MatchApplicationV.render,
         # ------------------------------------   ---------------------------------------
         # 1                                      2
         name='tic_tac_toe_v3o5o1_match_application'),
    #          ------------------------------------
    #          3
    # 1. 例えば `http://example.com/tic-tac-toe/v3o5o1/match-application/` のような URL のパスの部分
    #                              -------------------------------------
    # 2. TicTacToeV3o5o1MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3o5o1_match_application' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3o5o1 対局中
    path('tic-tac-toe/v3o5o1/playing/<str:kw_room_name>/', TicTacToeV3o5o1PlayingV.render,
         # ---------------------------------------------   ------------------------------
         # 1                                               2
         name='tic_tac_toe_v3o5o1_playing'),
    #          --------------------------
    #          3
    # 1. 例えば `http://example.com/tic-tac-toe/v3o5o1/playing/<部屋名>/` のような URL のパスの部分
    #                              ------------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3o5o1PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3o5o1_playing' %} のような形でURLを取得するのに使える
]
```

# Step O6o1 Web画面へアクセス

* 観戦モードのテストをするので、Webページを３窓で開き、一方が X プレイヤー、もう一方が O プレイヤー、もう一方は WatchingGame を選んでください
* テストするためには `サインアップ` してアカウントを作ってから、 `ログイン` してください
* 最初のテストは　既存でない部屋名で、次のテストは　既存の部屋名　で行うといいかもしれません

📖 [http://localhost:8000/accounts/v1/signup/](http://localhost:8000/accounts/v1/signup/)  
📖 [http://localhost:8000/accounts/v1/login/](http://localhost:8000/accounts/v1/login/)  
📖 [http://localhost:8000/tic-tac-toe/v3o5o1/match-application/](http://localhost:8000/tic-tac-toe/v3o5o1/match-application/)  

部屋、ユーザーを確認するには、管理画面を使うのが確実です:  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

# Step O7o1 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 tic_tac_toe_v3                   # アプリケーション Three
        │       ├── 📂 views
        │       │   └── 📂 o5o1
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 playing
        │       │           └── 📄 __init__.py
        │       └── 📂 templates
        │           └── 📂 tic_tac_toe_v3           # アプリケーションと同名
        │               └── 📂 o5o1
        │                   └── 📄 playing.html.txt
        └── 📂 project1                             # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/tic-tac-toe/v3o5o1/match-application/,〇×ゲーム v3.5 対局申込中
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  
