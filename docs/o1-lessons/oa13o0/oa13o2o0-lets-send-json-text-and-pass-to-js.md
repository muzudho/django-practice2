# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1.0/vuetify/textarea1/ver1o0/)  

# 目標

Web ページで表示する内容を、JSON形式のテキストで渡したい  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is     | This is                                   |
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
    │   │   ├── 📂 accounts_vol1o0    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   └── 📂 practice_vol1o0              # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       │   └── 📂 practice_vol1o0
    │   │       │       └── 📂 data
    │   │       │           └── 📂 desserts1
    │   │       │               └── 📄 ver1o0.json
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_vol1o0          # アプリケーションと同名
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
    │   │   ├── 📄 urls_accounts_vol1o0.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2                  # プロジェクト
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

## Step [OA13o2o0g1o0] Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step [OA13o2o0g2o0] データの再利用 - desserts.json ファイル

👇 以下の記事で掲載した JSON ファイルを再利用してほしい  

* 📖 [Django のビューの Python スクリプトで JSON ファイルを読み込んで HTML に埋め込んでいる JavaScript にデータを渡そう！](https://qiita.com/muzudho1/items/b3b0c25fc329eb9bc0c1)

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                └── 📂 static
                    └── 📂 practice_vol1o0              # アプリケーションと同名
                        └── 📂 data
                            └── 📂 desserts1
👉                              └── 📄 ver1o0.json
```

## Step [OA13o2o0g3o0] 画面作成 - vuetifies/textarea1/ver1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_vol1o0
                │       └── 📂 data
                │           └── 📂 desserts1
                │               └── 📄 ver1o0.json
                └── 📂 templates
                    └── 📂 practice_vol1o0              # アプリケーションと同名
                        └── 📂 vuetifies
                            └── 📂 textarea1
👉                              └── 📄 ver1o0.html
```

```html
<!-- BOF OA13o2o0g3o0 -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<!-- See also: https://vuetifyjs.com/en/components/textareas/#counter -->
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
        <title>ビューティファイのテキストエリア１</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container fluid>
                        {% block form_signature %}
                        <form method="POST" action="{% url 'practice1o0_vuetify_desserts_from_textarea1o0' %}">
                            <!--                    =========================================================
                                                    1
                                1. urls_*.py ファイルで pathへ指定したname属性
                               `http://example.com/{url}`
                                                   =====
                            -->
                            {% endblock form_signature %}
                            <!-- -->
                            {% csrf_token %}
                            <!--
                               ==========
                               2
                            2. form要素の中に csrf_token を入れてください
                            -->
                            <v-textarea counter name="textarea1" label="JSONを入力してください" :rules="rules" :value="value"></v-textarea>
                            <v-btn type="submit" class="mr-4">送信</v-btn>
                        </form>
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
                data: {
                    rules: [(v) => v.length <= 3000 || "Max 3000 characters"],
                    value: JSON.stringify(dessertsDoc, null, "    "),
                },
            });
        </script>
    </body>
</html>
<!-- EOF OA13o2o0g3o0 -->
```

## Step [OA13o2o0g4o0] HTMLファイルの再利用 - desserts1.html ファイル

👇 以下の記事で掲載した HTML ファイルを再利用してほしい  

* 📖 [Django のビューの Python スクリプトで JSON ファイルを読み込んで HTML に埋め込んでいる JavaScript にデータを渡そう！](https://qiita.com/muzudho1/items/b3b0c25fc329eb9bc0c1)

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_vol1o0
                │       └── 📂 data
                │           └── 📂 desserts1
                │               └── 📄 ver1o0.json
                └── 📂 templates
                    └── 📂 practice_vol1o0              # アプリケーションと同名
                        └── 📂 vuetifies
                            ├── 📂 desserts1
👉                          │   └── 📄 ver1o0.html
                            └── 📂 textarea1
                                └── 📄 ver1o0.html
```

## Step [OA13o2o0g5o0] ビュー作成 - vuetifies/textarea1/ver1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_vol1o0
                │       └── 📂 data
                │           └── 📂 desserts1
                │               └── 📄 ver1o0.json
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 vuetifies
                │           ├── 📂 desserts1
                │           │   └── 📄 ver1o0.html
                │           └── 📂 textarea1
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 vuetifies
                        └── 📂 textarea1
👉                          └── 📄 ver1o0.py
```

```py
# BOF OA13o2o0g5o0

import json
from django.shortcuts import render


