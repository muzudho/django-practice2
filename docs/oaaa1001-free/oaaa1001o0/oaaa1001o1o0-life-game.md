# サンプルを見る

📚 [この連載のゴール](http://tic.warabenture.com:8000/lifegame/v0.3/board)  
📖 [この記事のゴール](http://tic.warabenture.com:8000/lifegame/v0.1/board)  

# 情報

| What is        | This is                                                                 |
| -------------- | ----------------------------------------------------------------------- |
| この連載の目的 | ライフゲームを作る                                                      |
| この記事の目標 | いきなりライフゲームを作るのは難しいから、まず白紙のWebページを開設する |

# 始める前に

この記事は 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) のレッスン編を読み終えた人を対象とする  

オススメ動画:  👇 以下の６分程度の動画９本を全部見れば１時間でライフゲームの見所の知識が入る  

📺 [THE RECURSIVE COSMOS: Conway's Game of Life ライフゲームの世界](https://www.youtube.com/playlist?list=PLZC7Zqdh0Qb3wOpit5dewit3q2-Mqg9vC)  

# Step OAAA1001o1o0g1o0 Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step OAAA1001o1o0g2o0 フォルダー作成 - apps1/lifegame_v1 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1                # 複数のアプリケーションを入れるフォルダー
            └── 📂 lifegame_v1      # アプリケーション
```

# Step OAAA1001o1o0g3o0 アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp lifegame_v1 ./apps1/lifegame_v1 --settings=project1.settings
#                                                     ----------- -------------------            -----------------
#                                                     1           2                              3
# 1. 任意のDjangoアプリケーション名
# 2. アプリケーション フォルダーへのパス
# 3. `src1/project1/settings.py` 設定ファイルに従う
#          -----------------
```

👇 以下のようなディレクトリー、ファイルが自動生成される  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 lifegame_v1              # アプリケーション
👉              ├── 📂 migrations
👉              │   └── 📄 __init__.py
👉              ├── 📄 __init__.py
👉              ├── 📄 admin.py
👉              ├── 📄 apps.py
👉              ├── 📄 models.py
👉              ├── 📄 tests.py
👉              └── 📄 views.py
```

# Step OAAA1001o1o0g4o0 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1              # アプリケーション名
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
                ├── 📄 apps.py
👉              ├── 📄 models.py
                ├── 📄 tests.py
👉              └── 📄 views.py
```

# Step OAAA1001o1o0g5o0 アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 lifegame_v1              # アプリケーション
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
👉              ├── 📄 apps.py
                └── 📄 tests.py
```

```py
from django.apps import AppConfig


class LifegameV1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    # name = 'lifegame_v1'
    # * OAAA1001o1o0g5o0 変更後
    name = 'apps1.lifegame_v1'
    #       -----------------
    #       1
    # 1. `src1/apps1/lifegame_v1/apps.py`
    #          -----------------
```

# Step OAAA1001o1o0g6o0 アプリケーション登録 - settings.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1              # アプリケーション
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
# ...略...


INSTALLED_APPS = [
    # ...略...
    # あなたが追加したアプリケーション
    # ...略...


    # OAAA1001o1o0g6o0 ライフゲーム v1
    'apps1.lifegame_v1',


    # ...略...
    # Djangoの標準アプリケーション
    # ...略...
]


# ...略...
```

# Step OAAA1001o1o0g7o0 画面作成 - board/v0o1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1              # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1      # アプリケーションと同名
        │       │       └── 📂 board
👉      │       │           └── 📄 v0o1o0.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```html
<!-- OAAA1001o1o0g7o0 -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<html>
    <head>
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui" />
        <title>Life game</title>
        <style>
            /* 等幅 */
            .v-textarea textarea {
                font-family: monospace, monospace;
            }
        </style>
    </head>
    <body>
        {% block body %}
        <!-- -->
        ここに本体を書く
        <!-- -->
        {% endblock body %}
    </body>
</html>
```

# Step OAAA1001o1o0g8o0 設定変更 - settings.py ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1              # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1      # アプリケーションと同名
        │       │       └── 📂 board
        │       │           └── 📄 v0o1o0.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
👉          └── 📄 settings.py
```

👇 変更するのは `TEMPLATES[0]["DIRS"]` 変数  

```py
TEMPLATES = [
    {
        # ...略... 'BACKEND'


        'DIRS': [
            # ...略...


            # OAAA1001o1o0g8o0 ライフゲーム v1
            os.path.join(BASE_DIR, 'apps1/lifegame_v1/templates'),
            #                       ---------------------------
            #                       10
            # Example: /src1/apps1/lifegame_v1/templates/lifegame_v1/board/v0o1o0.html
            #                      -----------          ------------
            #                      11                   2
            #                ---------------------------
            #                10
            # 10. テンプレート ディレクトリーへのパス
            # 11. アプリケーション
            # 2. まるで `http://example.com/lifegame_v1` という素材フォルダーがあるかのように扱われる
            #                             ------------
        ],


        # ...略... 'APP_DIRS' や 'OPTIONS'
    },
]
```

# Step OAAA1001o1o0g9o0 ビュー作成 - board/v0o1 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1              # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1      # アプリケーションと同名
        │       │       └── 📂 board
        │       │           └── 📄 v0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v0o1o0
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
from django.shortcuts import render


class BoardView():
    """OAAA1001o1o0g9o0 盤"""

    @staticmethod
    def render(request):
        """描画"""

        # * `_lp` - Local path
        this_page_lp = 'lifegame_v1/board/v0o1o0.html'
        #               -----------------------------
        #               1
        # 1. `src1/apps1/lifegame_v1/templates/lifegame_v1/board/v0o1o0.html` を取得
        #                                      -----------------------------

        context = {}
        return render(request, this_page_lp, context)
```

# Step OAAA1001o1o0ga10o0 サブ ルート作成 - urls_lifegame.py

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1              # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1      # アプリケーションと同名
        │       │       └── 📂 board
        │       │           └── 📄 v0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v0o1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
👉          ├── 📄 urls_lifegame.py          # 新規作成
❌          └── 📄 urls.py                   # これではない
```

```py
from django.urls import path

# OAAA1001o1o0g9o0 ライフゲーム v0.1 の盤
from apps1.lifegame_v1.views.board.v0o1o0 import BoardView as BoardViewV0o1o0
#          -----------             ------        ---------    ---------------
#          11                      12            2            3
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [

    # OAAA1001o1o0ga10o0 ライフゲーム v0.1 の盤
    path('lifegame/v0.1/board',
         # ------------------
         # 1
         BoardViewV0o1o0.render, name='lifegame_v0o1o0_board'),
    #    ----------------------        ---------------------
    #    2                             3
    # 1. 例えば `http://example.com/lifegame/v0.1/board` のようなURLのパスの部分
    #                              -------------------
    # 2. BoardViewV0o1o0 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'lifegame_v0o1o0_board' %} のような形でURLを取得するのに使える
]
```

# Step OAAA1001o1o0ga11o0 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1
        │       │       └── 📂 board
        │       │           └── 📄 v0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v0o1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
❌          ├── 📄 urls_lifegame.py          # これではない
👉          └── 📄 urls.py                   # こっち
```

```py
# ...略...


urlpatterns = [
    # ...略...


    # OAAA1001o1o0ga11o0 ライフゲーム
    path('', include(f'{PROJECT_NAME}.urls_lifegame')),
    #    --            ----------------------------
    #    1             2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `src1/projectN/urls_lifegame.py` の urlpatterns を `1.` にぶら下げる
    #          ----------------------
]
```

# Step OAAA1001o1o0ga12o_1o__10o0 Webページにアクセスする

👇 接続の確認だけしてほしい  

📖 [http://localhost:8000/lifegame/v0.1/board](http://localhost:8000/lifegame/v0.1/board)  

# 続きの記事

📖 [DjangoとDocker自由課題OAAA1001o1o0ga12o_1o0 ライフゲームの思考エンジンを作ろう！](https://qiita.com/muzudho1/items/4ec5896c7a8fb27161ff)  

# 参考にした記事

## ライフゲーム

📖 [ライフゲーム Akihide Hanaki](http://math.shinshu-u.ac.jp/~hanaki/lifegame/)  
📖 [ライフゲームの数理 里村孔明](http://nalab.mind.meiji.ac.jp/2018/2019-satomura.pdf)  

## Vue.js

📖 [【Vue.js】ページ読み込み完了後・離脱時に処理を実行する](https://into-the-program.com/vue-page-onload-leave/)  
📖 [Vue.js v-show ディレクティブで要素の表示非表示を切り替える](https://anteku.jp/blog/develop/vue-js-v-show-%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E3%81%A7%E8%A6%81%E7%B4%A0%E3%81%AE%E8%A1%A8%E7%A4%BA%E9%9D%9E%E8%A1%A8%E7%A4%BA%E3%82%92%E5%88%87%E3%82%8A%E6%9B%BF/)  

## Vuetify

📖 [Colors](https://vuetifyjs.com/en/styles/colors/#material-colors)  

## Java Script

📖 [How to Stop setInterval() Call in JavaScript](https://www.tutorialrepublic.com/faq/how-to-stop-setinterval-call-in-javascript.php)  
📖 [Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)  

### テキスト

📖 [javascript 改行を全て削除する手順](https://mebee.info/2020/10/24/post-16225/)  

### 正規表現

📖 [正規表現](https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Regular_Expressions)  
