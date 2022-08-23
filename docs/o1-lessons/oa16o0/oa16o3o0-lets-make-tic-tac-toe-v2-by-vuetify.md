# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/tic-tac-toe/v2/match-application/)  

# 目標

フロントエンドに Vuetify を使って、  
１人２役で２窓で遊ぶ 〇×ゲーム（Tic tac toe）を作りたい  

〇×ゲームの思考エンジンは　前の記事で作った物を流用する  

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
    │   │   ├── 📂 allauth_customized_vol1o0    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   ├── 📂 tic_tac_toe_vol1o0           # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2           # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
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
    │   │       │       └── 📂 think
    │   │       │           └── 📂 engine_manual
    │   │       │               └── 📄 v1o0.html
    │   │       ├── 📂 views
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

## Step OA16o3o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## ~~Step OA16o3o0g2o0~~

Moved to OA16o3o_1o0g_1o0  

## Step OA16o3o0g3o0 受信メッセージ駆動実装 - msg/s2c_message_driven/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                └── 📂 static
                    └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                        └── 📂 msg
                            └── 📂 s2c_message_driven
👉                              └── 📄 v1o0.js
```

```js
// BOF OA16o3o0g3o0

/**
 * 受信メッセージ駆動
 */
class S2cMessageDriven {
    constructor() {
        this._handlers = {};
    }

    addHandler(eventName, handler) {
        this._handlers[eventName] = handler;
    }

    /**
     * サーバーからクライアントへ送られてきたメッセージをセットする関数を返します
     * @returns 関数
     */
    execute(message) {
        // `s2c_` は サーバーからクライアントへ送られてきた変数の目印
        // イベント名
        let eventName = message["s2c_event"];
        console.log(`[S2cMessageDriven execute] サーバーからのメッセージを受信しました eventName:${eventName}`);

        if (eventName in this._handlers) {
            // 実行
            const execute2 = this._handlers[eventName];
            execute2(message);
        } else {
            // Undefined behavior
            console.log(`[S2cMessageDriven execute] ignored. eventName=[${eventName}]`);
        }
    }
}

// EOF OA16o3o0g3o0
```

## Step OA16o3o0g4o0 Webソケット接続の実装 - gui/connection/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                └── 📂 static
                    └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                        ├── 📂 gui
                        │   └── 📂 connection
👉                      │       └── 📄 v1o0.js
                        └── 📂 msg
                            └── 📂 s2c_message_driven
                                └── 📄 v1o0.js
```

```js
// BOF OA16o3o0g4o0

// 参考にした記事
// -------------
// 📖[Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)

/**
 * 接続
 */
class Connection {
    /**
     * ウェブソケット
     */
    #webSock1;

    /**
     * 生成
     *
     * @param {string} roomName - 部屋名
     * @param {strint} connectionString - Webソケット接続文字列
     * @param {S2cMessageDriven} s2cMessageDriven - 受信メッセージ駆動
     * @param {function} onOpenWebSocket - Webソケットを開かれたとき
     * @param {function} onCloseWebSocket - Webソケットが閉じられたとき。 例: サーバー側にエラーがあって接続が切れたりなど
     * @param {function} onWebSocketError - Webソケットエラー時のメッセージ
     * @param {function} onRetryWaiting - 再接続のためのインターバルの定期的なメッセージ
     * @param {function} onGiveUp - 再接続を諦めたとき
     */
    constructor(roomName, connectionString, s2cMessageDriven, onOpenWebSocket, onCloseWebSocket, onWebSocketError, onRetryWaiting, onGiveUp) {
        // console.log(`[Connection constructor] roomName=[${roomName}] connectionString=[${connectionString}]`);

        // 部屋名
        this._roomName = roomName;

        // 接続文字列
        this._connectionString = connectionString;

        // リトライ回数
        this._retryCount = 0;
        // リトライ上限
        this._retryMax = 10;

        // 再接続のために記憶しておきます
        this._onOpenWebSocket = onOpenWebSocket;
        this._onCloseWebSocket = onCloseWebSocket;
        this._s2cMsgDrv = s2cMessageDriven;
        this._onWebSocketError = onWebSocketError;
        this._onRetryWaiting = onRetryWaiting;
        this._onGiveUp = onGiveUp;
    }

    /**
     * メッセージ送信
     */
    send(response) {
        this.#webSock1.send(JSON.stringify(response));
    }

    /**
     * 接続
     */
    connect() {
        // console.log(`[Connection#connect] Start this._connectionString=[${this._connectionString}]`);

        // Webソケット
        //
        // * 生成と同時に接続が始まる。そこで例外が起こるとキャッチはできないし、なぜか後続の処理に続かず関数を抜けてしまう
        // * １回切りの使い捨て。再接続機能は無い
        // * 再接続したいときは、再生成する
        try {
            this.#webSock1 = new WebSocket(this._connectionString);
            // 以下、接続に成功

            // イベントハンドラを毎回設定し直してください
            this.#webSock1.onopen = this._onOpenWebSocket;
            this.#webSock1.onclose = this._onCloseWebSocket;

            // 設定: サーバーからメッセージを受信したとき
            this.#webSock1.onmessage = (e) => {
                // JSON を解析、メッセージだけ抽出
                let data1 = JSON.parse(e.data);
                let message = data1["message"];
                this._s2cMsgDrv.execute(message);
            };

            this.#webSock1.addEventListener("open", (event1) => {
                console.log("[Connection connect] WebSockets connection created.");
                // 再接続カウンターをリセットします
                this._retryCount = 0;
            });
            this.#webSock1.addEventListener("error", (event1) => {
                this._onWebSocketError(event1);
            });

            // 状態を表示
            if (this.#webSock1.readyState == WebSocket.CONNECTING) {
                // 未接続
                console.log("[Connection connect] Connecting socket.");
            } else if (this.#webSock1.readyState == WebSocket.OPEN) {
                console.log("[Connection connect] Open socket.");
                this.#webSock1.onopen();
            } else if (this.#webSock1.readyState == WebSocket.CLOSING) {
                console.log("[Connection connect] Closing socket.");
            } else if (this.#webSock1.readyState == WebSocket.CLOSED) {
                // サーバーが落ちたりしたときは、ここ
                console.log("[Connection connect] Closed socket.");

                // 再接続のリトライを書くタイミングはここです
                this.reconnect();
            } else {
                console.log(`[Connection connect] #webSock1.readyState=${this.#webSock1.readyState}`);
            }
        } catch (exception) {
            // キャッチで捕まえられない
            console.log(`[Connection connect] exception:${exception}`);
        }
    }

    /**
     * 再接続
     */
    reconnect() {
        if (this._retryMax <= this._retryCount) {
            // 諦めます
            console.log(`[Connection reconnect] Give up`);
            this._onGiveUp();
            return;
        }

        console.log(`[Connection reconnect] Start...`);

        // 再接続のインターバルの開始を通知しますが、実際に接続するのは５秒後です
        // 最初は 0 回目なので、表示を考慮して +1 の下駄を履かせます
        this._onRetryWaiting(true, this._retryCount + 1, this._retryMax);

        setTimeout(() => {
            console.log(`[Connection reconnect] Try... to:${this._connectionString}`);

            // 事前にカウントを上げておきます
            this._retryCount += 1;
            // 再接続のインターバルの終了を通知しますが、実際には接続を開始します
            this._onRetryWaiting(false, this._retryCount, this._retryMax);
            // 接続
            this.connect();
            console.log(`[Connection reconnect] End. retried:${this._retryCount}/${this._retryMax}`);
        }, 5000);
    }
}

