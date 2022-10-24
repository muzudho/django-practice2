# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/launcher/vol1.0/finished-lesson/ver1.0/)  

# 目標

ランチャー(*1)を作る  

*1 … ボタンがいっぱい並んでいて、押すとアプリが開くようなもの  

これからレッスンが終わるたびに、終わったレッスンに飛べるボタンをランチャーに追加していけば あとで見返すのに便利だ  

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
    │   ├── 📂 apps1
    │   │   └── 📂 practice_vol1o0              # アプリケーション名
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_vol1o0
    │   │       │       ├── 📂 hello
    │   │       │       │   └── 📄 ver1o0.html
    │   │       │       └── 📂 page_to_be_added
    │   │       │           ├── 📄 ver1o0.html
    │   │       │           ├── 📄 ver2o0.html.txt
    │   │       │           └── 📄 ver3o0.html.txt
    │   │       └── 📂 views
    │   │           ├── 📂 hello
    │   │           │   └── 📂 ver1o0
    │   │           │       └── 📄 __init__.py
    │   │           └── 📂 page_to_be_added
    │   │               ├── 📂 ver2o0
    │   │               │   └── 📄 __init__.py
    │   │               └── 📂 ver3o0
    │   │                   └── 📄 __init__.py
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト名
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2
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
    └── 📄 .gitignore
```

# 手順

## Step O5o1o0g1o0 Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step O5o1o0g2o0 フォルダー作成 - apps1/launcher_vol1o0 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 launcher_vol1o0        # アプリケーション名
```

## Step O5o1o0g3o0 アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp launcher_vol1o0 ./apps1/launcher_vol1o0
#                                                     --------------- -----------------------
#                                                     1               2
# 1. 任意のDjangoアプリケーション名
# 2. パス
```

## Step O5o1o0g4o0 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 launcher_vol1o0                # アプリケーション名
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
                ├── 📄 apps.py
👉              ├── 📄 models.py
                ├── 📄 tests.py
👉              └── 📄 views.py
```

## Step O5o1o0g5o0 アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 launcher_vol1o0                # アプリケーション名
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
👉              ├── 📄 apps.py
                └── 📄 tests.py
```

```py
# BOF O5o1o0g5o0

from django.apps import AppConfig


class PortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # 変更前
    #name = 'launcher_vol1o0'
    # 変更後
    name = 'apps1.launcher_vol1o0'
    #       ---------------------
    #       1
    # 1. `src1/apps1/launcher_vol1o0/apps.py`
    #          ---------------------

# EOF O5o1o0g5o0
```

## Step O5o1o0g6o0 アプリケーション登録 - settings.py ファイル＜その２＞

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 launcher_vol1o0                # アプリケーション名
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


    # O5o1o0g6o0 ランチャー1.0巻
    'apps1.launcher_vol1o0',


    # ...中略...


]
```

これで、 `src1/apps1/launcher_vol1o0` フォルダーは launcher_vol1o0 アプリケーションとして認識される。  
例えば、 launcher_vol1o0 フォルダーの直下に置いた static フォルダーが Django の静的リソースの検索対象のパスになるといったメリットがある  

## Step O5o1o0g7o0 アイコンの設定 - favicon.ico ファイル

favicon.ico は、例えば 以下のサイトで作れる。作ってきてほしい  

📖 [Favicon Generator. For real.](https://realfavicongenerator.net/)  

例えば、以下の場所に置いてほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 launcher_vol1o0                # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
👉      │       │   └── 🚀 favicon.ico   # アプリケーション毎にアイコンを作るのがめんどくさいので static の直下に置いた
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

favicon.ico を有効にするには HTML で設定する必要があるが、まだ作成しない。以下は例。あとで全体を再掲する  

```plaintext
{% load static %} {% comment %} 👈あとで static "URL" を使うので load static します {% endcomment %}
<!DOCTYPE html>
<html>
    <head>
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <!--                                                ===================
                                                            1
            1. Example: `http://example.com/static/favicon.ico`
                                            ==================
        -->
        中略
        <title>Tic Tac Toe</title>
    </head>
    <body>
以下略
```

## Step O5o1o0g8o0 画面作成 - launcher_vol1o0/finished_lesson/ver1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 launcher_vol1o0                # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 🚀 favicon.ico   # アプリケーション毎にアイコンを作るのがめんどくさいので static の直下に置いた
        │       ├── 📂 templates
        │       │   └── 📂 launcher_vol1o0        # アプリケーションと同名
        │       │       └── 📂 finished_lesson
👉      │       │           └── 📄 ver1o0.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```html
<!-- BOF O5o1o0g8o0 -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <!--                                                ===================
                                                            1
            1. Example: `http://example.com/static/favicon.ico`
                                            ==================
        -->
        <title>ランチャー</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container>
                        <v-row class="my-2">
                            <h3>終わったレッスン</h3>
                        </v-row>
                        <v-row class="my-2">
                            <v-btn :href="vu_pathOfHello">こんにちわページ</v-btn>
                        </v-row>
                        <v-row class="my-2">
                            <v-btn :href="vu_pathOfPageToBeAdded1">１回追加されたページ</v-btn>
                        </v-row>
                        <v-row class="my-2">
                            <v-btn :href="vu_pathOfPageToBeAdded2">２回追加されたページ</v-btn>
                        </v-row>
                        {% block finished_lesson_footer %}
                        <!-- -->
                        {% endblock finished_lesson_footer %}
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            let vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // "vu_" は 「vue1.dataのメンバー」 の目印
                    // "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
                    vu_pathOfHello: `${location.protocol}//${location.host}{{ dj_path_of_hello }}`,
                    //               --------------------  ---------------]----------------------
                    //               1                     2               3
                    // 1. スキーム（HTTPプロトコル）
                    // 2. ホスト
                    // 3. パス
                    vu_pathOfPageToBeAdded1: `${location.protocol}//${location.host}{{ dj_path_of_page_to_be_added_1 }}`,
                    vu_pathOfPageToBeAdded2: `${location.protocol}//${location.host}{{ dj_path_of_page_to_be_added_2 }}`,
                    {% block vue1_data_footer %}
                    <!-- -->
                    {% endblock vue1_data_footer %}
                },
            });
        </script>
    </body>
