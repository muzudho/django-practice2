# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/tic-tac-toe/vol2.0/c2s-json-gen/ver1.0/)  

# 目標

〇×ゲーム（Tic tac toe）の通信対戦をしたい  

いきなり作るのは難しいので その前に、クライアントからサーバーへ送るメッセージを取り決めておく  

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

## ~~Step [OA16o3o_1o0g_1o__10o___100o0]~~

Removed  

## Step [OA16o3o_1o0g_1o__10o___101o0] メッセージ作成 - msg/c2s_json_gen/messages/moved/ver1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0               # アプリケーション
                └── 📂 static
                    └── 📂 tic_tac_toe_vol2o0       # アプリケーションと同名
                        └── 📂 msg
                            └── 📂 c2s_json_gen
                                └── 📂 messages
                                    └── 📂 moved
👉                                      └── 📄 ver1o0.js
```

```js
// BOF OA16o3o_1o0g_1o__10o___101o0

/**
 * クライアントからサーバーへ送るメッセージ
 *
 * * 駒の移動を表す
 */
class MovedC2sMessage {
    /**
     * 設定
     * @param {*} sq - マス番号
     * @param {*} pieceMoved - 動かした駒
     */
    constructor(sq, pieceMoved) {
        this._sq = sq;
        this._pieceMoved = pieceMoved;
    }

    /**
     * JSObject形式で取得
     * @returns JSObject形式
     */
    asJsObject() {
        return {
            // `c2s_` は クライアントからサーバーへ送る変数の目印
            c2s_type: "C2S_Moved",
            c2s_sq: this._sq,
            c2s_pieceMoved: this._pieceMoved,
        };
    }
}

// EOF OA16o3o_1o0g_1o__10o___101o0
```

## Step [OA16o3o_1o0g_1o__11o___102o0] メッセージ作成 - msg/c2s_json_gen/messages/end/ver1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                └── 📂 static
                    └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
                        └── 📂 msg
                            └── 📂 c2s_json_gen
                                └── 📂 messages
                                    ├── 📂 end
👉                                  │   └── 📄 ver1o0.js
                                    └── 📂 moved
                                        └── 📄 ver1o0.js
```

```js
// BOF OA16o3o_1o0g_1o__11o___102o0

/**
 * クライアントからサーバーへ送るメッセージ
 *
 * * 対局終了を表す
 */
class EndC2sMessage {
    constructor(winner) {
        this._winner = winner;
    }

    /**
     * JSObject形式で取得
     * @returns JSObject形式
     */
    asJsObject() {
        return {
            // `c2s_` は クライアントからサーバーへ送る変数の目印
            c2s_type: "C2S_End",
            c2s_winner: this._winner,
        };
    }
}

// EOF OA16o3o_1o0g_1o__11o___102o0
```

## Step [OA16o3o_1o0g_1o__11o___103o0] メッセージ作成 - msg/c2s_json_gen/messages/start/ver1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                └── 📂 static
                    └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
                        └── 📂 msg
                            └── 📂 c2s_json_gen
                                └── 📂 messages
                                    ├── 📂 end
                                    │   └── 📄 ver1o0.js
                                    ├── 📂 moved
                                    │   └── 📄 ver1o0.js
                                    └── 📂 start
👉                                      └── 📄 ver1o0.js
```

```js
// BOF OA16o3o_1o0g_1o__11o___103o0

/**
 * クライアントからサーバーへ送るメッセージ
 *
 * * 対局開始を表す
 */
class StartC2sMessage {
    constructor() {}

    /**
     * JSObject形式で取得
     * @returns JSObject形式
     */
    asJsObject() {
        return {
            // `c2s_` は クライアントからサーバーへ送る変数の目印
            c2s_type: "C2S_Start",
        };
    }
}