// EOF OA16o3o0g4o0
```

## Step OA16o3o0g5o0 対局申込画面作成 - gui/match_application/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       ├── 📂 gui
                │       │   └── 📂 connection
                │       │       └── 📄 v1o0.js
                │       └── 📂 msg
                │           └── 📂 s2c_message_driven
                │               └── 📄 v1o0.js
                └── 📂 templates
                    └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                        └── 📂 gui
                            └── 📂 match_application
👉                              └── 📄 v1o0.html
```

```html
{# OA16o3o0g5o0 #}
<!-- -->
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
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container fluid>
                        <h1>Welcome to Tic Tac Toe Game</h1>
                        <v-form method="POST">
                            {% csrf_token %}

                            <!-- `po_` は POST送信するパラメーター名の目印 -->
                            <!-- 部屋名 -->
                            <v-text-field name="po_room_name" required v-model="roomName.value" :rules="roomName.rules" counter="25" hint="A-Z, a-z, 0-9, No number at the beginning. Max 25 characters" label="Room name"></v-text-field>

                            <!--
                                自分の番。 "X" か "O"。 機能拡張も想定

                                * 戻り値をオブジェクトのまま受け取りたいときは、タグの属性として return-object を付ける
                            -->
                            <v-select name="po_my_turn" v-model="visitor.value" :items="visitor.select" item-text="text" item-value="value" label="Your turn" persistent-hint single-line></v-select>

                            <v-btn block elevation="2" type="submit"> Start Game </v-btn>
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
                    // 部屋名
                    roomName: {
                        value: "Elephant",
                        rules: [
                            (v) => v.length <= 25 || "Max 25 characters", // 文字数上限
                            (value) => {
                                const pattern = /^[A-Za-z][A-Za-z0-9]*$/; // 正規表現で指定
                                return pattern.test(value) || "Invalid format";
                            },
                        ],
                    },
                    // 入場者
                    visitor: {
                        // `dj_` は Djangoでレンダーするパラメーター名の目印
                        value: "{{dj_visitor_value}}",
                        select: JSON.parse("{{dj_visitor_select | escapejs}}"),
                    },
                },
            });
        </script>
    </body>
</html>
```

## Step OA16o3o0g6o0 対局画面作成 - gui/playing/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       ├── 📂 gui
                │       │   └── 📂 connection
                │       │       └── 📄 v1o0.js
                │       └── 📂 msg
                │           └── 📂 s2c_message_driven
                │               └── 📄 v1o0.js
                └── 📂 templates
                    └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                        └── 📂 gui
                            ├── 📂 match_application
                            │   └── 📄 v1o0.html
                            └── 📂 playing
