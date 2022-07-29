# 目的

Webサイトに来訪したユーザーが、コンテンツの存在に気づかずWebサイトを離脱した、ということを減らしたい  

MECE に考えると以下の４つ  

* ユーザーは、コンテンツの存在に気づき、コンテンツにアクセスした : **こうありたい**
* ユーザーは、コンテンツの存在に気づき、離脱した : **わらう**
* ユーザーは、コンテンツの存在に気付かず、コンテンツにアクセスした : **エスパーか**
* ユーザーは、コンテンツの存在に気付かず、離脱した : **人事を尽くしてこれを減らしたい**

# 手段

Webサイトのポータルページを作成する  

ポータルページは以下のようなURLと **したいが**  

```plain
http://example.com/
------]------------
1      2

1. スキーム（HTTPプロトコル）
2. ホストの例
```

まずは練習として以下のURLとする  

```plain
http://example.com/practice/v1/portal
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
    ├── 📂 host1
    │   ├── 📂 apps1
    │   │   └── 📂 practice_v1              # アプリケーション名
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1
    │   │       │       ├── 📂 o1o0
    │   │       │       │   └── 📄 page_the_hello.html
    │   │       │       │   └── 📄 page_to_be_added.html
    │   │       │       ├── 📂 o2o0
    │   │       │       │   └── 📄 page_to_be_added.html.txt
    │   │       │       └── 📂 o3o0
    │   │       │           └── 📄 page_to_be_added.html.txt
    │   │       └── 📂 views
    │   │           ├── 📂 o1o0
    │   │           │   └── 📂 page_the_hello
    │   │           │       └── 📄 __init__.py
    │   │           ├── 📂 o2o0
    │   │           │   └── 📂 page_to_be_added
    │   │           │       └── 📄 __init__.py
    │   │           └── 📂 o3o0
    │   │               └── 📂 page_to_be_added
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
    └── 📄 .gitignore
```

# Step O1o0 Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step O2o0 フォルダー作成 - apps1/portal_v1 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 portal_v1        # アプリケーション名
```

# Step O3o0 アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp portal_v1 ./apps1/portal_v1
#                                                     --------- -----------------
#                                                     1         2
# 1. 任意のDjangoアプリケーション名
# 2. パス
```

# Step O4o0 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 portal_v1                # アプリケーション名
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
                ├── 📄 apps.py
👉              ├── 📄 models.py
                ├── 📄 tests.py
👉              └── 📄 views.py
```

# Step O5o0 アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 portal_v1                # アプリケーション名
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
👉              ├── 📄 apps.py
                └── 📄 tests.py
```

```py
from django.apps import AppConfig


class PortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # 変更前
    #name = 'portal_v1'
    # 変更後
    name = 'apps1.portal_v1'
    #       ---------------
    #       1
    # 1. `host1/apps1/portal_v1/apps.py`
    #           ---------------
```

# Step O6o0 アプリケーション登録 - settings.py ファイル＜その２＞

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 portal_v1                # アプリケーション名
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


    'apps1.portal_v1',


    # ...中略...


]
```

これで、 `host1/apps1/portal_v1` フォルダーは portal_v1 アプリケーションとして認識される。  
例えば、 portal_v1 フォルダーの直下に置いた static フォルダーが Django の静的リソースの検索対象のパスになるといったメリットがある  

# Step O7o0 アイコンの設定 - favicon.ico ファイル

favicon.ico は、例えば 以下のサイトで作れる。作ってきてほしい  

📖 [Favicon Generator. For real.](https://realfavicongenerator.net/)  

例えば、以下の場所に置いてほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 portal_v1                # アプリケーション
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

# Step O8o0 画面作成 - portal_base.html ファイル

以下のファイルを作成してほしい。

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 portal_v1                # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 🚀 favicon.ico   # アプリケーション毎にアイコンを作るのがめんどくさいので static の直下に置いた
        │       ├── 📂 templates
        │       │   └── 📂 portal_v1        # アプリケーションと同名
        │       │       └── 📂 o1o0
👉      │       │           └── 📄 portal_base.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```html
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
        <title>ポータル</title>
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
                            <v-btn :href="vu_pathOfPageTheHello">おはようページ</v-btn>
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
                    vu_pathOfPageTheHello: `${location.protocol}//${location.host}{{ dj_path_of_page_the_hello }}`,
                    //                      --------------------  ---------------]-------------------------------
                    //                      1                     2               3
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
```

# Step O9o0 設定変更 - settings.py ファイル＜その２＞

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 portal_v1                # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 🚀 favicon.ico   # アプリケーション毎にアイコンを作るのがめんどくさいので static の直下に置いた
        │       ├── 📂 templates
        │       │   └── 📂 portal_v1        # アプリケーションと同名
        │       │       └── 📂 o1o0
        │       │           └── 📄 portal_base.html
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


            # ポータル
            os.path.join(BASE_DIR, 'apps1/portal_v1/templates'),
            #                       -------------------------
            #                       10
            # Example: /host1/apps1/portal_v1/templates/portal_v1/o1o0/portal_base.html
            #                       ---------          ----------
            #                       11                 2
            #                 -------------------------
            #                 10
            # 10. テンプレート ディレクトリーへのパス
            # 11. アプリケーション
            # 2. まるで `http://example.com/practice_v1` という素材フォルダーがあるかのように扱われる
            #                             --------------
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

