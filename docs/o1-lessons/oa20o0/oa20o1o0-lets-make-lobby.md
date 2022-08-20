# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/v1/lobby/)  

# 目標

対局できるまで待機しているロビー（待合室）を作る  

そこには 部屋や ユーザーを一覧するものとする  

## 詳細

画面設計:  

```plaintext
+------------------------------------------------------+
|　三 　ゲーム対局サーバー　　[自分のホームへ帰る]　        |
+------------------------------------------------------+
| ロビー（待合室）                                       |
| 部屋一覧                                              |
| ID  部屋名  盤面        棋譜        アクション          |
| --  ------  ---------  ---------  ---------           |
|  3  Lion    XOXOXOXOX  012345678  [観る]              |
|                                                       |
| アクティブ ユーザー一覧                                 |
| ID  参加者名    アクティブか  最終ログイン               |
| --  ----------  ----------  -----------               |
|  1  kifuwarabe  true        2022-07-06T14:11:25.690Z  |
+------------------------------------------------------+
```

👆 免責: `自分のホームへ帰る` ボタンはまだ実装していません  

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

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 room
    │   │   │           └── 📄 v1o0.py
    │   │   ├── 📂 tic_tac_toe_v1        # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2        # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       ├── 📂 gui
    │   │       │       └── 📂 think
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
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
    ├── 📂 src2_local                   # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# 手順

## Step OA20o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA20o1o0g2o0 画面作成 - lobby/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 lobby
👉                          └── 📄 v1o0.html
```

```html
{# OA20o1o0g2o0 #}
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
        <title>ロビー（待合室）</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <!-- v-app-bar に app プロパティを指定しないなら、背景画像を付けてほしい -->
                <v-app-bar app dense elevation="4">
                    <v-app-bar-nav-icon></v-app-bar-nav-icon>
                    <v-toolbar-title>ゲーム対局サーバー</v-toolbar-title>
                    <v-spacer></v-spacer>
                    <v-btn class="my-4" color="primary" :href="createPathOfHome()">自分のホームへ帰る</v-btn>
                </v-app-bar>
                <v-main>
                    <v-container>
                        <h2>ロビー（待合室）</h2>
                        <h3>部屋一覧</h3>
                        <v-simple-table>
                            <template v-slot:default>
                                <thead>
                                    <tr>
                                        <th>ID</th>
                                        <th>部屋名</th>
                                        <th>盤面</th>
                                        <th>棋譜</th>
                                        <th>アクション</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="room in vu_roomDic" :key="room.pk">
                                        {% comment %} Vue で二重波括弧（braces）は変数の展開に使っていることから、 Python のテンプレートに二重波括弧を変数の展開に使わないよう verbatim で指示します。 {% endcomment %} {% verbatim %}
                                        <td>{{ room.pk }}</td>
                                        <td>{{ room.name }}</td>
                                        <td>{{ room.board }}</td>
                                        <td>{{ room.record }}</td>
                                        <td><v-btn :href="createPathOfRoomsRead(room.pk)">観る</v-btn></td>
                                        {% endverbatim %}
                                    </tr>
                                </tbody>
                            </template>
                        </v-simple-table>
                    </v-container>
                    <v-container>
                        <h3>アクティブ ユーザー一覧</h3>
                        <v-simple-table>
                            <template v-slot:default>
                                <thead>
                                    <tr>
                                        <th>ID</th>
                                        <th>参加者名</th>
                                        <th>アクティブか</th>
                                        <th>最終ログイン</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="user in vu_userDoc" :key="user.pk">
                                        {% comment %} Vue で二重波括弧（braces）は変数の展開に使っていることから、 Python のテンプレートに二重波括弧を変数の展開に使わないよう verbatim で指示します。 {% endcomment %} {% verbatim %}
                                        <td>{{ user.pk }}</td>
                                        <td>{{ user.username }}</td>
                                        <td>{{ user.is_active }}</td>
                                        <td>{{ user.last_login }}</td>
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
            let vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // "vu_" は 「vue1.dataのメンバー」 の目印
                    vu_roomDic: JSON.parse("{{ dj_room_dic|escapejs }}"),
                    vu_userDoc: JSON.parse("{{ dj_user_dic|escapejs }}"),

                    vu_pathOfHome: "{{ dj_path_of_home }}",
                    vu_pathOfRoomsRead: "{{ dj_path_of_rooms_read }}",
                },
                methods: {
                    createPathOfHome() {
                        let url = `${location.protocol}//${location.host}${this.vu_pathOfHome}`;
                        //          --------------------  ---------------]---------------------
                        //          1                     2               3
                        // 1. protocol
                        // 2. host
                        // 3. path
                        console.log(`room url=[${url}]`);
                        return url;
                    },
                    createPathOfRoomsRead(roomId) {
                        let url = `${location.protocol}//${location.host}${this.vu_pathOfRoomsRead}${roomId}`;
                        //          --------------------  ---------------]-----------------------------------
                        //          1                     2               3
                        // 1. protocol
                        // 2. host
                        // 3. path
                        console.log(`room url=[${url}]`);
                        return url;
                    },
                },
            });
        </script>
    </body>
</html>
```

## Step OA20o1o0g3o0 モデルヘルパー作成 - room/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 room
                │       └── 📂 v1o0
👉              │           └── 📄 __init__.py
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 lobby
                            └── 📄 v1o0.html
```

```py
class MhRoom():
    """OA20o1o0g3o0 部屋モデルヘルパー"""

    # 以下のファイルはあとで作ります
    from .mh_get_all_rooms_as_dic import get_all_rooms_as_dic
    #    ------------------------        --------------------
    #    1                               2
    # 1. `src1/apps1/practice_v1/model_helper/room/v1o0/mh_get_all_rooms_as_dic.py`
    #                                                   -----------------------
    # 2. `1.` に含まれる関数
```

