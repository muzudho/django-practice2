# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/tic-tac-toe/vol1.0/match-application/ver1.0/)  

# 目標

Webサーバーと、クライアント側のアプリ間で通信する練習をしたい。  
だから 〇×ゲーム（Tic tac toe）のサンプルプログラムを真似する。  
１人２役で２窓で遊ぶ  

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
| Database         | Redis                                     |
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
    ├── 📂 src1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 accounts_vol1o0    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   └── 📂 practice_vol1o0              # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       │   └── 📂 practice_vol1o0
    │   │       │       └── 📂 data
    │   │       │           └── 📂 desserts1
    │   │       │               └── 📄 ver1o0.json
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_vol1o0          # アプリケーションと同名
    │   │       │       ├── 📂 prefecture
    │   │       │       └── 📂 vuetifies
    │   │       ├── 📂 views
    │   │       │   ├── 📂 prefecture
    │   │       │   └── 📂 vuetifies
    │   │       ├── 📂 websocks
    │   │       │   └── 📂 consumer
    │   │       │       └── 📄 ver1o0.py
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
    │   │   ├── 📄 urls.py
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

## Step [OA16o1o0g1o0] Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step [OA16o1o0g2o0] Pythonパッケージ インストール指定 - requirements.txt ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1                   # あなたの開発用ディレクトリー。任意の名前
👉      └── 📄 requirements.txt
```

```shell
# ...略...


# 以下を追加
# For tic-tac-toe-v1
channels_redis>=3.2
```

## Step [OA16o1o0g3o0] Dockerコンテナの停止～ビルド～起動

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

👆 これで Dockerコンテナに channels_redis パッケージをインストールした  

## Step [OA16o1o0g4o0] フォルダー作成 - apps1/tic_tac_toe_vol1o0 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
👉      │   └── 📂 tic_tac_toe_vol1o0    # アプリケーション
        └── 📄 requirements.txt
```

## Step [OA16o1o0g5o0] アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp tic_tac_toe_vol1o0 ./apps1/tic_tac_toe_vol1o0
#                                                     ------------------ --------------------------
#                                                     1                  2
# 1. 任意のDjangoアプリケーション名
# 2. 既存のアプリケーション ディレクトリーへのパス
```

👇 以下のようなディレクトリー、ファイルが自動生成される  

```plaintext
    └── 📂 src1
        └── 📂 apps1
👉          └── 📂 tic_tac_toe_vol1o0    # アプリケーション
👉              ├── 📂 migrations
👉              │   └── 📄 __init__.py
👉              ├── 📄 __init__.py
👉              ├── 📄 admin.py
👉              ├── 📄 apps.py
👉              ├── 📄 models.py
👉              ├── 📄 tests.py
👉              └── 📄 views.py
```

## Step [OA16o1o0g6o0] 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol1o0    # アプリケーション
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
                ├── 📄 apps.py
👉              ├── 📄 models.py
                ├── 📄 tests.py
👉              └── 📄 views.py
```

## Step [OA16o1o0g7o0] アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol1o0    # アプリケーション
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
👉              ├── 📄 apps.py
                └── 📄 tests.py
```

```py
from django.apps import AppConfig


class TicTacToeV1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    # name = 'tic_tac_toe_vol1o0'
    # * OA16o1o0g7o0 変更後
    name = 'apps1.tic_tac_toe_vol1o0'
    #       ------------------------
    #       1
    # 1. `src1/apps1/tic_tac_toe_vol1o0/apps.py`
    #          ------------------------
```

## Step [OA16o1o0g8o0] アプリケーション登録 - settings.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol1o0    # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
👉          └── 📄 settings.py
```

```py
# ...略...


INSTALLED_APPS = [
    # あなたが追加したアプリケーション


    # ...略...


    # OA16o1o0g8o0 〇×ゲーム1.0巻
    'apps1.tic_tac_toe_vol1o0',


    # ...略...
]
```

## Step [OA16o1o0g9o0] Web ページのスタイル作成 - style/main/ver1o0.css ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol1o0        # アプリケーションと同名
        │       │       └── 📂 style                 # ただのフォルダー
        │       │           └── 📂 main              # ただのフォルダー
