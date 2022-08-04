# サンプルを見る

📖 [http://tic.warabenture.com:8000/practice/v1/rooms/](http://tic.warabenture.com:8000/practice/v1/rooms/)  

# 目的

ゲームルームを一覧したい  

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

# はじめに

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key              | Value                                     |
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
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 room
    │   │   │           └── 📄 v1o0.py
    │   │   ├── 📂 tic_tac_toe_v1           # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2           # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       ├── 📂 gui
    │   │       │       │   ├── 📂 connection
    │   │       │       │   │   └── 📄 v1o0.js
    │   │       │       │   ├── 📂 incoming_messages
    │   │       │       │   │   └── 📄 v1o0.js
    │   │       │       │   └── 📂 outgoing_messages
    │   │       │       │       └── 📄 v1o0.js
    │   │       │       └── 📂 think
    │   │       │           ├── 📂 concepts
    │   │       │           │   └── 📄 v1o0.js
    │   │       │           ├── 📂 engine
    │   │       │           │   └── 📄 v1o0.js
    │   │       │           ├── 📂 judge_ctrl
    │   │       │           │   └── 📄 v1o0.js
    │   │       │           ├── 📂 position
    │   │       │           │   └── 📄 v1o0.js
    │   │       │           ├── 📂 things
    │   │       │           │   └── 📄 v1o0.js
    │   │       │           └── 📂 user_ctrl
    │   │       │               └── 📄 v1o0.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       ├── 📂 gui
    │   │       │       │   ├── 📂 match_application
    │   │       │       │   │   └── 📄 v1o0.html
    │   │       │       │   └── 📂 playing
    │   │       │       │       ├── 📄 v1o0.html
    │   │       │       │       └── 📄 v1o1o0.html.txt
    │   │       │       └── 📂 think
    │   │       │           └── 📂 engine_manual
    │   │       │               └── 📄 v1o0.html
    │   │       ├── 📂 views
    │   │       │   ├── 📂 gui
    │   │       │   │   ├── 📂 match_application
    │   │       │   │   │   └── 📂 v1o0
    │   │       │   │   │       ├── 📄 __init__.py
    │   │       │   │   │       └── 📄 v_render.py
    │   │       │   │   └── 📂 playing
    │   │       │   │       └── 📂 v1o0
    │   │       │   │           ├── 📄 __init__.py
    │   │       │   │           └── 📄 v_render.py
    │   │       │   └── 📂 think
    │   │       │       └── 📂 engine_manual
    │   │       │           └── 📂 v1o0
    │   │       │               ├── 📄 __init__.py
    │   │       │               └── 📄 v_render.py
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
    ├── 📂 src2_local                      # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# Step OA18o2o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step OA18o2o0g2o0 画面作成 - list.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 room
                            └── 📂 list
👉                              └── 📄 v1o0.html
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

# Step OA18o2o0g3o0 モデルヘルパー モジュール編集 - user/v1o0 フォルダー

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 v1o0
👉              │           └── 📄 __init__.py
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 room
                            └── 📂 list
                                └── 📄 v1o0.html
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
    # 1. `src1/apps1/practice_v1/model_helper/user/v1o0/mh_get_name_by_pk.py`
    #                                                   -----------------
    # 2. `1.` に含まれる関数
```

# Step OA18o2o0g4o0 モデルヘルパー モジュール編集 - mh_get_name_by_pk ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
👉              │           └── 📄 mh_get_name_by_pk.py
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 room
                            └── 📂 list
                                └── 📄 v1o0.html
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

# Step OA18o2o0g5o0 ビュー作成 - room フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_name_by_pk.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 room
                │           └── 📂 list
                │               └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 room
                        └── 📂 v1o0
👉                          └── 📄 __init__.py
```

```py
class RoomV():
    """OA18o2o0g5o0 対局部屋ビュー"""

    # OA18o2o0g5o0 一覧ページ
    _path_of_list_page = "practice_v1/room/list/v1o0.html"
    #                     -------------------------------
    #                     1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/room/list/v1o0.html` を取得
    #                                      -------------------------------

    @staticmethod
    def render_list(request):
        """OA18o2o0g5o0 描画 - 一覧"""

        # 以下のファイルはあとで作ります
        from ..list.v1o0 import render_list
        #    -----------        -----------
        #    1                  2
        # 1. `src1/apps1/practice_v1/views/room/list/v1o0.py`
        #                                       ---------
        # 2. `1.` に含まれる関数

        return render_list(request, RoomV._path_of_list_page)
```

# Step OA18o2o0g6o0 ビュー作成 - room/list/v1o0 ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_name_by_pk.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 room
                │           └── 📂 list
                │               └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 room
                        ├── 📂 list
👉                      │   └── 📄 v1o0.py
                        └── 📂 v1o0
                            └── 📄 __init__.py
```

```py
import json
from django.shortcuts import render

# 部屋モデル
from apps1.practice_v1.models.room.v1o0 import Room
#          -----------             ----        ----
#          11                      12          2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# ユーザー モデルヘルパー
from apps1.practice_v1.models_helper.user.v1o0 import MhUser
#          -----------                    ----        ------
#          11                             12          2
#    -----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_list(request, lp_room_list):
    """OA18o2o0g6o0 一覧ページ

    Parameters
    ----------
    lp_room_list : str
        ローカルパス
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
        "dj_read_room_path": "/practice/v1/rooms/read/",
    }
    return render(request, lp_room_list, context)
```

# Step OA18o2o0g7o0 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 user
        │       │       └── 📂 v1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 mh_get_name_by_pk.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 room
        │       │           └── 📂 list
        │       │               └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 room
        │               ├── 📂 list
        │               │   └── 📄 v1o0.py
        │               └── 📂 v1o0
        │                   └── 📄 __init__.py
        └── 📂 project1                          # プロジェクト
👉          └── 📄 urls_practice.py              # こちら
```

```py
# ...略...


# OA18o2o0g7o0 部屋ビュー v1.0
from apps1.practice_v1.views.room.v1o0 import RoomV as RoomVV1o0
#          -----------            ----        -----    ---------
#          11                     12          2        3
#    ---------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [
    # ...略...


    # OA18o2o0g7o0 対局部屋の一覧
    path('practice/v1/rooms/', RoomVV1o0.render_list, name='practice_v1_rooms'),
    #     ------------------   ---------------------        -----------------
    #     1                    2                            3
    # 1. 例えば `http://example.com/practice/v1/rooms/` のような URL のパスの部分
    #                              ------------------
    # 2. RoomVV1o0 クラスの render_list 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_rooms' %} のような形でURLを取得するのに使える
]
```

# Step OA18o2o0g8o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/rooms/](http://localhost:8000/practice/v1/rooms/)  

# Step OA18o2o0g9o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 user
        │       │       └── 📂 v1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 mh_get_name_by_pk.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 room
        │       │           └── 📂 list
        │       │               └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 room
        │               ├── 📂 list
        │               │   └── 📄 v1o0.py
        │               └── 📂 v1o0
        │                   └── 📄 __init__.py
        └── 📂 project1                          # プロジェクト
            └── 📄 urls_practice.py              # こちら
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/rooms/,対局部屋の一覧
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでゲーム対局部屋を読取しよう！](https://qiita.com/muzudho1/items/a39bea2f098951292916)  

# 参考にした記事

## Userオブジェクト

📖 [Get user object using userid in django](https://stackoverflow.com/questions/19805129/get-user-object-using-userid-in-django)  
