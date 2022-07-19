# 目的

`Play Again` （再戦）するかどうかは、プレイヤーが選べるのではなく、サーバー側が選ぶようにしたい  
そこで `Play Again` ボタンを外す  

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
    │   │   │       └── 📂 o2o1
    │   │   │           └── 📄 m_room.py
    │   │   ├── 📂 tic_tac_toe_v1        # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2        # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o2o1
    │   │       │           └── 📂 think
    │   │       │               ├── 📄 concepts.js
    │   │       │               ├── 📄 engine.js
    │   │       │               ├── 📄 judge_ctrl.js
    │   │       │               ├── 📄 position.js
    │   │       │               ├── 📄 things.js
    │   │       │               └── 📄 user_ctrl.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o2o1
    │   │       │           └── 📂 think
    │   │       │               └── 📄 engine_manual.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 o2o1
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

# Step 2. フォルダー作成 - apps1/tic_tac_toe_v3 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3                   # アプリケーション .Three
```

# Step 3. アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp tic_tac_toe_v3 ./apps1/tic_tac_toe_v3
#                                                     -------------- ----------------------
#                                                     1              2
# 1. 任意のDjangoアプリケーション名
# 2. 既存のディレクトリーへのパス
```

# Step 4. 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3                   # アプリケーション .Three
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
                ├── 📄 apps.py
👉              ├── 📄 models.py
                ├── 📄 tests.py
👉              └── 📄 views.py
```

# Step 5. アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v3                   # アプリケーション .Three
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
    # name = 'tic_tac_toe_v3'
    # * 変更後
    name = 'apps1.tic_tac_toe_v3'
    #       --------------------
    #       1
    # 1. `host1/apps1/tic_tac_toe_v3/apps.py`
    #           --------------------
```

# Step 6. アプリケーション登録 - settings.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                   # アプリケーション .Three
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


    'apps1.tic_tac_toe_v3',


    # ...中略...


]
```

これで、 `host1/apps1/tic_tac_toe_v3` フォルダーは tic_tac_toe_v3 アプリケーションとして認識される。  
例えば、 tic_tac_toe_v3 フォルダーの直下に置いた static フォルダーが Django の静的リソースの検索対象のパスになるといったメリットがある  

# Step 7. 対局画面作成 - playing.html.txt ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                   # アプリケーション .Three
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v3           # アプリケーションと同名
        │       │       └── 📂 o2o1
👉      │       │           └── 📄 playing.html.txt
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```html
{% extends "tic_tac_toe_v2/o2o1/gui/playing_base.html" %}
{#                       ^ two
            -----------------------------------------
            1
1. `host1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/o2o1/gui/playing_base.html`
                                         -----------------------------------------

    自動フォーマットしないでください
    Do not auto fomatting
#}


{% block footer_section1 %}
    <!-- フッターにボタンを置きません -->
{% endblock footer_section1 %}


{% block methods_footer %}
    // フッターのボタンは除きました
{% endblock methods_footer %}
```

# Step 8. 対局申込ビュー モジュール作成 - match_application フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                   # アプリケーション .Three
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v3           # アプリケーションと同名
        │       │       └── 📂 o2o1
        │       │           └── 📄 playing.html.txt
        │       ├── 📂 views
        │       │   └── 📂 o2o1                       # .one
        │       │       └── 📂 match_application
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
# 以前のバージョン
from apps1.tic_tac_toe_v2.views.o2o1.gui.match_application import MatchApplicationV as MatchApplicationVV2o2o1
#                       ^two
#    -----------------------------------------------------        -----------------    -----------------------
#    1                                                            2                    3
# 1. `host1/apps1/tic_tac_toe_v2/views/o2o1/gui/match_application/__init__.py`
#           -----------------------------------------------------
# 2. `1.` の __init__.py ファイルに含まれるクラス
# 3. '2.' の別名


class MatchApplicationV():
    """対局申込ビュー"""

    # 〇×ゲーム v3o2o1
    path_of_http_playing = "/tic-tac-toe/v3o2o1/playing/{0}/?&myturn={1}"
    #                                     ^
    #                       --------------------------------------------
    #                       1
    # 1. `http://example.com:8000/tic-tac-toe/v3o2o1/playing/Elephant/?&myturn=X`
    #                            -----------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o2o1.gui.match_application.v_render import render_match_application
        #                       ^two
        #    --------------------------------------------------------------        ------------------------
        #    1                                                                     2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o2o1/gui/match_application/v_render.py`
        #                                                                 --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV.path_of_http_playing,
            MatchApplicationVV2o2o1.path_of_html,
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
        return MatchApplicationVV2o2o1.open_context
```

# Step 9. 対局ビュー モジュール作成 - playing フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                   # アプリケーション .Three
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v3           # アプリケーションと同名
        │       │       └── 📂 o2o1
        │       │           └── 📄 playing.html.txt
        │       ├── 📂 views
        │       │   └── 📂 o2o1                       # .one
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 playing
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
# 以前のバージョン
from apps1.tic_tac_toe_v2.views.o2o1.gui.playing import PlayingV as PlayingVV2o2o1
#                       ^two
#          --------------                -------        --------    --------------
#          11                            12             2           3
#    -------------------------------------------
#    10
# 10. `host1/apps1/tic_tac_toe_v2/views/o2o1/gui/playing/__init__.py`
#            -------------------------------------------
# 11. アプリケーション
# 12. ただのディレクトリー
# 2. `12.` に含まれる `__init__.py` ファイルにさらに含まれるクラス
# 3. `2.` の別名


class PlayingV():
    """対局中ビュー"""

    path_of_ws_playing = "/tic-tac-toe/v2o1/playing/"
    #                                   ^ two
    #                     --------------------------
    #                     1
    # 1. `ws://example.com:8000/tic-tac-toe/v2o1/playing/`
    #                          --------------------------

    path_of_html = "tic_tac_toe_v3/o2o1/playing.html.txt"
    #                            ^ three
    #               ------------------------------------
    #               1
    # 1. `host1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/o2o1/playing.html.txt`
    #                                          ------------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.o2o1.gui.playing.v_render import render_playing
        #                       ^two
        #    ----------------------------------------------------        --------------
        #    1                                                           2
        # 1. `host1/apps1/tic_tac_toe_v2/views/o2o1/gui/playing/v_render.py`
        #           ----------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            PlayingV.path_of_ws_playing,
            PlayingV.path_of_html,
            PlayingV.on_update,
            PlayingVV2o2o1.expected_pieces)

    @staticmethod
    def on_update(request):
        """訪問後または送信後"""
        # 何もしません
        pass
