# 目的

Webサイトのポータルページを作成したい  

以下のようなURLで表示させる  

```plain
http://example.com/
------]------------
1      2

1. スキーム（HTTPプロトコル）
2. ホストの例
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
    │   ├── 📂apps1
    │   │   └── 📂practice              # アプリケーション名
    │   │       ├── 📂templates
    │   │       │   └── 📂practice
    │   │       │       └── 📂v0o0o1
    │   │       │           ├── 📄page1.html
    │   │       │           ├── 📄page2_base.html
    │   │       │           └── 📄page2_patch1.html.txt
    │   │       └── 📂views
    │   │           └── 📂v0o0o1
    │   │               └── 📄pages.py
    │   ├── 📂data
    │   ├── 📂project1                  # プロジェクト名
    │   │   ├── 📄__init__.py
    │   │   ├── 📄asgi.py
    │   │   ├── 📄settings.py
    │   │   ├── 📄urls_practice.py
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

# Step 2. フォルダー作成 - apps1/portal フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂portal        # アプリケーション名
```

# Step 3. アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp portal ./apps1/portal
#                                                     ------ --------------
#                                                     1      2
# 1. 任意のDjangoアプリケーション名
# 2. パス
```

# Step 4. 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂portal                # アプリケーション名
                ├── 📂migrations
                │   └── 📄__init__.py
                ├── 📄__init__.py
                ├── 📄admin.py
                ├── 📄apps.py
👉              ├── 📄models.py
                ├── 📄tests.py
👉              └── 📄views.py
```

# Step 5. 画面作成 - portal_base.html ファイル

以下のファイルを作成してほしい。

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂portal                # アプリケーション名
                ├── 📂migrations
                │   └── 📄__init__.py
                ├── 📂templates
                │   └── 📂portal        # アプリケーションと同名
                │       └── 📂v0o0o1
👉              │           └── 📄portal_base.html
                ├── 📄__init__.py
                ├── 📄admin.py
                ├── 📄apps.py
                └── 📄tests.py
```

```html
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
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

# Step 6. 設定変更 - settings.py ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂portal                # アプリケーション名
        │       ├── 📂migrations
        │       │   └── 📄__init__.py
        │       ├── 📂templates
        │       │   └── 📂portal
        │       │       └── 📂v0o0o1
        │       │           └── 📄portal_base.html
        │       ├── 📄__init__.py
        │       ├── 📄admin.py
        │       ├── 📄apps.py
        │       └── 📄tests.py
        └── 📂project1
👉          └── 📄settings.py
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


            # ...中略...


            # * 追加
            os.path.join(BASE_DIR, 'apps1/portal/templates'),
            #            --------   ----------------------
            #            1          2
            #
            # Example: /host1/apps1/portal/templates/portal/v0o0o1/portal_base.html
            #          ------ ----------------------
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

以下のファイルを作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂portal                # アプリケーション名
                ├── 📂migrations
                │   └── 📄__init__.py
                ├── 📂templates
                │   └── 📂portal        # アプリケーションと同名
                │       └── 📂v0o0o1
                │           └── 📄portal_base.html
                ├── 📂views
                │   └── 📂v0o0o1
👉              │       └── 📄pages.py
                ├── 📄__init__.py
                ├── 📄admin.py
                ├── 📄apps.py
                └── 📄tests.py
```

```py
from django.http import HttpResponse
from django.template import loader


class Portal():
    """ポータル ページ"""

    def render(request):
        """描画"""

        template = loader.get_template('portal/v0o0o1/portal_base.html')
        #                               ------------------------------
        #                               1
        # 1. host1/apps1/practice/templates/portal/v0o0o1/portal_base.html を取得
        #                                   ------------------------------

        context = {
            "dj_path_of_page1": "/practice/page1",
            "dj_path_of_page2_patch1": "/practice/page2_patch1",
            "dj_path_of_page2_patch2": "/practice/page2_patch2",
        }

        return HttpResponse(template.render(context, request))
```

# Step 8. サブ ルート作成 - urls_portal.py

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂portal                # アプリケーション名
        │       ├── 📂migrations
        │       │   └── 📄__init__.py
        │       ├── 📂templates
        │       │   └── 📂portal
        │       │       └── 📂v0o0o1
        │       │           └── 📄portal_base.html
        │       └── 📂views
        │           └── 📂v0o0o1
        │               └── 📄pages.py
        └── 📂project1
👉          ├── 📄urls_portal.py            # 新規作成
❌          └── 📄urls.py                   # これではない
```

```py
from django.urls import path

from apps1.portal.views.v0o0o1.pages import Portal
#    ------------------------- -----        ------
#    1                         2            3
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

# Step 9. 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂portal                # アプリケーション名
        │       ├── 📂migrations
        │       │   └── 📄__init__.py
        │       ├── 📂templates
        │       │   └── 📂portal
        │       │       └── 📂v0o0o1
        │       │           └── 📄portal_base.html
        │       └── 📂views
        │           └── 📂v0o0o1
        │               └── 📄pages.py
        └── 📂project1
❌          ├── 📄urls_portal.py            # これではない
👉          └── 📄urls.py                   # こっち
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

# Step 10. Webページにアクセスする

📖 [http://localhost:8000/](http://localhost:8000/)  

# 参考にした記事

📖 [DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92)  