👉      │       │               └── 📄 ver1o0.css
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```css
/*
 * OA16o1o0g9o0
 * See also : 📖 [Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)
 */
body {
  /* width: 100%; */
  height: 90vh;
  background: #f1f1f1;
  display: flex;
  justify-content: center;
  align-items: center;
}
#board {
  display: grid;
  grid-gap: 0.5em;
  grid-template-columns: repeat(3, 1fr);
  width: 16em;
  height: auto;
  margin: 0.5em 0;
}
.square {
  background: #2f76c7;
  width: 5em;
  height: 5em;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 0.5em;
  font-weight: 500;
  color: white;
  box-shadow: 0.025em 0.125em 0.25em rgba(0, 0, 0, 0.25);
}
.head {
  width: 16em;
  text-align: center;
}
.wrapper h1,
h3 {
  color: #0a2c1a;
}
label {
  font-size: 20px;
  color: #0a2c1a;
}
input,
select {
  margin-bottom: 10px;
  width: 100%;
  padding: 15px;
  border: 1px solid #125a33;
  font-size: 14px;
  background-color: #71d19e;
  color: white;
}
.button {
  color: white;
  white-space: nowrap;
  background-color: #31d47d;
  padding: 10px 20px;
  border: 0;
  border-radius: 2px;
  transition: all 150ms ease-out;
}
```

## Step [OA16o1o0gA10o0] 機能作成 - scripts/play/ver1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 style
        │       │       │   └── 📂 main
        │       │       │       └── 📄 ver1o0.css
        │       │       └── 📂 scripts
        │       │           └── 📂 play
👉      │       │               └── 📄 ver1o0.js
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```js
// BOF OA16o1o0gA10o0

// See also: 📖[Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)

let roomName = document.getElementById("board").getAttribute("room_name");
let myPiece = document.getElementById("board").getAttribute("my_piece");

let connectionString = `ws://${window.location.host}/tic-tac-toe/v1/playing/${roomName}/`;
//                      ----]----------------------- -----------------------------------
//                      11   12                      13
//                      ----------------------------------------------------------------
//                      10
// 10. URL
// 11. スキーム : Web Socket
// 12. ホスト アドレス
// 13. パス

let webSock1 = new WebSocket(connectionString);

const PC_EMPTY = -1; // A square without piece; PC is piece
// Game board for maintaing the state of the game
let board = [PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY];

// SQ is square
// +---------+
// | 0  1  2 |
// | 3  4  5 |
// | 6  7  8 |
// +---------+
const SQ_0 = 0;
const SQ_1 = 1;
const SQ_2 = 2;
const SQ_3 = 3;
const SQ_4 = 4;
const SQ_5 = 5;
const SQ_6 = 6;
const SQ_7 = 7;
const SQ_8 = 8;

// Winning indexes.
arrayOfSquaresOfWinPattern = [
    // +---------+
    // | *  *  * |
    // | .  .  . |
    // | .  .  . |
    // +---------+
    [SQ_0, SQ_1, SQ_2],
    // +---------+
    // | .  .  . |
    // | *  *  * |
    // | .  .  . |
    // +---------+
    [SQ_3, SQ_4, SQ_5],
    // +---------+
    // | .  .  . |
    // | .  .  . |
    // | *  *  * |
    // +---------+
    [SQ_6, SQ_7, SQ_8],
    // +---------+
    // | *  .  . |
    // | *  .  . |
    // | *  .  . |
    // +---------+
    [SQ_0, SQ_3, SQ_6],
    // +---------+
    // | .  *  . |
    // | .  *  . |
    // | .  *  . |
    // +---------+
    [SQ_1, SQ_4, SQ_7],
    // +---------+
    // | .  .  * |
    // | .  .  * |
    // | .  .  * |
    // +---------+
    [SQ_2, SQ_5, SQ_8],
    // +---------+
    // | *  .  . |
    // | .  *  . |
    // | .  .  * |
    // +---------+
    [SQ_0, SQ_4, SQ_8],
    // +---------+
    // | .  .  * |
    // | .  *  . |
    // | *  .  . |
    // +---------+
    [SQ_2, SQ_4, SQ_6],
];
let countOfMove = 0; // Number of moves done
let myTurn = true; // Boolean variable to get the turn of the player.

// Add the click event listener on every block.
let elementArrayOfSquare = document.getElementsByClassName("square");
for (const element of elementArrayOfSquare) {
    element.addEventListener("click", (event) => {
        const sq = event.path[0].getAttribute("square"); // Square; 0 <= sq
        if (board[sq] == PC_EMPTY) {
            if (!myTurn) {
                alert("Wait for other to place the move");
            } else {
                myTurn = false;
                document.getElementById("alert_move").style.display = "none"; // Hide
                makeMove(sq, myPiece);
            }
        }
    });
}

