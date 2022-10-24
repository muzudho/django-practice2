# サンプルを見る

📚 [この連載のゴール](http://tic.warabenture.com:8000/lifegame/vol1.0/board/ver0.3)  
📖 [この記事のゴール](http://tic.warabenture.com:8000/lifegame/vol1.0/board/ver0.2)  

# 目標

| What is        | This is                                                                     |
| -------------- | --------------------------------------------------------------------------- |
| この連載の目的 | ライフゲームを作る                                                          |
| この記事の目標 | いきなりライフゲームを作るのは難しいから、まずCUIベースの思考エンジンを作る |

# 情報

この記事はレッスン編と前回の記事を読み終えた人を対象とする  

| What is    | This is                                                                                                              |
| ---------- | -------------------------------------------------------------------------------------------------------------------- |
| レッスン編 | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)              |
| 前回の記事 | 📖 [DjangoとDocker自由課題OAAA1001o1o0 ライフゲームを作ろう！](https://qiita.com/muzudho1/items/a2c90f8d3dfaad849211) |

# Step [OAAA1001o1o0ga12o_1o0] 物の定義 - think/things/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_vol1o0                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_vol1o0          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           └── 📂 things
👉      │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_vol1o0
        │       │       └── 📂 board
        │       │           └── 📄 ver0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 ver0o1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
            ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```js
// OAAA1001o1o0ga12o_1o0

// +--------
// | 駒
// |

/**
 * PC は Piece （駒）の略です
 * @type {number}
 */
const PC_EMPTY = 0; // セルに何も置いていないことを表します
const PC_X = 1; // 塗りつぶしたセルを表します

/**
 * ラベル
 * @type {string}
 */
const PC_EMPTY_LABEL = ".";
const PC_X_LABEL = "x";

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
        default:
            return label;
    }
}

/**
 * 駒の有無を反転
 * @param {*} pc
 * @returns
 */
function flip_pc(pc) {
    switch (pc) {
        case PC_EMPTY:
            return PC_X;
        case PC_X:
            return PC_EMPTY;
        default:
            return pc;
    }
}

// |
// | 駒
// +--------
```

# Step [OAAA1001o1o0ga12o_2o_1o0] 盤の定義 - think/things/board/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_vol1o0                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_vol1o0          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           └── 📂 things
        │       │               ├── 📂 board
👉      │       │               │   └── 📄 ver1o0.js
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_vol1o0
        │       │       └── 📂 board
        │       │           └── 📄 ver0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 ver0o1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
            ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```js
// OAAA1001o1o0ga12o_2o_1o0

/*
 * SQ は Square （マス）の略です
 * 64x64サイズの例
 * +----------------------+
 * |    0     1  ...   63 |
 * |   64    65  ...  127 |
 * |  ...                 |
 * | 4032  4033  ... 4095 |
 * +----------------------+
 */

/**
 * 盤
 */
class Board {
    constructor() {
        // 盤の横幅
        this._width = 0;
        // 盤の縦幅
        this._height = 0;

        // 盤サイズ変更
        this.resize();
    }

    /**
     * 盤の横幅
     * @type {number}
     */
    get width() {
        return this._width;
    }

    set width(value) {
        this._width = value;

        // 盤サイズ変更
        this.resize();
    }

    /**
     * 盤の縦幅
     * @type {number}
     */
    get height() {
        return this._height;
    }

    set height(value) {
        this._height = value;

        // 盤サイズ変更
        this.resize();
    }

    /**
     * 盤上の升の数
     * @type {number}
     */
    get area() {
        return this._width * this._height;
    }

    /**
     * 各マスについて変換
     * @param {function} convertCell - (sq, cellValue)
     */
    convertEachSq(convertCell) {
        let nextBoard = Array(this.area);

        for (let sq = 0; sq < this.area; sq++) {
            let cell = convertCell(sq, this._squares[sq]);
            nextBoard[sq] = cell;
        }

        this._squares = nextBoard;
    }

    /**
     * 各マスについてアクション
     * @param {function} setCell - (sq, cellValue)
     */
    eachSq(setCell) {
        for (let sq = 0; sq < this.area; sq++) {
            setCell(sq, this._squares[sq]);
        }
    }

    /**
     * 周囲８近傍の生命の数
     * @param {*} sq
     * @returns
     */
    getLifeCountAround(sq) {
        let count = 0;

        // 上を北、右を東とする
        const north = -this._width; // 北
        const east = 1; // 東
        const south = this._width; // 南
        const west = -1; // 西

        let dirs = [];

        let isEastEnd = sq % this._width == this._width - 1; // 東端だ
        let isNorthernEnd = sq / this._width == 0; // 北端だ
        let isWestEnd = sq % this._width == 0; // 西端だ
        let isSouthEnd = sq / this._width == this._height - 1; // 南端だ

        if (!isEastEnd) {
            // 盤の東端でなければ
            //  |
            // -+* 東
            //  |
            dirs.push(east);

            if (!isNorthernEnd) {
                // かつ、盤の北端でもなければ
                //  |* 北東
                // -+-
                //  |
                dirs.push(north + east);
            }
        }

        if (!isNorthernEnd) {
            // 盤の北端でなければ
            //  * 北
            // -+-
            //  |
            dirs.push(north);

            if (!isWestEnd) {
                // かつ、盤の西端でもなければ
                // *| 北西
                // -+-
                //  |
                dirs.push(north + west);
            }
        }

        if (!isWestEnd) {
            // 盤の西端でなければ
            //  |
            // *+- 西
            //  |
            dirs.push(west);

            if (!isSouthEnd) {
                // かつ、盤の南端でもなければ
                //  |
                // -+-
                // *|  南西
                dirs.push(south + west);
            }
        }

        if (!isSouthEnd) {
            // 盤の南端でなければ
            //  |
            // -+-
            //  *  南
            dirs.push(south);

            if (!isEastEnd) {
                // かつ、盤の東端でもなければ
                //  |
                // -+-
                //  |* 南東
                dirs.push(south + east);
            }
        }

        for (const dir of dirs) {
            if (this._squares[sq + dir] === PC_X) {
                count += 1;
            }
        }

        return count;
    }

    /**
     * 盤上のマス番号で示して、駒を取得
     * @param {number} sq - マス番号
     */
    getPieceBySq(sq) {
        return this._squares[sq];
    }

    /**
     * 盤サイズ変更
     */
    resize() {
        // 各マス
        this._squares = Array(this.area);

        // 空マスで埋める
        this._squares.fill(PC_EMPTY);
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
     * 変換
     * @param {*} x
     * @param {*} y
     * @returns マス番号
     */
    toSq(x, y) {
        return y * this._width + x;
    }

    /**
     * データ用の部分数列
     *
     * * 矩形で部分指定
     * * シリアライズ = 改行を含まない
     */
    cropRect(ox, oy, width, height) {
        let vec = [];

        let x2 = ox + width;
        let y2 = oy + height;

        if (this._width < x2) {
            x2 = this._width;
        }

        if (this._height < y2) {
            y2 = this._height;
        }

        // 各行
        for (let y = oy; y < y2; y++) {
            for (let x = ox; x < x2; x++) {
                vec.push(this._squares[this.toSq(x, y)]);
            }
        }

        return vec;
    }

    /**
     * データ用の文字列貼り付け, 矩形
     */
    pasteRect(srcVec, width, height, dstX, dstY) {
        // 各行
        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                let srcSq = y * width + x;
                let dstSq = this.toSq(dstX + x, dstY + y);

                this._squares[dstSq] = label_to_pc(srcVec[srcSq]);
            }
        }
    }

    /**
     * 表示用の文字列　枠付き
     * @returns
     */
    toHumanPresentableText() {
        let s = "";

        // 上辺の横線
        s += "+";
        for (let x = 0; x < this._width; x++) {
            s += "-";
        }
        s += "+\n";

        // 各行
        let vec = this.cropRect(0, 0, this._width, this._height);
        let i = 0;
        for (let y = 0; y < this._height; y++) {
            let row = vec.slice(i, i + this._width);
            const line = row.map((n) => pc_to_label(n)).join("");
            s += `|${line}|\n`;
            i += this._width;
        }

        // 下辺の横線
        s += "+";
        for (let x = 0; x < this._width; x++) {
            s += "-";
        }
        s += "+\n";

        return s;
    }

    /**
     * 盤面を設定します
     *
     * @param {*} token - Example: `..x.x....`
     */
    parse(token) {
        this._squares = token.split("").map((x) => label_to_pc(x));
    }

    /**
     * ダンプ
     */
    dump(indent) {
        s = `
${indent}Board
${indent}-----`;

        for (let y = 0; y < this._height; y++) {
            s += `
${indent}`;
            for (let x = 0; x < this._width; x++) {
                s += `${this._squares[this.toSq(x, y)]}`;
            }
        }

        return s;
    }
}
```

# Step [OAAA1001o1o0ga12o_2o0] 局面作成 - think/position/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_vol1o0                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_vol1o0          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           ├── 📂 position
👉      │       │           │   └── 📄 ver1o0.js
        │       │           └── 📂 things
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_vol1o0
        │       │       └── 📂 board
        │       │           └── 📄 ver0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 ver0o1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
            ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```js
// OAAA1001o1o0ga12o_2o0

/**
 * 局面
 */
class Position {
    /**
     * 初期化
     *
     * * 対局開始時
     *
     * @param {number} boardsCount - 盤の数
     */
    constructor(boardsCount) {
        // 各盤
        this._boards = Array(boardsCount);

        // 全要素の初期化（.fill()は参照渡しなので使いません）
        for (let i = 0; i < this._boards.length; i++) {
            this._boards[i] = new Board();
        }
    }

    /**
     * 盤配列
     */
    get boards() {
        return this._boards;
    }

    /**
     * ダンプ
     */
    dump(indent) {
        let s = `
${indent}Position
${indent}--------`;

        for (let boardIndex = 0; boardIndex < this._boards.length; boardIndex++) {
            s += `
${indent}${this._boards[boardIndex].dump(indent + "    ")}`;
        }
    }
}
```

# Step [OAAA1001o1o0ga12o_3o0] ユーザーコントロール作成 - think/user_ctrl/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_vol1o0                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_vol1o0          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           ├── 📂 position
        │       │           │   └── 📄 ver1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 ver1o0.js
        │       │           └── 📂 user_ctrl
👉      │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_vol1o0
        │       │       └── 📂 board
        │       │           └── 📄 ver0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 ver0o1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
            ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```js
// OAAA1001o1o0ga12o_3o0

/**
 * ユーザーコントロール
 */
class UserCtrl {
    /**
     * 時間を１つ進めます
     *
     * @param {Position} position - 局面
     * @param {number} boardIndex - 盤番号
     */
    doMove(position, boardIndex) {
        this._position = position;
        // 盤[0] について
        // セルの変化
        this._position.boards[boardIndex].convertEachSq((sq, cellValue) => {
            let count = this._position.boards[boardIndex].getLifeCountAround(sq);

            switch (cellValue) {
                case PC_EMPTY: // 生命のいない場所
                    // 周囲８近傍に生命が３個あれば、ここに生命が誕生
                    if (count === 3) {
                        return PC_X;
                    }
                    return cellValue;

                case PC_X: // 生命のいる場所
                    // 周囲８近傍に生命が２個または３個あるケース以外では、この生命は消滅
                    if (count === 2 || count === 3) {
                        return cellValue;
                    }
                    return PC_EMPTY;

                default:
                    throw `Unexpected piece:${cellValue} sq:${sq}`;
            }
        });
        this._position = null;
    }
}
```

# Step [OAAA1001o1o0ga12o_4o_1o0] エンジン作成 - think/engine/parser/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_vol1o0                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_vol1o0          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           ├── 📂 engine
        │       │           │   └── 📂 parser
👉      │       │           │       └── 📄 ver1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 ver1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 ver1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_vol1o0
        │       │       └── 📂 board
        │       │           └── 📄 ver0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 ver0o1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
            ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```js
// OAAA1001o1o0ga12o_4o_1o0

/**
 * パーサー
 */
class Parser {
    /**
     * 生成
     */
    constructor() {
        // 実行時の現在のパーサー
        this._parseCurr = null;

        // 盤コマンドのイベントハンドラー
        this._onBoardWidth = null;
        this._onBoardHeight = null;
        this._onBoardPrint = null;
        this._onBoardStart = null;
        this._onBoardBody = null;
        this._onBoardEnd = null;
        this._onBoardCopyFrom = null;

        this._onStep = null;
    }

    set onBoardWidth(action) {
        this._onBoardWidth = action;
    }

    set onBoardHeight(action) {
        this._onBoardHeight = action;
    }

    set onBoardPrint(action) {
        this._onBoardPrint = action;
    }

    set onBoardStart(action) {
        this._onBoardStart = action;
    }

    set onBoardBody(action) {
        this._onBoardBody = action;
    }

    set onBoardEnd(action) {
        this._onBoardEnd = action;
    }

    set onBoardCopyFrom(action) {
        this._onBoardCopyFrom = action;
    }

    set onStep(action) {
        this._onStep = action;
    }

    set onReadLine(action) {
        this._onReadLine = action;
    }

    /**
     * コマンドの実行
     */
    execute(command) {
        // 内部状態
        let boardIndex = 0;

        let parseBoard = (line) => {
            switch (line) {
                case '"""':
                    {
                        this._onBoardEnd(boardIndex);
                        this._parseCurr = parseMain;
                    }
                    break;

                default:
                    {
                        this._onBoardBody(boardIndex, line);
                    }
                    break;
            }
        };
        let parseMain = (line) => {
            const tokens = line.split(" ");
            switch (tokens[0]) {
                case "board":
                    // Example: `board 0`
                    // Example: `board 0 width 64`
                    // Example: `board 0 """
                    //           ....X....
                    //           """`
                    // Example: `board 0 xy 3 3 copy_from board 1 rect 0 0 5 5`
                    boardIndex = parseInt(tokens[1]);

                    if (tokens.length < 3) {
                        this._onBoardPrint(tokens);
                        return;
                    }

                    let subCommand = tokens[2];
                    switch (subCommand) {
                        case "width":
                            this._onBoardWidth(tokens);
                            break;

                        case "height":
                            this._onBoardHeight(tokens);
                            break;

                        case "xy":
                            this._onBoardCopyFrom(tokens);
                            break;

                        case '"""':
                            this._onBoardStart(tokens);
                            this._parseCurr = parseBoard;
                            break;

                        default:
                            // Error
                            throw new Error(`subCommand:${subCommand} in line:${line}`);
                    }
                    break;

                case "step":
                    // Example: `step board 0`
                    this._onStep(tokens);
                    break;

                default:
                    // ignored
                    break;
            }
        };
        this._parseCurr = parseMain;

        const lines = command.split(/\r?\n/);
        for (const line of lines) {
            // 空行はパス
            if (line.trim() === "") {
                continue;
            }

            // Echo for Single line.
            this._onReadLine(`# ${line}\n`);

            this._parseCurr(line);
        }

        this._parseCurr = null;
    }
}
```

# Step [OAAA1001o1o0ga12o_4o0] エンジン作成 - think/engine/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_vol1o0                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_vol1o0          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           ├── 📂 engine
        │       │           │   ├── 📂 parser
        │       │           │   │   └── 📄 ver1o0.js
👉      │       │           │   └── 📄 ver1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 ver1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 ver1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_vol1o0
        │       │       └── 📂 board
        │       │           └── 📄 ver0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 ver0o1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
            ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```js
