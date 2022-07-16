# 目的

Webサーバーと、クライアント側のアプリ間で通信する練習をしたい。  
だから 〇×ゲーム（Tic tac toe）のサンプルプログラムを真似する。  
１人２役で２窓で遊ぶ  

# はじめに

この記事は Lesson0 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key              | Value                                     |
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
    ├── 📂 host_local1                   # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    ├── 📂 host1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   └── 📂 practice_v1              # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       │   └── 📂 practice_v1
    │   │       │       └── 📂 o1
    │   │       │           └── 📂 data
    │   │       │               └── 📄 desserts1.json
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1          # アプリケーションと同名
    │   │       │       └── 📂 o1
    │   │       │           ├── 📂 prefecture
    │   │       │           └── 📂 vuetify
    │   │       │               ├── 📄 textarea1_base.html
    │   │       │               └── 📄 desserts1.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 o1
    │   │       │       ├── 📂 prefecture
    │   │       │       └── 📂 vuetify
    │   │       │           ├── 📄 __init__.py
    │   │       │           └── 📄 v_textarea1.py
    │   │       ├── 📂 websocks
    │   │       │   └── 📂 o1
    │   │       │       └── 📄 consumer.py
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
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2                  # プロジェクト
    │   ├── 🐳 docker-compose-project2.yml
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

# Step 1. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. Pythonパッケージ インストール指定 - requirements.txt ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1                   # あなたの開発用ディレクトリー。任意の名前
👉      └── 📄 requirements.txt
```

```shell
# ...略...


# 以下を追加
# For tic-tac-toe-v1
channels_redis>=3.2
```

# Step 3. Dockerコンテナの停止～ビルド～起動

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

# Step 4. フォルダー作成 - apps1/tic_tac_toe_v1 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
👉      │   └── 📂 tic_tac_toe_v1    # アプリケーション
        └── 📄 requirements.txt
```

あとで `tic_tac_toe_v2` を作るので、今回は `v1` とした。  
`v1` と `v2` との間で依存はさせないので 別のアプリケーションとすることにした  

# Step 5. アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp tic_tac_toe_v1 ./apps1/tic_tac_toe_v1
#                                                     -------------- ----------------------
#                                                     1              2
# 1. 任意のDjangoアプリケーション名
# 2. 既存のアプリケーション ディレクトリーへのパス
```

👇 以下のようなディレクトリー、ファイルが自動生成される  

```plaintext
    └── 📂 host1
        └── 📂 apps1
👉          └── 📂 tic_tac_toe_v1    # アプリケーション
👉              ├── 📂 migrations
👉              │   └── 📄 __init__.py
👉              ├── 📄 __init__.py
👉              ├── 📄 admin.py
👉              ├── 📄 apps.py
👉              ├── 📄 models.py
👉              ├── 📄 tests.py
👉              └── 📄 views.py
```

# Step 6. 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v1    # アプリケーション
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
                ├── 📄 apps.py
👉              ├── 📄 models.py
                ├── 📄 tests.py
👉              └── 📄 views.py
```

# Step 7. アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v1    # アプリケーション
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
    # name = 'tic_tac_toe_v1'
    # * 変更後
    name = 'apps1.tic_tac_toe_v1'
    #       --------------------
    #       1
    # 1. `host1/apps1/tic_tac_toe_v1/apps.py`
    #           --------------------
```

# Step 8. アプリケーション登録 - settings.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1    # アプリケーション
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


    'apps1.tic_tac_toe_v1',


    # ...略...
]
```

# Step 9. Web ページのスタイル作成 - main.css ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1        # アプリケーションと同名
        │       │       └── 📂 o1                  # v(1.)0.1 ぐらいの意味。ただのフォルダー。無くてもいい
👉      │       │           └── 📄 main.css
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```css
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

# Step 10. 機能作成 - play.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
👉      │       │           └── 📄 play.js
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```js
// See also: 📖[Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)

