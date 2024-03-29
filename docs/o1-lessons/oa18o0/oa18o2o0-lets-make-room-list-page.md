# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1.0/rooms/ver1.0/)  

# 目標

ゲームルームを一覧したい  

## 詳細

表示例:  

```plaintext
一覧表示
ID    部屋名        先手Id  先手名  後手Id  後手名  盤面       棋譜       アクション
----  -----------  ------  -----  ------  -----  ---------  ---------  ---------
1     Elephant          1  aaaa        2  bbbb   XOXOXOXOX  012345678  [観る]
2     Giraffe           3  cccc        4  dddd   XOXOXOXOX  012345678  [観る]
3     Lion              5  eeee        6  ffff   XOXOXOXOX  012345678  [観る]
```

👆 `観る` ボタンを置いているが、クリックした先のページはまだ無い。あとで作る  

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
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_vol2o0
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

## Step [OA18o2o0g1o0] Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step [OA18o2o0g2o0] 画面作成 - list.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_vol1o0          # アプリケーションと同名
                        └── 📂 room
                            └── 📂 list
👉                              └── 📄 ver1o0.html
```

```html
{# OA18o2o0g2o0 #}
<!-- -->
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
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>部屋一覧</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container>
                        <h3>部屋一覧</h3>
                    </v-container>
                    <v-container>
                        <v-simple-table>
                            <template v-slot:default>
                                <thead>
                                    <tr>
                                        <th>ID</th>
                                        <th>部屋名</th>
                                        <th>先手Id</th>
                                        <th>先手名</th>
                                        <th>後手Id</th>
                                        <th>後手名</th>
                                        <th>盤面</th>
                                        <th>棋譜</th>
                                        <th>アクション</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="room in vu_roomArray" :key="room.id">
                                        {% comment %} Vue で二重波括弧（braces）は変数の展開に使っていることから、 Python のテンプレートに二重波括弧を変数の展開に使わないよう verbatim で指示します。 {% endcomment %}
                                        <!--  -->
                                        {% verbatim %}
                                        <td>{{ room.id }}</td>
                                        <td>{{ room.name }}</td>
                                        <td>{{ room.sente_id }}</td>
                                        <td>{{ room.sente_name }}</td>
                                        <td>{{ room.gote_id }}</td>
                                        <td>{{ room.gote_name }}</td>
                                        <td>{{ room.board }}</td>
                                        <td>{{ room.record }}</td>
                                        <td><v-btn :href="createRoomsReadPath(room.id)">観る</v-btn></td>
                                        {% endverbatim %}
                                    </tr>
                                </tbody>
                            </template>
                        </v-simple-table>
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            // "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
            var roomArray = JSON.parse("{{ dj_room_array|escapejs }}");
            // var rooms_array_str1 = JSON.stringify(roomArray, null, "    ");
            // console.log(`rooms_array_str1=${rooms_array_str1}`);

            let vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // "vu_" は 「vue1.dataのメンバー」 の目印
                    vu_roomArray: roomArray,
                    vu_readRoomPath: "{{ dj_read_room_path }}",
                },
                methods: {
                    /**
                     * vue1.createRoomsReadPath() のように使えます
                     */
                    createRoomsReadPath(id) {
                        let url = `${location.protocol}//${location.host}${this.vu_readRoomPath}${id}`;
                        //         --------------------  ---------------]----------------------------
                        //         1                     2               3
                        // 1. protocol
                        // 2. host
                        // 3. path
                        console.log(`read-page url=[${url}]`);
                        return url;
                    },
                },
            });
        </script>
    </body>
</html>
```

## Step [OA18o2o0g3o0] モデルヘルパー モジュール編集 - user/ver1o0 フォルダー

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 ver1o0
👉              │           └── 📄 __init__.py
                └── 📂 templates
                    └── 📂 practice_vol1o0
                        └── 📂 room
                            └── 📂 list
                                └── 📄 ver1o0.html
```

```py
class MhUser():
    """O9o1o0g3o0 ユーザー モデルヘルパー"""


    # ...略...


    # * 以下を追加
    # OA18o2o0g3o0 以下のファイルはあとで作ります
    from .mh_get_name_by_pk import get_name_by_pk
    #    ------------------        --------------
    #    1                         2
    # 1. `src1/apps1/practice_vol1o0/model_helper/user/ver1o0/mh_get_name_by_pk.py`
    #                                                         -----------------
    # 2. `1.` に含まれる関数
```

## Step [OA18o2o0g4o0] モデルヘルパー モジュール編集 - mh_get_name_by_pk ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 ver1o0
                │           ├── 📄 __init__.py
👉              │           └── 📄 mh_get_name_by_pk.py
                └── 📂 templates
                    └── 📂 practice_vol1o0
                        └── 📂 room
                            └── 📂 list
                                └── 📄 ver1o0.html
```

```py
from django.contrib.auth.models import User


def get_name_by_pk(id):
    """OA18o2o0g4o0 主キーを使って、ユーザーを絞りこみます"""

    try:
        user = User.objects.get(pk=id)
        return user.username

    except User.DoesNotExist:
        # ユーザーが存在しなかったときに代わりに出す文字列
        return "#unknown#"
```

## Step [OA18o2o0g5o0] ビュー作成 - room フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 ver1o0
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_name_by_pk.py
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 room
                │           └── 📂 list
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 room
                        └── 📂 ver1o0
👉                          └── 📄 __init__.py
```

