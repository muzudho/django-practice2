# 目的

Django に最初から入っている HTMLレンダラー に満足できない。  
見た目を今風にしたい。  
そこでフロントエンドに Vuetify を使う。  

# はじめに

この記事は Lesson0 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key       | Value                                     |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Auth      | allauth                                   |
| Frontside | Vuetify                                   |
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂host1
    │   ├── 📂apps1
    │   │   ├── 📂allauth_customized    # アプリケーション
    │   │   ├── 📂portal                # アプリケーション
    │   │   └── 📂practice              # アプリケーション
    │   │       ├── 📂management
    │   │       ├── 📂migrations
    │   │       ├── 📂models
    │   │       ├── 📂static
    │   │       ├── 📂templates
    │   │       │   └── 📂practice          # アプリケーションと同名
    │   │       │       └── 📂v0o0o1
    │   │       │           └── 📂prefecture
    │   │       │               ├── 📄delete.html
    │   │       │               ├── 📄list.html
    │   │       │               ├── 📄read.html
    │   │       │               └── 📄upsert.html
    │   │       ├── 📂views
    │   │       │   └── 📂v0o0o1
    │   │       │       └── 📂prefecture
    │   │       │           ├── 📄__init__.py
    │   │       │           ├── 📄v_delete.py
    │   │       │           ├── 📄v_list.py
    │   │       │           ├── 📄v_read.py
    │   │       │           └── 📄v_upsert.py
    │   │       ├── 📄__init__.py
    │   │       ├── 📄admin.py
    │   │       ├── 📄apps.py
    │   │       └── 📄tests.py
    │   ├── 📂data
    │   ├── 📂project1                  # プロジェクト
    │   │   ├── 📄__init__.py
    │   │   ├── 📄asgi.py
    │   │   ├── 📄settings_secrets_example.txt
    │   │   ├── 📄settings.py
    │   │   ├── 📄urls_accounts.py
    │   │   ├── 📄urls_practice.py
    │   │   ├── 📄urls.py
    │   │   └── 📄wsgi.py
    │   ├── 📂project2                  # プロジェクト
    │   ├── 🐳docker-compose-project2.yml
    │   ├── 🐳docker-compose.yml
    │   ├── 🐳Dockerfile
    │   ├── 📄manage.py
    │   └── 📄requirements.txt
    └── 📄.gitignore
```

# Step 1. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. 画面作成 - hello1.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                  # アプリケーション
                └── 📂templates
                    └── 📂practice              # アプリケーションと同名
                        └── 📂v0o0o1
                            └── 📂vuetify
👉                              └── 📄hello1.html
```

```html
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<!-- See also: https://vuetifyjs.com/en/getting-started/installation/#usage-with-cdn -->
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui" />
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />
        <!-- Vuetify -->
        <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <!--                                                ===================
                                                            1
            1. Example: `http://example.com/static/favicon.ico`
                                            ==================
        -->
        <title>ビューティファイのハロー</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container>
                        <v-alert type="success">This is a sample.</v-alert>
                        Hello world
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            new Vue({
                el: "#app",
                vuetify: new Vuetify(),
            });
        </script>
    </body>
</html>
```

👆 `<v-alert>` の説明は 📖[Vuetify Alerts Usage](https://vuetifyjs.com/en/components/alerts/#usage) のページにある  

# Step 3. ビュー作成 - v_hello1.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                  # アプリケーション
                ├── 📂templates
                │    └── 📂practice              # アプリケーションと同名
                │        └── 📂v0o0o1
                │            └── 📂vuetify
                │                └── 📄hello1.html
                └── 📂views
                    └── 📂v0o0o1
                        └── 📂vuetify
👉                          └── 📄v_hello1.py
```

```py
from django.http import HttpResponse
from django.template import loader


def render_hello1(request):
    """ハローの描画"""

    template = loader.get_template(
        'practice/v0o0o1/vuetify/hello1.html')
    #    -----------------------------------
    #    1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/vuetify/hello1.html` を取得
    #                                    -----------------------------------

    context = {
    }

    return HttpResponse(template.render(context, request))
```

# Step 4. ビュー作成 - VuetifyV モジュール

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                  # アプリケーション
                ├── 📂templates
                │   └── 📂practice
                │       └── 📂v0o0o1
                │           └── 📂vuetify
                │               └── 📄hello1.html
                └── 📂views
                    └── 📂v0o0o1
                        └── 📂vuetify
👉                          ├── 📄__init__.py
                            └── 📄v_hello1.py
```

```py
class VuetifyV(object):
    """ビューティファイの練習のビュー"""

    from .v_hello1 import render_hello1
```

# Step 5. ルート編集 - urls.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂practice                  # アプリケーション
        │       ├── 📂templates
        │       │   └── 📂practice
        │       │       └── 📂v0o0o1
        │       │           └── 📂vuetify
        │       │               └── 📄hello1.html
        │       └── 📂views
        │           └── 📂v0o0o1
        │               └── 📂vuetify
        │                   ├── 📄__init__.py
        │                   └── 📄v_hello1.py
        └── 📂project1                          # プロジェクト
👉          ├── 📄urls_practice.py              # こちら
❌          └── 📄urls.py                       # これではない
```

```py
from django.urls import path


# ...略...


from apps1.practice.views.v0o0o1.vuetify import VuetifyV
#    ----- -------- --------------------        --------
#    1     2        3                           4
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


urlpatterns = [


    # ...略...


    # ビューティファイでハロー
    path('practice/vuetify/hello1', VuetifyV.render_hello1, name='vuetify_hello1'),
    #     -----------------------   ----------------------        --------------
    #     1                         2                             3
    # 1. 例えば `http://example.com/practice/vuetify/hello1` のような URL のパスの部分
    #                              ------------------------
    # 2. VuetifyV クラスの render_hello1 メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_hello1' %} のような形でURLを取得するのに使える
]
```

# Step 6. Web画面へアクセス

📖 [http://localhost:8000/practice/vuetify/hello1](http://localhost:8000/practice/vuetify/hello1)  

# 次の記事

📖 [DjangoでVuetifyのData tableを使おう！](https://qiita.com/muzudho1/items/2b01d3acce5ec1b5770b)  
