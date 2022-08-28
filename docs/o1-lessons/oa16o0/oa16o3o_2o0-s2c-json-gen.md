# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/tic-tac-toe/vol2.0/s2c-json-gen/ver1.0/)  

# 目標

〇×ゲーム（Tic tac toe）の通信対戦をしたい  

いきなり作るのは難しいので その前に、サーバーからクライアントへ送るメッセージを取り決めておく  

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

以下、参考にした元記事は 📖[Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/) だ。  
わたしの記事は単に **やってみた** ぐらいの位置づけだ  

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1                            # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 accounts_vol1o0    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_vol1o0              # アプリケーション
    │   │   ├── 📂 tic_tac_toe_vol1o0           # アプリケーション
    │   │   └── 📂 tic_tac_toe_vol2o0           # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_vol2o0
    │   │       │       └── 📂 think
    │   │       │           ├── 📂 concepts
    │   │       │           │   └── 📄 ver1o0.js
    │   │       │           ├── 📂 engine
    │   │       │           │   └── 📄 ver1o0.js
    │   │       │           ├── 📂 judge_ctrl
    │   │       │           │   └── 📄 ver1o0.js
    │   │       │           ├── 📂 position
    │   │       │           │   └── 📄 ver1o0.js
    │   │       │           ├── 📂 things
    │   │       │           │   └── 📄 ver1o0.js
    │   │       │           └── 📂 user_ctrl
    │   │       │               └── 📄 ver1o0.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_vol2o0
    │   │       │       └── 📂 think
    │   │       │           └── 📂 engine_manual
    │   │       │               └── 📄 ver1o0.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 think
    │   │       │       └── 📂 engine_manual
    │   │       │           └── 📂 ver1o0
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

## Step. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA16o3o_2o0g1o_1o0 メッセージ作成 - msg/s2c_json_gen/messages/end/ver1o0/__init__.py ファイル

Separated from OA16o3o_2o0g1o0  

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                └── 📂 views
                    └── 📂 msg
                        └── 📂 s2c_json_gen
                            └── 📂 messages
                                └── 📂 end
                                    └── 📂 ver1o0
👉                                      └── 📄 __init__.py
```

```py
# BOF OA16o3o_2o0g1o_1o0

class EndS2cMessage:
    def __init__(self, args):
        """設定"""
        self._winner = args["player1"]

    def asDict(self):
        """Dict形式で取得"""
        return {
            'type': 'send_message',  # type属性は必須
            's2c_type': "S2C_End",
            's2c_winner': self._winner,
        }

# EOF OA16o3o_2o0g1o_1o0
```

## Step OA16o3o_2o0g1o_2o0 メッセージ作成 - msg/s2c_json_gen/messages/moved/ver1o0/__init__.py ファイル

Separated from OA16o3o_2o0g1o0  

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                └── 📂 views
                    └── 📂 msg
                        └── 📂 s2c_json_gen
                            └── 📂 messages
                                ├── 📂 end
                                │   └── 📂 ver1o0
                                │       └── 📄 __init__.py
                                └── 📂 moved
                                    └── 📂 ver1o0
👉                                      └── 📄 __init__.py
```

```py
# BOF OA16o3o_2o0g1o_2o0

class MovedS2cMessage:
    def __init__(self, args):
        """設定"""
        self._sq = args["sq1"]
        self._pieceMoved = args["piece1"]

    def asDict(self):
        """Dict形式で取得"""
        return {
            'type': 'send_message',  # type属性は必須
            's2c_type': 'S2C_Moved',
            's2c_sq': self._sq,
            's2c_pieceMoved': self._pieceMoved,
        }

# EOF OA16o3o_2o0g1o_2o0
```

## Step OA16o3o_2o0g1o_3o0 メッセージ作成 - msg/s2c_json_gen/messages/start/ver1o0/__init__.py ファイル

Separated from OA16o3o_2o0g1o0  

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                └── 📂 views
                    └── 📂 msg
                        └── 📂 s2c_json_gen
                            └── 📂 messages
                                ├── 📂 end
                                │   └── 📂 ver1o0
                                │       └── 📄 __init__.py
                                ├── 📂 moved
                                │   └── 📂 ver1o0
                                │       └── 📄 __init__.py
                                └── 📂 start
                                    └── 📂 ver1o0
👉                                      └── 📄 __init__.py
```

```py
# BOF OA16o3o_2o0g1o_3o0

class StartS2cMessage:
    def __init__(self, args):
        """設定"""
        pass

    def asDict(self):
        """Dict形式で取得"""
        return {
            'type': 'send_message',  # type属性は必須
            's2c_type': "S2C_Start",
        }

