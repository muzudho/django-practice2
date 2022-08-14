# 目的

ライフゲームを作る

# はじめに

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

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

# Step OAAA1001o1o0g7o0 画面作成 - board/v1o0.html ファイル

👇 以下のファイルを作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1              # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1      # アプリケーションと同名
        │       │       └── 📂 board
👉      │       │           └── 📄 v1o0.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```html
<!-- OAAA1001o1o0g7o0 -->
<html>
    <head>
        <title>ライフゲーム</title>
    </head>
    <body>
        ライフゲームの盤
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
        │       │           └── 📄 v1o0.html
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
            # Example: /src1/apps1/lifegame_v1/templates/lifegame_v1/board/v1o0.html
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

# Step OAAA1001o1o0g9o0 ビュー作成 - board/v1o0 フォルダー

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
        │       │           └── 📄 v1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v1o0
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
        this_page_lp = 'lifegame_v1/board/v1o0.html'
        #               ---------------------------
        #               1
        # 1. src1/apps1/lifegame_v1/templates/lifegame_v1/board/v1o0.html を取得
        #                                     ---------------------------

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
        │       │           └── 📄 v1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v1o0
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

# OAAA1001o1o0g9o0 盤
from apps1.lifegame_v1.views.board.v1o0 import BoardView as BoardViewV1o0
#          -----------             ----        ---------    -------------
#          11                      12          2            3
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [

    # OAAA1001o1o0ga10o0 ライフゲーム v1 の盤
    path('lifegame/v1/board',
         # ----------------
         # 1
         BoardViewV1o0.render, name='lifegame_v1_board'),
    #    --------------------        -----------------
    #    2                           3
    # 1. 例えば `http://example.com/lifegame/v1/board` のようなURLのパスの部分
    #                              -----------------
    # 2. BoardViewV1o0 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'lifegame_v1_board' %} のような形でURLを取得するのに使える
]
```

# Step OAAA1001o1o0ga11o0 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1
        │       │       └── 📂 board
        │       │           └── 📄 v1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v1o0
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

# Step OAAA1001o1o0ga12o0 Webページにアクセスする

📖 [http://localhost:8000/lifegame/v1/board](http://localhost:8000/lifegame/v1/board)  
