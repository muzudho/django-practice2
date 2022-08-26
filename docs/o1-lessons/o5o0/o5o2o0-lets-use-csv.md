# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/)  

# 目標

Pythonコードを編集しなくても、ランチャーのボタン（リンク）を増減できるようにする  

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
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   ├── 📂 launcher_vol1o0                # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   │   └── 📄 __init__.py
    │   │   │   ├── 📂 static
    │   │   │   │   └── 🚀 favicon.ico      # アプリケーション毎にアイコンを作るのがめんどくさいので static の直下に置いた
    │   │   │   ├── 📂 templates
    │   │   │   │   └── 📂 launcher_vol1o0        # アプリケーションと同名
    │   │   │   │       └── 📄 ver1o0.html
    │   │   │   ├── 📂 views
    │   │   │   │   └── 📂 launcher
    │   │   │   │       └── 📂 ver1o0
    │   │   │   │           └── 📄 __init__.py
    │   │   │   ├── 📄 __init__.py
    │   │   │   ├── 📄 admin.py
    │   │   │   ├── 📄 apps.py
    │   │   │   └── 📄 tests.py
    │   │   └── 📂 practice_vol1o0
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
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📄 urls.py
    └── 📄 .gitignore
```

# 手順

## Step O5o2o0g1o0 Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step O5o2o0g2o0 Pythonパッケージ インストール指定の編集 - requirements.txt ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1                   # あなたの開発用ディレクトリー。任意の名前
👉      └── 📄 requirements.txt
```

👇 追加

```plaintext
# ...略...


# CSV読取等
pandas
```

## Step O5o2o0g3o0 Visual Studio Code のエラー抑制 - pip コマンド

Python の pandas パッケージは、 Dockerコンテナにインストールされていればよく、  
Dockerコンテナの外側のPCにインストールしている必要はないが、  
しかし あなたの Visual Studio Code は  
👇 以下のような PROBLEMS （エラーメッセージ）を出しているかもしれない  

```plaintext
Import "pandas" could not be resolved from source
```

その Pythonソースは 外側のPCで実行するわけではないのだから無視して構わないが、気になるということはあるだろう。  
Dockerコンテナの外側のPCにも pandas をインストールすれば（本末転倒だが）エラーメッセージは解消する。  
👇 もし望むなら、以下のコマンドを打鍵してほしい  

```shell
pip install pandas
```

## Step O5o2o0g4o0 Dockerコンテナの停止～ビルド～起動

👇 以下のコマンドを打鍵してほしい  

```shell
# Dockerコンテナの停止
docker-compose down
# または Dockerマシンが走っているターミナルで `[Ctrl] + [C]` キーを打鍵
```

👇 以下のコマンドを打鍵してほしい  

```shell
# requirements.txtを変更したので、Pythonパッケージのインストールをやり直します
docker-compose build
```

👇 以下のコマンドを打鍵してほしい  

```shell
# Dockerコンテナの起動
docker-compose up
```

## Step O5o2o0g5o0 データ作成 - finished-lessons.csv ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 launcher_vol1o0
        │       └── 📂 data
        │           └── 📄 finished-lessons.csv
        └── 📄 requirements.txt
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
path,label
/launcher/vol1.0/ver1.0/,ランチャー1.0巻 1.0版
/,ポータル（ランチャー1.0巻 2.0版）
/admin,管理画面
/practice/vol1.0/page-the-hello/ver1.0/,こんにちわページ
/practice/vol1.0/page-to-be-added-1/ver1.0/,１回追加されたページ
/practice/vol1.0/page-to-be-added-2/ver1.0/,２回追加されたページ
```

## Step O5o2o0g6o0 画面作成 - launcher_vol1o0/ver2o0.html ファイル

以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 launcher_vol1o0                  # アプリケーション
        │       ├── 📂 data
        │       │   └── 📄 finished-lesson.csv
        │       └── 📂 templates
        │           └── 📂 launcher_vol1o0          # アプリケーションと同名
👉      │               └── 📄 ver2o0.html
        └── 📄 requirements.txt
```

```html
{# BOF O5o2o0g6o0 #}
<!-- -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <!--                                                ===================
                                                            1
            1. Example: `http://example.com/static/favicon.ico`
                                            ==================
        -->
        <title>ランチャー</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container>
                        <v-row class="my-2">
                            <h3>終わったレッスン</h3>
                        </v-row>
                        {# "vu_" は 「vue1のメンバー」 の目印 #}
                        <!-- -->
                        {# "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印 #}
                        <!-- -->
                        {% for item in dj_finished_lesson_list %}
                        <v-row class="my-2">
                            <v-btn :href="vu_createUrl('{{item.path}}')">{{item.label}}</v-btn>
                        </v-row>
                        {% endfor %}
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
                data: {},
                methods: {
                    /**
                     * URLを作成します
                     */
                    vu_createUrl(path) {
                        return `${location.protocol}//${location.host}${path}`;
                        //      --------------------  ---------------]-------
                        //      1                     2               3
                        // 1. スキーム（HTTPプロトコル）
                        // 2. ホスト
                        // 3. パス
                    },
                },
            });
        </script>
    </body>