/**
 * Make a move
 * @param {*} sq - Square; 0 <= sq
 * @param {*} myPiece
 * @returns
 */
function makeMove(sq, myPiece) {
    sq = parseInt(sq);
    let data = {
        event: "MOVE",
        message: {
            index: sq,
            player: myPiece,
        },
    };

    if (board[sq] == PC_EMPTY) {
        // if the valid move, update the board
        // state and send the move to the server.
        countOfMove++;

        switch (myPiece) {
            case "X":
                board[sq] = 1;
                break;
            case "O":
                board[sq] = 0;
                break;
            default:
                alert(`Invalid my piece = ${myPiece}`);
                return false;
        }

        webSock1.send(JSON.stringify(data));
    }
    // place the move in the game box.
    elementArrayOfSquare[sq].innerHTML = myPiece;
    // check for the winner
    const gameOver = isGameOver();
    if (myTurn) {
        // if player winner, send the END event.
        if (gameOver) {
            data = {
                event: "END",
                message: `${myPiece} is a winner. Play again?`,
            };
            webSock1.send(JSON.stringify(data));
        } else if (!gameOver && countOfMove == 9) {
            data = {
                event: "END",
                message: "It's a draw. Play again?",
            };
            webSock1.send(JSON.stringify(data));
        }
    }
}

// function to reset the game.
function reset() {
    board = [PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY];
    countOfMove = 0;
    myTurn = true;
    document.getElementById("alert_move").style.display = "inline";
    for (const element of elementArrayOfSquare) {
        element.innerHTML = "";
    }
}

/**
 * check if their is winning move
 * @param {*} squaresOfWinPattern
 * @returns
 */
function isPieceInLine(squaresOfWinPattern) {
    return board[squaresOfWinPattern[0]] !== PC_EMPTY && board[squaresOfWinPattern[0]] === board[squaresOfWinPattern[1]] && board[squaresOfWinPattern[0]] === board[squaresOfWinPattern[2]];
}

/**
 * function to check if player is winner.
 * @returns I won
 */
function isGameOver() {
    if (5 <= countOfMove) {
        for (let squaresOfWinPattern of arrayOfSquaresOfWinPattern) {
            if (isPieceInLine(squaresOfWinPattern)) {
                return true;
            }
        }
    }
    return false;
}

/**
 * Main function which handles the connection
 * of websocket.
 */
function connect() {
    // on websocket open, send the START event.
    webSock1.onopen = () => {
        // console.log("WebSockets connection created.");
        webSock1.send(
            JSON.stringify({
                event: "START",
                message: "",
            })
        );
    };

    webSock1.onclose = (e) => {
        // console.log("Socket is closed. Reconnect will be attempted in 1 second.", e.reason);
        setTimeout(function () {
            connect();
        }, 1000);
    };

    // Sending the info about the room
    webSock1.onmessage = (e) => {
        // On getting the message from the server
        // Do the appropriate steps on each event.
        let data = JSON.parse(e.data);
        data = data["payload"];
        let message = data["message"];
        let event = data["event"];
        switch (event) {
            case "START":
                console.log(`[Message] START e=${e.data}`); // ちゃんと動いているようなら消す
                reset();
                break;
            case "END":
                console.log(`[Message] END e=${e.data}`); // ちゃんと動いているようなら消す
                alert(message);
                reset();
                break;
            case "MOVE":
                console.log(`[Message] MOVE e=${e.data}`); // ちゃんと動いているようなら消す
                if (message["player"] != myPiece) {
                    makeMove(message["index"], message["player"]);
                    myTurn = true;
                    document.getElementById("alert_move").style.display = "inline";
                }
                break;
            default: // ちゃんと動いているようなら消す
                console.log(`[Message] (Others) e=${e.data}`);
                console.log("No event");
        }
    };

    if (webSock1.readyState == WebSocket.OPEN) {
        console.log("Open socket.");
        webSock1.onopen();
    }
}

//call the connect function at the start.
connect();

