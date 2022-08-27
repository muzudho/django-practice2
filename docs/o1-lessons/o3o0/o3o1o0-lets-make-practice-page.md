# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1.0/page-the-hello/ver1.0/)  

# 目標

Webサイトのページを追加したい  

## 詳細

以下のようなURLで表示させる  

```plain
http://example.com/practice/vol1.0/page-the-hello/ver1.0/
------]----------]---------------------------------------
1      2          3

1. スキーム（HTTPプロトコル）
2. ホストの例
3. パス
```

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is   | This is                                   |
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

# 手順

## Step O3o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step O3o1o0g2o0 フォルダー作成 - apps1/practice_vol1o0 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1                # 複数のアプリケーションを入れるフォルダー
            └── 📂 practice_vol1o0      # アプリケーション フォルダー
```

* `apps1` - 末尾の `1` は文字列検索しやすいように付けているだけで特別な意味はない
* `practice_vol1o0` - 末尾の `_vol1o0` はレッスンの都合で付けている `1.0巻` という意味だが無くてもいい

## Step O3o1o0g3o0 アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp practice_vol1o0 ./apps1/practice_vol1o0 --settings=project1.settings
#                                                     --------------- -----------------------            -----------------
#                                                     1               2                                  3
# 1. 任意のDjangoアプリケーション名
# 2. アプリケーション フォルダーへのパス
# 3. `src1/project1/settings.py` 設定ファイルに従う
#          -----------------
```

👇 以下のようなディレクトリー、ファイルが自動生成される  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0              # アプリケーション名
👉              ├── 📂 migrations
👉              │   └── 📄 __init__.py
👉              ├── 📄 __init__.py
👉              ├── 📄 admin.py
👉              ├── 📄 apps.py
👉              ├── 📄 models.py
👉              ├── 📄 tests.py
👉              └── 📄 views.py
```

## Step O3o1o0g4o0 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0              # アプリケーション名
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
                ├── 📄 apps.py
👉              ├── 📄 models.py
                ├── 📄 tests.py
👉              └── 📄 views.py
```

## Step O3o1o0g5o0 アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0              # アプリケーション名
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
👉              ├── 📄 apps.py
                └── 📄 tests.py
```

```py
# BOF O3o1o0g5o0

from django.apps import AppConfig


class PracticeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    #name = 'practice_v1'
    # * O3o1o0g5o0 変更後
    name = 'apps1.practice_vol1o0'
    #       ---------------------
    #       1
    # 1. `src1/apps1/practice_vol1o0/apps.py`
    #          ---------------------

# EOF O3o1o0g5o0
```

## Step O3o1o0g6o0 アプリケーション登録 - settings.py ファイル＜その２＞

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_vol1o0              # アプリケーション名
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
    # O3o1o0g6o0 練習1.0巻
    'apps1.practice_vol1o0',

    # Djangoの標準アプリケーション
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

これで、 `src1/apps1/practice_vol1o0` フォルダーは practice_vol1o0 アプリケーションとして認識される。  
そのメリットは　今後のレッスンで触れる  

## Step O3o1o0g7o0 画面作成 - hello/ver1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_vol1o0              # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0      # アプリケーションと同名
        │       │       └── 📂 hello
👉      │       │           └── 📄 ver1o0.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

* `templateの下のpractice_vol1o0` - あなたの Django の支配下のすべてのアプリケーションのテンプレート素材は、まるで実行時メモリの中で、あなたの Django の支配下のすべてのアプリケーションからアクセスできる１つの静的フォルダーに再配置されているかのように扱えると考えてほしい。あとは自分の頭で考えてほしい

```html
<!-- O3o1o0g7o0 -->
<html>
    <head>
        <title>ページ１</title>
    </head>
    <body>
        こんにちわ、世界！
    </body>