</html>
{# EOF O5o2o0g6o0 #}
```

## Step O5o2o0g7o0 ビュー作成 - launcher/ver2o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 launcher_vol1o0            # アプリケーション名
        │       ├── 📂 data
        │       │   └── 📄 finished-lesson.csv
        │       ├── 📂 templates
        │       │   └── 📂 launcher_vol1o0    # アプリケーション名と同名
        │       │       └── 📄 ver2o0.html
        │       └── 📂 views
        │           └── 📂 launcher
        │               └── 📂 ver2o0
👉      │                   └── 📄 __init__.py
        └── 📄 requirements.txt
```

```py
# BOF O5o2o0g7o0

import pandas as pd

from django.shortcuts import render


class Launcher():
    """O5o2o0g7o0 ランチャー1.0巻 2.0版"""

    def render(request):
        """描画"""

        template_path = 'launcher_vol1o0/ver2o0.html'
        #                                   ^two
        #                ---------------------------
        #                1
        # 1. src1/apps1/launcher_vol1o0/templates/launcher_vol1o0/ver2o0.html を取得
        #                                         ---------------------------

        df = pd.read_csv('apps1/launcher_vol1o0/data/finished-lessons.csv')
        #                 -----------------------------------------------
        #                 1
        # 1. `src1/apps1/launcher_vol1o0/data/finished-lessons.csv` を読取
        #          -----------------------------------------------

        # print(df)
        #
        # Example
        # -------
        #    path                                         label
        # 0  /practice/vol1.0/page-the-hello/ver1.0/      こんにちわページ
        # 1  /practice/vol1.0/page-to-be-added-1/ver1.0/  １回追加されたページ
        # 2  /practice/vol1.0/page-to-be-added-2/ver1.0/  ２回追加されたページ

        # print(df.columns)
        #
        # Example
        # -------
        # Index(['path', 'label'], dtype='object')

        # 使いやすい構造に変換します
        finished_lesson_list = []
        df = df.reset_index()  # make sure indexes pair with number of rows
        for index, row in df.iterrows():
            finished_lesson_list.append({
                "path": row['path'],
                "label": row['label'],
            })

        # for item in finished_lesson_list:
        #    print(f"{item['path']} , {item['label']}")

        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        context = {
            "dj_finished_lesson_list": finished_lesson_list,
        }

        return render(request, template_path, context)

# EOF O5o2o0g7o0
```

## ~~Step O5o2o0g8o0~~

Merged to O5o2o0g8o1o0  

## Step O5o2o0g8o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 launcher_vol1o0            # アプリケーション名
    │   │       ├── 📂 data
    │   │       │   └── 📄 finished-lesson.csv
    │   │       ├── 📂 templates
    │   │       │   └── 📂 launcher_vol1o0    # アプリケーション名と同名
    │   │       │       └── 📄 ver2o0.html
    │   │       └── 📂 views
    │   │           └── 📂 launcher
    │   │               └── 📂 ver2o0
    │   │                   └── 📄 __init__.py
    │   └── 📄 requirements.txt
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_launcher_vol1o0_autogen.py,,home,"O5o2o0g8o1o0 ランチャー1.0巻 2.0版",apps1.launcher_vol1o0.views.launcher.ver2o0,Launcher,LauncherView1o0g2o0,render
```

👆 path を値無しにしている。スクリプトの方で、例えば `http://example.com/` といったURLの直下を指すよう対応する
👆 name に `home` と指定した。 設定にもよるが、ログイン後の飛び先にしようとしている  

## Step O5o2o0g8o2o0 ルート編集 - コマンド打鍵

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

## Step O5o2o0g9o0 Webページにアクセスする

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでユーザー認証を付けよう！](https://qiita.com/muzudho1/items/55cb7ac55299afd51887)  

# 参考にした記事

## Python

📖 [Is there a built-in function to print all the current properties and values of an object?](https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a)  

## CSV

📖 [pandasでcsv/tsvファイル読み込み（read_csv, read_table）](https://note.nkmk.me/python-pandas-read-csv-tsv/)  

## Docker

📖 [初心者向けdocker-composeコマンド逆引き](https://qiita.com/okyk/items/a374ddb3f853d1688820)  