</html>
<!-- EOF O5o1o0g8o0 -->
```

## Step O5o1o0g9o0 設定変更 - settings.py ファイル＜その２＞

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 launcher_vol1o0                # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 🚀 favicon.ico   # アプリケーション毎にアイコンを作るのがめんどくさいので static の直下に置いた
        │       ├── 📂 templates
        │       │   └── 📂 launcher_vol1o0        # アプリケーションと同名
        │       │       └── 📂 finished_lesson
        │       │           └── 📄 ver1o0.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
👉          └── 📄 settings.py
```

👇 編集するのは `TEMPLATES[0]["DIRS"]` 変数  

```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # * 変更前
        # 'DIRS': [],
        # * 変更後
        'DIRS': [
            # ...略...


            # O5o1o0g9o0 ランチャー1.0巻
            os.path.join(BASE_DIR, 'apps1/launcher_vol1o0/templates'),
            #                       -------------------------------
            #                       10
            # Example: /src1/apps1/launcher_vol1o0/templates/launcher_vol1o0/finished_lesson/ver1o0.html
            #                      ---------------          ----------------
            #                      11                       2
            #                -------------------------------
            #                10
            # 10. テンプレート ディレクトリーへのパス
            # 11. アプリケーション
            # 2. まるで `http://example.com/launcher_vol1o0` という素材フォルダーがあるかのように扱われる
            #                             -----------------
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

## Step O5o1o0gA10o0 ビュー作成 - finished_lesson/ver1o0 フォルダー

👇 以下のファイルを作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 launcher_vol1o0                # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 🚀 favicon.ico      # アプリケーション毎にアイコンを作るのがめんどくさいので static の直下に置いた
        │       ├── 📂 templates
        │       │   └── 📂 launcher_vol1o0        # アプリケーションと同名
        │       │       └── 📂 finished_lesson
        │       │           └── 📄 ver1o0.html
        │       ├── 📂 views
        │       │   └── 📂 finished_lesson
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
# BOF O5o1o0gA10o0

from django.shortcuts import render


class Launcher():
    """O5o1o0gA10o0 練習1.0巻 ランチャー1.0版"""

    def render(request):
        """描画"""

        template_path = 'launcher_vol1o0/finished_lesson/ver1o0.html'
        #                -------------------------------------------
        #                1
        # 1. `src1/apps1/launcher_vol1o0/templates/launcher_vol1o0/finished_lesson/ver1o0.html` を取得
        #                                          -------------------------------------------

        context = {
            "dj_path_of_hello": "/practice/vol1.0/hello/ver1.0/",
            "dj_path_of_page_to_be_added_1": "/practice/vol1.0/page-to-be-added-1/ver1.0/",
            "dj_path_of_page_to_be_added_2": "/practice/vol1.0/page-to-be-added-2/ver1.0/",
        }

        return render(request, template_path, context)

# EOF O5o1o0gA10o0
```

## ~~Step O5o1o0gA11o0~~

Merged to O5o1o0gA11o1o0  

## Step O5o1o0gA11o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 launcher_vol1o0                # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 🚀 favicon.ico
    │   │       ├── 📂 templates
    │   │       │   └── 📂 launcher_vol1o0        # アプリケーションと同名
    │   │       │       └── 📂 finished_lesson
    │   │       │           └── 📄 ver1o0.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 launcher
    │   │       │       └── 📂 ver1o0
    │   │       │           └── 📄 __init__.py
    │   │       ├── 📄 __init__.py
    │   │       ├── 📄 admin.py
    │   │       ├── 📄 apps.py
    │   │       └── 📄 tests.py
    │   └── 📂 project1
    │       └── 📄 settings.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_launcher_vol1o0_autogen.py,launcher/vol1.0/finished-lesson/ver1.0/,,"O5o1o0gA11o1o0 ランチャー1.0巻 終了したレッスン1.0版",apps1.launcher_vol1o0.views.finished_lesson.ver1o0,Launcher,LauncherView1o0g1o0,render
```

## Step O5o1o0gA11o2o0 ルート編集 - コマンド打鍵

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

## ~~Step O5o1o0gA12o0~~

Merged to O5o1o0gA11o1o0  

## Step O5o1o0gA13o0 Webページにアクセスする

📖 [http://localhost:8000/launcher/vol1.0/finished-lesson/ver1.0/](http://localhost:8000/launcher/vol1.0/finished-lesson/ver1.0/)  

# 次の記事

📖 [DjangoでCSVとpandasを使ってPythonコードを編集しなくてもランチャーのリンクを増減できるようにしよう！](https://qiita.com/muzudho1/items/19c44296501c29c41d31)  

# 参考にした記事

📖 [DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92)  
