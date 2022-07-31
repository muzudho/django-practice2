# サンプルを見る

📖 [http://tic.warabenture.com:8000/practice/v1/page-the-hello](http://tic.warabenture.com:8000/practice/v1/page-the-hello)  

# 目的

Webサイトのページを追加したい。  
以下のようなURLで表示させる  

```plain
http://example.com/practice/v1/page-the-hello
------]----------]---------------------------
1      2          3

1. スキーム（HTTPプロトコル）
2. ホストの例
3. パス
```

# はじめに

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key       | Value                                     |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1
    │   ├── 📂 data
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets.py
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2
    │   ├── 🐳 docker-compose-project2.yml
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

# Step O3o1o0g1o0 Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step O3o1o0g2o0 フォルダー作成 - apps1/practice_v1 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1                # 複数のアプリケーションを入れるフォルダー
            └── 📂 practice_v1      # アプリケーション フォルダー
```

* `apps1` - 末尾の `1` は文字列検索しやすいように付けているだけで特別な意味はない
* `practice_v1` - 末尾の `_v1` はレッスンの都合で付けているだけで特別な意味はない

## この連載でのバージョン番号の付け方

一般的には プログラムのパッケージには `1.0.0` のような `セマンティック バージョニング` と呼ばれる法則が利用されていることがある  

この連載は、 `Webサイトのユーザーから見たWebアプリケーションのバージョン` と、 `プログラマーの扱うプログラムのパッケージのバージョン` は異なると考え、  
`セマンティック バージョニング` とは異なる法則でバージョン番号を付ける  

👇 URLでは、アプリケーション名とバージョン番号は分ける  

Example: `http://example.com/practice/v1/`  
Example: `http://example.com/practice/v1.2/`  

SEO対策などで「バージョン番号が異なってもアプリケーションとしては同じとカウントしてほしい」ケースがあるだろう。  
この連載では、 URL については この方法を採用する  

バージョン番号は メジャー番号 だけを使うか、 `v1` と `v1.2` の両方を残したい場合は マイナー番号 まで含める。  
バグ修正のたびに URL が変わるのは ナンセンスなので URL にパッチ番号は含めない  

👇 ローカルPC内では アプリケーションのバージョン番号のメジャー番号は、アプリケーション名の方に含める  

Example: `practice_v1`  

「バージョン番号はアプリケーション名では無いのだから、アプリケーション名に付けるのはおかしい」という考え方はあるが、  
「バージョンのメジャー番号が替われば別アプリケーションだ」と考えれば アプリケーション名にバージョンのメジャー番号を付けるのが合理的なので、  
この連載の アプリケーション名 ではこちらを採用する  

👇 レッスンの都合で プログラム名に付ける振り番には、以下のように表記したり、しなかったりすることがある  

Example: `O1o0`  
Example: `o1o0`  

この表記の名前は **電脳向量表記** と呼ぶことにする  

📖 [電脳向量表記 (Cyber Vector Notation)](https://crieit.net/posts/Cyber-Number-Notation)  

# Step O3o1o0g3o0 アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp practice_v1 ./apps1/practice_v1 --settings=project1.settings
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
            └── 📂 practice_v1              # アプリケーション名
👉              ├── 📂 migrations
👉              │   └── 📄 __init__.py
👉              ├── 📄 __init__.py
👉              ├── 📄 admin.py
👉              ├── 📄 apps.py
👉              ├── 📄 models.py
👉              ├── 📄 tests.py
👉              └── 📄 views.py
```

# Step O3o1o0g4o0 今回使わないファイルの削除

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

# Step O3o1o0g5o0 アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1              # アプリケーション名
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
👉              ├── 📄 apps.py
                └── 📄 tests.py
```

```py
from django.apps import AppConfig


class PracticeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    #name = 'practice_v1'
    # * 変更後
    name = 'apps1.practice_v1'
    #       -----------------
    #       1
    # 1. `src1/apps1/practice_v1/apps.py`
    #          -----------------
```

# Step O3o1o0g6o0 アプリケーション登録 - settings.py ファイル＜その２＞

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1              # アプリケーション名
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
# * 変更前
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# ]
#
# * 変更後
INSTALLED_APPS = [
    # あなたが追加したアプリケーション
    'apps1.practice_v1',

    # Djangoの標準アプリケーション
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

これで、 `src1/apps1/practice_v1` フォルダーは practice_v1 アプリケーションとして認識される。  
そのメリットは　今後のレッスンで触れる  

# Step O3o1o0g7o0 画面作成 - page1.html ファイル

以下のファイルを作成してほしい。

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1              # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1      # アプリケーションと同名
                        └── 📂 o1o0
👉                          └── 📄 page_the_hello.html
```

* `templateの下のpractice_v1` - あなたの Django の支配下のすべてのアプリケーションのテンプレート素材は、まるで実行時メモリの中で、あなたの Django の支配下のすべてのアプリケーションからアクセスできる１つの静的フォルダーに再配置されているかのように扱えると考えてほしい。あとは自分の頭で考えてほしい

```html
<html>
    <head>
        <title>ページ１</title>
    </head>
    <body>
        おはよう、世界！
    </body>
</html>
```

# Step O3o1o0g8o0 設定変更 - settings.py ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       └── 📂 templates
        │           └── 📂 practice_v1
        │               └── 📂 o1o0
        │                   └── 📄 page_the_hello.html
        └── 📂 project1
👉          └── 📄 settings.py
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
            # 練習
            os.path.join(BASE_DIR, 'apps1/practice_v1/templates'),
            #                       ---------------------------
            #                       10
            # Example: /src1/apps1/practice_v1/templates/practice_v1/o1o0/page_the_hello.html
            #                      -----------          ------------
            #                      11                   2
            #                ---------------------------
            #                10
            # 10. テンプレート ディレクトリーへのパス
            # 11. アプリケーション
            # 2. まるで `http://example.com/practice_v1` という素材フォルダーがあるかのように扱われる
            #                             ------------
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

# Step O3o1o0g9o0 ビュー モジュール作成 - page_the_hello フォルダー

👇 以下のファイルを新規作成してほしい

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📄 page_the_hello.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 page_the_hello
👉      │                   └── 📄 __init__.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
from django.http import HttpResponse
from django.template import loader


class PageTheHello():
    """おはようページ"""

    @staticmethod
    def render(request):
        """描画"""

        template = loader.get_template('practice_v1/o1o0/page_the_hello.html')
        #                               ------------------------------------
        #                               1
        # 1. src1/apps1/practice_v1/templates/practice_v1/o1o0/page_the_hello.html を取得
        #                                     ------------------------------------

        context = {}
        return HttpResponse(template.render(context, request))

        # テンプレートを使わず、HTMLをハードコーディングすることもできる
        # return HttpResponse("""Hello, world.<br/>
        #                    <a href="http://example.com/">ホーム</a>""")
```

# Step O3o1o0gA10o0 サブ ルート作成 - urls_practice.py

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📄 page_the_hello.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 page_the_hello
        │                   └── 📄 __init__.py
        └── 📂 project1
👉          ├── 📄 urls_practice.py          # 新規作成
❌          └── 📄 urls.py                   # これではない
```

```py
from django.urls import path

# おはようページ
from apps1.practice_v1.views.o1o0.page_the_hello import PageTheHello
#          -----------            --------------        ------------
#          11                     12                    2
#    -------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [

    # おはようページ
    path('practice/v1/page-the-hello',
         # -------------------------
         # 1
         PageTheHello.render, name='page_the_hello'),
    #    -------------------        --------------
    #    2                          3
    # 1. 例えば `http://example.com/practice/v1/page-the-hello` のようなURLのパスの部分
    #                              --------------------------
    # 2. PageTheHello クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page_the_hello' %} のような形でURLを取得するのに使える
]
```

# Step O3o1o0gA11o0 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📄 page_the_hello.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 page_the_hello
        │                   └── 📄 __init__.py
        └── 📂 project1
❌          ├── 📄 urls_practice.py          # これではない
👉          └── 📄 urls.py                   # こっち
```

```py
# ...略...


from django.urls import include, path # include を追加

# O3o1o0gA11o0 総合ルート編集
from .settings import PROJECT_NAME
#    ]--------        ------------
#    12               3
# 1. 同じディレクトリー
# 2. `src1/projectN/settings.py`
#                   --------
# 3. 変数


# ...略...


urlpatterns = [


    # ...中略...


    # O3o1o0gA11o0 練習
    path('', include(f'{PROJECT_NAME}.urls_practice')),
    #    --            ----------------------------
    #    1             2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `src1/projectN/urls_practice.py` の urlpatterns を `1.` にぶら下げる
    #          ----------------------
]
```

# Step O3o1o0gA12o0 Webページにアクセスする

📖 [http://localhost:8000/practice/v1/page-the-hello](http://localhost:8000/practice/v1/page-the-hello)  

# 次の記事

📖 [DjangoのHTMLのボイラープレートを減らすテンプレートを使おう！](https://qiita.com/muzudho1/items/7dcfc068e0bec009d371)  

# 参考にした記事

👇 より一般的なバージョン番号の付け方は、 **セマンティック バージョニング** が参考になる  

📖 [Semantic Versioning](https://qiita.com/usamik26/items/c8911219b610101e69a9)  
