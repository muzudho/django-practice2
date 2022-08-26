# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/tic-tac-toe/vol3.0/match-application/ver1.0/)  

# 目標

`Play Again` （再戦）するかどうかは、プレイヤーが選べるのではなく、サーバー側が選ぶようにしたい  
そこで `Play Again` ボタンを外す  

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
    ├── 📂 src2_local                       # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# 手順

## Step OA22o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA22o1o0g2o0 フォルダー作成 - apps1/tic_tac_toe_vol3o0 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol3o0                     # アプリケーション Three
```

## Step OA22o1o0g3o0 アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp tic_tac_toe_vol3o0 ./apps1/tic_tac_toe_vol3o0
#                                                     ------------------ --------------------------
#                                                     1                  2
# 1. 任意のDjangoアプリケーション名
# 2. 既存のディレクトリーへのパス
```

## Step OA22o1o0g4o0 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol3o0                     # アプリケーション Three
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
                ├── 📄 apps.py
👉              ├── 📄 models.py
                ├── 📄 tests.py
👉              └── 📄 views.py
```

## Step OA22o1o0g5o0 アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol3o0                 # アプリケーション Three
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
👉              ├── 📄 apps.py
                └── 📄 tests.py
```

```py
from django.apps import AppConfig


class TicTacToeV3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    # name = 'tic_tac_toe_vol3o0'
    # * OA22o1o0g5o0 変更後
    name = 'apps1.tic_tac_toe_vol3o0'
    #       --------------------
    #       1
    # 1. `src1/apps1/tic_tac_toe_vol3o0/apps.py`
    #          --------------------
```

## Step OA22o1o0g6o0 アプリケーション登録 - settings.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol3o0                     # アプリケーション Three
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
👉          └── 📄 settings.py
```

```py
INSTALLED_APPS = [
    # あなたが追加したアプリケーション


    # ...中略...


    # OA22o1o0g6o0 〇×ゲーム3.0巻
    'apps1.tic_tac_toe_vol3o0',


    # ...中略...


]
```

これで、 `src1/apps1/tic_tac_toe_vol3o0` フォルダーは tic_tac_toe_vol3o0 アプリケーションとして認識される。  
例えば、 tic_tac_toe_vol3o0 フォルダーの直下に置いた static フォルダーが Django の静的リソースの検索対象のパスになるといったメリットがある  

## Step OA22o1o0g7o0 対局画面作成 - playing/v1o0.html.txt ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol3o0                 # アプリケーション Three
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol3o0         # アプリケーションと同名
        │       │       └── 📂 playing
👉      │       │           └── 📄 ver1o0.html.txt
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```html
<!-- BOF OA22o1o0g7o0 -->
{% extends "tic_tac_toe_vol2o0/gui/playing/ver1o0.html" %}
{#                         ^two
            ------------------------------------------
            1
1. `src1/apps1/tic_tac_toe_vol2o0/templates/tic_tac_toe_vol2o0/gui/playing/ver1o0.html`
                                            ------------------------------------------

    自動フォーマットしないでください
    Do not auto fomatting
#}


{% block footer_section1 %}
    <!-- フッターにボタンを置きません -->
{% endblock footer_section1 %}


{% block methods_footer %}
    // フッターのボタンは除きました
{% endblock methods_footer %}
<!-- EOF OA22o1o0g7o0 -->
```

## Step OA22o1o0g8o0 対局申込ビュー作成 - match_application/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol3o0                   # アプリケーション Four
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol3o0           # アプリケーションと同名
        │       │       └── 📂 playing
        │       │           └── 📄 ver1o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 match_application
        │       │       └── 📂 ver1o0
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
# BOF OA22o1o0g8o0

# 〇×ゲーム2.0巻 対局申込1.0版
from apps1.tic_tac_toe_vol2o0.views.gui.match_application.ver1o0 import MatchApplicationV as MatchApplicationVV2g1o0
#                       ^two
#    -----------------------------------------------------------        -----------------    -----------------------
#    1                                                                  2                    3
# 1. `src1/apps1/tic_tac_toe_vol2o0/views/gui/match_application/ver1o0/__init__.py`
#          -----------------------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名


class MatchApplicationV():
    """OA22o1o0g8o0 対局申込ビュー"""

    # 〇×ゲーム3.0巻 対局中3.1版
    playing_web_path = "/tic-tac-toe/vol3.0/playing/ver1.0/{0}/?&myturn={1}"
    #                                   ^three
    #                   ---------------------------------------------------
    #                   1
    # 1. `http://example.com:8000/tic-tac-toe/vol3.0/playing/ver1.0/Elephant/?&myturn=X`
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
        #                                                                      --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV.playing_web_path,
            MatchApplicationVV2g1o0.template_path,
            MatchApplicationV.on_sent,
            MatchApplicationV.open)

    @staticmethod
    def on_sent(request):
        """送信後"""

        # 何もしません
        pass

    @staticmethod
    def open(request):
        """訪問後"""
        return MatchApplicationVV2g1o0.open_context

