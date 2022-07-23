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

この記事は LessonO[1 0] から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    ├── 📂 host_local1                   # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    ├── 📂 host1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 o2o1
    │   │   │           └── 📄 m_room.py
    │   │   ├── 📂 tic_tac_toe_v1        # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2        # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o2o1
    │   │       │           └── 📂 think
    │   │       │               ├── 📄 concepts.js
    │   │       │               ├── 📄 engine.js
    │   │       │               ├── 📄 judge_ctrl.js
    │   │       │               ├── 📄 position.js
    │   │       │               ├── 📄 things.js
    │   │       │               └── 📄 user_ctrl.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o2o1
    │   │       │           └── 📂 think
    │   │       │               └── 📄 engine_manual.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 o2o1
    │   │       │       └── 📂 think
    │   │       │           └── 📂 engine_manual
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
    └── 📄 .gitignore
```

# Step O[1 0] Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step O[2 0] 画面作成 - list.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 o2o1
                            └── 📂 room
👉                              └── 📄 list.html
```

```html
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
endcomment %}
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

# Step O[3 0] モデルヘルパー モジュール編集 - mh_user フォルダー

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 o2o1
                │       └── 📂 mh_user
👉              │           └── 📄 __init__.py
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 o2o1
                            └── 📂 room
                                └── 📄 list.html
```

```py
class MhUser():
    """ユーザー モデルヘルパー"""


    # ...略...


    # * 以下を追加
    # 以下のファイルはあとで作ります
    from .mh_get_name_by_pk import get_name_by_pk
    #    ------------------        --------------
    #    1                         2
    # 1. `host1/apps1/practice_v1/model_helper/o2o1/mh_user/mh_get_name_by_pk.py`
    #                                                       -----------------
    # 2. `1.` に含まれる関数
```

# Step O[4 0] モデルヘルパー モジュール編集 - mh_get_name_by_pk ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 o2o1
                │       └── 📂 mh_user
                │           ├── 📄 __init__.py
👉              │           └── 📄 mh_get_name_by_pk.py
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 o2o1
                            └── 📂 room
                                └── 📄 list.html
```

```py
from django.contrib.auth.models import User


@staticmethod
def get_name_by_pk(id):
    """主キーを使って、ユーザーを絞りこみます"""

    user = User.objects.get(pk=id)

    if user is None:
        # 該当なしは空文字列と決めておきます
        return ""

    return user.username
```

# Step O[5 0] ビュー モジュール作成 - room フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 o2o1
                │       └── 📂 mh_user
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_name_by_pk.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o2o1
                │           └── 📂 room
                │               └── 📄 list.html
                └── 📂 views
                    └── 📂 o2o1
                        └── 📂 room
👉                          └── 📄 __init__.py
```

```py
class RoomV():
    """対局部屋ビュー"""

    # 一覧ページ
    _path_of_list_page = "practice_v1/o2o1/room/list.html"
    #                     -------------------------------
    #                     1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o2o1/room/list.html` を取得
    #                                       -------------------------------

    @staticmethod
    def render_list(request):
        """描画 - 一覧"""

        # 以下のファイルはあとで作ります
        from .v_list import render_list
        #    -------        -----------
        #    1              2
        # 1. `host1/apps1/practice_v1/views/o2o1/room/v_list.py`
        #                                             ------
        # 2. `1.` に含まれる関数

        return render_list(request, RoomV._path_of_list_page)
```

# Step O[6 0] ビュー モジュール作成 - v_list ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 o2o1
                │       └── 📂 mh_user
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_name_by_pk.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o2o1
                │           └── 📂 room
                │               └── 📄 list.html
                └── 📂 views
                    └── 📂 o2o1
                        └── 📂 room
                            ├── 📄 __init__.py
👉                          └── 📄 v_list.py
```

```py
import json
from django.shortcuts import render

from apps1.practice_v1.models.o2o1.m_room import Room
#          -----------             ------        ----
#          1.1                     1.2           2
#    ------------------------------------
#    1
# 1, 1.2 ディレクトリー
# 1.1 アプリケーション
# 2. `1.2` に含まれる __init__.py ファイルにさらに含まれるクラス

# ユーザー モデルヘルパー
from apps1.practice_v1.models_helper.o2o1.mh_user import MhUser
#          -----------                    -------        ------
#          11                             12             2
#    --------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


@staticmethod
def render_list(request, path_of_list_page):
    """一覧ページ"""

    room_resultset = Room.objects.all().order_by('id')
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
    # print(f"context={context}")

    return render(request, path_of_list_page, context)
```

# Step O[7 0] ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 o2o1
        │       │       └── 📂 mh_user
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 mh_get_name_by_pk.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o2o1
        │       │           └── 📂 room
        │       │               └── 📄 list.html
        │       └── 📂 views
        │           └── 📂 o2o1
        │               └── 📂 room
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_list.py
        └── 📂 project1                          # プロジェクト
👉          └── 📄 urls_practice.py              # こちら
```

```py
# ...略...


# 部屋ビュー
from apps1.practice_v1.views.o2o1.room import RoomV
#          -----------            ----        -----
#          11                     12          2
#    ---------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [
    # ...略...


    # 対局部屋の一覧
    path('practice/v1/rooms/', RoomV.render_list, name='practice_v1_rooms'),
    #     ------------------   -----------------        -----------------
    #     1                    2                        3
    # 1. 例えば `http://example.com/practice/v1/rooms/` のような URL のパスの部分
    #                              ------------------
    # 2. RoomV クラスの render_list メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_rooms' %} のような形でURLを取得するのに使える
]
```

# Step O[8 0] Web画面へアクセス

📖 [http://localhost:8000/practice/v1/rooms/](http://localhost:8000/practice/v1/rooms/)  

# Step O[9 0] ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 o2o1
        │       │       └── 📂 mh_user
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 mh_get_name_by_pk.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o2o1
        │       │           └── 📂 room
        │       │               └── 📄 list.html
        │       └── 📂 views
        │           └── 📂 o2o1
        │               └── 📂 room
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_list.py
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
