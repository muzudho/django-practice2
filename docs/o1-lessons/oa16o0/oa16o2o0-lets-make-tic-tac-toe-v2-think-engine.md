# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/tic-tac-toe/vol2.0/ver1.0/engine-manual/)  

# 目標

前の記事で、１人２役で２窓で遊ぶ 〇×ゲーム（Tic tac toe）を作った  

これのフロントエンドを Vuetify に置き換えて、  
〇×ゲーム（Tic tac toe）の思考エンジンを作りたい  

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
    ├── 📂 src1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 accounts_vol1o0    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_vol1o0              # アプリケーション
    │   │   └── 📂 tic_tac_toe_vol1o0           # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_vol1o0
    │   │       │       ├── 📂 style
    │   │       │       │   └── 📂 main
    │   │       │       │       └── 📄 v1o0.css
    │   │       │       └── 📂 scripts
    │   │       │           └── 📂 play
    │   │       │               └── 📄 v1o0.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_vol1o0
    │   │       │       ├── 📂 match_application
    │   │       │       │   └── 📄 v1o0.html
    │   │       │       └── 📂 playing
    │   │       │           └── 📄 v1o0.html
    │   │       ├── 📂 views
    │   │       │   ├── 📂 match_application
    │   │       │   │   └── 📂 v1o0
    │   │       │   │       ├── 📄 __init__.py
    │   │       │   │       └── 📄 v_render.py
    │   │       │   └── 📂 playing
    │   │       │       └── 📂 v1o0
    │   │       │           ├── 📄 __init__.py
    │   │       │           └── 📄 v_render.py
    │   │       ├── 📂 websocks
    │   │       │   └── 📂 consumer
    │   │       │       └── 📄 v1o0.py
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
    ├── 📂 src2_local                   # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# 手順

## Step OA16o2o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA16o2o0g2o0 フォルダー作成 - apps1/tic_tac_toe_vol2o0 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
👉          └── 📂 tic_tac_toe_vol2o0    # アプリケーション
```

`tic_tac_toe_vol1o0` と依存関係は無い  

## Step OA16o2o0g3o0 アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp tic_tac_toe_vol2o0 ./apps1/tic_tac_toe_vol2o0
#                                                     ------------------ --------------------------
#                                                     1                  2
# 1. 任意のDjangoアプリケーション名
# 2. 既存のアプリケーション ディレクトリーへのパス
```

👇 以下のようなディレクトリー、ファイルが自動生成される  

```plaintext
    └── 📂 src1
        └── 📂 apps1
👉          └── 📂 tic_tac_toe_vol2o0    # アプリケーション
👉              ├── 📂 migrations
👉              │   └── 📄 __init__.py
👉              ├── 📄 __init__.py
👉              ├── 📄 admin.py
👉              ├── 📄 apps.py
👉              ├── 📄 models.py
👉              ├── 📄 tests.py
👉              └── 📄 views.py
```

## Step OA16o2o0g4o0 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
                ├── 📄 apps.py
👉              ├── 📄 models.py
                ├── 📄 tests.py
👉              └── 📄 views.py
```

## Step OA16o2o0g5o0 アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_vol2o0    # アプリケーション
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
👉              ├── 📄 apps.py
                └── 📄 tests.py
```

```py
from django.apps import AppConfig


class TicTacToeV2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    # name = 'tic_tac_toe_vol2o0'
    # * OA16o2o0g5o0 変更後
    name = 'apps1.tic_tac_toe_vol2o0'
    #       ------------------------
    #       1
    # 1. `src1/apps1/tic_tac_toe_vol2o0/apps.py`
    #          ------------------------
```

## Step OA16o2o0g6o0 アプリケーション登録 - settings.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol2o0    # アプリケーション
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


    # OA16o2o0g6o0 〇×ゲーム2.0巻
    'apps1.tic_tac_toe_vol2o0',


    # ...略...
]
```

## Step OA16o2o0g7o0 物の定義 - think/things/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol2o0    # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
        │       │       └── 📂 think
        │       │           └── 📂 things
👉      │       │               └── 📄 v1o0.js
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```js
// OA16o2o0g7o0

// +--------
// | 駒
// |

