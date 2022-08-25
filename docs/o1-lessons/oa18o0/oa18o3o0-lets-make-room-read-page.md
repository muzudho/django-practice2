# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1o0/rooms/read/ver1o0/1/)  

# 目標

（※いわゆる CRUD の R）  

`http://localhost:8000/practice/vol1o0/rooms/read/ver1o0/1/` へアクセスすると、  
id が 1 の部屋を表示したい  

## 詳細

表示例:  

```plaintext
部屋の詳細情報

名前
Elephant

先手Id
1

後手Id
2

盤面
+--+--+--+
| X|  |  |
+--+--+--+
|  | X|  |
+--+--+--+
| O| O| X|
+--+--+--+

棋譜
+----+
|   1|
+----+
|   7|
+----+
|   5|
+----+
|   8|
+----+
|   9|
+----+
```

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is          | This is                                   |
| ---------------- | ----------------------------------------- |
| OS               | Windows10                                 |
| Container        | Docker                                    |
| Database         | Postgresql, (Redis)                       |
| Program Language | Python 3                                  |
| Web framework    | Django                                    |
| Auth             | allauth                                   |
| Frontend         | Vuetify                                   |
| Data format      | JSON                                      |
| Others           | (Socket), Web socket                      |
| Editor           | Visual Studio Code （以下 VSCode と表記） |

参考にした元記事は 📖[DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92) だ。  
わたしの記事は単に **やってみた** ぐらいの位置づけだ  

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1                            # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 accounts_vol1o0    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_vol1o0              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 room
    │   │   │           └── 📄 ver1o0.py
    │   │   ├── 📂 tic_tac_toe_vol1o0           # アプリケーション
    │   │   └── 📂 tic_tac_toe_vol2o0           # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_vol2o0
    │   │       │       ├── 📂 gui
    │   │       │       └── 📂 think
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_vol2o0
    │   │       │       ├── 📂 gui
    │   │       │       └── 📂 think
    │   │       ├── 📂 views
    │   │       │   ├── 📂 gui
    │   │       │   └── 📂 think
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
    │   │   ├── 📄 urls_tic_tac_toe_v1.py
    │   │   ├── 📄 urls_tic_tac_toe_v2.py
    │   │   ├── 📄 urls.py
    │   │   ├── 📄 ws_urls_tic_tac_toe_v1.py
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
    ├── 📂 src2_local                      # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# 手順

## Step OA18o3o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA18o3o0g2o0 画面作成 - room/read/ver1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_vol1o0          # アプリケーションと同名
                        └── 📂 room
                            └── 📂 read
👉                              └── 📄 ver1o0.html
```

```html
<!-- BOF OA18o3o0g2o0 -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<!-- See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92 -->
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui" />
        <title>部屋読取</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container>
                        <h3>部屋の詳細情報</h3>
                        <div class="card" style="width: 18rem">
                            <!-- 部屋名，他 -->
                            <div class="card-body">
                                <h5 class="card-title">部屋名</h5>
                                <p class="card-text">{{ room.name }}</p>

                                <h5 class="card-title">先手Idと名前</h5>
                                <p class="card-text">
                                    {{ room.sente_id }}<br />
                                    {{ room.sente_name }}
                                </p>

                                <h5 class="card-title">後手Idと名前</h5>
                                <p class="card-text">
                                    {{ room.gote_id }}<br />
                                    {{ room.gote_name }}
                                </p>
                            </div>
                            <!-- 盤面 -->
                            <div class="card-body">
                                <h5 class="card-title">盤面</h5>
                                <v-container>
                                    <v-row justify="center" dense>
                                        <v-col>
                                            {% comment %} Vue で二重波括弧（braces）は変数の展開に使っていることから、 Python のテンプレートに二重波括弧を変数の展開に使わないよう verbatim で指示します。 {% endcomment %} {% verbatim %}
                                            <v-chip label color="grey lighten-4">{{label0}}</v-chip>
                                            <v-chip label color="grey lighten-4">{{label1}}</v-chip>
                                            <v-chip label color="grey lighten-4">{{label2}}</v-chip>
                                            {% endverbatim %}
                                        </v-col>
                                    </v-row>
                                    <v-row justify="center" dense>
                                        <v-col>
                                            {% verbatim %}
                                            <v-chip label color="grey lighten-4">{{label3}}</v-chip>
                                            <v-chip label color="grey lighten-4">{{label4}}</v-chip>
                                            <v-chip label color="grey lighten-4">{{label5}}</v-chip>
                                            {% endverbatim %}
                                        </v-col>
                                    </v-row>
                                    <v-row justify="center" dense>
                                        <v-col>
                                            {% verbatim %}
                                            <v-chip label color="grey lighten-4">{{label6}}</v-chip>
                                            <v-chip label color="grey lighten-4">{{label7}}</v-chip>
                                            <v-chip label color="grey lighten-4">{{label8}}</v-chip>
                                            {% endverbatim %}
                                        </v-col>
                                    </v-row>
                                </v-container>
                            </div>
                            <!-- 棋譜 -->
                            <div class="card-body">
                                <v-card class="mx-auto" max-width="300" tile>
                                    <v-subheader>棋譜</v-subheader>
                                    <v-list dense class="overflow-y-auto" max-height="200">
                                        <v-list-item-group color="primary">
                                            <v-list-item v-for="(item, i) in record" :key="i">
                                                <v-list-item-content>
                                                    <v-list-item-title v-text="item"></v-list-item-title>
                                                </v-list-item-content>
                                            </v-list-item>
                                        </v-list-item-group>
                                    </v-list>
                                </v-card>
                            </div>
                        </div>
                        <a href="{% url 'practice_vol1o0_rooms' %}" class="btn btn-default btn-sm">戻る</a>
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            var board = "{{ room.board|escapejs }}";
            var record = "{{ room.record|escapejs }}";

            let vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    label0: board[0],
                    label1: board[1],
                    label2: board[2],
                    label3: board[3],
                    label4: board[4],
                    label5: board[5],
                    label6: board[6],
                    label7: board[7],
                    label8: board[8],
                    record: [parseInt(record[0]) + 1, parseInt(record[1]) + 1, parseInt(record[2]) + 1, parseInt(record[3]) + 1, parseInt(record[4]) + 1, parseInt(record[5]) + 1, parseInt(record[6]) + 1, parseInt(record[7]) + 1, parseInt(record[8]) + 1],
                },
            });
        </script>
    </body>