# EOF OA16o3o_2o0g1o_3o0
```

## ~~Step OA16o3o_2o0g1o0~~

1. Separated to OA16o3o_2o0g1o_1o0
2. Separated to OA16o3o_2o0g1o_2o0
3. Separated to OA16o3o_2o0g1o_3o0
4. Removed

## Step OA16o3o_2o0g2o0 画面作成 - msg/s2c_json_gen/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
                │       └── 📂 msg
                │           └── 📂 s2c_json_gen
👉              │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 msg
                        └── 📂 s2c_json_gen
                            └── 📂 commands
                                └── 📂 ver1o0
                                    └── 📄 __init__.py
```

```html
<!-- BOF OA16o3o_2o0g2o0 -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<html>
    <head>
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui" />
        <title>Tic Tac Toe</title>
        <style>
            /* 等幅 */
            .v-textarea textarea {
                font-family: monospace, monospace;
            }
        </style>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container fluid>
                        <h1>Tic Tac Toe - S2C Json Generator</h1>
                        <form method="POST" action="">
                            <!--                    =
                                                    1
                            1. 宛先を間違えないように
                               `http://example.com/tic-tac-toe/vol2.0/ver1.0/`
                                                                             =
                            -->

                            {% csrf_token %}
                            <!--
                               ==========
                               1
                            1. form要素の中に csrf_token を入れてください
                            -->

                            <!-- 入力 -->
                            <!-- リスト -->
                            <!-- `po_` は POST送信するパラメーター名の目印 -->
                            <v-select name="po_messageType" v-model="c2sMessageTypeListbox.value" :items="c2sMessageTypeItems" label="サーバーからクライアントへ送られてくるメッセージの種類一覧"></v-select>
                            <v-select name="po_sq1" v-model="sqListbox.value" :items="sqItems" label="マス番号一覧"></v-select>
                            <v-select name="po_player1" v-model="playerListbox.value" :items="playerItems" label="プレイヤー一覧"></v-select>
                            <v-select name="po_piece1" v-model="pieceListbox.value" :items="pieceItems" label="駒一覧"></v-select>

                            <!-- ボタン -->
                            <v-btn type="submit" block elevation="2" v-on:click="pullVu()"> Pull </v-btn>

                            <!-- 出力 -->
                            <v-textarea required v-model="outputTextbox.value" label="Output" rows="10"/>
                        </v-form>
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="{% static 'tic_tac_toe_vol2o0/think/things/ver1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_vol2o0/think/concepts/ver1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_vol2o0/think/position/ver1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_vol2o0/think/user_ctrl/ver1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_vol2o0/think/judge_ctrl/ver1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_vol2o0/think/engine/ver1o0.js' %}"></script>
        <!--            =================================================
                        1
        1. src1/apps1/tic_tac_toe_vol2o0/static/tic_tac_toe_vol2o0/think/engine/ver1o0.js
                                         ================================================
        -->

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            const vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // 出力
                    outputTextbox: {
                        // `dj_` は Djangoでレンダーするパラメーター名の目印
                        value: JSON.stringify(JSON.parse('{{ dj_output_json|escapejs }}'), null, '    '),
                    },
                    // メッセージの種類リストボックス
                    c2sMessageTypeListbox: {
                        value: "S2C_End",
                    },
                    // マス番号リストボックス
                    sqListbox: {
                        value: "",
                    },
                    // プレイヤーリストボックス
                    playerListbox: {
                        value: "",
                    },
                    // 駒リストボックス
                    pieceListbox: {
                        value: "",
                    },
                    // メッセージの種類一覧
                    c2sMessageTypeItems: ["S2C_End", "S2C_Moved", "S2C_Start"],
                    // マス番号の一覧
                    sqItems: ["", 0, 1, 2, 3, 4, 5, 6, 7, 8],
                    // プレイヤーの一覧
                    playerItems: ["", "X", "O"],
                    // 駒の一覧
                    pieceItems: ["", "X", "O"],
                },
                methods: {
                    // 関数名の末尾の Vu は vue1 のメソッドであることを表す目印
                    /**
                     * po_input 欄のコマンドを入力します
                     */
                    pullVu() {
                        // ボタン押下後、ページ再読み込み前にやりたいことがあれば、ここに書いてください
                    },
                },
            });
        </script>
    </body>
</html>
<!-- EOF OA16o3o_2o0g2o0 -->
```

## Step OA16o3o_2o0g3o0 ビュー作成 - msg/s2c_json_gen/v1o0/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
                │       └── 📂 msg
                │           └── 📂 s2c_json_gen
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 msg
                        └── 📂 s2c_json_gen
                            ├── 📂 commands
                            │   └── 📂 ver1o0
                            │       └── 📄 __init__.py
                            └── 📂 ver1o0
👉                              └── 📄 v_render.py
```