def render_textarea1(request):
    """OA13o2o0g5o0 ビューティファイのテキストエリア１"""

    # Template path
    textarea1_base_tp = 'practice_vol1o0/vuetifies/textarea1/ver1o0.html'
    #                    -----------------------------------------------
    #                    1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/vuetifies/textarea1/ver1o0.html` を取得
    #                                          -----------------------------------------------

    with open('apps1/practice_vol1o0/static/practice_vol1o0/data/desserts1/ver1o0.json', mode='r', encoding='utf-8') as f:
        #      -----------------------------------------------------------------------
        #      1
        # 1. `src1/apps1/practice_vol1o0/static/practice_vol1o0/data/desserts1/ver1o0.json` を取得
        #          -----------------------------------------------------------------------
        doc = json.load(f)

    context = {
        'dessertsStr': json.dumps(doc)
    }
    return render(request, textarea1_base_tp, context)


def render_desserts1_from_textarea1(request):
    """OA13o2o0g5o0 ビューティファイのデザート１ . テキストエリア１から"""

    form1Textarea1 = request.POST["textarea1"]

    # Template path
    desserts1_tp = 'practice_vol1o0/vuetifies/desserts1/ver1o0.html'
    #               -----------------------------------------------
    #               1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/vuetifies/desserts1/ver1o0.html` を取得
    #                                          -----------------------------------------------

    context = {
        'dessertsStr': form1Textarea1
    }
    return render(request, desserts1_tp, context)

# EOF OA13o2o0g5o0
```

## Step [OA13o2o0g6o0] ビュー編集 - VuetifyV モジュール

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_vol1o0
                │       └── 📂 data
                │           └── 📂 desserts1
                │               └── 📄 ver1o0.json
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 vuetifies
                │           ├── 📂 desserts1
                │           │   └── 📄 ver1o0.html
                │           └── 📂 textarea1
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 vuetifies
                        ├── 📂 textarea1
                        │   └── 📄 ver1o0.py
👉                      └── 📄 __init__.py
```

```py
class VuetifyV(object):
    """OA12o1o0g4o0 ビューティファイの練習のビュー"""


    # ..略..


    # * 以下を追加
    # OA13o2o0g6o0 テキストエリア１
    from .textarea1.ver1o0 import render_textarea1, render_desserts1_from_textarea1
```

## ~~Step [OA13o2o0g7o0]~~

Merged to OA13o2o0g7o1o0  

## Step [OA13o2o0g7o1o0] ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_vol1o0                  # アプリケーション
    │           ├── 📂 static
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 data
    │           │           └── 📂 desserts1
    │           │               └── 📄 ver1o0.json
    │           ├── 📂 templates
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 vuetifies
    │           │           ├── 📂 desserts1
    │           │           │   └── 📄 ver1o0.html
    │           │           └── 📂 textarea1
    │           │               └── 📄 ver1o0.html
    │           └── 📂 views
    │               └── 📂 vuetifies
    │                   ├── 📂 textarea1
    │                   │   └── 📄 ver1o0.py
    │                   └── 📄 __init__.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/vuetify/textarea1/ver1.0/,,"OA13o2o0g7o1o0 練習1.0巻 ビューティファイでテキストエリア１ 1.0版",apps1.practice_vol1o0.views.vuetifies,VuetifyV,,render_textarea1
../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/vuetify/desserts-from-textarea/ver1.0/,,"OA13o2o0g7o1o0 練習1.0巻 ビューティファイでデザート１ . テキストエリア１から 1.0版",apps1.practice_vol1o0.views.vuetifies,VuetifyV,,render_desserts1_from_textarea1
```

## Step [OA13o2o0g7o2o0] ルート編集 - コマンド打鍵

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

## Step [OA13o2o0g8o0] Web画面へアクセス

📖 [http://localhost:8000/practice/vol1.0/vuetify/textarea1/ver1.0/](http://localhost:8000/practice/vol1.0/vuetify/textarea1/ver1.0/)  

## Step [OA13o2o0g9o0] ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_vol1o0                      # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 data
        │       │           └── 📂 desserts1
        │       │               └── 📄 ver1o0.json
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 vuetifies
        │       │           ├── 📂 desserts1
        │       │           │   └── 📄 ver1o0.html
        │       │           └── 📂 textarea1
        │       │               └── 📄 ver1o0.html
        │       └── 📂 views
        │           └── 📂 vuetifies
        │               ├── 📂 textarea1
        │               │   └── 📄 ver1o0.py
        │               └── 📄 __init__.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/vol1.0/vuetify/textarea1/ver1.0/,OA13o2o0g9o0 練習1.0巻 ビューティファイでテキストエリア１ 1.0版
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DjangoのサーバーからデータをJSON形式のテキストで受信しよう！](https://qiita.com/muzudho1/items/d83760a6a4abadaf19c4)  