// EOF OA16o1o0gA10o0
```

## Step [OA16o1o0gA11o0] 対局申込画面作成 - match_application/ver1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 style
        │       │       │   └── 📂 main
        │       │       │       └── 📄 ver1o0.css
        │       │       └── 📂 scripts
        │       │           └── 📂 play
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol1o0        # アプリケーションと同名
        │       │       └── 📂 match_application
👉      │       │           └── 📄 ver1o0.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```html
<!-- BOF OA16o1o0gA11o0 -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Tic Tac Toe</title>
        <link rel="stylesheet" href='{% static "tic_tac_toe_vol1o0/style/main/ver1o0.css" %}' />
        <!--                            ================================================
                                        1
        1. `src1/apps1/tic_tac_toe_vol1o0/static/tic_tac_toe_vol1o0/style/main/ver1o0.css`
                                          ===============================================
        -->
    </head>
    <body>
        <div class="wrapper">
            <h1>Welcome to Tic Tac Toe Game Copy</h1>

            <p>📖 Original: <a href="https://blog.logrocket.com/django-channels-and-websockets/">Django Channels and WebSockets</a></p>

            <form method="POST">
                {% csrf_token %}
                <div class="form-control">
                    <label for="room">Room id</label>
                    <input id="room" type="text" name="room_name" required />
                </div>
                <div class="form-control">
                    <label for="item_of_my_piece">Your character</label>
                    <select for="item_of_my_piece" name="my_piece">
                        <option value="X">X</option>
                        <option value="O">O</option>
                    </select>
                </div>
                <input type="submit" class="button" value="Start Game" />
            </form>
        </div>
    </body>
</html>
<!-- EOF OA16o1o0gA11o0 -->
```

## Step [OA16o1o0gA12o0] 対局画面作成 - playing/ver1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 style
        │       │       │   └── 📂 main
        │       │       │       └── 📄 ver1o0.css
        │       │       └── 📂 scripts
        │       │           └── 📂 play
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol1o0        # アプリケーションと同名
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 ver1o0.html
        │       │       └── 📂 playing
👉      │       │           └── 📄 ver1o0.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```html
<!-- BOF OA16o1o0gA12o0 -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Tic Tac Toe</title>
        <link rel="stylesheet" href='{% static "tic_tac_toe_vol1o0/style/main/ver1o0.css" %}' />
        <!--                            ================================================
                                        1
        1. `src1/apps1/tic_tac_toe/static/tic_tac_toe_vol1o0/style/main/ver1o0.css`
                                   ===============================================
        -->
    </head>
    <body>
        <div class="wrapper">
            <div class="head">
                <h1>TIC TAC TOE</h1>
                <h3>Welcome to room_{{room_name}}</h3>
            </div>
            <div id="board" room_name="{{room_name}}" my_piece="{{my_piece}}">
                <div class="square" square="0"></div>
                <div class="square" square="1"></div>
                <div class="square" square="2"></div>
                <div class="square" square="3"></div>
                <div class="square" square="4"></div>
                <div class="square" square="5"></div>
                <div class="square" square="6"></div>
                <div class="square" square="7"></div>
                <div class="square" square="8"></div>
            </div>
            <div id="alert_move">Your turn. Place your move <strong>{{my_piece}}</strong></div>
        </div>

        <script src="{% static 'tic_tac_toe_vol1o0/scripts/play/ver1o0.js' %}"></script>
        <!--            =================================================
                        1
        1. `src1/apps1/tic_tac_toe_vol1o0/static/tic_tac_toe_vol1o0/scripts/play/ver1o0.js`
                                          ================================================
        -->
        {% block javascript %} {% endblock javascript %}
    </body>
</html>
<!-- EOF OA16o1o0gA12o0 -->
```

## Step [OA16o1o0gA13o0] ビュー作成 - match_application/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 style
        │       │       │   └── 📂 main
        │       │       │       └── 📄 ver1o0.css
        │       │       └── 📂 scripts
        │       │           └── 📂 play
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol1o0        # アプリケーションと同名
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 ver1o0.html
        │       │       └── 📂 playing
        │       │           └── 📄 ver1o0.html
        │       ├── 📂 views
        │       │   └── 📂 match_application
        │       │       └── 📂 ver1o0
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```py
# BOF OA16o1o0gA13o0

