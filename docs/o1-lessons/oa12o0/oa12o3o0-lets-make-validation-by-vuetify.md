# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1o0/vuetify/validation1/ver1o0/)  

# 目標

Vuetify の テキストフィールド の バリデーション を練習したい  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is   | This is                                   |
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
    │   │   ├── 📂 accounts_vol1o0    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   └── 📂 practice_vol1o0              # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_vol1o0          # アプリケーションと同名
    │   │       │       ├── 📂 prefecture
    │   │       │       └── 📂 vuetifies
    │   │       │           ├── 📂 data_table1
    │   │       │           │   └── 📄 ver1o0.html
    │   │       │           └── 📂 hello
    │   │       │               └── 📄 ver1o0.html
    │   │       ├── 📂 views
    │   │       │   ├── 📂 prefecture
    │   │       │   └── 📂 vuetifies
    │   │       │       ├── 📂 data_table1
    │   │       │       │   └── 📄 ver1o0.py
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

## Step OA12o3o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA12o3o0g2o0 画面作成 - vuetifies/validation1/ver1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_vol1o0              # アプリケーションと同名
                        └── 📂 vuetifies
                            └── 📂 validation1
👉                              └── 📄 ver1o0.html
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

## Step OA12o3o0g3o0 ビュー作成 - v_validation1.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 templates
                │    └── 📂 practice_vol1o0              # アプリケーションと同名
                │       └── 📂 vuetifies
                │           └── 📂 validation1
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 vuetifies
                        └── 📂 validation1
👉                          └── 📄 ver1o0.py
```

```py
# BOF OA12o3o0g3o0

from django.shortcuts import render


def render_validation1(request):
    """OA12o3o0g3o0 バリデーション１の描画"""

    # Template path
    validation1_tp = 'practice_vol1o0/vuetifies/validation1/ver1o0.html'
    #                 -------------------------------------------------
    #                 1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/vuetifies/validation1/ver1o0.html` を取得
    #                                          -------------------------------------------------

    context = {}
    return render(request, validation1_tp, context)

# EOF OA12o3o0g3o0
```

## Step OA12o3o0g4o0 ビュー編集 - VuetifyV モジュール

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 vuetifies
                │           └── 📂 validation1
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 vuetifies
                        ├── 📂 validation1
                        │   └── 📄 ver1o0.py
👉                      └── 📄 __init__.py
```

```py
class VuetifyV(object):
    """OA12o1o0g4o0 ビューティファイの練習のビュー"""


    # ..略..


    # 以下を追加
    # OA12o3o0g4o0 バリデーション１
    from .validation1.ver1o0 import render_validation1
```

## ~~Step OA12o3o0g5o0~~

Merged to OA12o3o0g5o1o0  

## Step OA12o3o0g5o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_vol1o0                  # アプリケーション
    │           ├── 📂 templates
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 vuetifies
    │           │           └── 📂 validation1
    │           │               └── 📄 ver1o0.html
    │           └── 📂 views
    │               └── 📂 vuetifies
    │                   ├── 📂 validation1
    │                   │   └── 📄 ver1o0.py
    │                   └── 📄 __init__.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/vuetify/validation1/ver1.0/,,"OA12o3o0g5o1o0 練習1.0巻 ビューティファイでバリデーション１ 1.0版",apps1.practice_vol1o0.views.vuetifies,VuetifyV,,render_validation1
```

## Step OA12o3o0g5o2o0 ルート編集 - コマンド打鍵

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

## Step OA12o3o0g6o0 Web画面へアクセス

📖 [http://localhost:8000/practice/vol1o0/vuetify/validation1/ver1o0/](http://localhost:8000/practice/vol1o0/vuetify/validation1/ver1o0/)  

## Step OA12o3o0g7o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_vol1o0                      # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 vuetifies
        │       │           └── 📂 validation1
        │       │               └── 📄 ver1o0.html
        │       └── 📂 views
        │           └── 📂 vuetifies
        │               ├── 📂 validation1
        │               │   └── 📄 ver1o0.py
        │               └── 📄 __init__.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/vol1.0/vuetify/validation1/ver1o0/,OA12o3o0g7o0 練習1.0巻 ビューティファイでバリデーション１ 1.0版
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Django のビューの Python スクリプトで JSON ファイルを読み込んで HTML に埋め込んでいる JavaScript にデータを渡そう！](https://qiita.com/muzudho1/items/b3b0c25fc329eb9bc0c1)  

# 参考にした記事

📖 [Vuetifyでのバリデーションまとめ](https://inokawablog.org/vue-js/vuetify-validation/)  