# Step OA10o0 ビュー モジュール作成 - portal フォルダー

以下のファイルを作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 portal_v1                # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 🚀 favicon.ico      # アプリケーション毎にアイコンを作るのがめんどくさいので static の直下に置いた
        │       ├── 📂 templates
        │       │   └── 📂 portal_v1        # アプリケーションと同名
        │       │       └── 📂 o1o0
        │       │           └── 📄 portal_base.html
        │       ├── 📂 views
        │       │   └── 📂 o1o0
        │       │       └── 📂 portal
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
from django.http import HttpResponse
from django.template import loader


class Portal():
    """ポータル ページ"""

    def render(request):
        """描画"""

        template = loader.get_template('portal_v1/o1o0/portal_base.html')
        #                               -------------------------------
        #                               1
        # 1. host1/apps1/practice_v1/templates/portal_v1/o1o0/portal_base.html を取得
        #                                      -------------------------------

        context = {
            "dj_path_of_page_the_hello": "/practice/v1/page-the-hello",
            "dj_path_of_page_to_be_added_1": "/practice/v1/page-to-be-added-1",
            "dj_path_of_page_to_be_added_2": "/practice/v1/page-to-be-added-2",
        }

        return HttpResponse(template.render(context, request))
```

# Step OA11o0 サブ ルート作成 - urls_portal.py

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 portal_v1                # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 🚀 favicon.ico      # アプリケーション毎にアイコンを作るのがめんどくさいので static の直下に置いた
        │       ├── 📂 templates
        │       │   └── 📂 portal_v1        # アプリケーションと同名
        │       │       └── 📂 o1o0
        │       │           └── 📄 portal_base.html
        │       ├── 📂 views
        │       │   └── 📂 o1o0
        │       │       └── 📂 portal
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
👉          ├── 📄 urls_portal.py            # 新規作成
❌          └── 📄 urls.py                   # これではない
```

```py
from django.urls import path

# ポータルの練習
from apps1.portal_v1.views.o1o0.portal import Portal as PortalO1o0
#          ---------            ------        ------    ----------
#          11                   12            2         3
#    ---------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [

    # ポータルの練習
    path('practice/v1/portal',
         # -----------------
         # 1
         PortalO1o0.render, name='practice_v1_portal'),
    #    -----------------        ------------------
    #    2                        3
    # 1. 例えば `http://example.com/practice/v1/portal` のようなURLのパスの部分
    #                              -------------------
    # 2. PortalO1o0 (別名)クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_portal' %} のような形でURLを取得するのに使える
]
```

# Step OA12o0 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 portal_v1                # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 🚀 favicon.ico      # アプリケーション毎にアイコンを作るのがめんどくさいので static の直下に置いた
        │       ├── 📂 templates
        │       │   └── 📂 portal_v1        # アプリケーションと同名
        │       │       └── 📂 o1o0
        │       │           └── 📄 portal_base.html
        │       ├── 📂 views
        │       │   └── 📂 o1o0
        │       │       └── 📂 portal
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
❌          ├── 📄 urls_portal.py            # これではない
👉          └── 📄 urls.py                   # こっち
```

```py
from django.urls import include, path


# ...中略...


urlpatterns = [


    # ...中略...


    # ポータル
    path('', include('project1.urls_portal')),
    #    --           --------------------
    #      1          2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `host1/project1/urls_portal.py` の urlpatterns を (1.) にぶら下げる
    #           --------------------
]
```

# Step OA13o0 Webページにアクセスする

📖 [http://localhost:8000/practice/v1/portal](http://localhost:8000/practice/v1/portal)  

# 次の記事

📖 [DjangoでCSVとpandasを使ってPythonコードを編集しなくてもポータルページのリンクを増減できるようにしよう！](https://qiita.com/muzudho1/items/19c44296501c29c41d31)  

# 参考にした記事

📖 [DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92)  