👉                              └── 📄 v1o0.html
```

```html
{# BOF OA16o3o0g6o0 #}
<!-- -->
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
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container>
                        <h1>TIC TAC TOE</h1>
                        <h3>Welcome to room_{{dj_room_name}}</h3>
                    </v-container>

                    <form name="form1" method="POST">
                        {% csrf_token %}
                        <v-container>
                            <v-row justify="center" dense>
                                <v-col>
                                    {% comment %} Vue で二重波括弧（braces）は変数の展開に使っていることから、 Python のテンプレートに二重波括弧を変数の展開に使わないよう verbatim で指示します。 {% endcomment %}
                                    <!-- -->
                                    {% verbatim %}
                                    <v-btn id="square0" v-on:click="clickSquare(0)">{{label0}}</v-btn>
                                    <v-btn id="square1" v-on:click="clickSquare(1)">{{label1}}</v-btn>
                                    <v-btn id="square2" v-on:click="clickSquare(2)">{{label2}}</v-btn>
                                    {% endverbatim %}
                                </v-col>
                            </v-row>
                            <v-row justify="center" dense>
                                <v-col>
                                    {% verbatim %}
                                    <v-btn id="square3" v-on:click="clickSquare(3)">{{label3}}</v-btn>
                                    <v-btn id="square4" v-on:click="clickSquare(4)">{{label4}}</v-btn>
                                    <v-btn id="square5" v-on:click="clickSquare(5)">{{label5}}</v-btn>
                                    {% endverbatim %}
                                </v-col>
                            </v-row>
                            <v-row justify="center" dense>
                                <v-col>
                                    {% verbatim %}
                                    <v-btn id="square6" v-on:click="clickSquare(6)">{{label6}}</v-btn>
                                    <v-btn id="square7" v-on:click="clickSquare(7)">{{label7}}</v-btn>
                                    <v-btn id="square8" v-on:click="clickSquare(8)">{{label8}}</v-btn>
                                    {% endverbatim %}
                                </v-col>
                            </v-row>
                        </v-container>

                        <!-- `po_` は POST送信するパラメーター名の目印 -->
                        <input type="hidden" name="po_room_name" value="{{dj_room_name}}" />
                        <input type="hidden" name="po_my_turn" value="{{dj_my_turn}}" />
                    </form>
                    {% block footer_section1 %}
                    <!-- ボタン等を追加したいなら、ここに挿しこめる -->
                    {% endblock footer_section1 %}
                    <v-container>
                        {% verbatim %}
                        <v-alert type="success" v-show="isGameover">{{gameover_message}}</v-alert>
                        {% endverbatim %}
                        <v-alert type="info" v-show="isYourTurn">Your turn. Place your move <strong>{{dj_my_turn}}</strong></v-alert>
                        <v-alert type="warning" v-show="isItOpponentsTurnToMove">Wait for other to place the move</v-alert>
                        {% verbatim %}
                        <v-alert type="warning" v-show="isReconnecting">Reconnecting... {{reconnectionCount}}/{{reconnectionMax}}</v-alert>
                        {% endverbatim %}
                        <v-alert type="error" v-show="isSocketClosed">Lost connection</v-alert>
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="{% static 'tic_tac_toe_v2/think/things/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/think/concepts/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/think/position/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/think/user_ctrl/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/think/judge_ctrl/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/think/engine/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/gui/connection/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/msg/s2c_message_driven/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/msg/c2s_json_gen/v1o0.js' %}"></script>
        <!--            ===============================================
                        1
        1. src1/apps1/tic_tac_toe_v2/static/tic_tac_toe_v2/msg/c2s_json_gen/v1o0.js
                                     ==============================================
        -->

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            // 部屋名
            const roomName = document.forms["form1"]["po_room_name"].value;
            // 接続文字列
            // `dj_` は Djangoでレンダーするパラメーター名の目印
            const connectionString = `ws://${window.location.host}{{dj_path_of_ws_playing}}${roomName}/`;
            //                        ----]----------------------]-------------------------------------
            //                        1    2                      3
            // 1. プロトコル（Web socket）
            // 2. ホスト アドレス
            // 3. パス
            console.log(`[HTML] convertPartsToConnectionString roomName=${roomName} connectionString=${connectionString}`);

            // サーバーからクライアントへメッセージ送信
            const s2cMsgDrv = new S2cMessageDriven();
            // 対局開始時
            s2cMsgDrv.addHandler("S2C_Start", (message)=>{
                vue1.onStart();
            });
            // 対局終了時
            s2cMsgDrv.addHandler("S2C_End", (message)=>{
                // 勝者
                let winner = message["s2c_winner"];
                console.log(`[HTML onEnd] winner:${winner}`);
                vue1.onGameover(winner);
            });
            // 指し手受信時
            s2cMsgDrv.addHandler("S2C_Moved", (message)=>{
                // 升番号
                let sq = parseInt(message["s2c_sq"]);
                // 手番。 "X" か "O"
                let piece_moved = message["s2c_pieceMoved"];
                console.log(`[HTML onMoved] sq:${sq} piece_moved:${piece_moved} 自分の手番:${vue1.engine.position.turn.me}`);

                if (piece_moved != vue1.engine.position.turn.me) {
                    // 相手の手番なら、自動で動かします
                    vue1.engine.userCtrl.doMove(vue1.engine.position, piece_moved, sq);

                    // 「相手の手番で動かした」アラートの取りさげ
                    vue1.isItOpponentsTurnToMove = false;
                }

                // ゲームオーバー判定
                vue1.engine.judgeCtrl.doJudge(vue1.engine.position);
            });

            // クライアントからサーバーへ送るJSON生成
            const c2sMessages = new C2sJsonGen();

            // 接続
            var connection = new Connection(
                roomName,
                connectionString,
                // サーバーからのメッセージを受信したとき
                s2cMsgDrv,
                // Webソケットを開かれたとき
                () => {
                    console.log("WebSockets connection created.");
                    let response = c2sMessages.createStart();
                    connection.send(response);
                },
                // Webソケットが閉じられたとき
                (exception) => {
                    console.log(`Socket is closed. Reconnect it. ${exception.reason}`);
                    // 再接続の初回トライを書いてよいのはこのタイミングです
                    connection.reconnect();
                },
                // エラー時
                (exception) => {
                    console.log(`Socket is error. ${exception.reason}`);
                },
                /**
                 * 再接続のためのインターバルの通知
                 *
                 * アラートが、接続中に短く非表示、次の接続までの待機中に長く表示と、逆になっているが、そうしないと表示が短くなってしまう
                 *
                 * @param {bool} isBeginWait - 次の再接続までの待ち時間に入ったら真
                 * @param {int} retryCount - リトライ回数
                 * @param {int} retryMax - リトライ回数上限
                 */
                (isBeginWait, retryCount, retryMax)=>{
                    // console.log(`WebSockets reconnection isBeginWait:${isBeginWait}`);
                    vue1.isReconnecting = isBeginWait;
                    vue1.reconnectionCount = retryCount;
                    vue1.reconnectionMax = retryMax;
                },
                /**
                 * 再接続を諦めたとき
                 */
                ()=>{
                    vue1.isSocketClosed = true;
                });

            let vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // 思考エンジン
                    engine: new Engine(
                        // `po_` は POST送信するパラメーター名の目印
                        // 自分の番。 X か O
                        document.forms["form1"]["po_my_turn"].value,
                        // ユーザーコントロール
                        new UserCtrl(
                            /**
                             * onDidMove - 駒を置いたあと
                             *
                             * * 手番がひっくり返っていることに注意してください
                             *
                             * @param {int} sq - マス番号
                             * @param {string} pieceMoved - 動かした駒
                             */
                            (sq, pieceMoved) => {
                                // ボタンのラベルを更新
                                vue1.setLabelOfButton(sq, pieceMoved);

                                console.log(`[Engine onDidMove] sq=${sq} pieceMoved=${pieceMoved}`);

                                // 自分の指し手なら送信
                                if (vue1.engine.position.turn.me == pieceMoved) {
                                    let response = c2sMessages.createDoMove(sq, pieceMoved);
                                    connection.send(response);
                                }

                                // 手番の再描画を通知
                                vue1.raiseMyTurnChanged();
                            }
                        ),
                        // 審判コントロール
                        new JudgeCtrl(
                            /**
                             * onDoJudge - 判断したとき
                             *
                             * @param {*} gameoverSet - ゲームオーバー集合
                             */
                            (gameoverSet) => {
                                vue1.engine.gameoverSet = gameoverSet;
                                let response;

                                switch (gameoverSet.value) {
                                    case GameoverSet.won:
                                        // 自分が勝ったとき
                                        response = c2sMessages.createWon(vue1.engine.position.turn.me);
                                        connection.send(response);
                                        break;
                                    case GameoverSet.draw:
                                        // 引き分けたとき
                                        response = c2sMessages.createDraw();
                                        connection.send(response);
                                        break;
                                    case GameoverSet.lost:
                                        // 自分が負けたとき
                                        break;
                                    case GameoverSet.none:
                                        // なんでもなかったとき
                                        break;
                                    default:
                                        throw new Error(`Unexpected gameoverSet.value=${gameoverSet.value}`);
                                }
                            }
                        )
                    ),
                    label0: PC_EMPTY_LABEL,
                    label1: PC_EMPTY_LABEL,
                    label2: PC_EMPTY_LABEL,
                    label3: PC_EMPTY_LABEL,
                    label4: PC_EMPTY_LABEL,
                    label5: PC_EMPTY_LABEL,
                    label6: PC_EMPTY_LABEL,
                    label7: PC_EMPTY_LABEL,
                    label8: PC_EMPTY_LABEL,
                    isReconnecting: false,
                    reconnectionCount: 0,
                    reconnectionMax: 0,
                    isSocketClosed: false,
                    isYourTurn: false,
                    isGameover: false,
                    // 「相手の手番に着手しないでください」というアラートの可視性
                    isItOpponentsTurnToMove: false,
                    roomState: new RoomState(RoomState.none,(oldValue, newValue)=>{
                        // changeRoomState
                        console.log(`[data roomState changeRoomState] state old=${oldValue} new=${newValue}`);
                        vue1.raiseRoomStateChanged();
                    }),
                    gameover_message : "",
                    messages: {
                        draw: "It's a draw.",
                        youLost: "You lost.",
                        youWon: "You won!",
                        {% block appendix_message %}
                        // メッセージを追加したければ、ここに挿しこめる
                        {% endblock appendix_message %}
                    }
                },
                // page loaded
                mounted: () => {
                    // * ここで vue1 はまだ初期化されていない
                    // * ここで this は Window を指している
                    console.log(`[mounted] ★dataより後か先か？`);
                    console.log(`[mounted] ★this:${this}`);
                    // console.log(`[mounted] ★vue1.data.messages.youWon:${vue1.messages.youWon}`);
                },
                methods: {
                    // 対局開始時
                    onStart() {
                        console.log("[methods onStart]");

                        // 「相手の手番に着手しないでください」というアラートの非表示
                        this.isItOpponentsTurnToMove = false;

                        // 先に 対局中状態 にしておいてから、エンジンをスタートさせてください
                        this.roomState.value = RoomState.playing;
                        this.engine.start();
                        this.raisePositionChanged();


                        // ボタンのラベルをクリアー
                        for (let sq = 0; sq < BOARD_AREA; sq += 1) {
                            this.setLabelOfButton(sq, "");
                        }

                        // ダンプ
                        this.dump();
                    },
                    /**
                     * 升ボタンをクリックしたとき
                     * @param {*} sq - Square; 0 <= sq
                     */
                    clickSquare(sq) {
                        console.log(`[methods clickSquare] gameoverSet:${this.engine.gameoverSet.value}`);
                        if (this.engine.gameoverSet.value != GameoverSet.none) {
                            // Ban on illegal move
                            console.log(`Ban on illegal move. gameoverSet:${this.engine.gameoverSet.value}`);
                            return;
                        }

                        if (this.engine.position.board.getPieceBySq(sq) == PC_EMPTY) {
                            if (!this.engine.position.turn.isMe) {
                                // Wait for other to place the move
                                console.log("Wait for other to place the move");
                                this.isItOpponentsTurnToMove = true;
                            } else {
                                if (this.engine.gameoverSet.value != GameoverSet.none) {
                                    // ゲームオーバー後に駒を置いてはいけません
                                    console.log(`warning of illegal move. gameoverSet:${this.engine.gameoverSet.value}`);
                                    return;
                                }

                                // 自分の一手
                                this.engine.userCtrl.doMove(this.engine.position, this.engine.position.turn.me, parseInt(sq));
                            }
                        }
                    },
                    /**
                     * 対局は終了しました
                     */
                    onGameover(winner) {
                        console.log(`[methods onGameover] winner=${winner}`);
                        this.engine.winner = winner;
                        this.roomState.value = RoomState.none; // 画面を対局終了状態へ

                        this.gameover_message = this.createGameoverMessage();
                    },
                    /**
                     * ゲームオーバー時のメッセージ作成
                     */
                    createGameoverMessage() {
                        {% block create_gameover_message %}
                        // 返却値を変えたいなら、ここに挿しこめる
                        {% endblock create_gameover_message %}

                        switch (this.engine.gameoverSet.value) {
                            case GameoverSet.draw:
                                return this.messages.draw;
                            case GameoverSet.won:
                                return this.messages.youWon;
                            case GameoverSet.lost:
                                return this.messages.youLost;
                            case GameoverSet.none:
                                // ここに来るのはおかしい
                                return "";
                            default:
                                throw `unknown this.engine.gameoverSet.value = ${this.engine.gameoverSet.value}`;
                        }
                    },
                    /**
                     * 升ボタンのラベルの設定
                     *
                     * @param {number} sq - Square; 0 <= sq
                     * @param {*} piece - text
                     */
                    setLabelOfButton(sq, piece) {
                        console.log(`[methods setLabelOfButton] sq=${sq} piece=${piece}`);
                        switch (sq) {
                            case 0:
                                this.label0 = piece;
                                break;
                            case 1:
                                this.label1 = piece;
                                break;
                            case 2:
                                this.label2 = piece;
                                break;
                            case 3:
                                this.label3 = piece;
                                break;
                            case 4:
                                this.label4 = piece;
                                break;
                            case 5:
                                this.label5 = piece;
                                break;
                            case 6:
                                this.label6 = piece;
                                break;
                            case 7:
                                this.label7 = piece;
                                break;
                            case 8:
                                this.label8 = piece;
                                break;
                            default:
                                alert(`[Error] sq=${sq}`);
                                break;
                        }
                    },
                    /**
                     * (1) 対局中か
                     * (2) 自分の手番か
                     */
                    updateYourTurn(){
                        console.log(`[methods updateYourTurn 1] this.roomState=${this.roomState.value} 私の番か:${this.engine.position.turn.isMe}`);
                        let isYourTurn = this.roomState.value == RoomState.playing && this.engine.position.turn.isMe;

                        {% block isYourTurn_patch1 %}
                        // 条件を追加したいなら、ここに挿しこめる
                        {% endblock isYourTurn_patch1 %}

                        console.log(`[methods updateYourTurn 2] isYourTurn=${isYourTurn}`);

                        // v-show="" は複雑なメソッドを指定すると動かないようなので、プロパティにします
                        this.isYourTurn = isYourTurn;
                    },
                    raiseRoomStateChanged() {
                        console.log(`[methods raiseRoomStateChanged] roomState=${this.roomState.value}`);
                        this.isGameover = this.roomState.value == RoomState.none;

                        this.updateYourTurn();
                    },
                    raiseMyTurnChanged() {
                        console.log(`[methods raiseMyTurnChanged]`);
                        this.updateYourTurn();
                    },
                    raisePositionChanged() {
                        console.log(`[methods raisePositionChanged]`);
                        this.raiseMyTurnChanged();
                    },
                    {% block methods_footer %}
                    // メソッドを追加したければ、ここに挿しこめる
                    {% endblock methods_footer %}
                    /**
                     * ダンプ
                     */
                    dump() {
                        console.log(`[DUMP] vue1\n${this.engine.dump("")}`)
                    },
                },
            });

            console.log(`[HTML] ★WS接続`);
            connection.connect();
        </script>
    </body>
