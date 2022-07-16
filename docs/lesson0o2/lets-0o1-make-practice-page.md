# 目的

Webサイトのページを追加したい。  
以下のようなURLで表示させる  

```plain
http://example.com/practice/v1/page1
------]----------]------------------
1      2          3

1. スキーム（HTTPプロトコル）
2. ホストの例
3. パス
```

# はじめに

この記事は Lesson0 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key       | Value                                     |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 host1
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

# Step 1. Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. フォルダー作成 - apps1/practice_v1 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1                # 複数のアプリケーションを入れるフォルダー
            └── 📂 practice_v1      # アプリケーション フォルダー
```

* `apps1` - 末尾の `1` は文字列検索しやすいように付けているだけで特別な意味はない
* `practice_v1` - 末尾の `_v1` はレッスンの都合で付けているだけで特別な意味はない

## この連載でのバージョン番号の付け方

この連載では `セマンティック バージョニング` とは異なる法則でバージョン番号を付ける  

👇 メジャー番号は アプリケーション名に付ける  

Example: `practice_v1`  

「バージョン番号はアプリケーション名では無いのだから、アプリケーション名に付けるのはおかしい」という考え方はあるが、  
「メジャー番号が替われば別アプリケーションだ」と考えれば アプリケーション名にメジャー番号を付けるのが合理的なので、  
この連載ではこちらを採用する  

👇 URLでは、アプリケーション名とメジャー番号は分ける  

Example: `http://example.com/practice/v1/`  

「メジャー番号は異なってもアプリケーションは同じシリーズだ」と主張するのが合理的なので、  
この連載ではこちらを採用する  

👇 マイナー番号は、この連載では以下のように表記したり、しなかったりすることがある  

Example: `o1o1`  

この表記の名前は仮に **ビーズ記数法** とでも呼ぶことにする  