var roomName = document.getElementById("board").getAttribute("room_name");
var myPiece = document.getElementById("board").getAttribute("my_piece");

var connectionString = `ws://${window.location.host}/tic-tac-toe/v1o0o1/playing/${roomName}/`;
//                      ----]----------------------- ---------------------------------------
//                      1    2                       3
//                      ------------------------------------------------------------------
//                      4
// 1. スキーム : Web Socket
// 2. ホスト アドレス
// 3. パス
// 4. URL

var webSock1 = new WebSocket(connectionString);

const PC_EMPTY = -1; // A square without piece; PC is piece
// Game board for maintaing the state of the game
var board = [PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY];

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
        console.log("WebSockets connection created.");
        webSock1.send(
            JSON.stringify({
                event: "START",
                message: "",
            })
        );
    };

    webSock1.onclose = (e) => {
        console.log("Socket is closed. Reconnect will be attempted in 1 second.", e.reason);
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
```

# Step 11. 対局申込画面作成 - match_application.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1        # アプリケーションと同名
        │       │       └── 📂 o1
👉      │       │           └── 📄 match_application.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```html
{% load static %} {% comment %} 👈あとで static "URL" を使うので load static します {% endcomment %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Tic Tac Toe</title>
        <link rel="stylesheet" href='{% static "tic_tac_toe_v1/o1/main.css" %}' />
        <!--                            ==================================
                                        1
        1. `host1/apps1/tic_tac_toe_v1/static/tic_tac_toe_v1/o1/main.css`
                                       =================================
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
```

# Step 12. 対局画面作成 - playing.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1        # アプリケーションと同名
        │       │       └── 📂 o1
        │       │           ├── 📄 match_application.html
👉      │       │           └── 📄 playing.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```html
{% load static %} {% comment %} 👈あとで static "URL" を使うので load static します {% endcomment %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Tic Tac Toe</title>
        <link rel="stylesheet" href='{% static "tic_tac_toe_v1/o1/main.css" %}' />
        <!--                            ==================================
                                        1
        1. `host1/apps1/tic_tac_toe/static/tic_tac_toe_v1/o1/main.css`
                                    =================================
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

        <script src="{% static 'tic_tac_toe_v1/o1/play.js' %}"></script>
        <!--            =================================
                        1
        1. `host1/apps1/tic_tac_toe_v1/static/tic_tac_toe_v1/o1/play.js`
                                       ================================
        -->
        {% block javascript %} {% endblock javascript %}
    </body>
</html>
```

# Step 13. ビュー モジュール作成 - match_application フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1        # アプリケーションと同名
        │       │       └── 📂 o1
        │       │           ├── 📄 match_application.html
        │       │           └── 📄 playing.html
        │       ├── 📂 views
        │       │   └── 📂 o1
        │       │       └── 📂 match_application
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```py
class MatchApplicationV():
    """対局申込ビュー"""

    _path_of_http_playing = "/tic-tac-toe/v1/playing/{0}/?&mypiece={1}"
    #                                      ^one
    #                        -----------------------------------------
    #                        1
    # 1. http://example.com:8000/tic-tac-toe/v1/playing/Elephant/?&mypiece=X
    #                           --------------------------------------------

    path_of_html = "tic_tac_toe_v1/o1/match_application.html"
    #                            ^one
    #               ----------------------------------------
    #               1
    # 1. host1/apps1/tic_tac_toe_v1/templates/tic_tac_toe_v1/o1/match_application.html
    #                                         ----------------------------------------

    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_match_application
        #    ---------        ------------------------
        #    1                2
        # 1. `host1/apps1/tic_tac_toe_v1/views/o1/match_application/v_render.py`
        #                                                           --------
        # 2. `1.` に含まれる関数

        return render_match_application(
            request,
            MatchApplicationV._path_of_http_playing,
            MatchApplicationV.path_of_html)
```


# Step 14. ビュー モジュール作成 - match_application/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1        # アプリケーションと同名
        │       │       └── 📂 o1
        │       │           ├── 📄 match_application.html
        │       │           └── 📄 playing.html
        │       ├── 📂 views
        │       │   └── 📂 o1
        │       │       └── 📂 match_application
        │       │           ├── 📄 __init__.py
👉      │       │           └── 📄 v_render.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```py
from django.shortcuts import render, redirect


def render_match_application(request, path_of_http_playing, path_of_html):
    """描画 - 対局申込"""

    if request.method == "POST":
        # 送信後
        room_name = request.POST.get("room_name")
        myPiece = request.POST.get("my_piece")
        # TODO バリデーションチェックしたい
        return redirect(path_of_http_playing.format(room_name, myPiece))

    # 訪問後
    return render(request, path_of_html, {})
```

# Step 15. ビュー モジュール作成 - playing フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1        # アプリケーションと同名
        │       │       └── 📂 o1
        │       │           ├── 📄 match_application.html
        │       │           └── 📄 playing.html
        │       ├── 📂 views
        │       │   └── 📂 o1
        │       │       ├── 📂 match_application
        │       │       │   ├── 📄 __init__.py
        │       │       │   └── 📄 v_render.py
        │       │       └── 📂 playing
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```py
class PlayingV():
    """対局中ビュー"""

    path_of_html = "tic_tac_toe_v1/o1/playing.html"
    #                               ^one
    #               ------------------------------
    #               1
    # 1. `host1/apps1/tic_tac_toe_v1/templates/tic_tac_toe_v1/o1/playing.html`
    #                                          ------------------------------

    def render(request, room_name):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_playing
        #    ---------        --------------
        #    1                2
        # 1. `host1/apps1/tic_tac_toe_v1/views/o1/playing/v_render.py`
        #                                                 --------
        # 2. `1.` に含まれる関数

        return render_playing(request, room_name, PlayingV.path_of_html)
```

# Step 16. ビュー モジュール作成 - playing/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 match_application.html
        │       │           └── 📄 playing.html
        │       ├── 📂 views
        │       │   └── 📂 o1
        │       │       ├── 📂 match_application
        │       │       │   ├── 📄 __init__.py
        │       │       │   └── 📄 v_render.py
        │       │       └── 📂 playing
        │       │           ├── 📄 __init__.py
👉      │       │           └── 📄 v_render.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📄 requirements.txt
```

```py
from django.http import Http404
from django.shortcuts import render


def render_playing(request, room_name, path_of_html):
    """描画 - 対局"""

    myPiece = request.GET.get("mypiece")
    if myPiece not in ['X', 'O']:
        raise Http404(f"My piece '{myPiece}' does not exists")

    context = {
        "my_piece": myPiece,
        "room_name": room_name
    }
    return render(request, path_of_html, context)
```

# Step 17. ルート新規作成 - urls_tic_tac_toe_v1.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 match_application.html
        │       │           └── 📄 playing.html
        │       ├── 📂 views
        │       │   └── 📂 o1
        │       │       ├── 📂 match_application
        │       │       │   ├── 📄 __init__.py
        │       │       │   └── 📄 v_render.py
        │       │       └── 📂 playing
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        ├── 📂 project1                      # プロジェクト
👉      │   └── 📄 urls_tic_tac_toe_v1.py
        └── 📄 requirements.txt
```

```py
from django.urls import path

from apps1.tic_tac_toe_v1.views.v1o0o1.match_application import MatchApplicationV
#    ----- -------------- ------------------------------        -----------------
#    1     2              3                                     4
#    ---------------------------------------------------
#    5
# 1. 開発者用ディレクトリーの一部
# 2. アプリケーション フォルダー名
# 3. ディレクトリー名
# 4. クラス名
# 5. Pythonモジュール名

from apps1.tic_tac_toe_v1.views.v1o0o1.playing import PlayingV


urlpatterns = [

    # 対局申込
    path('tic-tac-toe/v1/match-application/',
         # --------------------------------
         # 1
         MatchApplicationV.render),
    #    ------------------------
    #    2
    # 1. 例えば `http://example.com/tic-tac-toe/v1/match-application/` のような URL のパスの部分
    #                              ---------------------------------
    # 2. MatchApplicationV クラスの render 静的メソッド

    # 対局中
    path('tic-tac-toe/v1/playing/<str:room_name>/',
         # --------------------------------------
         # 1
         PlayingV.render),
    #    ---------------
    #    2
    # 1. 例えば `http://example.com/tic-tac-toe/v1/playing/<部屋名>/` のような URL のパスの部分。
    #                              --------------------------------
    #    <部屋名> に入った文字列は room_name 変数に渡されます
    # 2. PlayingV クラスの render 静的メソッド
]
```

# Step 18. 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 match_application.html
        │       │           └── 📄 playing.html
        │       ├── 📂 views
        │       │   └── 📂 o1
        │       │       ├── 📂 match_application
        │       │       │   ├── 📄 __init__.py
        │       │       │   └── 📄 v_render.py
        │       │       └── 📂 playing
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        ├── 📂 project1                      # プロジェクト
        │   ├── 📄 urls_tic_tac_toe_v1.py
👉      │   └── 📄 urls.py
        └── 📄 requirements.txt
```

```py
from django.urls import include, path


# ...略...


urlpatterns = [


    # ...略...


    # 〇×ゲーム v1.0.1
    path('', include('project1.urls_tic_tac_toe_v1')),
    #    --           ----------------------------
    #      1          2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `host1/project1/urls_tic_tac_toe_v1.py` の urlpatterns を (1.) にぶら下げる
    #           ----------------------------
]
```

# Step 19. consumer.py ファイルの作成

以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 match_application.html
        │       │           └── 📄 playing.html
        │       ├── 📂 views
        │       │   └── 📂 o1
        │       │       ├── 📂 match_application
        │       │       │   ├── 📄 __init__.py
        │       │       │   └── 📄 v_render.py
        │       │       └── 📂 playing
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
        │       ├── 📂 websocks
        │       │   └── 📂 o1
👉      │       │       └── 📄 consumer.py
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
    """非同期のWebソケットのコンシューマー"""

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

# Step 20. Webソケット用ルート新規作成 - ws_urls_tic_tac_toe_v1.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 match_application.html
        │       │           └── 📄 playing.html
        │       ├── 📂 views
        │       │   └── 📂 o1
        │       │       ├── 📂 match_application
        │       │       │   ├── 📄 __init__.py
        │       │       │   └── 📄 v_render.py
        │       │       └── 📂 playing
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
        │       ├── 📂 websocks
        │       │   └── 📂 o1
        │       │       └── 📄 consumer.py
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
# ...略...


# 〇×ゲーム v1.0.1
from apps1.tic_tac_toe_v1.websocks.o1.consumer import TicTacToeV1Consumer
#    ----- -------------- ----------- --------        -------------------
#    1     2              3           4               5
#    -----------------------------------------
#    6
# 1. 開発者用ディレクトリーの一部
# 2. アプリケーション フォルダー名
# 3. ディレクトリー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名
# 6. モジュール名

websocket_urlpatterns = [
    # ...略...


    # 〇×ゲーム v1.0.1
    url(r'^tic-tac-toe/v1o0o1/playing/(?P<room_name>\w+)/$',
        # ------------------------------------------------
        # 1
        TicTacToeV1Consumer.as_asgi()),
    #   -----------------------------
    #   2
    # 1. 例えば `ws://example.com/tic-tac-toe/v1o0o1/playing/Elephant/` のようなURLのパスの部分
    #                            ------------------------------------
    #    room_name は変数として渡される
    # 2. クラス名とメソッド。 URL を ASGI形式にする
]
```

# Step 21. Webソケット用総合ルート設定 - asgi.py ファイル＜その２＞

👇以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 match_application.html
        │       │           └── 📄 playing.html
        │       ├── 📂 views
        │       │   └── 📂 o1
        │       │       ├── 📂 match_application
        │       │       │   ├── 📄 __init__.py
        │       │       │   └── 📄 v_render.py
        │       │       └── 📂 playing
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
        │       ├── 📂 websocks
        │       │   └── 📂 o1
        │       │       └── 📄 consumer.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        ├── 📂 project1                      # プロジェクト
👉      │   ├── 📄 asgi.py
        │   ├── 📄 urls_tic_tac_toe_v1.py
        │   ├── 📄 urls.py
        │   └── 📄 ws_urls_tic_tac_toe_v1.py
        └── 📄 requirements.txt
```

```py
# ...略...


# * 以下を追加
import project1.ws_urls_tic_tac_toe_v1
#      -------------------------------
#      1
# 1. `host1/project1/ws_urls_tic_tac_toe_v1.py`
#           -------------------------------


# ...略...
# この辺に os.environ.setdefault(...)


# ...略...


# 複数のアプリケーションの websocket_urlpatterns をマージします
websocket_urlpatterns_merged = []


# ...略...


# * 以下を追加
websocket_urlpatterns_merged.extend(
    project1.ws_urls_tic_tac_toe_v1.websocket_urlpatterns)
```



# Step 22. Djangoの設定 - settings.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v1            # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 match_application.html
        │       │           └── 📄 playing.html
        │       ├── 📂 views
        │       │   └── 📂 o1
        │       │       ├── 📂 match_application
        │       │       │   ├── 📄 __init__.py
        │       │       │   └── 📄 v_render.py
        │       │       └── 📂 playing
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
        │       ├── 📂 websocks
        │       │   └── 📂 o1
        │       │       └── 📄 consumer.py
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
            # 〇×ゲーム v1
            os.path.join(BASE_DIR, 'apps1/tic_tac_toe_v1/templates'),
            #                       ------------------------------
            #                       10
            #
            # Example: `/host1/apps1/tic_tac_toe_v1/templates/tic_tac_toe_v1/o1o0/match_application.html`
            #                        --------------          ---------------
            #                        11                      2
            #                  ------------------------------
            #                  10
            # 10. テンプレート ディレクトリーへのパス
            # 11. アプリケーション
            # 2. まるで `http://example.com/tic_tac_toe_v1` という素材フォルダーがあるかのように扱われる
            #                             ---------------
        ],


        # ...略...


    },
]
```

# Step 23. Web画面へアクセス

このゲームは２人用なので、Webページを２窓で開き、片方が X プレイヤー、もう片方が O プレイヤーとして遊んでください  

📖 [http://localhost:8000/tic-tac-toe/v1/match-application/](http://localhost:8000/tic-tac-toe/v1/match-application/)  

# Step 24. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 tic_tac_toe_v1                # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 main.css
        │       │           └── 📄 play.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v1
        │       │       └── 📂 o1
        │       │           ├── 📄 match_application.html
        │       │           └── 📄 playing.html
        │       ├── 📂 views
        │       │   └── 📂 o1
        │       │       ├── 📂 match_application
        │       │       │   ├── 📄 __init__.py
        │       │       │   └── 📄 v_render.py
        │       │       └── 📂 playing
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
        │       ├── 📂 websocks
        │       │   └── 📂 o1
        │       │       └── 📄 consumer.py
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
/tic-tac-toe/v1/match-application/,〇×ゲーム v1
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DockerでTic-Tac-Toeの思考エンジンを作ろう！](https://qiita.com/muzudho1/items/69021deb9ec541406cfb)  

# 参考にした記事

## Web Socket

📖 [Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)  

## Django settings

📖 [スタティックファイルの利用](https://python.keicode.com/django/how-to-serve-static-files.php)  