</html>
{# EOF OA16o3o0g6o0 #}
```

## Step OA16o3o0g7o0 対局画面作成 - gui/playing/v1o1o0.html.txt ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       ├── 📂 gui
                │       │   └── 📂 connection
                │       │       └── 📄 v1o0.js
                │       └── 📂 msg
                │           └── 📂 s2c_message_driven
                │               └── 📄 v1o0.js
                └── 📂 templates
                    └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                        └── 📂 gui
                            ├── 📂 match_application
                            │   └── 📄 v1o0.html
                            └── 📂 playing
                                ├── 📄 v1o0.html
👉                              └── 📄 v1o1o0.html.txt
```

👆 自動フォーマットされてくないので、拡張子をテキストファイルにしておく  

```html
{# OA16o3o0g7o0 #}
<!-- -->
{% extends "tic_tac_toe_v2/gui/playing/v1o0.html" %}
{#          ------------------------------------
            1
1. src1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/gui/playing/v1o0.html
                                       ------------------------------------

    自動フォーマットしないでください
    Do not auto fomatting
#}

{% block footer_section1 %}
    <v-container>
        <v-btn block elevation="2" v-on:click="clickPlayAgain()" :disabled="isDisabledPlayAgainButton()"> Play again </v-btn>
    </v-container>
{% endblock footer_section1 %}

{% block methods_footer %}
    /**
     *
     */
    clickPlayAgain() {
        console.log(`Play Again`);

        // 対局開始時
        this.onStart();
    },
    /**
     * Play again ボタンは非表示か
     */
    isDisabledPlayAgainButton() {
        switch (this.roomState.value) {
            case RoomState.none: // ゲームオーバー中
                return false; // Enable
            default:
                return true; // Disable
        }
    },
{% endblock methods_footer %}
```

## Step OA16o3o0g8o0 通信プロトコル作成 - gui/message_driven/v1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       ├── 📂 gui
                │       │   └── 📂 connection
                │       │       └── 📄 v1o0.js
                │       └── 📂 msg
                │           └── 📂 s2c_message_driven
                │               └── 📄 v1o0.js
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                │       └── 📂 gui
                │           ├── 📂 match_application
                │           │   └── 📄 v1o0.html
                │           └── 📂 playing
                │               ├── 📄 v1o0.html
                │               └── 📄 v1o1o0.html.txt
                └── 📂 websocks
                    └── 📂 gui
                        └── 📂 message_driven
👉                          └── 📄 v1o0.py
```

```py
# BOF OA16o3o0g8o0

class TicTacToeV2MessageDriven():
    """OA16o3o0g8o0 〇×ゲーム v2 メッセージ駆動"""

    def __init__(self):
        self._handlersAsync = {}

    def addHandler(self, eventName, handlerAsync):
        self._handlersAsync[eventName] = handlerAsync

    async def execute(self, scope, doc_received):
        """クライアントからサーバーへ送られてきた変数を解析し、
        サーバーからクライアントへ送信するメッセージの作成"""

        # ログインしていなければ AnonymousUser
        # user = scope["user"]
        # print(f"[TicTacToeV2MessageDriven execute] user=[{user}]")

        # `c2s_` は クライアントからサーバーへ送られてきた変数の目印
        eventName = doc_received.get("c2s_event", None)

        if(eventName in self._handlersAsync):
            response_json = await self._handlersAsync[eventName](scope, doc_received)
            return response_json

        raise ValueError(
            f"[TicTacToeV2MessageDriven execute] unknown event: {eventName}")


# EOF OA16o3o0g8o0
```

## Step OA16o3o0g9o0 Webソケットの通信プロトコル作成 - gui/consumer/v1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       ├── 📂 gui
                │       │   └── 📂 connection
                │       │       └── 📄 v1o0.js
                │       └── 📂 msg
                │           └── 📂 s2c_message_driven
                │               └── 📄 v1o0.js
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                │       └── 📂 gui
                │           ├── 📂 match_application
                │           │   └── 📄 v1o0.html
                │           └── 📂 playing
                │               ├── 📄 v1o0.html
                │               └── 📄 v1o1o0.html.txt
                └── 📂 websocks
                    └── 📂 gui
                        ├── 📂 consumer
👉                      │   └── 📄 v1o0.py
                        └── 📂 message_driven
                            └── 📄 v1o0.py
```

```py
# BOF OA16o3o0g9o0

# 参考にした記事
# -------------
# 📖[Django Channels and WebSockets](https: // blog.logrocket.com/django-channels-and-websockets/)
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class TicTacToeV2ConsumerBase(AsyncJsonWebsocketConsumer):
    """OA16o3o0g9o0 Webソケット用コンシューマー"""

    def __init__(self):
        super().__init__()

    async def connect(self):
        """接続"""
        print("Connect")
        # ログインしていれば、ユーザーのPrimaryKeyは以下で取得可能。ログインしていなければ None
        # print(f'Connect self.scope["user"].pk={self.scope["user"].pk}')

        self.room_name = self.scope['url_route']['kwargs']['kw_room_name']
        self.room_group_name = f'room_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        """切断"""
        print("Disconnected")
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """クライアントからのメッセージの受信"""

        # ちゃんと動いているようなら消す
        # print(f"[TicTacToeV2ConsumerBase receive] text_data={text_data}")

        doc_received = json.loads(text_data)

        response = await self.on_receive(doc_received)

        # 部屋のメンバーに一斉送信します
        await self.channel_layer.group_send(self.room_group_name, response)

    async def on_receive(self, doc_received):
        """クライアントからメッセージを受信したとき

        Returns
        -------
        response
        """
        return {}  # Empty

    async def send_message(self, message):
        """メッセージ送信"""
        await self.send(text_data=json.dumps({
            "message": message,
        }))

# EOF OA16o3o0g9o0
```

## Step OA16o3o0gA10o0 Webソケットの通信プロトコル作成 - gui/consumer/v1o1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       ├── 📂 gui
                │       │   └── 📂 connection
                │       │       └── 📄 v1o0.js
                │       └── 📂 msg
                │           └── 📂 s2c_message_driven
                │               └── 📄 v1o0.js
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                │       └── 📂 gui
                │           ├── 📂 match_application
                │           │   └── 📄 v1o0.html
                │           └── 📂 playing
                │               ├── 📄 v1o0.html
                │               └── 📄 v1o1o0.html.txt
                └── 📂 websocks
                    └── 📂 gui
                        ├── 📂 consumer
                        │   ├── 📄 v1o0.py
👉                      │   └── 📄 v1o1o0.py
                        └── 📂 message_driven
                            └── 📄 v1o0.py
```

```py
# BOF OA16o3o0gA10o0

# Webソケット コンシューマー v1.0
from apps1.tic_tac_toe_v2.websocks.gui.consumer.v1o0 import TicTacToeV2ConsumerBase
#          --------------                       ----        -----------------------
#          11                                   12          2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス

# 〇×ゲーム v2 Webソケット メッセージ駆動 v1.0
from apps1.tic_tac_toe_v2.websocks.gui.message_driven.v1o0 import TicTacToeV2MessageDriven
#          --------------                             ----        ------------------------
#          11                                         12          2
#    -----------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス

# OA16o3o_2o0g1o0 S2C JSON ジェネレーター
from apps1.tic_tac_toe_v2.views.msg.s2c_json_gen.commands.v1o0 import S2cJsonGenCommands as CommandsGen
#          --------------                                 ----        ------------------    -----------
#          11                                             12          2                     3
#    ---------------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス
# 3. `2.` の別名


class TicTacToeV2o1o0ConsumerCustom(TicTacToeV2ConsumerBase):
    """OA16o3o0gA10o0 Webソケット用コンシューマー"""

    def __init__(self):
        super().__init__()

        self._messageDriven = TicTacToeV2MessageDriven()
        self._messageDriven.addHandler('C2S_End', self.on_end)
        self._messageDriven.addHandler('C2S_Moved', self.on_move)
        self._messageDriven.addHandler('C2S_Start', self.on_start)

    async def on_receive(self, doc_received):
        """クライアントからメッセージを受信したとき

        Returns
        -------
        response
        """

        return await self._messageDriven.execute(self.scope, doc_received)

    async def on_end(self, scope, doc_received):
        """対局終了時"""
        print("[TicTacToeV2MessageDriven on_end]")
        # TODO 現状、クライアント側から勝者を送ってきているが、勝敗判定のロジックはサーバー側に置きたい
        winner = doc_received.get("c2s_winner", None)

        args = {
            "player1": winner
        }

        return CommandsGen.create_end(args)

    async def on_move(self, scope, doc_received):
        """駒を置いたとき"""

        # `s2c_` は サーバーからクライアントへ送る変数の目印
        c2s_sq = doc_received.get("c2s_sq", None)
        piece_moved = doc_received.get("c2s_pieceMoved", None)
        print(
            f"[TicTacToeV2MessageDriven on_move] C2S_Moved c2s_sq=[{c2s_sq}] piece_moved=[{piece_moved}]")

        args = {
            "sq1": c2s_sq,
            "piece1": piece_moved,
        }

        return CommandsGen.create_moved(args)

    async def on_start(self, scope, doc_received):
        """対局開始時"""
        print("[TicTacToeV2MessageDriven on_start]")

        args = {}

        return CommandsGen.create_start(args)

# EOF OA16o3o0gA10o0
```

## Step OA16o3o0gA11o0 ビュー作成 - gui/match_application/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       ├── 📂 gui
                │       │   └── 📂 connection
                │       │       └── 📄 v1o0.js
                │       └── 📂 msg
                │           └── 📂 s2c_message_driven
                │               └── 📄 v1o0.js
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                │       └── 📂 gui
                │           ├── 📂 match_application
                │           │   └── 📄 v1o0.html
                │           └── 📂 playing
                │               ├── 📄 v1o0.html
                │               └── 📄 v1o1o0.html.txt
                ├── 📂 views
                │   └── 📂 gui
                │       └── 📂 match_application
                │           └── 📂 v1o0
👉              │               └── 📄 __init__.py
                └── 📂 websocks
                    └── 📂 gui
                        ├── 📂 consumer
                        │   ├── 📄 v1o0.py
                        │   └── 📄 v1o1o0.py
                        └── 📂 message_driven
                            └── 📄 v1o0.py
```

```py
import json


class MatchApplicationV():
    """OA16o3o0gA11o0 対局申込ビュー"""

    # 対局申込 - 訪問後
    open_context = {
        # `dj_` は Djangoでレンダーするパラメーター名の目印
        # 入場者データ
        "dj_visitor_value": "X",
        # Python と JavaScript 間で配列データを渡すために JSON 文字列形式にします
        "dj_visitor_select": json.dumps([
            {"text": "X", "value": "X"},
            {"text": "O", "value": "O"},
        ]),
    }

    playing_web_path = "/tic-tac-toe/v2/playing/{0}/?&myturn={1}"
    #                                 ^ two
    #                   ----------------------------------------
    #                   1
    # 1. `http://example.com:8000/tic-tac-toe/v2/playing/Elephant/?&myturn=X`
    #                            -------------------------------------------

    template_path = "tic_tac_toe_v2/gui/match_application/v1o0.html"
    #                             ^two
    #                ----------------------------------------------
    #                1
    # 1. src1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/gui/match_application/v1o0.html
    #                                        ----------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_match_application
        #    ---------        ------------------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_v2/views/gui/match_application/v1o0/v_render.py`
        #                                                                --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV.playing_web_path,
            MatchApplicationV.template_path,
            MatchApplicationV.on_sent,
            MatchApplicationV.open)

    @staticmethod
    def on_sent(request):
        """送信後"""
        pass

    @staticmethod
    def open(request):
        """訪問後"""
        return MatchApplicationV.open_context