# EOF OA22o1o0g8o0
```

## Step OA22o1o0g9o0 対局ビュー作成 - playing/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol3o0                 # アプリケーション .Three
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol3o0         # アプリケーションと同名
        │       │       └── 📂 playing
        │       │           └── 📄 ver1o0.html.txt
        │       ├── 📂 views
        │       │   ├── 📂 match_application
        │       │   │   └── 📂 ver1o0
        │       │   │       └── 📄 __init__.py
        │       │   └── 📂 playing
        │       │       └── 📂 ver1o0
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
# BOF OA22o1o0g9o0

# 〇×ゲーム2.0巻 1.0版
from apps1.tic_tac_toe_vol2o0.views.gui.playing.ver1o0 import PlayingV as PlayingVV2g1o0
#                         ^two
#          ------------------                   ------        --------    --------------
#          11                                   12            2           3
#    -------------------------------------------------
#    10
# 10. `src1/apps1/tic_tac_toe_vol2o0/views/gui/playing/ver1o0/__init__.py`
#           -------------------------------------------------
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名


class PlayingV():
    """OA22o1o0g9o0 対局中ビュー"""

    web_socket_path = "/tic-tac-toe/v2/playing/"
    #                                ^two
    #                  ------------------------
    #                  1
    # 1. `ws://example.com:8000/tic-tac-toe/v2/playing/`
    #                          ------------------------

    template_path = "tic_tac_toe_vol3o0/playing/ver1o0.html.txt"
    #                               ^three
    #                ------------------------------------------
    #                1
    # 1. `src1/apps1/tic_tac_toe_vol3o0/templates/tic_tac_toe_vol3o0/playing/ver1o0.html.txt`
    #                                             ------------------------------------------

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
            PlayingV.web_socket_path,
            PlayingV.template_path,
            PlayingV.on_update,
            PlayingVV2g1o0.expected_pieces)

    @staticmethod
    def on_update(request):
        """訪問後または送信後"""
        # 何もしません
        pass

# EOF OA22o1o0g9o0
```

## ~~Step OA22o1o0gA10o0~~

Merged to OA22o1o0gA10o1o0  

## Step OA22o1o0gA10o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 tic_tac_toe_vol3o0                   # アプリケーション Four
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_vol3o0           # アプリケーションと同名
    │   │       │       └── 📂 playing
    │   │       │           └── 📄 ver1o0.html.txt
    │   │       ├── 📂 views
    │   │       │   ├── 📂 match_application
    │   │       │   │   └── 📂 ver1o0
    │   │       │   │       └── 📄 __init__.py
    │   │       │   └── 📂 playing
    │   │       │       └── 📂 ver1o0
    │   │       │           └── 📄 __init__.py
    │   │       ├── 📄 __init__.py
    │   │       ├── 📄 admin.py
    │   │       ├── 📄 apps.py
    │   │       └── 📄 tests.py
    │   └── 📂 project1                             # プロジェクト
    │       └── 📄 settings.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_tic_tac_toe_vol3o0_autogen.py,tic-tac-toe/vol3.0/match-application/ver1.0/,,"OA22o1o0gA10o1o0 〇×ゲーム3.0巻 対局申込中1.0版",apps1.tic_tac_toe_vol3o0.views.match_application.ver1o0,MatchApplicationV,TicTacToe3o0MatchApplicationView1o0,render
../src1/project1/urls_tic_tac_toe_vol3o0_autogen.py,tic-tac-toe/vol3.0/playing/ver1.0/<str:kw_room_name>/,,"OA22o1o0gA10o1o0 〇×ゲーム3.0巻 対局中1.0版",apps1.tic_tac_toe_vol3o0.views.playing.ver1o0,PlayingV,TicTacToe3o0PlayingView1o0,render
```

備考:  

```plaintext
path('tic-tac-toe/vol3.0/playing/ver1.0/<str:kw_room_name>/', XxxView.render, name="playing")
      -----------------------------------------------------   --------------        -------
      1                                                       2                     3
1. 例えば `http://example.com/tic-tac-toe/vol3.0/playing/ver1.0/<部屋名>/` のような URL のパスの部分にマッチする
                             -------------------------------------------
   <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡される
2. XxxView クラスの render メソッド
3. HTMLテンプレートの中で {% url 'playing' %} のような形でURLを取得するのに使える
```

## Step OA22o1o0gA10o2o0 ルート編集 - コマンド打鍵

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

## Step OA22o1o0gA11o0 Web画面へアクセス

このゲームは２人用なので、Webページを２窓で開き、片方が X プレイヤー、もう片方が O プレイヤーとして遊んでください  

📖 [http://localhost:8000/tic-tac-toe/vol3.0/match-application/ver1.0/](http://localhost:8000/tic-tac-toe/vol3.0/match-application/ver1.0/)  

## Step OA22o1o0gA12o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 tic_tac_toe_vol3o0                 # アプリケーション Four
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol3o0         # アプリケーションと同名
        │       │       └── 📂 playing
        │       │           └── 📄 ver1o0.html.txt
        │       ├── 📂 views
        │       │   ├── 📂 match_application
        │       │   │   └── 📂 ver1o0
        │       │   │       └── 📄 __init__.py
        │       │   └── 📂 playing
        │       │       └── 📂 ver1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1                             # プロジェクト
            ├── 📄 settings.py
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/tic-tac-toe/vol3.0/match-application/ver1.0/,OA22o1o0gA12o0 〇×ゲーム3.0巻 対局申込中1.0版
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでチェックインを作ろう！](https://qiita.com/muzudho1/items/1ce542dd66929d7bce3f)  