/**
 * PC は Piece （駒）の略です
 * @type {number}
 */
const PC_EMPTY = 0; // Pieceがないことを表します
const PC_X = 1;
const PC_O = 2;

/**
 * ラベル
 * @type {string}
 */
const PC_EMPTY_LABEL = ".";
const PC_X_LABEL = "X";
const PC_O_LABEL = "O";

/**
 * 定数をラベルに変換
 *
 * @param {int} pc
 * @returns {str} label
 */
function pc_to_label(pc) {
    switch (pc) {
        case PC_EMPTY:
            return PC_EMPTY_LABEL;
        case PC_X:
            return PC_X_LABEL;
        case PC_O:
            return PC_O_LABEL;
        default:
            return pc;
    }
}

/**
 * ラベルを定数に変換
 *
 * @param {str} - label
 * @returns {int} - pc
 */
function label_to_pc(label) {
    switch (label) {
        case PC_EMPTY_LABEL:
            return PC_EMPTY;
        case PC_X_LABEL:
            return PC_X;
        case PC_O_LABEL:
            return PC_O;
        default:
            return label;
    }
}

// |
// | 駒
// +--------

// +--------
// | 盤
// |

/**
 * 盤上の升の数
 * @type {number}
 */
const BOARD_AREA = 9;

/**
 * SQ は Square （マス）の略です
 * +---------+
 * | 0  1  2 |
 * | 3  4  5 |
 * | 6  7  8 |
 * +---------+
 * @type {number}
 */
const SQ_0 = 0;
const SQ_1 = 1;
const SQ_2 = 2;
const SQ_3 = 3;
const SQ_4 = 4;
const SQ_5 = 5;
const SQ_6 = 6;
const SQ_7 = 7;
const SQ_8 = 8;

/**
 * 盤
 */
class Board {
    constructor() {
        // 各マス
        this._squares = [PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY, PC_EMPTY];
    }

    /**
     * 盤上のマス番号で示して、駒を取得
     * @param {number} sq - マス番号
     */
    getPieceBySq(sq) {
        return this._squares[sq];
    }

    /**
     * 盤上のマスに駒を上書きします
     *
     * @param {*} sq - マス番号
     * @param {*} piece - 駒
     */
    setPiece(sq, piece) {
        this._squares[sq] = piece;
    }

    /**
     *
     * @returns コピー配列
     */
    toArray() {
        // スプレッド構文
        return [...this._squares];
    }

    /**
     * 盤面を設定します
     *
     * @param {*} token - Example: `..O.X....`
     */
    parse(token) {
        this._squares = token.split("").map((x) => label_to_pc(x));
    }

    /**
     * ダンプ
     */
    dump(indent) {
        return `
${indent}Board
${indent}-----
${indent}_squares:${this._squares}`;
    }
}

// | 盤
// |
// +--------

// +--------
// | 棋譜
// |

/**
 * 棋譜
 */
class Record {
    constructor() {
        this._squares = [];
    }

    /**
     * 棋譜の破棄
     */
    clear() {
        this._squares = [];
    }

    /**
     *
     * @param {*} sq - 駒を置いた場所
     */
    push(sq) {
        this._squares.push(sq);
    }

    /**
     * 最後尾の要素を削除して返します
     * @returns {int} sq - 空なら undefined
     */
    pop() {
        return this._squares.pop();
    }

    get length() {
        return this._squares.length;
    }

    /**
     * 棋譜を設定します
     *
     * @param {*} token - Example: `53`
     */
    parse(token) {
        this._squares = token.split("").map((x) => parseInt(x));
    }

    /**
     * 棋譜を先頭から読取ります
     *
     * @param {function(int)} setSq - callback
     */
    forEach(setSq) {
        for (const sq of this._squares) {
            setSq(sq);
        }
    }

    toMovesString() {
        return this._squares.join("");
    }

    /**
     * ダンプ
     */
    dump(indent) {
        return `
${indent}Record
${indent}------
${indent}_squares:${this._squares}`;
    }
}

// | 棋譜
// |
// +--------
```

## Step OA16o2o0g8o0 概念の定義 - think/concepts/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol2o0    # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol2o0
        │       │       └── 📂 think
        │       │           ├── 📂 concepts
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 things
👉      │       │               └── 📄 v1o0.js
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```js
// OA16o2o0g8o0

