# サンプルを見る

📖 [http://tic.warabenture.com:8000/practice/v1/vuetify/hello1](http://tic.warabenture.com:8000/practice/v1/vuetify/hello1)  

# 目的

Django に最初から入っている HTMLレンダラー に満足できない。  
見た目を今風にしたい。  
そこでフロントエンドに Vuetify を使う  

# はじめに

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   └── 📂 practice_v1              # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1          # アプリケーションと同名
    │   │       │       └── 📂 prefecture
    │   │       │           └── 📂 v1o0
    │   │       │               ├── 📄 delete.html
    │   │       │               ├── 📄 list.html
    │   │       │               ├── 📄 read.html
    │   │       │               └── 📄 upsert.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 prefecture
    │   │       │       └── 📂 v1o0
    │   │       │           ├── 📄 __init__.py
    │   │       │           ├── 📄 v_delete.py
    │   │       │           ├── 📄 v_list.py
    │   │       │           ├── 📄 v_read.py
    │   │       │           └── 📄 v_upsert.py
    │   │       ├── 📄 __init__.py
    │   │       ├── 📄 admin.py
    │   │       ├── 📄 apps.py
    │   │       └── 📄 tests.py
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_accounts.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2                  # プロジェクト
    │   ├── 🐳 docker-compose-project2.yml
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

# Step OA12o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step OA12o1o0g2o0 画面作成 - hello/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 vuetifies
                            └── 📂 hello
👉                              └── 📄 v1o0.html
```

```html
{# OA12o1o0g2o0 #}
<!-- -->
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

# Step OA12o1o0g3o0 ビュー作成 - v_hello1.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 templates
                │    └── 📂 practice_v1              # アプリケーションと同名
                │        └── 📂 vuetifies
                │            └── 📂 hello
                │                └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 vuetifies
                        └── 📂 hello
👉                          └── 📄 v1o0.py
```

```py
from django.shortcuts import render


def render_hello1(request):
    """OA12o1o0g3o0 ハローの描画"""

    # * `lp_` - Local path
    lp_hello = 'practice_v1/vuetifies/hello/v1o0.html'
    #           -------------------------------------
    #           1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/vuetifies/hello/v1o0.html` を取得
    #                                      -------------------------------------

    context = {}
    return render(request, lp_hello, context)
```

# Step OA12o1o0g4o0 ビュー作成 - vuetifies フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 vuetifies
                │           └── 📂 hello
                │               └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 vuetifies
👉                      ├── 📄 __init__.py
                        └── 📂 hello
                            └── 📄 v1o0.py
```

```py
class VuetifyV(object):
    """OA12o1o0g4o0 ビューティファイの練習のビュー"""

    # OA12o1o0g4o0 こんにちわ
    from .hello.v1o0 import render_hello1
```

# Step OA12o1o0g5o0 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 vuetifies
        │       │           └── 📂 hello
        │       │               └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 vuetifies
        │               ├── 📄 __init__.py
        │               └── 📂 hello
        │                   └── 📄 v1o0.py
        └── 📂 project1                          # プロジェクト
👉          ├── 📄 urls_practice.py              # こちら
❌          └── 📄 urls.py                       # これではない
```

```py
# ...略...


# OA12o1o0g5o0 ビューティファイ練習
from apps1.practice_v1.views.vuetifies import VuetifyV
#          -----------       ---------        --------
#          11                12               2
#    ---------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [


    # ...略...


    # OA12o1o0g5o0 ビューティファイでハロー
    path('practice/v1/vuetify/hello1', VuetifyV.render_hello1,
         # -------------------------   ----------------------
         # 1                           2
         name='practice_v1_vuetify_hello1'),
    #          --------------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/vuetify/hello1` のような URL のパスの部分
    #                              --------------------------
    # 2. VuetifyV クラスの render_hello1 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_hello1' %} のような形でURLを取得するのに使える
]
```

# Step OA12o1o0g6o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/vuetify/hello1](http://localhost:8000/practice/v1/vuetify/hello1)  

# Step OA12o1o0g7o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 vuetifies
        │       │           └── 📂 hello
        │       │               └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 vuetifies
        │               ├── 📄 __init__.py
        │               └── 📂 hello
        │                   └── 📄 v1o0.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/vuetify/hello1,ビューティファイでハロー
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DjangoでVuetifyのData tableを使おう！](https://qiita.com/muzudho1/items/2b01d3acce5ec1b5770b)  