```

## Step OA16o3o0gA12o0 ビュー作成 - gui/match_application/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       ├── 📂 gui
                │       │   └── 📂 connection
                │       │       └── 📄 v1o0.js
                │       └── 📂 msg
                │           └── 📂 s2c_message_driven
                │               └── 📄 v1o0.js
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                │       └── 📂 gui
                │           ├── 📂 match_application
                │           │   └── 📄 v1o0.html
                │           └── 📂 playing
                │               ├── 📄 v1o0.html
                │               └── 📄 v1o1o0.html.txt
                ├── 📂 views
                │   └── 📂 gui
                │       └── 📂 match_application
                │           └── 📂 v1o0
                │               ├── 📄 __init__.py
👉              │               └── 📄 v_render.py
                └── 📂 websocks
                    └── 📂 gui
                        ├── 📂 consumer
                        │   ├── 📄 v1o0.py
                        │   └── 📄 v1o1o0.py
                        └── 📂 message_driven
                            └── 📄 v1o0.py
```

```py
# BOF OA16o3o0gA12o0

from django.shortcuts import render, redirect


def render_match_application(request, playing_web_path, match_application_tp, on_sent, on_open):
    """OA16o3o0gA12o0 対局申込 - 描画

    Parameters
    ----------
    match_application_tp : str
        Template path
    """
    if request.method == "POST":
        # 送信後
        on_sent(request)

        # `po_` は POST送信するパラメーター名の目印
        po_room_name = request.POST.get("po_room_name")
        # 自分の番。 "X" か "O"。 機能拡張も想定
        my_turn = request.POST.get("po_my_turn")

        # TODO バリデーションチェックしたい

        return redirect(playing_web_path.format(po_room_name, my_turn))

    # 訪問後
    context = on_open(request)

    return render(request, match_application_tp, context)

# EOF OA16o3o0gA12o0
```