/**
 * 部屋の状態
 */
class RoomState {
    /**
     * ゲームしてません
     */
    static get none() {
        return 0;
    }

    /**
     * ゲーム中
     */
    static get playing() {
        return 1;
    }

    /**
     * 生成
     * @param {int} value
     * @param {function} onChangeValue - 値の変更時
     */
    constructor(value, onChangeValue) {
        console.log(`[RoomState constructor]`);

        this._value = value;
        this._onChangeValue = onChangeValue;
    }

    /**
     * 値
     */
    get value() {
        return this._value;
    }

    set value(value) {
        console.log(`[RoomState set value]`);

        if (this._value === value) {
            return;
        }

        let oldValue = this._value;
        this._value = value;
        this._onChangeValue(oldValue, this._value);
    }

    /**
     * ダンプ
     * @param {str} indent
     * @returns
     */
    dump(indent) {
        return `
${indent}RoomState
${indent}---------
${indent}_value:${this._value}`;
    }
}

/**
 * 番
 */
class Turn {
    /**
     * 生成
     * @param {*} myTurn - 自分の手番。 "X", "O"
     */
    constructor(myTurn) {
        // 自分の手番
        this._me = myTurn;

        // 初期局面でコンストラクターが呼び出される想定で、"X" の方なら先手
        if (myTurn == PC_X_LABEL) {
            // 先手は自分
            this._next = myTurn;
        } else {
            // 先手は相手
            this._next = flipTurn(myTurn);
        }
    }

    /**
     * 自分の手番
     */
    get me() {
        return this._me;
    }

    /**
     * 次の番，手番
     */
    get next() {
        return this._next;
    }

    set next(value) {
        this._next = value;
    }

    /**
     * 私の番か？
     */
    get isMe() {
        return this._me == this._next;
    }

    /**
     * ダンプ
     * @param {str} indent
     * @returns
     */
    dump(indent) {
        return `
${indent}Turn
${indent}----
${indent}_me:${this._me}
${indent}_next:${this._next}
${indent}_isMe:${this._isMe}`;
    }
}

/**
 * ゲームオーバー集合
 *
 * * 自分視点
 */
class GameoverSet {
    /**
     * ゲームオーバーしてません
     */
    static get none() {
        return 0;
    }

    /**
     * 勝った
     */
    static get won() {
        return 1;
    }

    /**
     * 引き分けた
     */
    static get draw() {
        return 2;
    }

    /**
     * 負けた
     */
    static get lost() {
        return 3;
    }

    /**
     * 生成
     * @param {int} value
     */
    constructor(value) {
        this._value = value;
    }

    /**
     * 値
     */
    get value() {
        return this._value;
    }

    toString() {
        switch (this._value) {
            case GameoverSet.none:
                return "=\n.\n";
            case GameoverSet.won:
                return "= won\n.\n";
            case GameoverSet.draw:
                return "= draw\n.\n";
            case GameoverSet.lost:
                return "= lost\n.\n";
            default:
                throw Error(`[GameoverSet dump] Unexpected value=${this._value}`);
        }
    }

    /**
     * ダンプ
     * @param {str} indent
     * @returns
     */
    dump(indent) {
        return `
${indent}GameoverSet
${indent}-----------
${indent}_value:${this._value}
${indent}toString():${this.toString()}`;
    }
}

/**
 * 駒が３つ並んでいるパターン
 */
