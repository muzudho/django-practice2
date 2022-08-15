# サンプルを見る

📖 [http://tic.warabenture.com:8000/practice/v1/vuetify/validation1](http://tic.warabenture.com:8000/practice/v1/vuetify/validation1)  

# 目的

Vuetify の テキストフィールド の バリデーション を練習したい  

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
    │   │       │       ├── 📂 prefecture
    │   │       │       └── 📂 vuetifies
    │   │       │           ├── 📂 data_table1
    │   │       │           │   └── 📄 v1o0.html
    │   │       │           └── 📂 hello
    │   │       │               └── 📄 v1o0.html
    │   │       ├── 📂 views
    │   │       │   ├── 📂 prefecture
    │   │       │   └── 📂 vuetifies
    │   │       │       ├── 📂 data_table1
    │   │       │       │   └── 📄 v1o0.py
    │   │       │       └── 📄 __init__.py
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

# Step OA12o3o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step OA12o3o0g2o0 画面作成 - vuetifies/validation1/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 vuetifies
                            └── 📂 validation1
👉                              └── 📄 v1o0.html
```

```html
{# OA12o3o0g2o0 #}
<!-- -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
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
        <title>ビューティファイのバリデーション１</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container fluid>
                        <h1>ビューティファイのバリデーション１</h1>
                        <v-form method="POST">
                            {% csrf_token %}

                            <v-text-field v-model="userName.value" :rules="userName.rules" counter="16" hint="a-z, 0-9, No number at the beginning. Max 16 characters" label="User name" name="user_name"></v-text-field>

                            <v-text-field v-model="roomName.value" :rules="roomName.rules" counter="25" hint="a-z, A-Z, _. Max 25 characters" label="Room name" name="room_name"></v-text-field>
                        </v-form>
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
                    userName: {
                        value: "elephant1234",
                        rules: [
                            (value) => !!value || "Required", // 空欄の禁止
                            (v) => v.length <= 16 || "Max 16 characters", // 文字数上限
                            (value) => {
                                const pattern = /^[a-z][a-z0-9]*$/; // 正規表現で指定
                                return pattern.test(value) || "Invalid format";
                            },
                        ],
                    },
                    roomName: {
                        value: "Elephant",
                        rules: [
                            (value) => !!value || "Required", // 空欄の禁止
                            (v) => v.length <= 25 || "Max 25 characters", // 文字数上限
                            (value) => {
                                const pattern = /^[A-Za-z_]+$/; // 正規表現で指定
                                return pattern.test(value) || "Invalid format";
                            },
                        ],
                    },
                    selectedMyPiece: "X",
                    pieces: ["X", "O"],
                },
            });
        </script>
    </body>
</html>
```

# Step OA12o3o0g3o0 ビュー作成 - v_validation1.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 templates
                │    └── 📂 practice_v1              # アプリケーションと同名
                │       └── 📂 vuetifies
                │           └── 📂 validation1
                │               └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 vuetifies
                        └── 📂 validation1
👉                          └── 📄 v1o0.py
```

```py
from django.shortcuts import render


def render_validation1(request):
    """OA12o3o0g3o0 バリデーション１の描画"""

    # * `lp_` - Local path
    lp_validation1 = 'practice_v1/vuetifies/validation1/v1o0.html'
    #                 -------------------------------------------
    #                 1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/vuetifies/validation1/v1o0.html` を取得
    #                                      -------------------------------------------

    context = {}
    return render(request, lp_validation1, context)
```

# Step OA12o3o0g4o0 ビュー編集 - VuetifyV モジュール

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 vuetifies
                │           └── 📂 validation1
                │               └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 vuetifies
                        ├── 📂 validation1
                        │   └── 📄 v1o0.py
👉                      └── 📄 __init__.py
```

```py
class VuetifyV(object):
    """OA12o1o0g4o0 ビューティファイの練習のビュー"""


    # ..略..


    # 以下を追加
    # OA12o3o0g4o0 バリデーション１
    from .validation1.v1o0 import render_validation1
```

# Step OA12o3o0g5o0 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 vuetifies
        │       │           └── 📂 validation1
        │       │               └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 vuetifies
        │               ├── 📂 validation1
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


    # OA12o3o0g5o0 ビューティファイでバリデーション１
    path('practice/v1/vuetify/validation1',
         # ------------------------------
         # 1
         VuetifyV.render_validation1, name='practice_v1_vuetify_validation1'),
    #    ---------------------------        -------------------------------
    #    2                                  3
    # 1. 例えば `http://example.com/practice/v1/vuetify/validation1` のような URL のパスの部分
    #                              -------------------------------
    # 2. VuetifyV クラスの render_validation1 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_validation1' %} のような形でURLを取得するのに使える
]
```

# Step OA12o3o0g6o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/vuetify/validation1](http://localhost:8000/practice/v1/vuetify/validation1)  

# Step OA12o3o0g7o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 vuetifies
        │       │           └── 📂 validation1
        │       │               └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 vuetifies
        │               ├── 📂 validation1
        │               │   └── 📄 v1o0.py
        │               └── 📄 __init__.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/vuetify/validation1,ビューティファイでバリデーション１
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Django のビューの Python スクリプトで JSON ファイルを読み込んで HTML に埋め込んでいる JavaScript にデータを渡そう！](https://qiita.com/muzudho1/items/b3b0c25fc329eb9bc0c1)  

# 参考にした記事

📖 [Vuetifyでのバリデーションまとめ](https://inokawablog.org/vue-js/vuetify-validation/)  