```

# Step 10. ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v3                   # アプリケーション .Three
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v3           # アプリケーションと同名
        │       │       └── 📂 o2o1
        │       │           └── 📄 playing.html.txt
        │       ├── 📂 views
        │       │   └── 📂 o2o1                       # .One
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 playing
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1                             # プロジェクト
            ├── 📄 settings.py
👉          └── 📄 urls_practice.py
```

```py
# ...略...


# 〇×ゲーム v3o1 対局申込中
from apps1.tic_tac_toe_v3.views.o2o1.match_application import MatchApplicationV as TicTacToeV3o2o1MatchApplicationV
#                       ^three
#          --------------            -----------------        -----------------    --------------------------------
#          11                        12                       2                    3
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名

# 〇×ゲーム v3o2o1 対局中
from apps1.tic_tac_toe_v3.views.o2o1.playing import PlayingV as TicTacToeV3o2o1PlayingV
#                       ^three
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


    # 〇×ゲーム v3o2o1 対局申込中
    path('tic-tac-toe/v3o2o1/match-application/', TicTacToeV3o2o1MatchApplicationV.render,
         # ------------------------------------   ---------------------------------------
         # 1                                      2
         name='tic_tac_toe_v3o2o1_match_application'),
    #          ------------------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3o1/match-application/` のような URL のパスの部分
    #                              -----------------------------------
    # 2. TicTacToeV3o2o1MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3o1_match_application' %} のような形でURLを取得するのに使える

    # 〇×ゲーム v3o2o1 対局中
    path('tic-tac-toe/v3o2o1/playing/<str:kw_room_name>/', TicTacToeV3o2o1PlayingV.render,
         # ---------------------------------------------   ------------------------------
         # 1                                               2
         name='tic_tac_toe_v3o2o1_playing'),
    #          --------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3o2o1/playing/<部屋名>/` のような URL のパスの部分
    #                              ------------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3o2o1PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3o2o1_playing' %} のような形でURLを取得するのに使える
]
```

# Step 11. Web画面へアクセス

このゲームは２人用なので、Webページを２窓で開き、片方が X プレイヤー、もう片方が O プレイヤーとして遊んでください  

📖 [http://localhost:8000/tic-tac-toe/v3o1/match-application/](http://localhost:8000/tic-tac-toe/v3o1/match-application/)  

# Step 12. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 tic_tac_toe_v3                   # アプリケーション .Three
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v3           # アプリケーションと同名
        │       │       └── 📂 o2o1
        │       │           └── 📄 playing.html.txt
        │       ├── 📂 views
        │       │   └── 📂 o2o1                       # .One
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 playing
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
/tic-tac-toe/v3o1/match-application/,〇×ゲーム v3.1 対局申込中
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでチェックインを作ろう！](https://qiita.com/muzudho1/items/1ce542dd66929d7bce3f)  