</html>
```

## Step O3o1o0g8o0 設定変更 - settings.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_vol1o0              # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0      # アプリケーションと同名
        │       │       └── 📂 hello
        │       │           └── 📄 ver1o0.html
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
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # * 変更前
        # 'DIRS': [],
        # * 変更後
        'DIRS': [
            # O3o1o0g8o0 練習1.0巻
            os.path.join(BASE_DIR, 'apps1/practice_vol1o0/templates'),
            #                       -------------------------------
            #                       10
            # Example: /src1/apps1/practice_vol1o0/templates/practice_vol1o0/hello/ver1o0.html
            #                      ---------------          ----------------
            #                      11                       2
            #                -------------------------------
            #                10
            # 10. テンプレート ディレクトリーへのパス
            # 11. アプリケーション
            # 2. まるで `http://example.com/practice_vol1o0` という素材フォルダーがあるかのように扱われる
            #                             ----------------
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

## Step O3o1o0g9o0 ビュー作成 - hello/ver1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_vol1o0                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 hello
        │       │           └── 📄 ver1o0.html
        │       ├── 📂 views
        │       │   └── 📂 hello
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
# BOF O3o1o0g9o0

from django.shortcuts import render


class HelloView():
    """O3o1o0g9o0 こんにちわページ"""

    @staticmethod
    def render(request):
        """描画"""

        template_path = 'practice_vol1o0/hello/ver1o0.html'
        #                ---------------------------------
        #                1
        # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/hello/ver1o0.html` を取得
        #                                          ---------------------------------

        context = {}
        return render(request, template_path, context)

        # テンプレートを使わず、HTMLをハードコーディングすることもできる
        # return HttpResponse("""Hello, world.<br/>
        #                    <a href="http://example.com/">ホーム</a>""")

        # 以下のような書き方もある
        # from django.http import HttpResponse
        # from django.template import loader
        # template = loader.get_template('this/is/a/local/path/example.html')
        # context = {}
        # HttpResponse(template.render(context, request))

# EOF O3o1o0g9o0
```

## Step O3o1o0gA10o0 サブ ルート作成 - urls_practice.py

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_vol1o0                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 hello
        │       │           └── 📄 ver1o0.html
        │       ├── 📂 views
        │       │   └── 📂 hello
        │       │       └── 📂 ver1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
👉          ├── 📄 urls_practice.py          # 新規作成
❌          └── 📄 urls.py                   # これではない
```

```py
# BOF O3o1o0gA10o0

from django.urls import path

# O3o1o0gA10o0 練習1.0巻 こんにちわページ1.0版
from apps1.practice_vol1o0.views.hello.ver1o0 import HelloView
#          ---------------             ------        ---------
#          11                          12            2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [

    # O3o1o0gA10o0 練習1.0巻 こんにちわページ1.0版
    path('practice/vol1.0/page-the-hello/ver1.0/',
         # -------------------------------------
         # 1
         HelloView.render, name='hello'),
    #    ----------------        -----
    #    2                       3
    # 1. 例えば `http://example.com/practice/vol1.0/page-the-hello/ver1.0/` のようなURLのパスの部分
    #                              ---------------------------------------
    # 2. HelloView クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'hello' %} のような形でURLを取得するのに使える
]

# EOF O3o1o0gA10o0
```

## Step O3o1o0gA11o0 総合ルート編集 - urls.py

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_vol1o0                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 hello
        │       │           └── 📄 ver1o0.html
        │       ├── 📂 views
        │       │   └── 📂 hello
        │       │       └── 📂 ver1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
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

## Step O3o1o0gA12o0 Webページにアクセスする

📖 [http://localhost:8000/practice/vol1.0/page-the-hello/ver1.0/](http://localhost:8000/practice/vol1.0/page-the-hello/ver1.0/)  

# 次の記事

📖 [o3o2o_1o0 URL設定を自動化しよう！](https://qiita.com/muzudho1/items/eed6f70c0c1502942738)  

# 参考にした記事

👇 より一般的なバージョン番号の付け方は、 **セマンティック バージョニング** が参考になる  

📖 [Semantic Versioning](https://qiita.com/usamik26/items/c8911219b610101e69a9)  
