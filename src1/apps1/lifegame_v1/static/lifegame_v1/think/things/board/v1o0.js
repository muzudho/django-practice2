// OAAA1001o1o0ga12o_2o_A10o0

/**
 * 盤の横幅
 * @type {number}
 */
const BOARD_WIDTH = 64;

/**
 * 盤の縦幅
 * @type {number}
 */
const BOARD_HEIGHT = 64;

/**
 * 盤上の升の数
 * @type {number}
 */
const BOARD_AREA = BOARD_WIDTH * BOARD_HEIGHT;

/*
 * SQ は Square （マス）の略です
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
        // 各マス
        this._squares = Array(BOARD_AREA);
        this._squares.fill(PC_EMPTY);
    }

    /**
     * 各マスについて変換
     * @param {function} convertCell - (sq, cellValue)
     */
    convertEachSq(convertCell) {
        let nextBoard = Array(BOARD_AREA);

        for (let sq = 0; sq < BOARD_AREA; sq++) {
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
        for (let sq = 0; sq < BOARD_AREA; sq++) {
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
        const north = -BOARD_WIDTH; // 北
        const east = 1; // 東
        const south = BOARD_WIDTH; // 南
        const west = -1; // 西

        let dirs = [];

        let isEastEnd = sq % BOARD_WIDTH == BOARD_WIDTH - 1; // 東端だ
        let isNorthernEnd = sq / BOARD_WIDTH == 0; // 北端だ
        let isWestEnd = sq % BOARD_WIDTH == 0; // 西端だ
        let isSouthEnd = sq / BOARD_WIDTH == BOARD_HEIGHT - 1; // 南端だ

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
        return y * BOARD_WIDTH + x;
    }

    /**
     * 文字列化
     * @returns
     */
    toString() {
        // 各マス
        const label_of_squares = this.toArray().map((n) => pc_to_label(n));

        let s = "";

        // 上辺の横線
        s += "+";
        for (let x = 0; x < BOARD_WIDTH; x++) {
            s += "-";
        }
        s += "+\n";

        // 各行
        for (let y = 0; y < BOARD_HEIGHT; y++) {
            s += "|";
            for (let x = 0; x < BOARD_WIDTH; x++) {
                s += label_of_squares[this.toSq(x, y)];
            }
            s += "|\n";
        }

        // 下辺の横線
        s += "+";
        for (let x = 0; x < BOARD_WIDTH; x++) {
            s += "-";
        }
        s += "+\n";

        return s;
    }

    /**
     * 盤面を設定します
     *
     * @param {*} token - Example: `..X.X....`
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

        for (let y = 0; y < BOARD_HEIGHT; y++) {
            s += `
${indent}`;
            for (let x = 0; x < BOARD_WIDTH; x++) {
                s += `${this._squares[this.toSq(x, y)]}`;
            }
        }

        return s;
    }
}