// EOF OA16o3o_1o0g_1o__11o___103o0
```

## Step [OA16o3o_1o0g_1o__10o0] イベント作成 - msg/c2s_json_gen/events/do_move/ver1o0.js ファイル

Separated from OA16o3o_1o0g_1o0  

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                └── 📂 static
                    └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
                        └── 📂 msg
                            └── 📂 c2s_json_gen
                                ├── 📂 events
                                │   └── 📂 do_move
👉                              │       └── 📄 ver1o0.js
                                └── 📂 messages
                                    ├── 📂 end
                                    │   └── 📄 ver1o0.js
                                    ├── 📂 moved
                                    │   └── 📄 ver1o0.js
                                    └── 📂 start
                                        └── 📄 ver1o0.js
```

```js
// BOF OA16o3o_1o0g_1o__10o0

/**
 * イベント
 *
 * * 自分のターンに駒を置いたとき
 */
class EvtDoMove {
    /**
     * メッセージ新規作成
     * @param {int} sq - 升番号
     * @param {string} pieceMoved - 駒を置いたプレイヤー。 X か O
     * @returns メッセージ
     */
    createMessage(sq, pieceMoved) {
        return new MovedC2sMessage(sq, pieceMoved);
    }
}

// EOF OA16o3o_1o0g_1o__10o0
```

## Step [OA16o3o_1o0g_1o__11o0] イベント作成 - msg/c2s_json_gen/events/draw/ver1o0.js ファイル

Separated from OA16o3o_1o0g_1o0  

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                └── 📂 static
                    └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
                        └── 📂 msg
                            └── 📂 c2s_json_gen
                                ├── 📂 events
                                │   ├── 📂 do_move
                                │   │   └── 📄 ver1o0.js
                                │   └── 📂 draw
👉                              │       └── 📄 ver1o0.js
                                └── 📂 messages
                                    ├── 📂 end
                                    │   └── 📄 ver1o0.js
                                    ├── 📂 moved
                                    │   └── 📄 ver1o0.js
                                    └── 📂 start
                                        └── 📄 ver1o0.js
```

```js
// BOF OA16o3o_1o0g_1o__11o0

/**
 * イベント
 *
 * * 引き分けで対局終了したと納得したとき
 */
class EvtDraw {
    /**
     * メッセージ新規作成
     * @returns メッセージ
     */
    createMessage() {
        return new EndC2sMessage(PC_EMPTY_LABEL);
    }
}

// EOF OA16o3o_1o0g_1o__11o0
```

## Step [OA16o3o_1o0g_1o__12o0] メッセージ作成 - msg/c2s_json_gen/events/start/ver1o0.js ファイル

Separated from OA16o3o_1o0g_1o0  

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                └── 📂 static
                    └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
                        └── 📂 msg
                            └── 📂 c2s_json_gen
                                ├── 📂 events
                                │   ├── 📂 do_move
                                │   │   └── 📄 ver1o0.js
                                │   ├── 📂 draw
                                │   │   └── 📄 ver1o0.js
                                │   └── 📂 start
👉                              │       └── 📄 ver1o0.js
                                └── 📂 messages
                                    ├── 📂 end
                                    │   └── 📄 ver1o0.js
                                    ├── 📂 moved
                                    │   └── 📄 ver1o0.js
                                    └── 📂 start
                                        └── 📄 ver1o0.js
```

```js
// BOF OA16o3o_1o0g_1o__12o0

/**
 * イベント
 *
 * * 対局開始に納得したとき
 */
class EvtStart {
    /**
     * メッセージ新規作成
     * @returns メッセージ
     */
    createMessage() {
        return new StartC2sMessage();
    }
}

// EOF OA16o3o_1o0g_1o__12o0
```

## Step [OA16o3o_1o0g_1o__13o0] イベント作成 - msg/c2s_json_gen/events/won/ver1o0.js ファイル

Separated from OA16o3o_1o0g_1o0  

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                └── 📂 static
                    └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
                        └── 📂 msg
                            └── 📂 c2s_json_gen
                                ├── 📂 events
                                │   ├── 📂 do_move
                                │   │   └── 📄 ver1o0.js
                                │   ├── 📂 draw
                                │   │   └── 📄 ver1o0.js
                                │   ├── 📂 start
                                │   │   └── 📄 ver1o0.js
                                │   └── 📂 won