WIN_PATTERN = [
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

/**
 * 手番反転
 *
 * @param {*} piece
 * @returns
 */
function flipTurn(piece) {
    if (piece == PC_X_LABEL) {
        return PC_O_LABEL;
    } else if (piece == PC_O_LABEL) {
        return PC_X_LABEL;
    }

    return piece;
}
```

## Step OA16o2o0g9o0 局面作成 - think/position/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol2o0    # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol2o0
        │       │       └── 📂 think
        │       │           ├── 📂 concepts
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
👉      │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 things
        │       │               └── 📄 v1o0.js
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```js
// OA16o2o0g9o0

/**
 * 局面
 */
class Position {
    /**
     * 初期化
     *
     * * 対局開始時
     *
     * @param {string} myTurn - 自分の手番。 "X", "O"
     */
    constructor(myTurn) {
        // console.log(`[Position constructor] 自分の手番:${myTurn}`);

        // 盤面
        this._board = new Board();

        // 棋譜
        this._record = new Record();

        // 番
        this._turn = new Turn(myTurn);
    }

    /**
     * 盤
     */
    get board() {
        return this._board;
    }

    /**
     * 棋譜
     */
    get record() {
        return this._record;
    }

    /**
     * 番
     */
    get turn() {
        return this._turn;
    }

    /**
     * マスがすべて埋まっていますか
     */
    isBoardFill() {
        return this.record.length == 9;
    }

    /**
     * 同じ駒が３個ありますか
     */
    isThere3SamePieces() {
        return 5 <= this.record.length;
    }

    toBoardString() {
        // 何手目
        const moves = this._record.length + 1;

        // 手番
        let currentTurn;
        if (this._turn.isMe) {
            currentTurn = this._turn.me;
        } else {
            currentTurn = flipTurn(this._turn.me);
        }

        // 各マス
        const squares = this._board.toArray();
        // console.log(`[Position toBoardString] squares:${squares}`);
        const [a, b, c, d, e, f, g, h, i] = squares.map((x) => pc_to_label(x));

        return `= [Next ${moves} moves / ${currentTurn} turn]
. +---+---+---+
. | ${a} | ${b} | ${c} |
. +---+---+---+
. | ${d} | ${e} | ${f} |
. +---+---+---+
. | ${g} | ${h} | ${i} |
. +---+---+---+
. moves ${this._record.toMovesString()}
.
`;
    }

    /**
     * ダンプ
     */
    dump(indent) {
        return `
${indent}Position
${indent}--------
${indent}${this._board.dump(indent + "    ")}
${indent}${this._record.dump(indent + "    ")}
${indent}${this._turn.dump(indent + "    ")}`;
    }
}
```

## Step OA16o2o0gA10o0 ユーザーコントロール作成 - think/user_ctrl/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol2o0    # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol2o0
        │       │       └── 📂 think
        │       │           ├── 📂 concepts
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
👉      │       │               └── 📄 v1o0.js
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```js
// OA16o2o0gA10o0

/**
 * ユーザーコントロール
 */
class UserCtrl {
    /**
     * 初期化
     *
     * @param {function} onDidMove - 駒を置いたあと
     */
    constructor(onDidMove) {
        this._onDidMove = onDidMove;
    }

    /**
     * 駒を置きます
     *
     * @param {Position} position - 局面
     * @param {number} sq - 升番号; 0 <= sq
     * @param {*} piece - X か O
     * @returns 駒を置けたら真、それ以外は偽
     */
    doMove(position, piece, sq) {
        if (position.board.getPieceBySq(sq) == PC_EMPTY) {
            // 空升なら駒を置きます
            // console.log(`[UserCtrl doMove] 置いたマス:${sq} 動かした駒:${piece}`);

            position.record.push(sq); // 棋譜に追加

            // 駒を置きます
            switch (piece) {
                case PC_X_LABEL:
                    position.board.setPiece(sq, PC_X);
                    break;
                case PC_O_LABEL:
                    position.board.setPiece(sq, PC_O);
                    break;
                default:
                    console.log(`[UserCtrl doMove] illegal move. invalid piece:${piece}`);
                    return false;
            }

            // console.log(`[UserCtrl doMove] 反転前の手番=${position.turn.next}`);
            position.turn.next = flipTurn(position.turn.next);
            // console.log(`[UserCtrl doMove] 反転後の手番=${position.turn.next}`);

            this._onDidMove(sq, piece);
            return true;
        }

        // 駒が置いてあるマスに駒は置けません
        console.log(`[UserCtrl doMove] illegal move. not empty square. sq:${sq}`);
        return false;
    }

    /**
     * 一手戻します
     *
     * @param {Position} position - 局面
     * @returns {bool} wasItDelete - 削除しました
     */
    undoMove(position) {
        const previousSq = position.record.pop();
        // console.log(`[UserCtrl undoMove] previousSq:${previousSq}`);

        if (typeof previousSq === "undefined") {
            return false;
        }

        // console.log(`[UserCtrl doMove] 反転前の手番:${position.turn.next}`);
        position.turn.next = flipTurn(position.turn.next);
        // console.log(`[UserCtrl doMove] 反転後の手番:${position.turn.next}`);

        // 盤上の駒を消します
        position.board.setPiece(previousSq, PC_EMPTY);
        return true;
    }
}
```

## Step OA16o2o0gA11o0 審判作成 - think/judge_ctrl/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol2o0    # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol2o0
        │       │       └── 📂 think
        │       │           ├── 📂 concepts
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 judge_ctrl
👉      │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```js
// OA16o2o0gA11o0

/**
 * 審判コントロール
 */
class JudgeCtrl {
    /**
     * 初期化
     *
     * @param {function} onJudged - 判断したとき。 (pieceMoved, gameoverSetValue) => {};
     */
    constructor(onJudged) {
        // 判断したとき
        this._onJudged = onJudged;
    }

    /**
     * ゲームオーバー判定
     *
     * * 自分が指した後の盤面（＝手番が相手に渡った始めの盤面）を評価することに注意してください
     *
     * @param {Position} position - 局面
     */
    doJudge(position) {
        let gameoverSet = this.#makeGameoverSet(position);
        this._onJudged(gameoverSet);

        return gameoverSet;
    }

    /**
     * ゲームオーバー判定
     *
     * @param {Position} position - 局面
     * @returns ゲームオーバー元
     */
    #makeGameoverSet(position) {
        if (position.isThere3SamePieces()) {
            // 先手番が駒を３つ置いてから、判定を始めます
            for (let squaresOfWinPattern of WIN_PATTERN) {
                // 勝ちパターンの１つについて
                if (this.#isPieceInLine(position, squaresOfWinPattern)) {
                    // 当てはまるなら
                    if (position.turn.isMe) {
                        // 相手が指して自分の手番になったときに ３目が揃った。私の負け
                        return new GameoverSet(GameoverSet.lost);
                    } else {
                        // 自分がが指して相手の手番になったときに ３目が揃った。私の勝ち
                        return new GameoverSet(GameoverSet.won);
                    }
                }
            }
        }

        // 勝ち負けが付かず、盤が埋まったら引き分け
        if (position.isBoardFill()) {
            return new GameoverSet(GameoverSet.draw);
        }

        // ゲームオーバーしてません
        return new GameoverSet(GameoverSet.none);
    }

    /**
     * 駒が３つ並んでいるか？
     *
     * @param {Position} position - 局面
     * @param {*} squaresOfWinPattern - 勝ちパターン
     * @returns 並んでいれば真、それ以外は偽
     */
    #isPieceInLine(position, squaresOfWinPattern) {
        return (
            position.board.getPieceBySq(squaresOfWinPattern[0]) !== PC_EMPTY && //
            position.board.getPieceBySq(squaresOfWinPattern[0]) === position.board.getPieceBySq(squaresOfWinPattern[1]) &&
            position.board.getPieceBySq(squaresOfWinPattern[0]) === position.board.getPieceBySq(squaresOfWinPattern[2])
        );
    }
}
```

## Step OA16o2o0gA12o0 思考エンジン作成 - think/engine/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol2o0    # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol2o0
        │       │       └── 📂 think
        │       │           ├── 📂 concepts
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 engine
👉      │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 judge_ctrl
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```js
// OA16o2o0gA12o0

