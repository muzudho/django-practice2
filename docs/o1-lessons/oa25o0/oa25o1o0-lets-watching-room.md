# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/tic-tac-toe/v3.4/match-application/)  

# 目標

観戦したい  

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

# 手順

## Step OA25o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA25o1o0g2o0 対局画面作成 - playing/v4o0.html.txt ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3              # アプリケーション Three
                └── 📂 templates
                    └── 📂 tic_tac_toe_v3      # アプリケーションと同名
                        └── 📂 playing
👉                          └── 📄 v4o0.html.txt
```

```html
{# OA25o1o0g2o0 #}
<!-- -->
{% extends "tic_tac_toe_v3/playing/v1o0.html.txt" %}
{#                                  ^one
            ------------------------------------
            1
1. src1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/playing/v1o0.html.txt
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

## Step OA25o1o0g3o0 対局申込ビュー作成 - match_application/v4o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3              # アプリケーション Three
                ├── 📂 views
                │   └── 📂 match_application
                │       └── 📂 v4o0
👉              │           └── 📄 __init__.py
                └── 📂 templates
                    └── 📂 tic_tac_toe_v3      # アプリケーションと同名
                        └── 📂 playing
                            └── 📄 v4o0.html.txt
```

```py
# BOF OA25o1o0g3o0

import json

# 〇×ゲーム v2 対局申込 v.1.0
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
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名

# 〇×ゲーム v3 対局申込 v1.0
from apps1.tic_tac_toe_v3.views.match_application.v1o0 import MatchApplicationV as MatchApplicationVV3g1o0
#                       ^three                     ^one
#          --------------                         ----        -----------------    -----------------------
#          11                                     12          2                    3
#    -------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v3/views/match_application/v1o0/__init__.py`
#           -------------------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class MatchApplicationV():
    """OA25o1o0g3o0 対局申込ビュー"""

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

    playing_web_path = "/tic-tac-toe/v3.4/playing/{0}/?&myturn={1}"
    #                                 ^three
    #                   ------------------------------------------
    #                   1
    # 1. `http://example.com:8000/tic-tac-toe/v3.4/playing/Elephant/?&myturn=X`
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
            MatchApplicationV.open)

    @staticmethod
    def open(request):
        """訪問後"""
        return MatchApplicationV.open_context

# EOF OA25o1o0g3o0
```

## Step OA25o1o0g4o0 対局申込ビュー作成 - playing/v4o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3                 # アプリケーション Three
                ├── 📂 views
                │   ├── 📂 match_application
                │   │   └── 📂 v4o0
                │   │       └── 📄 __init__.py
                │   └── 📂 playing
                │       └── 📂 v4o0
👉              │           └── 📄 __init__.py
                └── 📂 templates
                    └── 📂 tic_tac_toe_v3
                        └── 📂 playing
                            └── 📄 v4o0.html.txt
```

```py
# BOF OA25o1o0g4o0

# 〇×ゲーム v3 対局中 v1.0
from apps1.tic_tac_toe_v3.views.playing.v1o0 import PlayingV as PlayingVV3o1o0
#          --------------               ----        --------    --------------
#          11                           12          2           3
#    ---------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v3/views/playing/v1o0/__init__.py`
#           ---------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名

# 〇×ゲーム v3 対局中 v3.0
from apps1.tic_tac_toe_v3.views.playing.v3o0 import PlayingV as PlayingVV3o3o0
#          --------------               ----        --------    --------------
#          11                           12          2           3
#    ---------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_v3/views/playing/v3o0/__init__.py`
#           ---------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. '2.' の別名


class PlayingV():
    """OA25o1o0g4o0 対局中ビュー"""

    # 駒
    expected_pieces = ['X', 'O', '_']

    template_path = "tic_tac_toe_v3/playing/v4o0.html.txt"
    #                                        ^four
    #                ------------------------------------
    #                1
    # 1. `src1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/playing/v4o0.html.txt`
    #                                         ------------------------------------

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
            PlayingVV3o3o0.web_socket_path,
            PlayingV.template_path,
            PlayingVV3o1o0.on_update,
            PlayingV.expected_pieces)