</html>
<!-- EOF OA18o3o0g2o0 -->
```

## Step OA18o3o0g3o0 ビュー編集 - room/ver1o0 フォルダー

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 room
                │           └── 📂 read
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 room
                        └── 📂 ver1o0
👉                          └── 📄 __init__.py
```

```py
class RoomV():
    """OA18o2o0g5o0 対局部屋ビュー"""


    # ...略...


    # OA18o3o0g3o0 練習1.0巻 詳細ページ1.0版
    _path_of_read_page = "practice_vol1o0/room/read/ver1o0.html"
    #                     -------------------------------------
    #                     1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/room/read/ver1o0.html` を取得
    #                                          -------------------------------------


    # ...略...


    @staticmethod
    def render_read(request, id):
        """OA18o3o0g3o0 練習1.0巻 詳細ページ1.0版"""

        # 以下のファイルはあとで作ります
        from ..read.ver1o0 import render_read
        #    -------------        -----------
        #    1                    2
        # 1. `src1/apps1/practice_vol1o0/views/room/read/ver1o0.py`
        #                                           -----------
        # 2. `1.` に含まれる関数

        return render_read(request, id, RoomV._path_of_read_page)
```

## Step OA18o3o0g4o0 ビュー作成 - room/read/ver1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 room
                │           └── 📂 read
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 room
                        ├── 📂 read
👉                      │   └── 📄 ver1o0.py
                        └── 📂 ver1o0
                            └── 📄 __init__.py
```

```py
# BOF OA18o3o0g4o0

from django.shortcuts import render

# 部屋モデル
from apps1.practice_vol1o0.models.room.ver1o0 import Room
#          ---------------             ------        ----
#          11                          12            2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# ユーザー モデルヘルパー
from apps1.practice_vol1o0.models_helper.user.ver1o0 import MhUser
#          ---------------                    ------        ------
#          11                                 12            2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_read(request, room_pk, room_read_tp):
    """OA18o3o0g4o0 読取ページ

    Parameters
    ----------
    room_read_tp : str
        Template path
    """

    # idを指定してメンバーを１人取得
    room_resultset = Room.objects.filter(pk=room_pk)

    # 使いやすい形に変換します
    if len(room_resultset) < 1:
        room_dic = {
            "pk": room_pk,
            "name": "",
            "sente_id": "",
            "sente_name": "",
            "gote_id": "",
            "gote_name": "",
            "board": "",
            "record": "",
        }
    else:
        # 先頭の１件
        room = room_resultset[0]

        sente_id = room.sente_id
        gote_id = room.gote_id

        room_dic = {
            "pk": room.pk,
            "name": room.name,
            "sente_id": sente_id,
            "sente_name": MhUser.get_name_by_pk(sente_id),
            "gote_id": gote_id,
            "gote_name": MhUser.get_name_by_pk(gote_id),
            "board": room.board,
            "record": room.record,
        }

    context = {
        'room': room_dic,
    }
    return render(request, room_read_tp, context)

# EOF OA18o3o0g4o0
```

## ~~Step OA18o3o0g5o0~~

Merged to OA18o3o0g5o1o0  

## Step OA18o3o0g5o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_vol1o0                  # アプリケーション
    │           ├── 📂 templates
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 room
    │           │           └── 📂 read
    │           │               └── 📄 ver1o0.html
    │           └── 📂 views
    │               └── 📂 room
    │                   ├── 📂 read
    │                   │   └── 📄 ver1o0.py
    │                   └── 📂 ver1o0
    │                       └── 📄 __init__.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/rooms/read/ver1.0/<int:id>/,practice_vol1o0_rooms_read,"OA18o3o0g5o1o0 練習1.0巻 対局部屋の詳細1.0版",apps1.practice_vol1o0.views.room.ver1o0,RoomV,RoomVV1o0,render_read
```

## Step OA18o2o0g7o2o0 ルート編集 - コマンド打鍵

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

## Step OA18o3o0g6o0 Web画面へアクセス

👇 部屋番号は適宜変えてほしい  

📖 [http://localhost:8000/practice/vol1o0/rooms/read/ver1o0/1/](http://localhost:8000/practice/vol1o0/rooms/read/ver1o0/1/)  

## Step OA18o3o0g7o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

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
        │       │       └── 📂 room
        │       │           └── 📂 read
        │       │               └── 📄 ver1o0.html
        │       └── 📂 views
        │           └── 📂 room
        │               ├── 📂 read
        │               │   └── 📄 ver1o0.py
        │               └── 📂 ver1o0
        │                   └── 📄 __init__.py
        └── 📂 project1                          # プロジェクト
            └── 📄 urls_practice.py              # こちら
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/vol1.0/rooms/read/ver1o0/1/,OA18o3o0g7o0 練習1.0巻 対局部屋の詳細1.0版 Id=1
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでゲーム対局部屋を削除しよう！](https://qiita.com/muzudho1/items/172485842e7adfb749aa)  