/**
 * 思考エンジン
 */
class Engine {
    /**
     * 生成
     * @param {string} myTurn - 自分の手番。 "X" か "O"。 部屋に入ると変えることができない
     * @param {UserCtrl} userCtrl - ユーザーコントロール
     * @param {JudgeCtrl} judgeCtrl - 審判コントロール
     */
    constructor(myTurn, userCtrl, judgeCtrl) {
        // console.log(`[Engine constructor] 自分の手番:${myTurn}`);

        // あれば勝者 "X", "O" なければ空文字列
        this._winner = "";

        // 局面
        this._position = new Position(myTurn);

        // ゲームオーバー集合
        this._gameoverSet = new GameoverSet(GameoverSet.none);

        // ユーザーコントロール
        this._userCtrl = userCtrl;

        // 審判コントロール
        this._judgeCtrl = judgeCtrl;
    }

    /**
     * 局面
     */
    get position() {
        return this._position;
    }

    /**
     * ユーザーコントロール
     */
    get userCtrl() {
        return this._userCtrl;
    }

    /**
     * 審判コントロール
     */
    get judgeCtrl() {
        return this._judgeCtrl;
    }

    /**
     * 勝者
     */
    get winner() {
        return this._winner;
    }

    set winner(value) {
        this._winner = value;
    }