class MatchApplicationV():
    """OA16o1o0gA13o0 対局申込ビュー"""

    playing_web_path = "/tic-tac-toe/vol1.0/playing/ver1.0/{0}/?&mypiece={1}"
    #                                   ^one
    #                   ----------------------------------------------------
    #                   1
    # 1. `http://example.com:8000/tic-tac-toe/vol1.0/playing/ver1.0/Elephant/?&mypiece=X`
    #                            -------------------------------------------------------

    template_path = "tic_tac_toe_vol1o0/match_application/ver1o0.html"
    #                               ^one
    #                ------------------------------------------------
    #                1
    # 1. src1/apps1/tic_tac_toe_vol1o0/templates/tic_tac_toe_vol1o0/match_application/ver1o0.html
    #                                            ------------------------------------------------

    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_match_application
        #    ---------        ------------------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_vol1o0/views/match_application/v1o0/v_render.py`
        #                                                                --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV.playing_web_path,
            MatchApplicationV.template_path)

# EOF OA16o1o0gA13o0
```


## Step [OA16o1o0gA14o0] ビュー作成 - match_application/v1o0/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 style
        │       │       │   └── 📂 main
        │       │       │       └── 📄 ver1o0.css
        │       │       └── 📂 scripts
        │       │           └── 📂 play
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol1o0        # アプリケーションと同名
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 ver1o0.html
        │       │       └── 📂 playing
        │       │           └── 📄 ver1o0.html
        │       ├── 📂 views
        │       │   └── 📂 match_application
        │       │       └── 📂 ver1o0
        │       │           ├── 📄 __init__.py
👉      │       │           └── 📄 v_render.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```py
# BOF OA16o1o0gA14o0

from django.shortcuts import render, redirect


def render_match_application(request, upf_playing, match_application_tp):
    """OA16o1o0gA14o0 描画 - 対局申込

    Parameters
    ----------
    upf_playing : str
        Url Path Format
    match_application_tp : str
        Template path
    """

    if request.method == "POST":
        # 送信後
        room_name = request.POST.get("room_name")
        myPiece = request.POST.get("my_piece")
        # TODO バリデーションチェックしたい
        return redirect(upf_playing.format(room_name, myPiece))

    # 訪問後
    return render(request, match_application_tp, {})

# EOF OA16o1o0gA14o0
```

## Step [OA16o1o0gA15o0] ビュー作成 - playing/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 style
        │       │       │   └── 📂 main
        │       │       │       └── 📄 ver1o0.css
        │       │       └── 📂 scripts
        │       │           └── 📂 play
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol1o0        # アプリケーションと同名
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 ver1o0.html
        │       │       └── 📂 playing
        │       │           └── 📄 ver1o0.html
        │       ├── 📂 views
        │       │   ├── 📂 match_application
        │       │   │   └── 📂 ver1o0
        │       │   │       ├── 📄 __init__.py
        │       │   │       └── 📄 v_render.py
        │       │   └── 📂 playing
        │       │       └── 📂 ver1o0
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```py
# BOF OA16o1o0gA15o0

class PlayingV():
    """OA16o1o0gA15o0 対局中ビュー"""

    template_path = "tic_tac_toe_vol1o0/playing/ver1o0.html"
    #                                              ^one
    #                --------------------------------------
    #                1
    # 1. `src1/apps1/tic_tac_toe_vol1o0/templates/tic_tac_toe_vol1o0/playing/ver1o0.html`
    #                                             --------------------------------------

    def render(request, room_name):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_playing
        #    ---------        --------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_vol1o0/views/playing/v1o0/v_render.py`
        #                                                      --------
        # 2. `1.` に含まれる関数

        return render_playing(request, room_name, PlayingV.template_path)

# EOF OA16o1o0gA15o0
```

## Step [OA16o1o0gA16o0] ビュー作成 - playing/v1o0/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 style
        │       │       │   └── 📂 main
        │       │       │       └── 📄 ver1o0.css
        │       │       └── 📂 scripts
        │       │           └── 📂 play
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 ver1o0.html
        │       │       └── 📂 playing
        │       │           └── 📄 ver1o0.html
        │       ├── 📂 views
        │       │   ├── 📂 match_application
        │       │   │   └── 📂 ver1o0
        │       │   │       ├── 📄 __init__.py
        │       │   │       └── 📄 v_render.py
        │       │   └── 📂 playing
        │       │       └── 📂 ver1o0
        │       │           ├── 📄 __init__.py
👉      │       │           └── 📄 v_render.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```py
# BOF OA16o1o0gA16o0

from django.http import Http404
from django.shortcuts import render