// OAAA1001o1o0ga12o_4o0

/**
 * 思考エンジン
 */
class Engine {
    /**
     * 生成
     * @param {UserCtrl} userCtrl - ユーザーコントロール
     * @param {number} boardsCount - 盤の数
     */
    constructor(userCtrl, boardsCount) {
        // 局面
        this._position = new Position(boardsCount);

        // ユーザーコントロール
        this._userCtrl = userCtrl;

        // パーサー
        this._parser = new Parser();
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
     * 対局開始時
     */
    start() {
        // 局面の初期化
        this._position = new Position();
    }

    /**
     * コマンドの実行
     */
    execute(command) {
        // ログ
        let log = "";
        let textOfBoards = ["", ""];

        // 盤の表示
        // Example: `board 0`
        //           ----- -
        //           0     1
        this._parser.onBoardPrint = (tokens) => {
            let boardIndex = parseInt(tokens[1]);
            log += this._position.boards[boardIndex].toHumanPresentableText();
        };

        // 盤の横幅設定
        // Example: `board 0 width 64`
        //           ----- - ----- --
        //           0     1 2     3
        this._parser.onBoardWidth = (tokens) => {
            let boardIndex = parseInt(tokens[1]);
            let width = parseInt(tokens[3]);
            console.log(`board width change: boardIndex:${boardIndex} width:${width} curr:${this._position.boards[boardIndex].width}`);
            this._position.boards[boardIndex].width = width;
        };

        // 盤の縦幅設定
        // Example: `board 0 height 16`
        //           ----- - ------ --
        //           0     1 2      3
        this._parser.onBoardHeight = (tokens) => {
            let boardIndex = parseInt(tokens[1]);
            let height = parseInt(tokens[3]);
            this._position.boards[boardIndex].height = height;
        };

        // 盤の設定（複数行）開始
        // Example: `board 0 """`
        //           ----- - ---
        //           0     1 2
        this._parser.onBoardStart = (tokens) => {
            let boardIndex = parseInt(tokens[1]);
            textOfBoards[boardIndex] = "";
        };

        // Example: `....X....` in board multi-line
        //           ---------
        //           1
        // 1. line
        this._parser.onBoardBody = (boardIndex, line) => {
            textOfBoards[boardIndex] += line;
        };

        // Example: `"""` end of board multi-line
        this._parser.onBoardEnd = (boardIndex) => {
            this.position.boards[boardIndex].parse(textOfBoards[boardIndex]);
            textOfBoards[boardIndex] = "";
        };

        // 複写
        // Example: `board 0 xy 3 3 copy_from board 1 rect 0 0 5 5`
        //           ----- - -- - - --------- ----- - ---- - - - -
        //           0     1 2  3 4 5         6     7 8    9 101112
        this._parser.onBoardCopyFrom = (tokens) => {
            let dstBoardIndex = parseInt(tokens[1]);
            let dstX = parseInt(tokens[3]);
            let dstY = parseInt(tokens[4]);
            let srcBoardIndex = parseInt(tokens[7]);
            let srcX = parseInt(tokens[9]);
            let srcY = parseInt(tokens[10]);
            let srcWidth = parseInt(tokens[11]);
            let srcHeight = parseInt(tokens[12]);
            let dstBoard = this.position.boards[dstBoardIndex];
            let srcBoard = this.position.boards[srcBoardIndex];
            //             console.log(`dstBoardIndex:${dstBoardIndex}
            // dstX:${dstX}
            // dstY:${dstY}
            // srcBoardIndex:${srcBoardIndex}
            // srcX:${srcX}
            // srcY:${srcY}
            // srcWidth:${srcWidth}
            // srcHeight:${srcHeight}`);

            let vec = srcBoard.cropRect(srcX, srcY, srcWidth, srcHeight);
            let cropText1 = vec.map((n) => pc_to_label(n)).join("");
            // console.log(`cropText1:${cropText1}`);

            dstBoard.pasteRect(vec, srcWidth, srcHeight, dstX, dstY);
        };

        // Example: `step board 0`
        //           ---- ----- -
        //           0    1     2
        this._parser.onStep = (tokens) => {
            const boardIndex = parseInt(tokens[2]);

            this._userCtrl.doMove(this._position, boardIndex);
            // Ok
            log += "=\n.\n";
        };

        this._parser.onReadLine = (line) => {
            log += line;
        };

        this._parser.execute(command);

        return log;
    }

    dump(indent) {
        return `
${indent}Engine
${indent}------
${indent}${this._position.dump(indent + "    ")}`;
    }
}
```

# Step [OAAA1001o1o0ga12o_5o0] 画面作成 - board/ver0o2o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_vol1o0                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_vol1o0          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           ├── 📂 engine
        │       │           │   ├── 📂 parser
        │       │           │   │   └── 📄 ver1o0.js
        │       │           │   └── 📄 ver1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 ver1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 ver1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_vol1o0
        │       │       └── 📂 board
        │       │           ├── 📄 ver0o1o0.html
👉      │       │           └── 📄 ver0o2o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 ver0o1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
            ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```html
<!-- BOF OAAA1001o1o0ga12o_5o0 -->
{% extends "lifegame_vol1o0/board/ver0o1o0.html" %}
{#          -----------------------------------
            1
1. src1/apps1/lifegame_vol1o0/templates/lifegame_vol1o0/board/ver0o1o0.html
                                        -----------------------------------
#}
{% load static %} {# 👈あとで static "URL" を使うので load static します #}

{% block body %}
        <div id="app">
            <v-app>
                <v-main>
                    <v-container fluid>
                        <h1>Life game Engine Test</h1>
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

        <script src="{% static 'lifegame_vol1o0/think/engine/parser/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_vol1o0/think/engine/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_vol1o0/think/position/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_vol1o0/think/things/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_vol1o0/think/things/board/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_vol1o0/think/user_ctrl/v1o0.js' %}"></script>
        <!--            ===============================================
                        1
        1. src1/apps1/lifegame_vol1o0/static/lifegame_vol1o0/think/user_ctrl/v1o0.js
                                      ==============================================
        -->

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            /**
             * 盤の数
             */
            let BOARDS_COUNT = 3;

            const vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // 入力
                    inputText: {
                        value: `# 盤[0]サイズ
board 0 width 64
board 0 height 32
# グライダー
board 0 """
................................................................
................................................................
....x...........................................................
.....x..........................................................
...xxx..........................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
"""
board 0
step board 0
board 0
step board 0
board 0
step board 0
board 0
step board 0
board 0
`,
                    },
                    // 出力
                    outputText: {
                        value: 'Please push "Execute" button.',
                    },
                    // 思考エンジン
                    engine: new Engine(
                        // ユーザーコントロール
                        new UserCtrl(),
                        // 盤の数
                        BOARDS_COUNT
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
{% endblock body %}
<!-- EOF OAAA1001o1o0ga12o_5o0 -->
```

# Step [OAAA1001o1o0ga12o_6o0] ビュー作成 - board/ver0o2o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_vol1o0                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_vol1o0          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           ├── 📂 engine
        │       │           │   ├── 📂 parser
        │       │           │   │   └── 📄 ver1o0.js
        │       │           │   └── 📄 ver1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 ver1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 ver1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 ver1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_vol1o0
        │       │       └── 📂 board
        │       │           ├── 📄 ver0o1o0.html
        │       │           └── 📄 ver0o2o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       ├── 📂 ver0o1o0
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 ver0o2o0
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
            ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```py
# BOF OAAA1001o1o0ga12o_6o0

from django.shortcuts import render


class BoardView():
    """OAAA1001o1o0ga12o_6o0 盤"""

    @staticmethod
    def render(request):
        """描画"""

        # Template path
        this_page_tp = 'lifegame_vol1o0/board/ver0o2o0.html.txt'
        #               ---------------------------------------
        #               1
        # 1. `src1/apps1/lifegame_vol1o0/templates/lifegame_vol1o0/board/ver0o2o0.html.txt` を取得
        #                                          ---------------------------------------

        context = {}
        return render(request, this_page_tp, context)

# EOF OAAA1001o1o0ga12o_6o0
```

# ~~Step [OAAA1001o1o0ga12o_7o0]~~

Merged to OAAA1001o1o0ga12o_7o1o0  

# Step [OAAA1001o1o0ga12o_7o1o0] ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 lifegame_vol1o0                  # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 lifegame_vol1o0          # アプリケーションと同名
    │   │       │       └── 📂 think
    │   │       │           ├── 📂 engine
    │   │       │           │   ├── 📂 parser
    │   │       │           │   │   └── 📄 ver1o0.js
    │   │       │           │   └── 📄 ver1o0.js
    │   │       │           ├── 📂 position
    │   │       │           │   └── 📄 ver1o0.js
    │   │       │           ├── 📂 things
    │   │       │           │   └── 📄 ver1o0.js
    │   │       │           └── 📂 user_ctrl
    │   │       │               └── 📄 ver1o0.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 lifegame_vol1o0
    │   │       │       └── 📂 board
    │   │       │           ├── 📄 ver0o1o0.html
    │   │       │           └── 📄 ver0o2o0.html.txt
    │   │       ├── 📂 views
    │   │       │   └── 📂 board
    │   │       │       ├── 📂 ver0o1o0
    │   │       │       │   └── 📄 __init__.py
    │   │       │       └── 📂 ver0o2o0
    │   │       │           └── 📄 __init__.py
    │   │       ├── 📄 __init__.py
    │   │       ├── 📄 admin.py
    │   │       ├── 📄 apps.py
    │   │       └── 📄 tests.py
    │   └── 📂 project1
    │       ├── 📄 settings.py
    │       └── 📄 urls.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_lifegame_vol1o0_autogen.py,lifegame/vol1.0/board/ver0.2,,"OAAA1001o1o0ga12o_7o1o0 ライフゲーム1.0巻 盤0.2版",apps1.lifegame_vol1o0.views.board.ver0o2o0,BoardView,Lifegame1o0BoardView0o2o0,render
```

## Step [OAAA1001o1o0ga10o2o0] ルート編集 - コマンド打鍵

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

# Step [OAAA1001o1o0ga12o0] Webページにアクセスする

📖 [http://localhost:8000/lifegame/vol1.0/board/ver0.2](http://localhost:8000/lifegame/vol1.0/board/ver0.2)  

# 続きの記事

📖 [DjangoとDocker自由課題OAAA1001o1o0ga13o__10o0 ライフゲームのGUIを作ろう！](https://qiita.com/muzudho1/items/01d2482576f8ca8d7e0e)  
