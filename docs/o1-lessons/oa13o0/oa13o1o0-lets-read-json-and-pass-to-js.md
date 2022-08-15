# サンプルを見る

📖 [http://tic.warabenture.com:8000/practice/v1/vuetify/desserts1](http://tic.warabenture.com:8000/practice/v1/vuetify/desserts1)  

# 目的

Vuetify に JSON形式でデータを渡したい  

# はじめに

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key         | Value                                     |
| ----------- | ----------------------------------------- |
| OS          | Windows10                                 |
| Container   | Docker                                    |
| Auth        | allauth                                   |
| Frontend    | Vuetify                                   |
| Data format | JSON                                      |
| Editor      | Visual Studio Code （以下 VSCode と表記） |

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
    │   │       │       ├── 📂 prefecture
    │   │       │       └── 📂 vuetifies
    │   │       ├── 📂 views
    │   │       │   ├── 📂 prefecture
    │   │       │   └── 📂 vuetifies
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

# Step OA13o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step OA13o1o0g2o0 データ作成 - desserts1/v1o0.json ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 static
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 data
                            └── 📂 desserts1
👉                              └── 📄 v1o0.json
```

```json
{
    "headers": [
        {
            "text": "Dessert (100g serving)",
            "align": "start",
            "sortable": false,
            "value": "name"
        },
        { "text": "Calories", "value": "calories" },
        { "text": "Fat (g)", "value": "fat" },
        { "text": "Carbs (g)", "value": "carbs" },
        { "text": "Protein (g)", "value": "protein" },
        { "text": "Iron (%)", "value": "iron" }
    ],
    "desserts": [
        {
            "name": "Frozen Yogurt",
            "calories": 159,
            "fat": 6.0,
            "carbs": 24,
            "protein": 4.0,
            "iron": "1%"
        },
        {
            "name": "Ice cream sandwich",
            "calories": 237,
            "fat": 9.0,
            "carbs": 37,
            "protein": 4.3,
            "iron": "1%"
        },
        {
            "name": "Eclair",
            "calories": 262,
            "fat": 16.0,
            "carbs": 23,
            "protein": 6.0,
            "iron": "7%"
        },
        {
            "name": "Cupcake",
            "calories": 305,
            "fat": 3.7,
            "carbs": 67,
            "protein": 4.3,
            "iron": "8%"
        },
        {
            "name": "Gingerbread",
            "calories": 356,
            "fat": 16.0,
            "carbs": 49,
            "protein": 3.9,
            "iron": "16%"
        },
        {
            "name": "Jelly bean",
            "calories": 375,
            "fat": 0.0,
            "carbs": 94,
            "protein": 0.0,
            "iron": "0%"
        },
        {
            "name": "Lollipop",
            "calories": 392,
            "fat": 0.2,
            "carbs": 98,
            "protein": 0,
            "iron": "2%"
        },
        {
            "name": "Honeycomb",
            "calories": 408,
            "fat": 3.2,
            "carbs": 87,
            "protein": 6.5,
            "iron": "45%"
        },
        {
            "name": "Donut",
            "calories": 452,
            "fat": 25.0,
            "carbs": 51,
            "protein": 4.9,
            "iron": "22%"
        },
        {
            "name": "KitKat",
            "calories": 518,
            "fat": 26.0,
            "carbs": 65,
            "protein": 7,
            "iron": "6%"
        }
    ]
}
```

👆 このJSONは 📖[Vuetify - Data tables - Usage](https://vuetifyjs.com/en/components/data-tables/#dense) のスクリプトに埋め込まれてある  

# Step OA13o1o0g3o0 画面作成 - desserts1.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 data
                │           └── 📂 desserts1
                │               └── 📄 v1o0.json
                └── 📂 templates
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 vuetifies
                            └── 📂 desserts1
👉                              └── 📄 v1o0.html
```

```html
{# OA13o1o0g3o0 #}
<!-- -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<!-- See also: https://vuetifyjs.com/en/components/data-tables/#dense -->
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
        <title>ビューティファイのデザート１</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container>
                        <v-data-table :headers="headers" :items="desserts" :items-per-page="5" class="elevation-1"></v-data-table>
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            var dessertsDoc = JSON.parse("{{ dessertsStr|escapejs }}");

            new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: dessertsDoc,
            });
        </script>
    </body>
</html>
```

# Step OA13o1o0g4o0 ビュー作成 - v_desserts1.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 data
                │           └── 📂 desserts1
                │               └── 📄 v1o0.json
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 vuetifies
                │           └── 📂 desserts1
                │               └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 vuetifies
                        └── 📂 desserts1
👉                          └── 📄 v1o0.py
```

```py
import json
from django.shortcuts import render


def render_desserts1(request):
    """OA13o1o0g4o0 ビューティファイのデザート１"""

    # * `lp_` - Local path
    lp_desserts1 = 'practice_v1/vuetifies/desserts1/v1o0.html'
    #               -----------------------------------------
    #               1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/vuetifies/desserts1/v1o0.html` を取得
    #                                      -----------------------------------------

    with open('apps1/practice_v1/static/practice_v1/data/desserts1/v1o0.json', mode='r', encoding='utf-8') as f:
        #      -------------------------------------------------------------
        #      1
        # 1. `src1/apps1/practice_v1/static/practice_v1/data/desserts1/v1o0.json` を取得
        #          -------------------------------------------------------------
        doc = json.load(f)

    context = {
        'dessertsStr': json.dumps(doc)
    }
    return render(request, lp_desserts1, context)
```

# Step OA13o1o0g5o0 ビュー編集 - VuetifyV モジュール

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 data
                │           └── 📂 desserts1
                │               └── 📄 v1o0.json
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 vuetifies
                │           └── 📂 desserts1
                │               └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 vuetifies
                        ├── 📂 desserts1
                        │   └── 📄 v1o0.py
👉                      └── 📄 __init__.py
```

```py
class VuetifyV(object):
    """OA12o1o0g4o0 ビューティファイの練習のビュー"""


    # ..略..


    # * 以下を追加
    # OA13o1o0g5o0 デザート１
    from .dessert1.v1o0 import render_desserts1
```

# Step OA13o1o0g6o0 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 practice_v1
        │       │       └── 📂 data
        │       │           └── 📂 desserts1
        │       │               └── 📄 v1o0.json
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 vuetifies
        │       │           └── 📂 desserts1
        │       │               └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 vuetifies
        │               ├── 📂 desserts1
        │               │   └── 📄 v1o0.py
        │               └── 📄 __init__.py
        └── 📂 project1                          # プロジェクト
👉          ├── 📄 urls_practice.py              # こちら
❌          └── 📄 urls.py                       # これではない
```

```py
# ...略...


urlpatterns = [


    # ...略...


    # OA13o1o0g6o0 ビューティファイでデザート１
    path('practice/v1/vuetify/desserts1',
         # ----------------------------
         # 1
         VuetifyV.render_desserts1, name='practice_v1_vuetify_desserts1'),
    #    -------------------------        -----------------------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/v1/vuetify/desserts1` のような URL のパスの部分
    #                              -----------------------------
    # 2. VuetifyV クラスの render_desserts1 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_desserts1' %} のような形でURLを取得するのに使える
]
```

# Step OA13o1o0g7o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/vuetify/desserts1](http://localhost:8000/practice/v1/vuetify/desserts1)  

# Step OA13o1o0g8o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 practice_v1
        │       │       └── 📂 data
        │       │           └── 📂 desserts1
        │       │               └── 📄 v1o0.json
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 vuetifies
        │       │           └── 📂 desserts1
        │       │               └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 vuetifies
        │               ├── 📂 desserts1
        │               │   └── 📄 v1o0.py
        │               └── 📄 __init__.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/vuetify/desserts1,ビューティファイでデザート１
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DjangoのWebページへJSON形式のテキストを渡そう！](https://qiita.com/muzudho1/items/c50859d9bde800d06a62)  

# 参考にした記事

* JSONをビューからテンプレートへ渡す方法
    * 📖 [Django: passing JSON from view to template](https://stackoverflow.com/questions/31151229/django-passing-json-from-view-to-template)
* Vuetifyのサンプルプログラム
    * 📖 [Vuetify - Data tables - Dense](https://vuetifyjs.com/en/components/data-tables/#dense)