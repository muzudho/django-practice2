# 目的

Pythonコードを編集しなくても、ポータルページのリンクを増減できるようにする  

# 手段

CSV と pandas を使う  

# はじめに

この記事は LessonO[1 0] から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key       | Value                                     |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 host1
    │   ├── 📂 apps1
    │   │   ├── 📂 portal_v1                # アプリケーション名
    │   │   │   ├── 📂 migrations
    │   │   │   │   └── 📄 __init__.py
    │   │   │   ├── 📂 static
    │   │   │   │   └── 🚀 favicon.ico
    │   │   │   ├── 📂 templates
    │   │   │   │   └── 📂 portal_v1
    │   │   │   │       └── 📂 o1o0
    │   │   │   │           └── 📄 portal_base.html
    │   │   │   └── 📂 views
    │   │   │       └── 📂 o1o0
    │   │   │           └── 📄 pages.py
    │   │   └── 📂 practice_v1
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
    └── 📄 .gitignore
```

# Step O[1 0] Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step O[2 0] Pythonパッケージ インストール指定の編集 - requirements.txt ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1                   # あなたの開発用ディレクトリー。任意の名前
👉      └── 📄 requirements.txt
```

👇 追加

```plaintext
# ...略...


# CSV読取等
pandas
```

# Step O[3 0] Visual Studio Code のエラー抑制 - pip コマンド

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

# Step O[4 0] Dockerコンテナの停止～ビルド～起動

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

# Step O[5 0] データ作成 - finished-lessons.csv ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 portal_v1
        │       └── 📂 data
        │           └── 📄 finished-lessons.csv
        └── 📄 requirements.txt
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
path,label
/,ポータル
/admin,管理画面
/practice/v1/page1,ページ１
/practice/v1/page2_patch1,ページ２ パッチ１
/practice/v1/page2_patch2,ページ２ パッチ２
```

# Step O[6 0] 画面作成 - portal_base.html ファイル

以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 portal_v1                    # アプリケーション名
        │       ├── 📂 data
        │       │   └── 📄 finished-lesson.csv
        │       └── 📂 templates
        │           └── 📂 portal_v1            # アプリケーション名と同名
❌      │               ├── 📂 o1o0               # これではない
        │               └── 📂 o3o1             # こちら
👉      │                   └── 📄 portal_base.html
        └── 📄 requirements.txt
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
```

# Step O[7 0] ビュー作成 - pages.py ファイル

以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 portal_v1            # アプリケーション名
        │       ├── 📂 data
        │       │   └── 📄 finished-lesson.csv
        │       ├── 📂 templates
        │       │   └── 📂 portal_v1    # アプリケーション名と同名
        │       │       └── 📂 o3o1
        │       │           └── 📄 portal_base.html
        │       └── 📂 views
❌      │           ├── 📂 o1o0           # これではない
        │           └── 📂 o3o1         # こちら
👉      │               └── 📄 pages.py
        └── 📄 requirements.txt
```

```py
import pandas as pd

from django.http import HttpResponse
from django.template import loader


class Portal():
    """ポータル ページ"""

    def render(request):
        """描画"""

        template = loader.get_template('portal_v1/o3o1/portal_base.html')
        #                                          ^three
        #                               -------------------------------
        #                               1
        # 1. host1/apps1/portal_v1/templates/portal_v1/o3o1/portal_base.html を取得
        #                                    -------------------------------

        df = pd.read_csv('apps1/portal_v1/data/finished-lessons.csv')
        #                 -----------------------------------------
        #                 1
        # 1. `host1/apps1/portal_v1/data/finished-lessons.csv` を読取
        #           -----------------------------------------

        print(df)
        #
        # Example
        # -------
        #                         path      label
        # 0         /practice/v1/page1     ページ１
        # 1  /practice/v1/page2_patch1  ページ２ パッチ１
        # 2  /practice/v1/page2_patch2  ページ２ パッチ２

        print(df.columns)
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

        for item in finished_lesson_list:
            print(f"{item['path']} , {item['label']}")
        #
        # Example
        # -------
        # /practice/v1/page1 , ページ１
        # /practice/v1/page2_patch1 , ページ２ パッチ１
        # /practice/v1/page2_patch2 , ページ２ パッチ２

        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        context = {
            "dj_finished_lesson_list": finished_lesson_list,
        }

        return HttpResponse(template.render(context, request))
```

# Step O[8 0] サブ ルート編集 - urls_portal.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 portal_v1                # アプリケーション
        │       ├── 📂 data
        │       │   └── 📄 finished-lesson.csv
        │       ├── 📂 templates
        │       │   └── 📂 portal_v1        # アプリケーションと同名
        │       │       └── 📂 o3o1
        │       │           └── 📄 portal_base.html
        │       └── 📂 views
        │           ├── 📂 o1o0
        │           └── 📂 o3o1
        │               └── 📄 pages.py
        ├── 📂 project1
👉      │   ├── 📄 urls_portal.py           # こちら
❌      │   └── 📄 urls.py                  # これではない
        └── 📄 requirements.txt
```

```py
# * 変更前
#from apps1.portal_v1.views.o1o0.pages import Portal
# * 変更後
from apps1.portal_v1.views.o3o1.pages import Portal
#                           ^three
```

# Step O[9 0] Webページにアクセスする

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでユーザー認証を付けよう！](https://qiita.com/muzudho1/items/55cb7ac55299afd51887)  

# 参考にした記事

## CSV

📖 [pandasでcsv/tsvファイル読み込み（read_csv, read_table）](https://note.nkmk.me/python-pandas-read-csv-tsv/)  

## Docker

📖 [初心者向けdocker-composeコマンド逆引き](https://qiita.com/okyk/items/a374ddb3f853d1688820)  