## Step OA16o3o0gA13o0 ビュー作成 - gui/playing/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       ├── 📂 gui
                │       │   └── 📂 connection
                │       │       └── 📄 v1o0.js
                │       └── 📂 msg
                │           └── 📂 s2c_message_driven
                │               └── 📄 v1o0.js
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                │       └── 📂 gui
                │           ├── 📂 match_application
                │           │   └── 📄 v1o0.html
                │           └── 📂 playing
                │               ├── 📄 v1o0.html
                │               └── 📄 v1o1o0.html.txt
                ├── 📂 views
                │   └── 📂 gui
                │       ├── 📂 match_application
                │       │   └── 📂 v1o0
                │       │       ├── 📄 __init__.py
                │       │       └── 📄 v_render.py
                │       └── 📂 playing
                │           └── 📂 v1o0
👉              │               └── 📄 __init__.py
                └── 📂 websocks
                    └── 📂 gui
                        ├── 📂 consumer
                        │   ├── 📄 v1o0.py
                        │   └── 📄 v1o1o0.py
                        └── 📂 message_driven
                            └── 📄 v1o0.py
```

```py
class PlayingV():
    """OA16o3o0gA13o0 対局中ビュー"""

    # 駒
    expected_pieces = ['X', 'O']

    # Webソケット v2
    web_socket_path = "/tic-tac-toe/v2/playing/"
    #                                ^two
    #                  ------------------------
    #                  1
    # 1. `ws://example.com:8000/tic-tac-toe/v2/playing/`
    #                          ------------------------

    # HTML
    template_path = "tic_tac_toe_v2/gui/playing/v1o1o0.html.txt"
    #                             ^two
    #                ------------------------------------------
    #                1
    # 1. `src1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/gui/playing/v1o1o0.html.txt`
    #                                         ------------------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_playing
        #    ---------        --------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_v2/views/gui/playing/v1o0/v_render.py`
        #                                                      --------
        # 2. `1.` に含まれる関数

        return render_playing(
            request,
            kw_room_name,
            PlayingV.web_socket_path,
            PlayingV.template_path,
            PlayingV.on_update,
            PlayingV.expected_pieces)

    @staticmethod
    def on_update(request):
        """訪問後または送信後"""
        # 拡張したい挙動があれば、ここに書く
        pass