👉                              │       └── 📄 ver1o0.js
                                └── 📂 messages
                                    ├── 📂 end
                                    │   └── 📄 ver1o0.js
                                    ├── 📂 moved
                                    │   └── 📄 ver1o0.js
                                    └── 📂 start
                                        └── 📄 ver1o0.js
```

```js
// BOF OA16o3o_1o0g_1o__13o0

/**
 * イベント
 *
 * * 勝ったことに納得したとき
 */
class EvtWon {
    /**
     * メッセージ新規作成
     * @param {*} winner - 勝者。 "X" か "O"
     * @returns メッセージ
     */
    createMessage(winner) {
        return new EndC2sMessage(winner);
    }
}

// EOF OA16o3o_1o0g_1o__13o0
```

## ~~Step [OA16o3o_1o0g_1o0]~~

1. Separated from OA16o3o0g2o0  
2. Separate to OA16o3o_1o0g_1o__10o0
3. Separate to OA16o3o_1o0g_1o__11o0
4. Separate to OA16o3o_1o0g_1o__12o0
5. Separate to OA16o3o_1o0g_1o__13o0
6. Removed

## Step [OA16o3o_1o0g1o0] 画面作成 - msg/c2s_json_gen/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_vol2o0
                │       └── 📂 msg
                │           └── 📂 c2s_json_gen
                │               ├── 📂 events
                │               │   ├── 📂 do_move
                │               │   │   └── 📄 ver1o0.js
                │               │   ├── 📂 draw
                │               │   │   └── 📄 ver1o0.js
                │               │   ├── 📂 start
                │               │   │   └── 📄 ver1o0.js
                │               │   └── 📂 won
                │               │       └── 📄 ver1o0.js
                │               └── 📂 messages
                │                   ├── 📂 end
                │                   │   └── 📄 ver1o0.js
                │                   ├── 📂 moved
                │                   │   └── 📄 ver1o0.js
                │                   └── 📂 start
                │                       └── 📄 ver1o0.js
                └── 📂 templates
                    └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
                        └── 📂 msg
                            └── 📂 c2s_json_gen
👉                              └── 📄 ver1o0.html
```

