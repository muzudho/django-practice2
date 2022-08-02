# サンプルを見る

📖 [http://tic.warabenture.com:8000/practice/v1/vuetify/textarea1](http://tic.warabenture.com:8000/practice/v1/vuetify/textarea1)  

# 目的

Web ページで表示する内容を、JSON形式のテキストで渡したい  

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
    │   │       │   └── 📂 practice_v1
    │   │       │       └── 📂 o1o0
    │   │       │           └── 📂 data
    │   │       │               └── 📄 desserts1.json
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1          # アプリケーションと同名
    │   │       │       └── 📂 o1o0
    │   │       │           ├── 📂 prefecture
    │   │       │           └── 📂 vuetify
    │   │       │               └── 📄 desserts1.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 o1o0
    │   │       │       ├── 📂 prefecture
    │   │       │       └── 📂 vuetify
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

# Step OA13o2o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step OA13o2o0g2o0 データの再利用 - desserts.json ファイル

👇 以下の記事で掲載した JSON ファイルを再利用してほしい  

* 📖 [Django のビューの Python スクリプトで JSON ファイルを読み込んで HTML に埋め込んでいる JavaScript にデータを渡そう！](https://qiita.com/muzudho1/items/b3b0c25fc329eb9bc0c1)

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 static
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 o1o0
                            └── 📂 data
👉                              └── 📄 desserts1.json
```

# Step OA13o2o0g3o0 画面作成 - textarea1_base.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 o1o0
                │           └── 📂 data
                │               └── 📄 desserts1.json
                └── 📂 templates
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 o1o0
                            └── 📂 vuetify
👉                              └── 📄 textarea1_base.html
```

```html
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
                        <form method="POST" action="desserts1-from-textarea1">
                            <!--                    ========================
                                                    1
                            1. 宛先を間違えないように
                               `http://example.com/practice/v1/vuetify/desserts1-from-textarea1`
                                                                       ========================
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
```

# Step OA13o2o0g4o0 HTMLファイルの再利用 - desserts1.html ファイル

👇 以下の記事で掲載した HTML ファイルを再利用してほしい  

* 📖 [Django のビューの Python スクリプトで JSON ファイルを読み込んで HTML に埋め込んでいる JavaScript にデータを渡そう！](https://qiita.com/muzudho1/items/b3b0c25fc329eb9bc0c1)

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 o1o0
                │           └── 📂 data
                │               └── 📄 desserts1.json
                └── 📂 templates
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 o1o0
                            └── 📂 vuetify
👉                              ├── 📄 desserts1.html
                                └── 📄 textarea1_base.html
```

# Step OA13o2o0g5o0 ビュー作成 - v_textarea1.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 o1o0
                │           └── 📂 data
                │               └── 📄 desserts1.json
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o1o0
                │           └── 📂 vuetify
                │               ├── 📄 desserts1.html
                │               └── 📄 textarea1_base.html
                └── 📂 views
                    └── 📂 o1o0
                        └── 📂 vuetify
👉                          └── 📄 v_textarea1.py
```

```py
import json
from django.shortcuts import render


def render_textarea1(request):
    """OA13o2o0g5o0 ビューティファイのテキストエリア１"""

    # * `lp_` - Local path
    lp_textarea1_base = 'practice_v1/o1o0/vuetify/textarea1_base.html'
    #                    --------------------------------------------
    #                    1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/o1o0/vuetify/textarea1_base.html` を取得
    #                                      --------------------------------------------

    with open('apps1/practice_v1/static/practice_v1/o1o0/data/desserts1.json', mode='r', encoding='utf-8') as f:
        #      -------------------------------------------------------------
        #      1
        # 1. `src1/apps1/practice_v1/static/practice_v1/o1o0/data/desserts1.json` を取得
        #          -------------------------------------------------------------
        doc = json.load(f)

    context = {
        'dessertsStr': json.dumps(doc)
    }
    return render(request, lp_textarea1_base, context)


def render_desserts1_from_textarea1(request):
    """OA13o2o0g5o0 ビューティファイのデザート１ . テキストエリア１から"""

    form1Textarea1 = request.POST["textarea1"]

    # * `lp_` - Local path
    lp_desserts1 = 'practice_v1/o1o0/vuetify/desserts1.html'
    #               ---------------------------------------
    #               1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/o1o0/vuetify/desserts1.html` を取得
    #                                      ---------------------------------------

    context = {
        'dessertsStr': form1Textarea1
    }
    return render(request, lp_desserts1, context)
```

# Step OA13o2o0g6o0 ビュー編集 - VuetifyV モジュール

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 o1o0
                │           └── 📂 data
                │               └── 📄 desserts1.json
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o1o0
                │           └── 📂 vuetify
                │               ├── 📄 desserts1.html
                │               └── 📄 textarea1_base.html
                └── 📂 views
                    └── 📂 o1o0
                        └── 📂 vuetify
👉                          ├── 📄 __init__.py
                            └── 📄 v_textarea1.py
```

```py
class VuetifyV(object):
    """ビューティファイの練習のビュー"""

    # ..略..


    # 以下を追加
    from .v_textarea1 import render_textarea1, render_desserts1_from_textarea1
```

# Step OA13o2o0g7o0 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📂 data
        │       │               └── 📄 desserts1.json
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📂 vuetify
        │       │               ├── 📄 textarea1_base.html
        │       │               └── 📄 desserts1.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 vuetify
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_textarea1.py
        └── 📂 project1                          # プロジェクト
👉          ├── 📄 urls_practice.py              # こちら
❌          └── 📄 urls.py                       # これではない
```

```py
from django.urls import path


# ...略...


# 都道府県ビュー
from apps1.practice_v1.views.o1o0.vuetify import VuetifyV
#          -----------            -------        --------
#          11                     12             2
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [


    # ...略...


    # ビューティファイでテキストエリア１
    path('practice/v1/vuetify/textarea1',
         # ----------------------------
         # 1
         VuetifyV.render_textarea1, name='practice_v1_vuetify_textarea1'),
    #    -------------------------        -----------------------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/v1/vuetify/textarea1` のような URL のパスの部分
    #                              -----------------------------
    # 2. VuetifyV クラスの render_textarea1 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_textarea1' %} のような形でURLを取得するのに使える

    # ビューティファイでデザート１ . テキストエリア１から
    path('practice/v1/vuetify/desserts1-from-textarea1',
         # -------------------------------------------
         # 1
         VuetifyV.render_desserts1_from_textarea1, name='practice_v1_vuetify_desserts1_from_textarea1'),
    #    ----------------------------------------        --------------------------------------------
    #    2                                               3
    # 1. 例えば `http://example.com/practice/v1/vuetify/desserts1-from-textarea1` のような URL のパスの部分
    #                              ---------------------------------------------
    # 2. VuetifyV クラスの render_desserts1_from_textarea1 メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_desserts1_from_textarea1' %} のような形でURLを取得するのに使える
]
```

# Step OA13o2o0g8o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/vuetify/textarea1](http://localhost:8000/practice/v1/vuetify/textarea1)  

# Step OA13o2o0g9o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

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
        │       │       └── 📂 o1o0
        │       │           └── 📂 data
        │       │               └── 📄 desserts1.json
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📂 vuetify
        │       │               ├── 📄 textarea1_base.html
        │       │               └── 📄 desserts1.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 vuetify
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_textarea1.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/vuetify/textarea1,ビューティファイでテキストエリア１
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DjangoのサーバーからデータをJSON形式のテキストで受信しよう！](https://qiita.com/muzudho1/items/d83760a6a4abadaf19c4)  