    /**
     * ゲームオーバー集合
     */
    get gameoverSet() {
        return this._gameoverSet;
    }

    set gameoverSet(value) {
        this._gameoverSet = value;
    }

    /**
     * 対局開始時
     */
    start() {
        console.log(`[Engine start] 自分の手番=${this._position.turn.me}`);

        // 勝者のクリアー
        this._winner = "";

        // ゲームオーバー状態のクリアー
        this._gameoverSet = new GameoverSet(GameoverSet.none);

        // 局面の初期化
        this._position = new Position(this._position.turn.me);
    }

    /**
     * コマンドの実行
     */
    execute(command) {
        let log = "";

        const lines = command.split(/\r?\n/);
        for (const line of lines) {
            // 空行はパス
            if (line.trim() === "") {
                continue;
            }

            // Echo for Single line.
            log += "# " + line + "\n";

            const tokens = line.split(" ");
            switch (tokens[0]) {
                case "board":
                    {
                        // Example: `board`
                        log += this._position.toBoardString();
                    }
                    break;

                case "judge":
                    {
                        // Example: `judge`
                        const gameoverSet = this._judgeCtrl.doJudge(this._position);
                        log += gameoverSet.toString();
                    }
                    break;

                case "play":
                    {
                        // Example: `play X 2`
                        const isOk = this._userCtrl.doMove(this._position, tokens[1], parseInt(tokens[2]));
                        if (isOk) {
                            log += "=\n.\n";
                        } else {
                            log += "? this engine couldn't play\n.\n";
                        }
                    }
                    break;

                case "position":
                    {
                        // Example: `position ..O.X.... next X moves 53`
                        //           -------- --------- ---- - ----- --
                        //           0        1         2    3 4     5
                        // 1. 初期局面
                        // 2. 次の番，手番
                        // 3. 初期局面からの棋譜
                        this._position.board.parse(tokens[1]);
                        this._position.turn.next = tokens[3];

                        // 棋譜の配列を作る
                        const arr = tokens[5].split("");
                        // 指定局面から指す，棋譜作成
                        this._position.record.clear();
                        for (const sq of arr) {
                            this._userCtrl.doMove(this._position, this._position.turn.next, sq);
                        }
                        log += `=\n.\n`;
                    }
                    break;

                case "undo":
                    {
                        // Example: `undo`
                        const isOk = this._userCtrl.undoMove(this._position);
                        if (isOk) {
                            log += "=\n.\n";
                        } else {
                            log += "? this engine couldn't undo\n.\n";
                        }
                    }
                    break;

                default:
                    // ignored
                    break;
            }
        }

        return log;
    }