```html
<!-- BOF OA16o3o_1o0g1o0 -->
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
                        <h1>Tic Tac Toe - C2S Json Generator</h1>
                        <v-form method="POST">
                            {% csrf_token %}

                            <!-- `po_` は POST送信するパラメーター名の目印 -->

                            <!-- リスト -->
                            <v-select v-model="c2sEventNameListbox.value" :items="c2sEventNameItems" label="クライアントからサーバーへ送るメッセージが作られるイベント一覧"></v-select>
                            <v-select v-model="sqListbox.value" :items="sqItems" label="マス番号一覧"></v-select>
                            <v-select v-model="playerListbox.value" :items="playerItems" label="プレイヤー一覧"></v-select>

                            <!-- ボタン -->
                            <v-btn block elevation="2" v-on:click="postVu()"> Generate JSON </v-btn>

                            <!-- 出力 -->
                            <v-textarea name="po_output" required v-model="outputTextbox.value" label="Output" rows="10"></v-textarea>
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
        <script src="{% static 'tic_tac_toe_vol2o0/msg/c2s_json_gen/messages/end/ver1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_vol2o0/msg/c2s_json_gen/messages/moved/ver1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_vol2o0/msg/c2s_json_gen/messages/start/ver1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_vol2o0/msg/c2s_json_gen/events/do_move/ver1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_vol2o0/msg/c2s_json_gen/events/draw/ver1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_vol2o0/msg/c2s_json_gen/events/start/ver1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_vol2o0/msg/c2s_json_gen/events/won/ver1o0.js' %}"></script>
        <!--            ================================================================
                        1
        1. src1/apps1/tic_tac_toe_vol2o0/static/tic_tac_toe_vol2o0/msg/c2s_json_gen/events/won/ver1o0.js
                                         ===============================================================
        -->

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            // Create message by event
            const dictCreateMsg = {};

            dictCreateMsg["DoMove"] = () => {
                const sq = vue1.sqListbox.value;
                const myTurn = vue1.playerListbox.value;
                return new EvtDoMove().createMessage(sq, myTurn);
            };
            dictCreateMsg["Draw"] = () => {
                return new EvtDraw().createMessage();
            };
            dictCreateMsg["Start"] = () => {
                return new EvtStart().createMessage();
            };
            dictCreateMsg["Won"] = () => {
                const winner = vue1.playerListbox.value;
                return new EvtWon().createMessage(winner);
            };

            const vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // 出力
                    outputTextbox: {
                        value: 'Please push "Generate JSON" button.',
                    },
                    // イベントの種類リストボックス
                    c2sEventNameListbox: {
                        value: "DoMove",
                    },
                    // マス番号リストボックス
                    sqListbox: {
                        value: "",
                    },
                    // プレイヤーリストボックス
                    playerListbox: {
                        value: "",
                    },
                    // イベント名一覧
                    c2sEventNameItems: ["DoMove", "Draw", "Start", "Won"],
                    // マス番号の一覧
                    sqItems: ["", 0, 1, 2, 3, 4, 5, 6, 7, 8],
                    // プレイヤーの一覧
                    playerItems: ["", "X", "O"],
                },
                methods: {
                    // 関数名の末尾の Vu は vue1 のメソッドであることを表す目印
                    /**
                     * po_input 欄のコマンドを入力します
                     */
                    postVu() {
                        const eventName = this.c2sEventNameListbox.value;
                        if (eventName in dictCreateMsg) {
                            const message = dictCreateMsg[eventName]();
                            this.outputTextbox.value = JSON.stringify(message.asJsObject(), null, "    ");
                        }
                    },
                },
            });
        </script>
    </body>
</html>
<!-- EOF OA16o3o_1o0g1o0 -->
```

## Step [OA16o3o_1o0g2o0] ビュー作成 - msg/c2s_json_gen/v1o0/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_vol2o0
                │       └── 📂 msg
                │           └── 📂 c2s_json_gen
                │               ├── 📂 events
                │               │   ├── 📂 do_move
                │               │   │   └── 📄 ver1o0.js
                │               │   ├── 📂 draw
                │               │   │   └── 📄 ver1o0.js
                │               │   ├── 📂 start
                │               │   │   └── 📄 ver1o0.js
                │               │   └── 📂 won
                │               │       └── 📄 ver1o0.js
                │               └── 📂 messages
                │                   ├── 📂 end
                │                   │   └── 📄 ver1o0.js
                │                   ├── 📂 moved
                │                   │   └── 📄 ver1o0.js
                │                   └── 📂 start
                │                       └── 📄 ver1o0.js
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
                │       └── 📂 msg
                │           └── 📂 c2s_json_gen
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 msg
                        └── 📂 c2s_json_gen
                            └── 📂 ver1o0
👉                              └── 📄 v_render.py
```

```py
# BOF OA16o3o_1o0g2o0

from django.shortcuts import render


def render_main(request, template_path):
    """OA16o3o_1o0g2o0 C2S JSON ジェネレーター - 描画

    Parameters
    ----------
    template_path : str
        Template path
    """

    context = {}

    return render(request, template_path, context)