## Step OA20o1o0g4o0 モデルヘルパー作成 - room/v1o0/mh_get_all_rooms_as_dic.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 room
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
👉              │           └── 📄 mh_get_all_rooms_as_dic.py
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 lobby
                            └── 📄 v1o0.html
```

```py
# 部屋モデル
from apps1.practice_v1.models.room.v1o0 import Room
#          -----------             ----        ----
#          11                      12          2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def get_all_rooms_as_dic():
    """OA20o1o0g4o0 全ての対局部屋をディクショナリー構造で取得"""

    room_resultset = Room.objects.all().order_by('id')

    # 使いやすい形に変換します
    room_dic = dict()
    for room in room_resultset:

        # Example:
        # room: {'model': 'webapp1.room', 'pk': 2, 'fields': {'name': 'Elephant', 'board': 'XOXOXOXOX', 'record': '012345678'}}

        room_dic[room.pk] = {
            "pk": room.pk,
            "name": room.name,
            "board": room.board,
            "record": room.record,
        }

    return room_dic
```

## Step OA20o1o0g5o0 ビュー作成 - lobby/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 room
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_all_rooms_as_dic.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 lobby
                │           └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 lobby
                        └── 📂 v1o0
👉                          └── 📄 __init__.py
```

```py
class LobbyV():
    """OA20o1o0g5o0 ロビー ビュー"""

    # 一覧ページ
    _path_of_lobby_page = "practice_v1/lobby/v1o0.html"
    #                      ---------------------------
    #                      1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/lobby/v1o0.html` を取得
    #                                      ---------------------------

    @staticmethod
    def render_lobby(request):
        """描画 - ロビー"""

        # 以下のファイルはあとで作ります
        from .v_lobby import render_lobby
        #    --------        ------------
        #    1               2
        # 1. `src1/apps1/practice_v1/views/lobby/v1o0/v_lobby.py`
        #                                             -------
        # 2. `1.` に含まれる関数

        return render_lobby(request, LobbyV._path_of_lobby_page)
```

## Step OA20o1o0g6o0 ビュー作成 - lobby/v1o0/v_lobby.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 room
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_all_rooms_as_dic.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 lobby
                │           └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 lobby
                        └── 📂 v1o0
                            ├── 📄 __init__.py
👉                          └── 📄 v_lobby.py
```

```py
# BOF OA20o1o0g6o0

import json
from django.shortcuts import render

# 部屋モデルヘルパー
from apps1.practice_v1.models_helper.room.v1o0 import MhRoom
#          -----------                    ----        ------
#          11                             12          2
#    -----------------------------------------
#    10
# 11, 12. ディレクトリー
# 10. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


# セッション モデルヘルパー
from apps1.practice_v1.models_helper.session.v1o0 import MhSession
#          -----------                    -------        ---------
#          11                             12             2
#    --------------------------------------------
#    10
# 11, 12. ディレクトリー
# 10. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_lobby(request, lobby_tp):
    """OA20o1o0g6o0 ロビー（待合室）

    Parameters
    ----------
    lobby_tp : str
        Template path
    """

    # 部屋の一覧
    room_dic = MhRoom.get_all_rooms_as_dic()

    # ユーザーの一覧
    user_dic = MhSession.get_all_logged_in_users()

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        'dj_room_dic': json.dumps(room_dic),
        'dj_user_dic': json.dumps(user_dic),
        # FIXME URL を urls.py で変更しても、こちらに反映されないが、どうするか？
        "dj_path_of_home": "/practice/v1/my/",
        "dj_path_of_rooms_read": "/practice/v1/rooms/read/",
    }

    return render(request, lobby_tp, context)

# EOF OA20o1o0g6o0
```

## Step OA20o1o0g7o0 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 room
        │       │       └── 📂 v1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 mh_get_all_rooms_as_dic.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 lobby
        │       │           └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 lobby
        │               └── 📂 v1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_lobby.py
        └── 📂 project1                          # プロジェクト
👉          └── 📄 urls_practice.py
```

```py
# ...略...


# OA20o1o0g7o0 ロビー ビュー
from apps1.practice_v1.views.lobby.v1o0 import LobbyV
#          -----------             ----        ------
#          11                      12          2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [
    # ...略...


    # OA20o1o0g7o0 ロビー
    path('practice/v1/lobby/', LobbyV.render_lobby, name='practice_v1_lobby'),
    #     ------------------   -------------------        -----------------
    #     1                    2                          3
    # 1. 例えば `http://example.com/practice/v1/lobby/` のような URL のパスの部分
    #                              ------------------
    #    数字列は `2.` の関数の引数 id で取得できる
    # 2. LobbyV クラスの render_lobby 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_lobby' %} のような形でURLを取得するのに使える
]
```

## Step OA20o1o0g8o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/lobby/](http://localhost:8000/practice/v1/lobby/)  

## Step OA20o1o0g9o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 room
        │       │       └── 📂 v1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 mh_get_all_rooms_as_dic.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 lobby
        │       │           └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 lobby
        │               └── 📂 v1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_lobby.py
        └── 📂 project1                          # プロジェクト
👉          └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/lobby/,ロビー
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoで自動リロードするページを作ろう！](https://qiita.com/muzudho1/items/8df599dc0e0acb25f649)  

# 関連する記事

📖 [djangoでログイン状態を判定する機能](https://techpr.info/python/django-login-judge/)  
📖 [DjangoのUserモデルを拡張する方法](https://hodalog.com/how-to-extend-django-user-model/)  
