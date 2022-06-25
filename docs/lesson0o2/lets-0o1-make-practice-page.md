# 目的

Webサイトのページを追加したい。  
以下のようなURLで表示させる。  

```plain
http://example.com/practice/page1
------]----------]---------------
1      2          3

1. プロトコル
2. ホスト
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

# Step 2. アプリケーション作成

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

# Step 3. 今回使わないファイルの削除

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


# Step 4. 画面作成 - page1.html ファイル

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

# Step 5. ビュー作成 - pages.py ファイル

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


def render_page1(request):
    template = loader.get_template('practice/v0o0o1/page1.html')
    #                               --------------------------
    #                               1
    # 1. host1/apps1/practice/templates/practice/v0o0o1/page1.html を取得
    #                                   --------------------------

    context = {}
    return HttpResponse(template.render(context, request))
```