def render_playing(request, room_name, playing_tp):
    """OA16o1o0gA16o0 描画 - 対局

    Parameters
    ----------
    playing_tp : str
        Template path
    """

    myPiece = request.GET.get("mypiece")
    if myPiece not in ['X', 'O']:
        raise Http404(f"My piece '{myPiece}' does not exists")

    context = {
        "my_piece": myPiece,
        "room_name": room_name
    }
    return render(request, playing_tp, context)

# EOF OA16o1o0gA16o0
```

## ~~Step [OA16o1o0gA17o0]~~

Merged to OA16o1o0gA17o1o0  

## Step [OA16o1o0gA17o1o0] ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_vol1o0
    │   │       │       ├── 📂 style
    │   │       │       │   └── 📂 main
    │   │       │       │       └── 📄 ver1o0.css
    │   │       │       └── 📂 scripts
    │   │       │           └── 📂 play
    │   │       │               └── 📄 ver1o0.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_vol1o0
    │   │       │       ├── 📂 match_application
    │   │       │       │   └── 📄 ver1o0.html
    │   │       │       └── 📂 playing
    │   │       │           └── 📄 ver1o0.html
    │   │       ├── 📂 views
    │   │       │   ├── 📂 match_application
    │   │       │   │   └── 📂 ver1o0
    │   │       │   │       ├── 📄 __init__.py
    │   │       │   │       └── 📄 v_render.py
    │   │       │   └── 📂 playing
    │   │       │       └── 📂 ver1o0
    │   │       │           ├── 📄 __init__.py
    │   │       │           └── 📄 v_render.py
    │   │       ├── 📄 __init__.py
    │   │       ├── 📄 admin.py
    │   │       ├── 📄 apps.py
    │   │       └── 📄 tests.py
    │   └── 📄 requirements.txt
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_tic_tac_toe_vol1o0_autogen.py,tic-tac-toe/vol1.0/match-application/ver1.0/,,"OA16o1o0gA17o1o0 〇×ゲーム1.0巻 対局申込中1.0版",apps1.tic_tac_toe_vol1o0.views.match_application.ver1o0,MatchApplicationV,,render
../src1/project1/urls_tic_tac_toe_vol1o0_autogen.py,tic-tac-toe/vol1.0/playing/ver1.0/<str:room_name>/,,"OA16o1o0gA17o1o0 〇×ゲーム1.0巻 対局中1.0版",apps1.tic_tac_toe_vol1o0.views.playing.ver1o0,PlayingV,,render
```

## Step [OA16o1o0gA17o2o0] ルート編集 - コマンド打鍵

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

## ~~Step [OA16o1o0gA18o0]~~

Merged to OA16o1o0gA17o1o0  

## Step [OA16o1o0gA19o0] consumer/ver1o0.py ファイルの作成

以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 style
        │       │       │   └── 📂 main
        │       │       │       └── 📄 ver1o0.css
        │       │       └── 📂 scripts
        │       │           └── 📂 play
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 ver1o0.html
        │       │       └── 📂 playing
        │       │           └── 📄 ver1o0.html
        │       ├── 📂 views
        │       │   ├── 📂 match_application
        │       │   │   └── 📂 ver1o0
        │       │   │       ├── 📄 __init__.py
        │       │   │       └── 📄 v_render.py
        │       │   └── 📂 playing
        │       │       └── 📂 ver1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
        │       ├── 📂 websocks
        │       │   └── 📂 consumer
👉      │       │       └── 📄 ver1o0.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        ├── 📂 project1                      # プロジェクト
        │   ├── 📄 urls_tic_tac_toe_v1.py
        │   └── 📄 urls.py
        └── 📄 requirements.txt