📖 [数珠玉記数法](https://qiita.com/muzudho1/items/7aafcf17fc4bb8fe551b)  

`o` は単に数を区切っている。基本的に先頭に `o` は置かないが、置くこともできる。特に意図がないなら、末尾を `o0` にすることを避ける。  
`o1o1` の次は `o2o1` でも `o1o2` でも `o1o1o1` でも いずれでも構わない  

メジャー番号とマイナー番号をつなげて使う例は以下の通り  

Example: `ws://example.com/practice/v1o1o1/`  

この連載では パッチ番号 のようなものは使わない  

# Step 3. アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp practice_v1 ./apps1/practice_v1 --settings=project1.settings
#                                                     ----------- -------------------            -----------------
#                                                     1           2
# 1. 任意のDjangoアプリケーション名
# 2. アプリケーション フォルダーへのパス
# 3. `host1/project1/settings.py` 設定ファイルに従う
#           -----------------
```

👇 以下のようなディレクトリー、ファイルが自動生成される  

```plaintext
    └── 📂 host1
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

# Step 4. 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂 host1
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

# Step 5. アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1
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
    # 1. `host1/apps1/practice_v1/apps.py`
    #           -----------------
```

# Step 6. アプリケーション登録 - settings.py ファイル＜その２＞

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 host1
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

これで、 `host1/apps1/practice_v1` フォルダーは practice_v1 アプリケーションとして認識される。  
そのメリットは　今後のレッスンで触れる  

# Step 7. 画面作成 - page1.html ファイル

以下のファイルを作成してほしい。

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1              # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1      # アプリケーションと同名
                        └── 📂 o1
👉                          └── 📄 page1.html
```

* `templateの下のpractice_v1` - あなたの Django の支配下のすべてのアプリケーションのテンプレート素材は、まるで実行時メモリの中で、あなたの Django の支配下のすべてのアプリケーションからアクセスできる１つの静的フォルダーに再配置されているかのように扱えると考えてほしい。あとは自分の頭で考えてほしい
* `o1o0` - Version 1.1.0 の後ろの `.1.0` のつもり。頭の `1` は practice_v1 の後ろに付いている。ただのフォルダー。無くてもいい

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

# Step 8. 設定変更 - settings.py ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       └── 📂 templates
        │           └── 📂 practice_v1
        │               └── 📂 o1
        │                   └── 📄 page1.html
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
            os.path.join(BASE_DIR, 'apps1/practice_v1/templates'),
            #                       ---------------------------
            #                       1
            #
            # Example: /host1/apps1/practice_v1/templates/practice_v1/o1/page1.html
            #                       -----------           -----------
            #                       1.1                   2.1
            #          ---------------------------------]------------
            #          1                                 2
            #
            # 1. テンプレート ディレクトリーへのパス
            # 1.1 アプリケーション
            # 2. まるで `http://example.com/practice_v1` という素材フォルダーがあるかのように扱われる
            #                             ------------
            # 2.1 ただのディレクトリー
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

# Step 9. ビュー モジュール作成 - page1 フォルダー

👇 以下のファイルを新規作成してほしい

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1
        │       │           └── 📄 page1.html
        │       └── 📂 views
        │           └── 📂 o1
        │               └── 📂 page1
👉      │                   └── 📄 __init__.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
from django.http import HttpResponse
from django.template import loader


class Page1():
    """ページ１"""

    @staticmethod
    def render(request):
        """描画"""

        template = loader.get_template('practice_v1/o1/page1.html')
        #                               -------------------------
        #                               1
        # 1. host1/apps1/practice_v1/templates/practice_v1/o1/page1.html を取得
        #                                      -------------------------

        context = {}
        return HttpResponse(template.render(context, request))

        # テンプレートを使わず、HTMLをハードコーディングすることもできる
        # return HttpResponse("""Hello, world.<br/>
        #                    <a href="home/v1/">ホーム</a>""")
```

# Step 10. サブ ルート作成 - urls_practice.py

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1
        │       │           └── 📄 page1.html
        │       └── 📂 views
        │           └── 📂 o1
        │               └── 📂 page1
        │                   └── 📄 __init__.py
        └── 📂 project1
👉          ├── 📄 urls_practice.py          # 新規作成
❌          └── 📄 urls.py                   # これではない
```

```py
from django.urls import path

# 練習ページ１
from apps1.practice_v1.views.o1.page1 import Page1
#          -----------          -----        -----
#          11                   12           2
#    --------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [

    path('practice/v1/page1', Page1.render, name='page1'),
    #     -----------------   ------------        -----
    #     1                   2                   3
    # 1. 例えば `http://example.com/practice/v1/page1` のようなURLのパスの部分
    #                              -----------------
    # 2. Page1 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page1' %} のような形でURLを取得するのに使える
]
```

# Step 11. 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1
        │       │           └── 📄 page1.html
        │       └── 📂 views
        │           └── 📂 o1
        │               └── 📂 page1
        │                   └── 📄 __init__.py
        └── 📂 project1
❌          ├── 📄 urls_practice.py          # これではない
👉          └── 📄 urls.py                   # こっち
```

```py
from django.urls import include, path # include を追加


# ...中略...


urlpatterns = [


    # ...中略...


    # 練習
    path('', include('project1.urls_practice')),
    #    --           ----------------------
    #      1          2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `host1/project1/urls_practice.py` の urlpatterns を (1.) にぶら下げる
    #           ----------------------
]
```

# Step 12. Webページにアクセスする

📖 [http://localhost:8000/practice/v1/page1](http://localhost:8000/practice/v1/page1)  

# 次の記事

📖 [DjangoのHTMLのボイラープレートを減らすテンプレートを使おう！](https://qiita.com/muzudho1/items/7dcfc068e0bec009d371)  

# 参考にした記事

👇 より一般的なバージョン番号の付け方は、 **セマンティック バージョニング** が参考になる  

📖 [Semantic Versioning](https://qiita.com/usamik26/items/c8911219b610101e69a9)  