```

## Step OA16o3o0gA14o0 ビュー作成 - gui/playing/v1o0/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       ├── 📂 gui
                │       │   └── 📂 connection
                │       │       └── 📄 v1o0.js
                │       └── 📂 msg
                │           └── 📂 s2c_message_driven
                │               └── 📄 v1o0.js
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                │       └── 📂 gui
                │           ├── 📂 match_application
                │           │   └── 📄 v1o0.html
                │           └── 📂 playing
                │               ├── 📄 v1o0.html
                │               └── 📄 v1o1o0.html.txt
                ├── 📂 views
                │   └── 📂 gui
                │       ├── 📂 match_application
                │       │   └── 📂 v1o0
                │       │       ├── 📄 __init__.py
                │       │       └── 📄 v_render.py
                │       └── 📂 playing
                │           └── 📂 v1o0
                │               ├── 📄 __init__.py
👉              │               └── 📄 v_render.py
                └── 📂 websocks
                    └── 📂 gui
                        ├── 📂 consumer
                        │   ├── 📄 v1o0.py
                        │   └── 📄 v1o1o0.py
                        └── 📂 message_driven
                            └── 📄 v1o0.py
```

```py
# BOF OA16o3o0gA14o0

from django.http import Http404
from django.shortcuts import render


def render_playing(request, kw_room_name, wsp_playing, playing_tp, on_update, expected_pieces):
    """OA16o3o0gA14o0 対局中 - 描画

    Parameters
    ----------
    wsp_playing : str
        Webソケットパス
    playing_tp : str
        Template path
    """

    my_turn = request.GET.get("myturn")
    if my_turn not in expected_pieces:
        raise Http404(f"My piece '{my_turn}' does not exists")

    on_update(request)

    # `dj_` は Djangoでレンダーするパラメーター名の目印
    context = {
        "dj_room_name": kw_room_name,
        "dj_my_turn": my_turn,
        "dj_path_of_ws_playing": wsp_playing,
    }
    return render(request, playing_tp, context)

# EOF OA16o3o0gA14o0
```

## ~~Step OA16o3o0gA15o0~~

Merged to OA16o3o0gA15o1o0  

## Step OA16o3o0gA15o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 tic_tac_toe_v2    # アプリケーション
    │           ├── 📂 static
    │           │   └── 📂 tic_tac_toe_v2
    │           │       ├── 📂 gui
    │           │       │   └── 📂 connection
    │           │       │       └── 📄 v1o0.js
    │           │       └── 📂 msg
    │           │           └── 📂 s2c_message_driven
    │           │               └── 📄 v1o0.js
    │           ├── 📂 templates
    │           │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
    │           │       └── 📂 gui
    │           │           ├── 📂 match_application
    │           │           │   └── 📄 v1o0.html
    │           │           └── 📂 playing
    │           │               ├── 📄 v1o0.html
    │           │               └── 📄 v1o1o0.html.txt
    │           ├── 📂 views
    │           │   └── 📂 gui
    │           │       ├── 📂 match_application
    │           │       │   └── 📂 v1o0
    │           │       │       ├── 📄 __init__.py
    │           │       │       └── 📄 v_render.py
    │           │       └── 📂 playing
    │           │           └── 📂 v1o0
    │           │               ├── 📄 __init__.py
    │           │               └── 📄 v_render.py
    │           └── 📂 websocks
    │               └── 📂 gui
    │                   ├── 📂 consumer
    │                   │   ├── 📄 v1o0.py
    │                   │   └── 📄 v1o1o0.py
    │                   └── 📂 message_driven
    │                       └── 📄 v1o0.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_tic_tac_toe_v2_autogen.py,tic-tac-toe/v2/match-application/,,"OA16o3o0gA15o1o0 〇×ゲーム v2 対局申込ページ",apps1.tic_tac_toe_v2.views.gui.match_application.v1o0,MatchApplicationV,,render
../src1/project1/urls_tic_tac_toe_v2_autogen.py,tic-tac-toe/v2/playing/<str:kw_room_name>/,,"OA16o3o0gA15o1o0 〇×ゲーム v2 対局中ページ",apps1.tic_tac_toe_v2.views.gui.playing.v1o0,PlayingV,,render
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