# EOF OA25o1o0g4o0
```

## Step OA25o1o0g5o0 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                 # アプリケーション Three
        │       ├── 📂 views
        │       │   ├── 📂 match_application
        │       │   │   └── 📂 v4o0
        │       │   │       └── 📄 __init__.py
        │       │   └── 📂 playing
        │       │       └── 📂 v4o0
        │       │           └── 📄 __init__.py
        │       └── 📂 templates
        │           └── 📂 tic_tac_toe_v3
        │               └── 📂 playing
        │                   └── 📄 v4o0.html.txt
        └── 📂 project1                             # プロジェクト
👉          └── 📄 urls_practice.py
```

```py
# ...略...


# OA25o1o0g5o0 〇×ゲーム v3.4 対局申込中
from apps1.tic_tac_toe_v3.views.match_application.v4o0 import MatchApplicationV as TicTacToeV3g4o0MatchApplicationV
#                       ^three                     ^four
#          --------------                         ----        -----------------    --------------------------------
#          11                                     12          2                    3
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# OA25o1o0g5o0 〇×ゲーム v3.4 対局中
from apps1.tic_tac_toe_v3.views.playing.v4o0 import PlayingV as TicTacToeV3g4o0PlayingV
#                       ^three           ^four
#          --------------               ----        --------    -----------------------
#          11                           12          2           3
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [
    # ...略...


    # OA25o1o0g5o0 〇×ゲーム v3.4 対局申込中
    path('tic-tac-toe/v3.4/match-application/', TicTacToeV3g4o0MatchApplicationV.render,
         # ----------------------------------   ---------------------------------------
         # 1                                    2
         name='tic_tac_toe_v3g4o0_match_application'),
    #          --------------------------------------
    #          3
    # 1. 例えば `http://example.com/tic-tac-toe/v3.4/match-application/` のような URL のパスの部分
    #                              -----------------------------------
    # 2. TicTacToeV3g4o0MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g4o0_match_application' %} のような形でURLを取得するのに使える

    # OA25o1o0g5o0 〇×ゲーム v3.4 対局中
    path('tic-tac-toe/v3.4/playing/<str:kw_room_name>/', TicTacToeV3g4o0PlayingV.render,
         # -------------------------------------------   ------------------------------
         # 1                                             2
         name='tic_tac_toe_v3g4o0_playing'),
    #          ----------------------------
    #          3
    # 1. 例えば `http://example.com/tic-tac-toe/v3.4/playing/<部屋名>/` のような URL のパスの部分
    #                              ----------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3g4o0PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3g4o0_playing' %} のような形でURLを取得するのに使える
]
```

## Step OA25o1o0g6o0 Web画面へアクセス

* 観戦モードのテストをするので、Webページを３窓で開き、一方が X プレイヤー、もう一方が O プレイヤー、もう一方は WatchingGame を選んでください
* テストするためには `サインアップ` してアカウントを作ってから、 `ログイン` してください
* 最初のテストは　既存でない部屋名で、次のテストは　既存の部屋名　で行うといいかもしれません

📖 [http://localhost:8000/accounts/v1/signup/](http://localhost:8000/accounts/v1/signup/)  
📖 [http://localhost:8000/accounts/v1/login/](http://localhost:8000/accounts/v1/login/)  
📖 [http://localhost:8000/tic-tac-toe/v3.4/match-application/](http://localhost:8000/tic-tac-toe/v3.4/match-application/)  

部屋、ユーザーを確認するには、管理画面を使うのが確実です:  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

## Step OA25o1o0g7o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 tic_tac_toe_v3                 # アプリケーション Three
        │       ├── 📂 views
        │       │   ├── 📂 match_application
        │       │   │   └── 📂 v4o0
        │       │   │       └── 📄 __init__.py
        │       │   └── 📂 playing
        │       │       └── 📂 v4o0
        │       │           └── 📄 __init__.py
        │       └── 📂 templates
        │           └── 📂 tic_tac_toe_v3
        │               └── 📂 playing
        │                   └── 📄 v4o0.html.txt
        └── 📂 project1                             # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/tic-tac-toe/v3.4/match-application/,〇×ゲーム v3.4 対局申込中
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  