# EOF OA16o3o_1o0g2o0
```

## Step [OA16o3o_1o0g3o0] ビュー作成 - msg/c2s_json_gen/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_vol2o0
                │       └── 📂 msg
                │           └── 📂 c2s_json_gen
                │               ├── 📂 events
                │               │   ├── 📂 do_move
                │               │   │   └── 📄 ver1o0.js
                │               │   ├── 📂 draw
                │               │   │   └── 📄 ver1o0.js
                │               │   ├── 📂 start
                │               │   │   └── 📄 ver1o0.js
                │               │   └── 📂 won
                │               │       └── 📄 ver1o0.js
                │               └── 📂 messages
                │                   ├── 📂 end
                │                   │   └── 📄 ver1o0.js
                │                   ├── 📂 moved
                │                   │   └── 📄 ver1o0.js
                │                   └── 📂 start
                │                       └── 📄 ver1o0.js
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
                │       └── 📂 msg
                │           └── 📂 c2s_json_gen
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 msg
                        └── 📂 c2s_json_gen
                            └── 📂 ver1o0
👉                              └── 📄 __init__.py
```

```py
# BOF OA16o3o_1o0g3o0

class C2sJsonGenView():
    """OA16o3o_1o0g3o0 C2S Json ジェネレーター ビュー"""

    template_path = "tic_tac_toe_vol2o0/msg/c2s_json_gen/ver1o0.html"
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
        # 1. `src1/apps1/tic_tac_toe_vol2o0/views/msg/c2s_json_gen/ver1o0/v_render.py`
        #                                                                 --------
        # 2. `1.` に含まれる関数

        return render_main(
            request,
            C2sJsonGenView.template_path)

# EOF OA16o3o_1o0g3o0
```

## ~~Step [OA16o3o_1o0g4o0]~~

Merged to OA16o3o_1o0g4o1o0  

## Step [OA16o3o_1o0g4o1o0] ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 tic_tac_toe_vol2o0    # アプリケーション
    │           ├── 📂 static
    │           │   └── 📂 tic_tac_toe_vol2o0
    │           │       └── 📂 msg
    │           │           └── 📂 c2s_json_gen
    │           │               ├── 📂 events
    │           │               │   ├── 📂 do_move
    │           │               │   │   └── 📄 ver1o0.js
    │           │               │   ├── 📂 draw
    │           │               │   │   └── 📄 ver1o0.js
    │           │               │   ├── 📂 start
    │           │               │   │   └── 📄 ver1o0.js
    │           │               │   └── 📂 won
    │           │               │       └── 📄 ver1o0.js
    │           │               └── 📂 messages
    │           │                   ├── 📂 end
    │           │                   │   └── 📄 ver1o0.js
    │           │                   ├── 📂 moved
    │           │                   │   └── 📄 ver1o0.js
    │           │                   └── 📂 start
    │           │                       └── 📄 ver1o0.js
    │           ├── 📂 templates
    │           │   └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
    │           │       └── 📂 msg
    │           │           └── 📂 c2s_json_gen
    │           │               └── 📄 ver1o0.html
    │           └── 📂 views
    │               └── 📂 msg
    │                   └── 📂 c2s_json_gen
    │                       └── 📂 ver1o0
    │                           └── 📄 __init__.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_tic_tac_toe_vol2o0_autogen.py,tic-tac-toe/vol2.0/c2s-json-gen/ver1.0/,,"OA16o3o_1o0g4o1o0 〇×ゲーム2.0巻 C2S JSON ジェネレーター1.0版",apps1.tic_tac_toe_vol2o0.views.msg.c2s_json_gen.ver1o0,C2sJsonGenView,C2sJsonGenViewV1o0,render
```

## Step [OA16o3o_1o0g4o2o0] ルート編集 - コマンド打鍵

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

📖 [http://localhost:8000/tic-tac-toe/vol2.0/c2s-json-gen/ver1.0/](http://localhost:8000/tic-tac-toe/vol2.0/c2s-json-gen/ver1.0/)  

# 次の記事

📖 [DjangoとDocker練習OA16o3o_2o0 Tic-Tac-Toeのサーバーからクライアントへ送る通信メッセージを取り決めしよう！](https://qiita.com/muzudho1/items/b8522ca256e329977288)  

# 参考にした記事

## Vuetify

📖 [Set initial vuetify v-select value](https://stackoverflow.com/questions/51392719/set-initial-vuetify-v-select-value)  