## Step OA16o3o0gA16o0 Webソケット用ルート新規作成 - ws_urls_tic_tac_toe_v2.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v2    # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v2
        │       │       ├── 📂 gui
        │       │       │   └── 📂 connection
        │       │       │       └── 📄 v1o0.js
        │       │       └── 📂 msg
        │       │           └── 📂 s2c_message_driven
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
        │       │       └── 📂 gui
        │       │           ├── 📂 match_application
        │       │           │   └── 📄 v1o0.html
        │       │           └── 📂 playing
        │       │               ├── 📄 v1o0.html
        │       │               └── 📄 v1o1o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 gui
        │       │       ├── 📂 match_application
        │       │       │   └── 📂 v1o0
        │       │       │       ├── 📄 __init__.py
        │       │       │       └── 📄 v_render.py
        │       │       └── 📂 playing
        │       │           └── 📂 v1o0
        │       │               ├── 📄 __init__.py
        │       │               └── 📄 v_render.py
        │       └── 📂 websocks
        │           └── 📂 gui
        │               ├── 📂 consumer
        │               │   ├── 📄 v1o0.py
        │               │   └── 📄 v1o1o0.py
        │               └── 📂 message_driven
        │                   └── 📄 v1o0.py
        └── 📂 project1                      # プロジェクト
            ├── 📄 urls_tic_tac_toe_v2.py
👉          └── 📄 ws_urls_tic_tac_toe_v2.py
```

```py
# BOF OA16o3o0gA16o0

# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# OA16o3o0gA16o0 〇×ゲーム v2
from apps1.tic_tac_toe_v2.websocks.gui.consumer.v1o1o0 import TicTacToeV2o1o0ConsumerCustom
#          --------------                       ------        -----------------------------
#          11                                   12            2
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス


websocket_urlpatterns = [

    # OA16o3o0gA16o0 〇×ゲーム v2
    url(r'^tic-tac-toe/v2/playing/(?P<kw_room_name>\w+)/$',
        # -----------------------------------------------
        # 1
        TicTacToeV2o1o0ConsumerCustom.as_asgi()),
    #   ---------------------------------------
    #   2
    # 1. 例えば `ws://example.com/tic-tac-toe/v2/playing/Elephant/` のようなURLのパスの部分
    #                            --------------------------------
    #    kw_room_name は変数として渡される
    # 2. クラス名とメソッド。 URL を ASGI形式にする
]

# EOF OA16o3o0gA16o0
```

## Step OA16o3o0gA17o0 Webソケット用総合ルート編集 - asgi.py ファイル＜その２＞

👇以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v2    # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v2
        │       │       ├── 📂 gui
        │       │       │   └── 📂 connection
        │       │       │       └── 📄 v1o0.js
        │       │       └── 📂 msg
        │       │           └── 📂 s2c_message_driven
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
        │       │       └── 📂 gui
        │       │           ├── 📂 match_application
        │       │           │   └── 📄 v1o0.html
        │       │           └── 📂 playing
        │       │               ├── 📄 v1o0.html
        │       │               └── 📄 v1o1o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 gui
        │       │       ├── 📂 match_application
        │       │       │   └── 📂 v1o0
        │       │       │       ├── 📄 __init__.py
        │       │       │       └── 📄 v_render.py
        │       │       └── 📂 playing
        │       │           └── 📂 v1o0
        │       │               ├── 📄 __init__.py
        │       │               └── 📄 v_render.py
        │       └── 📂 websocks
        │           └── 📂 gui
        │               ├── 📂 consumer
        │               │   ├── 📄 v1o0.py
        │               │   └── 📄 v1o1o0.py
        │               └── 📂 message_driven
        │                   └── 📄 v1o0.py
        └── 📂 project1                      # プロジェクト
👉          ├── 📄 asgi.py
            ├── 📄 urls_tic_tac_toe_v2.py
            └── 📄 ws_urls_tic_tac_toe_v2.py
```

```py
# ...略...


# * 以下を追加
# OA16o3o0gA17o0 〇×ゲーム v2
from . import ws_urls_tic_tac_toe_v2
#                                  ^two
#    -        ----------------------
#    1        2
# 1. 同じディレクトリー
# 2. `src1/projectN/ws_urls_tic_tac_toe_v2.py`
#                   ----------------------


# ...略...
# この辺に os.environ.setdefault(...)


# ...略...


# 複数のアプリケーションの websocket_urlpatterns をマージします
websocket_urlpatterns_merged = []


# ...略...


# * 以下を追加
# OA16o3o0gA17o0 〇×ゲーム v2
websocket_urlpatterns_merged.extend(
    ws_urls_tic_tac_toe_v2.websocket_urlpatterns)
#                        ^two
```

## Step OA16o3o0gA18o0 Web画面へアクセス

このゲームは２人用なので、Webページを２窓で開き、片方が X プレイヤー、もう片方が O プレイヤーとして遊んでください  

📖 [http://localhost:8000/tic-tac-toe/v2/match-application/](http://localhost:8000/tic-tac-toe/v2/match-application/)  

## Step OA16o3o0gA19o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 tic_tac_toe_v2                # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v2
        │       │       ├── 📂 gui
        │       │       │   └── 📂 connection
        │       │       │       └── 📄 v1o0.js
        │       │       └── 📂 msg
        │       │           └── 📂 s2c_message_driven
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v2
        │       │       └── 📂 gui
        │       │           ├── 📂 match_application
        │       │           │   └── 📄 v1o0.html
        │       │           └── 📂 playing
        │       │               ├── 📄 v1o0.html
        │       │               └── 📄 v1o1o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 gui
        │       │       ├── 📂 match_application
        │       │       │   └── 📂 v1o0
        │       │       │       ├── 📄 __init__.py
        │       │       │       └── 📄 v_render.py
        │       │       └── 📂 playing
        │       │           └── 📂 v1o0
        │       │               ├── 📄 __init__.py
        │       │               └── 📄 v_render.py
        │       └── 📂 websocks
        │           └── 📂 gui
        │               ├── 📂 consumer
        │               │   ├── 📄 v1o0.py
        │               │   └── 📄 v1o1o0.py
        │               └── 📂 message_driven
        │                   └── 📄 v1o0.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 asgi.py
            ├── 📄 urls_tic_tac_toe_v2.py
            └── 📄 ws_urls_tic_tac_toe_v2.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/tic-tac-toe/v2/match-application/,〇×ゲーム v2
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Django さくらVPS 備忘録](https://qiita.com/muzudho1/items/1d3b4b5608716463184c)  

# 参考にした記事

## Vuetify 関連

📖 [Vuetifyのv-selectにてitemsのキーがtextとvalueじゃないときの対処法](https://qiita.com/akido_/items/96ced6cd5fd9929c666f)  

## Web socket 関連

📖 [Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)  

## メモリ関連

📖 [メモリ管理](https://developer.mozilla.org/ja/docs/Web/JavaScript/Memory_Management)  