```

```py
# See also: 📖[Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class TicTacToeV1Consumer(AsyncJsonWebsocketConsumer):
    """OA16o1o0gA19o0 非同期のWebソケットのコンシューマー"""

    async def connect(self):
        """接続時"""
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'room_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        """切断時"""
        print("Disconnected")
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """メッセージ受信時
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        print(
            f"[Debug] Consumer1 receive text_data={text_data}")  # ちゃんと動いているようなら消す
        response = json.loads(text_data)
        event = response.get("event", None)
        message = response.get("message", None)
        if event == 'MOVE':
            # Send message to room group
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',  # type属性は必須
                'message': message,
                "event": "MOVE"
            })

        if event == 'START':
            # Send message to room group
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',  # type属性は必須
                'message': message,
                'event': "START"
            })

        if event == 'END':
            # Send message to room group
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',  # type属性は必須
                'message': message,
                'event': "END"
            })

    async def send_message(self, res):
        """メッセージ送信時
        Receive message from room group
        """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "payload": res,
        }))
```

## Step [OA16o1o0gA20o0] Webソケット用ルート新規作成 - ws_urls_tic_tac_toe_v1.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 style
        │       │       │   └── 📂 main
        │       │       │       └── 📄 ver1o0.css
        │       │       └── 📂 scripts
        │       │           └── 📂 play
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 ver1o0.html
        │       │       └── 📂 playing
        │       │           └── 📄 ver1o0.html
        │       ├── 📂 views
        │       │   ├── 📂 match_application
        │       │   │   └── 📂 ver1o0
        │       │   │       ├── 📄 __init__.py
        │       │   │       └── 📄 v_render.py
        │       │   └── 📂 playing
        │       │       └── 📂 ver1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
        │       ├── 📂 websocks
        │       │   └── 📂 consumer
        │       │       └── 📄 ver1o0.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        ├── 📂 project1                      # プロジェクト
        │   ├── 📄 urls_tic_tac_toe_v1.py
        │   ├── 📄 urls.py
👉      │   └── 📄 ws_urls_tic_tac_toe_v1.py
        └── 📄 requirements.txt
```

```py
# BOF OA16o1o0gA20o0

# See also: 📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# OA16o1o0gA20o0 〇×ゲーム1.0巻 1.0版
from apps1.tic_tac_toe_vol1o0.websocks.consumer.ver1o0 import TicTacToeV1Consumer
#          ------------------                   ------        -------------------
#          11                                   12            2
#    -------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


websocket_urlpatterns = [

    # OA16o1o0gA20o0 〇×ゲーム1.0巻 1.0版
    url(r'^tic-tac-toe/v1/playing/(?P<room_name>\w+)/$',
        # --------------------------------------------
        # 1
        TicTacToeV1Consumer.as_asgi()),
    #   -----------------------------
    #   2
    # 1. 例えば `ws://example.com/tic-tac-toe/v1/playing/Elephant/` のようなURLのパスの部分
    #                            --------------------------------
    #    room_name は変数として渡される
    # 2. クラス名とメソッド。 URL を ASGI形式にする
]

# EOF OA16o1o0gA20o0
```

## Step [OA16o1o0gA21o0] Webソケット用総合ルート編集 - asgi.py ファイル＜その２＞

👇以下の既存のファイルを編集してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_vol1o0
    │   │       │       ├── 📂 style
    │   │       │       │   └── 📂 main
    │   │       │       │       └── 📄 ver1o0.css
    │   │       │       └── 📂 scripts
    │   │       │           └── 📂 play
    │   │       │               └── 📄 ver1o0.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_vol1o0
    │   │       │       ├── 📂 match_application
    │   │       │       │   └── 📄 ver1o0.html
    │   │       │       └── 📂 playing
    │   │       │           └── 📄 ver1o0.html
    │   │       ├── 📂 views
    │   │       │   ├── 📂 match_application
    │   │       │   │   └── 📂 ver1o0
    │   │       │   │       ├── 📄 __init__.py
    │   │       │   │       └── 📄 v_render.py
    │   │       │   └── 📂 playing
    │   │       │       └── 📂 ver1o0
    │   │       │           ├── 📄 __init__.py
    │   │       │           └── 📄 v_render.py
    │   │       ├── 📂 websocks
    │   │       │   └── 📂 consumer
    │   │       │       └── 📄 ver1o0.py
    │   │       ├── 📄 __init__.py
    │   │       ├── 📄 admin.py
    │   │       ├── 📄 apps.py
    │   │       └── 📄 tests.py
    │   ├── 📂 project1                      # プロジェクト
👉  │   │   ├── 📄 asgi.py
    │   │   ├── 📄 urls_tic_tac_toe_v1.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 ws_urls_tic_tac_toe_v1.py
    │   └── 📄 requirements.txt
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📄 urls.py
    └── 📄 .gitignore
```

```py
# ...略...


# * 以下を追加
# OA16o1o0gA21o0 〇×ゲーム v1
from . import ws_urls_tic_tac_toe_v1
#    -        ----------------------
#    1        2
# 1. 同じディレクトリー
# 2. `src1/projectN/ws_urls_tic_tac_toe_v1.py`
#                   ----------------------


# ...略...
# この辺に os.environ.setdefault(...)


# ...略...


# OA15o1o0g9o0 複数のアプリケーションの websocket_urlpatterns をマージします
websocket_urlpatterns_merged = []


# ...略...


# * 以下を追加
# OA16o1o0gA21o0 〇×ゲーム v1
websocket_urlpatterns_merged.extend(
    ws_urls_tic_tac_toe_v1.websocket_urlpatterns)
```



## Step [OA16o1o0gA22o0] Djangoの設定 - settings.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol1o0            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 style
        │       │       │   └── 📂 main
        │       │       │       └── 📄 ver1o0.css
        │       │       └── 📂 scripts
        │       │           └── 📂 play
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 ver1o0.html
        │       │       └── 📂 playing
        │       │           └── 📄 ver1o0.html
        │       ├── 📂 views
        │       │   ├── 📂 match_application
        │       │   │   └── 📂 ver1o0
        │       │   │       ├── 📄 __init__.py
        │       │   │       └── 📄 v_render.py
        │       │   └── 📂 playing
        │       │       └── 📂 ver1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
        │       ├── 📂 websocks
        │       │   └── 📂 consumer
        │       │       └── 📄 ver1o0.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        ├── 📂 project1                      # プロジェクト
        │   ├── 📄 asgi.py
👉      │   ├── 📄 settings.py
        │   ├── 📄 urls_tic_tac_toe_v1.py
        │   ├── 📄 urls.py
        │   └── 📄 ws_urls_tic_tac_toe_v1.py
        └── 📄 requirements.txt
```

```py
# ...略...


TEMPLATES = [
    {
        # ...略...


        'DIRS': [
            # ...略...


            # * 以下を追加
            # OA16o1o0gA22o0 〇×ゲーム1.0巻
            os.path.join(BASE_DIR, 'apps1/tic_tac_toe_vol1o0/templates'),
            #                       ----------------------------------
            #                       10
            #
            # Example: `/src1/apps1/tic_tac_toe_vol1o0/templates/tic_tac_toe_vol1o0/match_application/ver1o0.html`
            #                       ------------------          -------------------
            #                       11                          2
            #                 ----------------------------------
            #                 10
            # 10. テンプレート ディレクトリーへのパス
            # 11. アプリケーション
            # 2. まるで `http://example.com/tic_tac_toe_vol1o0` という素材フォルダーがあるかのように扱われる
            #                             --------------------
        ],


        # ...略...


    },
]
```

## Step [OA16o1o0gA23o0] Web画面へアクセス

このゲームは２人用なので、Webページを２窓で開き、片方が X プレイヤー、もう片方が O プレイヤーとして遊んでください  

📖 [http://localhost:8000/tic-tac-toe/vol1.0/match-application/ver1.0/](http://localhost:8000/tic-tac-toe/vol1.0/match-application/ver1.0/)  

## Step [OA16o1o0gA24o0] ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 tic_tac_toe_vol1o0                # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 style
        │       │       │   └── 📂 main
        │       │       │       └── 📄 ver1o0.css
        │       │       └── 📂 scripts
        │       │           └── 📂 play
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol1o0
        │       │       ├── 📂 match_application
        │       │       │   └── 📄 ver1o0.html
        │       │       └── 📂 playing
        │       │           └── 📄 ver1o0.html
        │       ├── 📂 views
        │       │   ├── 📂 match_application
        │       │   │   └── 📂 ver1o0
        │       │   │       ├── 📄 __init__.py
        │       │   │       └── 📄 v_render.py
        │       │   └── 📂 playing
        │       │       └── 📂 ver1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
        │       ├── 📂 websocks
        │       │   └── 📂 consumer
        │       │       └── 📄 ver1o0.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        ├── 📂 project1                          # プロジェクト
        │   ├── 📄 urls_tic_tac_toe_v1.py
        │   ├── 📄 urls.py
        │   └── 📄 ws_urls_tic_tac_toe_v1.py
        └── 📄 requirements.txt
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/tic-tac-toe/vol1.0/match-application/ver1.0/,OA16o1o0gA24o0 〇×ゲーム1.0巻 対局申込中1.0版
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DockerでTic-Tac-Toeの思考エンジンを作ろう！](https://qiita.com/muzudho1/items/69021deb9ec541406cfb)  

# 参考にした記事

## Web Socket

📖 [Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)  

## Django settings

📖 [スタティックファイルの利用](https://python.keicode.com/django/how-to-serve-static-files.php)  