    dump(indent) {
        return `
${indent}Engine
${indent}------
${indent}_winner:${this._winner}
${indent}${this._gameoverSet.dump(indent + "    ")}
${indent}${this._position.dump(indent + "    ")}`;
    }
}
```

## Step OA16o2o0gA13o0 画面作成 - think/engine_manual/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol2o0    # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol2o0
        │       │       └── 📂 think
        │       │           ├── 📂 concepts
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 engine
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 judge_ctrl
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
        │       │       └── 📂 think
        │       │           └── 📂 engine_manual
👉      │       │               └── 📄 v1o0.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```html
<!-- BOF OA16o2o0gA13o0 -->
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
                        <h1>Tic Tac Toe Engine Test</h1>
                        <v-form method="POST">
                            {% csrf_token %}

                            <!-- `po_` は POST送信するパラメーター名の目印 -->
                            <!-- 入力 -->
                            <v-textarea name="po_input" required v-model="inputText.value" label="Input"></v-textarea>

                            <v-btn block elevation="2" v-on:click="executeVu()"> Execute </v-btn>

                            <!-- 出力 -->
                            <v-textarea name="po_output" required v-model="outputText.value" label="Output"></v-textarea>
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
                    // 入力
                    inputText: {
                        value: `board
judge
play X 1
board
judge
play O 4
board
judge
play X 5
board
judge
play O 2
board
judge
play X 6
board
judge
play O 0
board
judge
play X 8
board
judge
play O 7
board
judge
play X 3
board
judge

position ..O.X.... next X moves 53
board
undo
board
undo
board
undo
board
`,
                    },
                    // 出力
                    outputText: {
                        value: 'Please push "Execute" button.',
                    },
                    // 思考エンジン
                    engine: new Engine(
                        // 自分の番。 とりあえず "X" としておく
                        PC_X_LABEL,
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
                                // console.log(`[Engine onDidMove] 置いたマス:${sq} 動かした駒:${pieceMoved}`);
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
                                // console.log(`[Engine onDoJudge] 自分の番:${vue1.engine.position.turn.me}`);
                                vue1.engine.gameoverSet = gameoverSet;

                                switch (gameoverSet.value) {
                                    case GameoverSet.won:
                                        // 勝ったとき
                                        // console.log(`[Engine onDoJudge] 勝ち`);
                                        break;
                                    case GameoverSet.draw:
                                        // 引き分けたとき
                                        // console.log(`[Engine onDoJudge] 引き分け`);
                                        break;
                                    case GameoverSet.lost:
                                        // 負けたとき
                                        // console.log(`[Engine onDoJudge] 負け`);
                                        break;
                                    case GameoverSet.none:
                                        // なんでもなかったとき
                                        // console.log(`[Engine onDoJudge] 何もなし`);
                                        break;
                                    default:
                                        throw new Error(`Unexpected gameoverSet.value=${gameoverSet.value}`);
                                }
                            }
                        )
                    ),
                },
                methods: {
                    // 関数名の末尾の Vu は vue1 のメソッドであることを表す目印
                    /**
                     * po_input 欄のコマンドを入力します
                     */
                    executeVu() {
                        // console.log(`[methods executeVu]`);
                        vue1.outputText.value = vue1.engine.execute(vue1.inputText.value);
                    },
                },
            });
        </script>
    </body>
</html>
<!-- EOF OA16o2o0gA13o0 -->
```

## Step OA16o2o0gA14o0 ビュー作成 - think/engine_manual/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol2o0    # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol2o0
        │       │       └── 📂 think
        │       │           ├── 📂 concepts
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 engine
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 judge_ctrl
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
        │       │       └── 📂 think
        │       │           └── 📂 engine_manual
        │       │               └── 📄 v1o0.html
        │       ├── 📂 views
        │       │   └── 📂 think
        │       │       └── 📂 engine_manual
        │       │           └── 📂 v1o0
👉      │       │               └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
# BOF OA16o2o0gA14o0

class EngineManual():
    """OA16o2o0gA14o0 エンジン手動"""

    template_path = "tic_tac_toe_vol2o0/think/engine_manual/ver1o0.html"
    #                --------------------------------------------------
    #                1
    # 1. src1/apps1/tic_tac_toe_vol2o0/templates/tic_tac_toe_vol2o0/think/engine_manual/ver1o0.html
    #                                            --------------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_engine_manual
        #    ---------        --------------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_vol2o0/views/think/engine_manual/ver1o0/v_render.py`
        #                                                                    --------
        # 2. `1.` に含まれる関数

        return render_engine_manual(request, EngineManual.template_path)

