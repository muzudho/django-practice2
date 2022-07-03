# 目的

Vuetify を自由自在に使えるよう、使用スキルを上げたい。  
Data table を作れば上がる。だから説明する  

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
    │   │       │           ├── 📂prefecture
    │   │       │           └── 📂vuetify
    │   │       │               └── 📄hello1.html
    │   │       ├── 📂views
    │   │       │   └── 📂v0o0o1
    │   │       │       ├── 📂prefecture
    │   │       │       └── 📂vuetify
    │   │       │           ├── 📄__init__.py
    │   │       │           └── 📄v_hello1.py
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

# Step 2. 画面作成 - data_table1.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                  # アプリケーション
                └── 📂templates
                    └── 📂practice              # アプリケーションと同名
                        └── 📂v0o0o1
                            └── 📂vuetify
👉                              └── 📄data_table1.html
```

```html
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<!-- See also: https://vuetifyjs.com/en/components/data-tables/#dense -->
<html>
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
        <title>ビューティファイのデータテーブル１</title>
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
            new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    headers: [
                        {
                            text: "Dessert (100g serving)",
                            align: "start",
                            sortable: false,
                            value: "name",
                        },
                        { text: "Calories", value: "calories" },
                        { text: "Fat (g)", value: "fat" },
                        { text: "Carbs (g)", value: "carbs" },
                        { text: "Protein (g)", value: "protein" },
                        { text: "Iron (%)", value: "iron" },
                    ],
                    desserts: [
                        {
                            name: "Frozen Yogurt",
                            calories: 159,
                            fat: 6.0,
                            carbs: 24,
                            protein: 4.0,
                            iron: "1%",
                        },
                        {
                            name: "Ice cream sandwich",
                            calories: 237,
                            fat: 9.0,
                            carbs: 37,
                            protein: 4.3,
                            iron: "1%",
                        },
                        {
                            name: "Eclair",
                            calories: 262,
                            fat: 16.0,
                            carbs: 23,
                            protein: 6.0,
                            iron: "7%",
                        },
                        {
                            name: "Cupcake",
                            calories: 305,
                            fat: 3.7,
                            carbs: 67,
                            protein: 4.3,
                            iron: "8%",
                        },
                        {
                            name: "Gingerbread",
                            calories: 356,
                            fat: 16.0,
                            carbs: 49,
                            protein: 3.9,
                            iron: "16%",
                        },
                        {
                            name: "Jelly bean",
                            calories: 375,
                            fat: 0.0,
                            carbs: 94,
                            protein: 0.0,
                            iron: "0%",
                        },
                        {
                            name: "Lollipop",
                            calories: 392,
                            fat: 0.2,
                            carbs: 98,
                            protein: 0,
                            iron: "2%",
                        },
                        {
                            name: "Honeycomb",
                            calories: 408,
                            fat: 3.2,
                            carbs: 87,
                            protein: 6.5,
                            iron: "45%",
                        },
                        {
                            name: "Donut",
                            calories: 452,
                            fat: 25.0,
                            carbs: 51,
                            protein: 4.9,
                            iron: "22%",
                        },
                        {
                            name: "KitKat",
                            calories: 518,
                            fat: 26.0,
                            carbs: 65,
                            protein: 7,
                            iron: "6%",
                        },
                    ],
                },
            });
        </script>
    </body>
</html>
```

👆 `<v-data-table>` の説明は 📖[Vuetify - Data tables - Usage](https://vuetifyjs.com/en/components/data-tables/#dense) のページにある  

# Step 3. ビュー作成 - v_data_table1.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                  # アプリケーション
                ├── 📂templates
                │    └── 📂practice              # アプリケーションと同名
                │        └── 📂v0o0o1
                │            └── 📂vuetify
                │                └── 📄data_table1.html
                └── 📂views
                    └── 📂v0o0o1
                        └── 📂vuetify
👉                          └── 📄v_data_table1.py
```

```py
from django.http import HttpResponse
from django.template import loader


def render_data_table1(request):
    """データテーブル１の描画"""

    template = loader.get_template(
        'practice/v0o0o1/vuetify/data_table1.html')
    #    ----------------------------------------
    #    1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/vuetify/data_table1.html` を取得
    #                                    ----------------------------------------

    context = {
    }

    return HttpResponse(template.render(context, request))
```

# Step 4. ビュー編集 - VuetifyV モジュール

👇 以下の既存ファイルを編集してほしい  

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
                            └── 📄v_data_table1.py
```

```py
class VuetifyV(object):
    """ビューティファイの練習のビュー"""

    # ..略..


    # 以下を追加
    from .v_data_table1 import render_data_table1
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
        │       │               └── 📄data_table1.html
        │       └── 📂views
        │           └── 📂v0o0o1
        │               └── 📂vuetify
        │                   ├── 📄__init__.py
        │                   └── 📄v_data_table1.py
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


    # ビューティファイでデータテーブル１
    path('practice/vuetify/data-table1',
         # ---------------------------
         # 1
         VuetifyV.render_data_table1, name='vuetify_data_table1'),
    #    ---------------------------        -------------------
    #    2                                  3
    # 1. 例えば `http://example.com/practice/vuetify/data-table1` のような URL のパスの部分
    #                              ----------------------------
    # 2. VuetifyV クラスの render_data_table1 メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_data_table1' %} のような形でURLを取得するのに使える
]
```

# Step 6. Web画面へアクセス

📖 [http://localhost:8000/practice/vuetify/data-table1](http://localhost:8000/practice/vuetify/data-table1)  
