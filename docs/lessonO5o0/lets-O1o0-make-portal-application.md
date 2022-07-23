# 目的

Webサイトに来訪したユーザーが、コンテンツの存在に気づかずWebサイトを離脱した、ということを減らしたい  

MECE に考えると以下の４つ  

* ユーザーは、コンテンツの存在に気づき、コンテンツにアクセスした : **こうありたい**
* ユーザーは、コンテンツの存在に気づき、離脱した : **わらう**
* ユーザーは、コンテンツの存在に気付かず、コンテンツにアクセスした : **エスパーか**
* ユーザーは、コンテンツの存在に気付かず、離脱した : **人事を尽くしてこれを減らしたい**

# 手段

Webサイトのポータルページを作成する  

ポータルページは以下のようなURLとする  

```plain
http://example.com/
------]------------
1      2

1. スキーム（HTTPプロトコル）
2. ホストの例
```

# はじめに

この記事は LessonO[1 0] から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    │   │       │       └── 📂 o2o1
    │   │       │           ├── 📄 page1.html
    │   │       │           ├── 📄 page2_base.html
    │   │       │           └── 📄 page2_patch1.html.txt
    │   │       └── 📂 views
    │   │           └── 📂 o2o1
    │   │               └── 📄 pages.py
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

# Step [1] Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step [2] フォルダー作成 - apps1/portal_v1 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 portal_v1        # アプリケーション名
```

# Step [3] アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp portal_v1 ./apps1/portal_v1
#                                                     --------- -----------------
#                                                     1         2
# 1. 任意のDjangoアプリケーション名
# 2. パス
```

# Step [4] 今回使わないファイルの削除

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

# Step [5] アプリケーション設定変更 - apps.py

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
    #       ------------
    #       1
    # 1. `host1/apps1/portal_v1/apps.py`
    #           ---------------
```

# Step [6] アプリケーション登録 - settings.py ファイル＜その２＞

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

# Step [7] アイコンの設定 - favicon.ico ファイル

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

# Step [8] 画面作成 - portal_base.html ファイル

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
        │       │       └── 📂 o2o1
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
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <!--                                                ===================
                                                            1
            1. Example: `http://example.com/static/favicon.ico`
                                            ==================
        -->
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
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
                            <v-btn :href="vu_pathOfPage1">ページ１</v-btn>
                        </v-row>
                        <v-row class="my-2">
                            <v-btn :href="vu_pathOfPage2Patch1">ページ２ パッチ１</v-btn>
                        </v-row>
                        <v-row class="my-2">
                            <v-btn :href="vu_pathOfPage2Patch2">ページ２ パッチ２</v-btn>
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
                    vu_pathOfPage1: `${location.protocol}//${location.host}{{ dj_path_of_page1 }}`,
                    //               --------------------  ---------------]----------------------
                    //               1                     2               3
                    // 1. スキーム（HTTPプロトコル）
                    // 2. ホスト
                    // 3. パス
                    vu_pathOfPage2Patch1: `${location.protocol}//${location.host}{{ dj_path_of_page2_patch1 }}`,
                    vu_pathOfPage2Patch2: `${location.protocol}//${location.host}{{ dj_path_of_page2_patch2 }}`,
                    {% block vue1_data_footer %}
                    <!-- -->
                    {% endblock vue1_data_footer %}
                },
            });
        </script>
    </body>
</html>
```

# Step [9] 設定変更 - settings.py ファイル＜その２＞

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
        │       │       └── 📂 o2o1
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
            # Example: /host1/apps1/portal_v1/templates/portal_v1/o2o1/portal_base.html
            #                       ---------          ----------
            #                       11                 2
            #                 -------------------------
            #                 10
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

# Step [10] ビュー作成 - pages.py ファイル

以下のファイルを作成してほしい  

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
        │       │       └── 📂 o2o1
        │       │           └── 📄 portal_base.html
        │       ├── 📂 views
        │       │   └── 📂 o2o1
👉      │       │       └── 📄 pages.py
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

        template = loader.get_template('portal_v1/o2o1/portal_base.html')
        #                               -------------------------------
        #                               1
        # 1. host1/apps1/practice_v1/templates/portal_v1/o2o1/portal_base.html を取得
        #                                      -------------------------------

        context = {
            "dj_path_of_page1": "/practice/v1/page1",
            "dj_path_of_page2_patch1": "/practice/v1/page2_patch1",
            "dj_path_of_page2_patch2": "/practice/v1/page2_patch2",
        }

        return HttpResponse(template.render(context, request))
```

# Step [11] サブ ルート作成 - urls_portal.py

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
        │       │       └── 📂 o2o1
        │       │           └── 📄 portal_base.html
        │       ├── 📂 views
        │       │   └── 📂 o2o1
        │       │       └── 📄 pages.py
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

from apps1.portal_v1.views.o2o1.pages import Portal
#    -------------------------- -----        ------
#    1                          2            3
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き
# 3. クラス名


urlpatterns = [

    # ポータル
    path('', Portal.render, name='page1'),
    #    --  -------------        -----
    #    1   2                    3
    # 1. 例えば `http://example.com/` のようなURLの直下
    # 2. Portal クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page1' %} のような形でURLを取得するのに使える
]
```

# Step [12] 総合ルート編集 - urls.py

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
        │       │       └── 📂 o2o1
        │       │           └── 📄 portal_base.html
        │       ├── 📂 views
        │       │   └── 📂 o2o1
        │       │       └── 📄 pages.py
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

# Step [13] Webページにアクセスする

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DjangoでCSVとpandasを使ってPythonコードを編集しなくてもポータルページのリンクを増減できるようにしよう！](https://qiita.com/muzudho1/items/19c44296501c29c41d31)  

# 参考にした記事

📖 [DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92)  