# EOF OA16o2o0gA14o0
```

## Step OA16o2o0gA15o0 ビュー作成 - think/engine_manual/v1o0/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol2o0    # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol2o0
        │       │       └── 📂 think
        │       │           ├── 📂 concepts
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 engine
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 judge_ctrl
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol2o0    # アプリケーションと同名
        │       │       └── 📂 think
        │       │           └── 📂 engine_manual
        │       │               └── 📄 v1o0.html
        │       ├── 📂 views
        │       │   └── 📂 think
        │       │       └── 📂 engine_manual
        │       │           └── 📂 v1o0
        │       │               ├── 📄 __init__.py
👉      │       │               └── 📄 v_render.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
# BOF OA16o2o0gA15o0

from django.shortcuts import render


def render_engine_manual(request, engine_manual_tp):
    """OA16o2o0gA15o0 描画 - エンジン手動

    Parameters
    ----------
    engine_manual_tp : str
        Template path
    """

    context = {}

    return render(request, engine_manual_tp, context)

# EOF OA16o2o0gA15o0
```

## ~~Step OA16o2o0gA16o0~~

Merged to OA16o2o0gA16o1o0  

## Step OA16o2o0gA16o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 tic_tac_toe_vol2o0    # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_vol2o0
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
    │   │       │   └── 📂 tic_tac_toe_vol2o0
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
    │   └── 📂 project1
    │       └── 📄 settings.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_tic_tac_toe_vol2o0_autogen.py,tic-tac-toe/vol2.0/ver1.0/engine-manual/,,"OA16o2o0gA16o1o0 〇×ゲーム2.0巻 1.0版 思考エンジン手動",apps1.tic_tac_toe_vol2o0.views.think.engine_manual.v1o0,EngineManual,,render
```

## Step OA16o2o0gA16o2o0 ルート編集 - コマンド打鍵

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

## Step OA16o2o0gA17o0 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_vol2o0    # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol2o0
        │       │       └── 📂 think
        │       │           ├── 📂 concepts
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 engine
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 judge_ctrl
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol2o0
        │       │       └── 📂 think
        │       │           └── 📂 engine_manual
        │       │               └── 📄 v1o0.html
        │       ├── 📂 views
        │       │   └── 📂 think
        │       │       └── 📂 engine_manual
        │       │           └── 📂 v1o0
        │       │               ├── 📄 __init__.py
        │       │               └── 📄 v_render.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
            ├── 📄 urls_tic_tac_toe_v2.py
👉          └── 📄 urls.py
```

```py
# ...略...


urlpatterns = [


    # ...略...


    # OA16o2o0gA17o0 〇×ゲーム v2
    path('', include(f'{PROJECT_NAME}.urls_tic_tac_toe_v2')),
    #    --            ----------------------------------
    #    1             2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `src1/project1/urls_tic_tac_toe_v2.py` の urlpatterns を `1.` にぶら下げる
    #          ----------------------------
]
```

## Step OA16o2o0gA18o0 Web画面へアクセス

📖 [http://localhost:8000/tic-tac-toe/vol2.0/ver1.0/engine-manual/](http://localhost:8000/tic-tac-toe/vol2.0/ver1.0/engine-manual/)  

## Step OA16o2o0gA19o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 tic_tac_toe_vol2o0                # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_vol2o0
        │       │       └── 📂 think
        │       │           ├── 📂 concepts
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 engine
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 judge_ctrl
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_vol2o0
        │       │       └── 📂 think
        │       │           └── 📂 engine_manual
        │       │               └── 📄 v1o0.html
        │       ├── 📂 views
        │       │   └── 📂 think
        │       │       └── 📂 engine_manual
        │       │           └── 📂 v1o0
        │       │               ├── 📄 __init__.py
        │       │               └── 📄 v_render.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 settings.py
            ├── 📄 urls_tic_tac_toe_v2.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/tic-tac-toe/vol2.0/ver1.0/engine-manual/,〇×ゲーム2.0巻 1.0版 思考エンジン手動テスト
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DjangoとDocker練習OA16o3o_1o0 Tic-Tac-Toeのクライアントからサーバーへ送る通信メッセージを取り決めしよう！](https://qiita.com/muzudho1/items/931982d06927dd17e353)  

# 参考にした記事

## Java Script

📖 [【JavaScript】配列を複製する](https://zenn.dev/kou_pg_0131/articles/js-clone-array) - スプレッド構文  
📖 [Split a String by Newline in JavaScript](https://bobbyhadz.com/blog/javascript-split-string-by-newline#split-a-string-by-newline-in-javascript) - 改行でスプリット  
