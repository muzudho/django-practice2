# 目的

Webサイトのページを追加したい。  
以下のようなURLで表示させる。  

```plain
http://example.com/practice/page1
------]----------]---------------
1      2          3

1. スキーム（HTTPプロトコル）
2. ホストの例
3. パス
```

# はじめに

この記事は Lesson01 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key       | Value                                     |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂host1
    │   ├── 📂data
    │   ├── 📂project1
    │   │   ├── 📄__init__.py
    │   │   ├── 📄asgi.py
    │   │   ├── 📄settings.py
    │   │   ├── 📄urls.py
    │   │   └── 📄wsgi.py
    │   ├── 📂project2
    │   ├── 🐳docker-compose-project2.yml
    │   ├── 🐳docker-compose.yml
    │   ├── 🐳Dockerfile
    │   ├── 📄manage.py
    │   └── 📄requirements.txt
    └── 📄.gitignore
```

# Step 1. Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. フォルダー作成 - apps1 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1         # 複数のアプリケーションを入れるフォルダー。末尾の 1 は文字列検索しやすいように付けているだけで特別な意味はない
            └── 📂practice  # アプリケーション名
```

# Step 3. アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp practice ./apps1/practice
#                                                     -------- ----------------
#                                                     1        2
# 1. 任意のDjangoアプリケーション名
# 2. パス
```

👇 以下のようなディレクトリー、ファイルが自動生成される  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice              # アプリケーション名
👉              ├── 📂migrations
👉              │   └── 📄__init__.py
👉              ├── 📄__init__.py
👉              ├── 📄admin.py
👉              ├── 📄apps.py
👉              ├── 📄models.py
👉              ├── 📄tests.py
👉              └── 📄views.py
```

# Step 4. 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice              # アプリケーション名
                ├── 📂migrations
                │   └── 📄__init__.py
                ├── 📄__init__.py
                ├── 📄admin.py
                ├── 📄apps.py
👉              ├── 📄models.py
                ├── 📄tests.py
👉              └── 📄views.py
```


# Step 5. 画面作成 - page1.html ファイル

以下のファイルを作成してほしい。

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice              # アプリケーション名
                └── 📂templates
                    └── 📂practice      # アプリケーション名と同名
                        └── 📂v0o0o1        # Version 0.0.1 の意味で付けた任意の名前
👉                          └── 📄page1.html
```

```html
<html>
    <head>
        <title>ページ１</title>
    </head>
    <body>
        テストだよ
    </body>
</html>
```

# Step 6. 設定変更 - settings.py ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂practice              # アプリケーション名
        │       └── 📂templates
        │           └── 📂practice
        │               └── 📂v0o0o1
        │                   └── 📄page1.html
        └── 📂project1
            └── 📄settings.py
```

👇 変更するのは `TEMPLATES[0]["DIRS"]` 変数  

```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # * 変更前
        # 'DIRS': [],
        # * 変更後
        'DIRS': [
            os.path.join(BASE_DIR, 'apps1/practice/templates'),
            #            --------   ------------------------
            #            1          2
            #
            # Example: /host1/apps1/practice/templates/practice/v0o0o1/page1.html
            #          ------ ------------------------
            #          1      2
            #
            # 1. あなたの開発用ディレクトリー相当
            # 2. テンプレートへのパス
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

# Step 7. ビュー作成 - pages.py ファイル

👇 以下のファイルを作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice              # アプリケーション名
                ├── 📂templates
                │   └── 📂practice
                │       └── 📂v0o0o1
                │           └── 📄page1.html
                └── 📂views
                    └── 📂v0o0o1            # Version 0.0.1 の意味で付けた任意の名前
👉                      └── 📄pages.py
```

```py
from django.http import HttpResponse
from django.template import loader


class Page1():
    """ページ１"""

    @staticmethod
    def render(request):
        """描画"""

        template = loader.get_template('practice/v0o0o1/page1.html')
        #                               --------------------------
        #                               1
        # 1. host1/apps1/practice/templates/practice/v0o0o1/page1.html を取得
        #                                   --------------------------

        context = {}
        return HttpResponse(template.render(context, request))
```

# Step 8. サブ ルート作成 - urls_practice.py

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂practice              # アプリケーション名
        │       ├── 📂templates
        │       │   └── 📂practice
        │       │       └── 📂v0o0o1
        │       │           └── 📄page1.html
        │       └── 📂views
        │           └── 📂v0o0o1
        │               └── 📄pages.py
        └── 📂project1
👉          ├── 📄urls_practice.py          # 新規作成
❌          └── 📄urls.py                   # これではない
```

```py
from django.urls import path

from apps1.practice.views.v0o0o1.pages import Page1
#    --------------------------- -----        -----
#    1                           2            3
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き
# 3. クラス名


urlpatterns = [

    path('practice/page1', Page1.render, name='page1'),
    #     --------------   ------------        -----
    #     1                2                   3
    # 1. 例えば `http://example.com/practice/page1` のようなURLのパスの部分
    #                              --------------
    # 2. Page1 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page1' %} のような形でURLを取得するのに使える
]
```

# Step 9. 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂practice              # アプリケーション名
        │       ├── 📂templates
        │       │   └── 📂practice
        │       │       └── 📂v0o0o1
        │       │           └── 📄page1.html
        │       └── 📂views
        │           └── 📂v0o0o1
        │               └── 📄pages.py
        └── 📂project1
❌          ├── 📄urls_practice.py          # これではない
👉          └── 📄urls.py                   # こっち
```

```py
from django.urls import include, path # include を追加


# ...中略...


urlpatterns = [


    # ...中略...


    # ページ１
    path('', include('project1.urls_practice')),
    #    --           ----------------------
    #      1          2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `host1/project1/urls_practice.py` の urlpatterns を (1.) にぶら下げる
    #           ----------------------
]
```

# Step 10. Webページにアクセスする

📖 [http://localhost:8000/practice/page1](http://localhost:8000/practice/page1)  

# 次の記事

📖 [DjangoのHTMLのボイラープレートを減らすテンプレートを使おう！](https://qiita.com/muzudho1/items/7dcfc068e0bec009d371)  