```py
# BOF OA16o3o_2o0g3o0

import json
from django.shortcuts import render

# OA16o3o_2o0g1o_1o0 〇×ゲーム2.0巻 S2cメッセージ End 1.0版
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.end.ver1o0 import EndS2cMessage
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.moved.ver1o0 import MovedS2cMessage
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.start.ver1o0 import StartS2cMessage
#          ------------------                                       ------        ---------------
#          11                                                       12            2
#    ---------------------------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス


def render_main(request, template_path):
    """OA16o3o_2o0g3o0 S2C JSON ジェネレーター - 描画

    Parameters
    ----------
    template_path : str
        Template path
    """

    if request.method == "POST":
        # 送信後

        messageType = request.POST.get("po_messageType")
        args = {
            "player1": request.POST.get("po_player1"),
            "sq1": request.POST.get("po_sq1"),
            "piece1": request.POST.get("po_piece1"),
        }
        # print(
        #     f'[render_main] messageType:{messageType} player1:{args["player1"]} sq1:{args["sq1"]} piece1:{args["piece1"]}')
        # TODO バリデーションチェックしたい

        message_object_dict = {
            "S2C_End": EndS2cMessage(args),
            "S2C_Moved": MovedS2cMessage(args),
            "S2C_Start": StartS2cMessage(args),
        }

        if messageType in message_object_dict:
            doc = message_object_dict.get(messageType).asDict()
            dj_output_json = json.dumps(doc)
        else:
            # 空っぽのJSON文字列
            dj_output_json = "{}"

    else:
        # 空っぽのJSON文字列
        dj_output_json = "{}"

    context = {
        # `dj_` は Djangoでレンダーするパラメーター名の目印
        "dj_output_json": dj_output_json,
    }

    return render(request, template_path, context)

# EOF OA16o3o_2o0g3o0
```

## Step OA16o3o_2o0g4o0 ビュー作成 - msg/s2c_json_gen/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
                │       └── 📂 msg
                │           └── 📂 s2c_json_gen
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 msg
                        └── 📂 s2c_json_gen
                            ├── 📂 commands
                            │   └── 📂 ver1o0
                            │       └── 📄 __init__.py
                            └── 📂 ver1o0
👉                              ├── 📄 __init__.py
                                └── 📄 v_render.py
```

```py
# BOF OA16o3o_2o0g4o0

class S2cJsonGenView():
    """OA16o3o_2o0g4o0 S2C Json ジェネレーター ビュー"""

    template_path = "tic_tac_toe_vol2o0/msg/s2c_json_gen/ver1o0.html"
    #                               ^two
    #                -----------------------------------------------
    #                1
    # 1. src1/apps1/tic_tac_toe_vol2o0/templates/tic_tac_toe_vol2o0/msg/c2s_json_gen/ver1o0.html
    #                                            -----------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_main
        #    ---------        -----------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_vol2o0/views/msg/c2s_json_gen/v1o0/v_render.py`
        #                                                               --------
        # 2. `1.` に含まれる関数

        return render_main(
            request,
            S2cJsonGenView.template_path)

# EOF OA16o3o_2o0g4o0
```

## ~~Step OA16o3o_2o0g5o0~~

Merged to OA16o3o_2o0g5o1o0  

## Step OA16o3o_2o0g5o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 tic_tac_toe_vol2o0    # アプリケーション
    │           ├── 📂 templates
    │           │   └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
    │           │       └── 📂 msg
    │           │           └── 📂 s2c_json_gen
    │           │               └── 📄 ver1o0.html
    │           └── 📂 views
    │               └── 📂 msg
    │                   └── 📂 s2c_json_gen
    │                       ├── 📂 commands
    │                       │   └── 📂 ver1o0
    │                       │       └── 📄 __init__.py
    │                       └── 📂 ver1o0
    │                           ├── 📄 __init__.py
    │                           └── 📄 v_render.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_tic_tac_toe_vol2o0_autogen.py,tic-tac-toe/vol2.0/s2c-json-gen/ver1.0/,,"OA16o3o_2o0g5o1o0 〇×ゲーム2.0巻 S2C JSON ジェネレーター1.0版",apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.ver1o0,S2cJsonGenView,S2cJsonGenViewV1o0,render
```

## Step OA16o3o_2o0g5o2o0 ルート編集 - コマンド打鍵

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

## Step. Web画面へアクセス

📖 [http://localhost:8000/tic-tac-toe/vol2.0/s2c-json-gen/ver1.0/](http://localhost:8000/tic-tac-toe/vol2.0/s2c-json-gen/ver1.0/)  

# 次の記事

📖 [OA16o3o0 Webブラウザ越しに２人対戦できる〇×ゲームを作ろう！ Vuetify編](https://qiita.com/muzudho1/items/f302bdb40fb5c13f9603)  

# 参考にした記事

## Python

📖 [3 Ways to Implement Python Switch Case Statement](https://favtutor.com/blogs/python-switch-case)  