```py
class RoomV():
    """OA18o2o0g5o0 対局部屋ビュー"""

    # OA18o2o0g5o0 練習1.0巻 一覧ページ1.0版
    _path_of_list_page = "practice_vol1o0/room/list/ver1o0.html"
    #                     -------------------------------------
    #                     1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/room/list/ver1o0.html` を取得
    #                                          -------------------------------------

    @staticmethod
    def render_list(request):
        """OA18o2o0g5o0 練習1.0巻 一覧ページ1.0版"""

        # 以下のファイルはあとで作ります
        from ..list.ver1o0 import render_list
        #    -------------        -----------
        #    1                    2
        # 1. `src1/apps1/practice_vol1o0/views/room/list/ver1o0.py`
        #                                           -----------
        # 2. `1.` に含まれる関数

        return render_list(request, RoomV._path_of_list_page)
```

## Step [OA18o2o0g6o0] ビュー作成 - room/list/ver1o0 ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 ver1o0
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_name_by_pk.py
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 room
                │           └── 📂 list
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 room
                        ├── 📂 list
👉                      │   └── 📄 ver1o0.py
                        └── 📂 ver1o0
                            └── 📄 __init__.py
```

```py
# BOF OA18o2o0g6o0

import json
from django.shortcuts import render

# 練習1.0巻 部屋モデル1.0版
from apps1.practice_vol1o0.models.room.ver1o0 import Room
#          ---------------             ------        ----
#          11                          12            2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 練習1.0巻 ユーザー モデルヘルパー1.0版
from apps1.practice_vol1o0.models_helper.user.ver1o0 import MhUser
#          ---------------                    ------        ------
#          11                                 12            2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_list(request, room_list_tp):
    """OA18o2o0g6o0 一覧ページ

    Parameters
    ----------
    room_list_tp : str
        Template path
    """

    room_resultset = Room.objects.all().order_by('id')
    # print(f"room_table_doc={json.dumps(room_table_doc, indent=4)}")
    """
    # Example
    room_table_doc=
    [
        {
            "model": "webapp1.room",
            "pk": 2,
            "fields": {
                "name": "Elephant",
                "sente_id": 1,
                "gote_id": 2,
                "board": "XOXOXOXOX",
                "record": "012345678"
            }
        },
        ...中略...
    ]
    """

    # 使いやすい形に変換します
    room_list = []

    for room in room_resultset:
        sente_id = room.sente_id
        gote_id = room.gote_id

        room_list.append(
            {
                "id": room.pk,
                "name": room.name,
                "sente_id": sente_id,
                "sente_name": MhUser.get_name_by_pk(sente_id),
                "gote_id": gote_id,
                "gote_name": MhUser.get_name_by_pk(gote_id),
                "board": room.board,
                "record": room.record,
            }
        )

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        # Vue には、 JSONオブジェクト を渡すのではなく、 JSON文字列 を渡します
        "dj_room_array": json.dumps(room_list),
        # FIXME URL を urls.py で変更しても、こちらに反映されないが、どうするか？
        "dj_read_room_path": "/practice/vol1.0/rooms/read/ver1.0/",
    }
    return render(request, room_list_tp, context)

# EOF OA18o2o0g6o0
```

## ~~Step [OA18o2o0g7o0]~~

Merged to OA18o2o0g7o1o0  

## Step [OA18o2o0g7o1o0] ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_vol1o0                      # アプリケーション
    │           ├── 📂 models_helper
    │           │   └── 📂 user
    │           │       └── 📂 ver1o0
    │           │           ├── 📄 __init__.py
    │           │           └── 📄 mh_get_name_by_pk.py
    │           ├── 📂 templates
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 room
    │           │           └── 📂 list
    │           │               └── 📄 ver1o0.html
    │           └── 📂 views
    │               └── 📂 room
    │                   ├── 📂 list
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


../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/rooms/ver1.0/,practice_vol1o0_rooms,"OA18o2o0g7o1o0 練習1.0巻 対局部屋の一覧1.0版",apps1.practice_vol1o0.views.room.ver1o0,RoomV,RoomVV1o0,render_list
```

## Step [OA18o2o0g7o2o0] ルート編集 - コマンド打鍵

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

## Step [OA18o2o0g8o0] Web画面へアクセス

📖 [http://localhost:8000/practice/vol1.0/rooms/ver1.0/](http://localhost:8000/practice/vol1.0/rooms/ver1.0/)  

## Step [OA18o2o0g9o0] ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_vol1o0                      # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 user
        │       │       └── 📂 ver1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 mh_get_name_by_pk.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 room
        │       │           └── 📂 list
        │       │               └── 📄 ver1o0.html
        │       └── 📂 views
        │           └── 📂 room
        │               ├── 📂 list
        │               │   └── 📄 ver1o0.py
        │               └── 📂 ver1o0
        │                   └── 📄 __init__.py
        └── 📂 project1                          # プロジェクト
            └── 📄 urls_practice.py              # こちら
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/vol1.0/rooms/ver1.0/,OA18o2o0g9o0 練習1.0巻 対局部屋の一覧1.0版
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでゲーム対局部屋を読取しよう！](https://qiita.com/muzudho1/items/a39bea2f098951292916)  

# 参考にした記事

## Userオブジェクト

📖 [Get user object using userid in django](https://stackoverflow.com/questions/19805129/get-user-object-using-userid-in-django)  
