// OAAA1001o1o0ga12o_9o0

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
const PC_X_LABEL = "X";

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

// |
// | 駒
// +--------

// +--------
// | 盤
// |

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
    eachSq(convertCell) {
        let nextBoard = Array(BOARD_AREA);

        for (let y = 0; y < BOARD_HEIGHT; y++) {
            for (let x = 0; x < BOARD_WIDTH; x++) {
                let sq = this.toSq(x, y);
                let cell = convertCell(sq, this._squares[sq]);
                nextBoard[sq] = cell;
            }
        }

        this._squares = nextBoard;
    }

    /**
     * 周囲８近傍の生命の数
     * @param {*} sq
     * @returns
     */
    getLifeCountAround(sq) {
        let count = 0;

        const north = -BOARD_WIDTH; // 北
        const east = 1; // 東
        const south = BOARD_WIDTH; // 南
        const west = -1; // 西
        const next = [
            sq + north, // 北
            sq + north + east, // 北東
            sq + east, // 東
            sq + south + east, // 南東
            sq + south, // 南
            sq + south + west, // 南西
            sq + west, // 西
            sq + north + west, // 北西
        ];

        for (const nx of next) {
            if (0 <= nx && nx < BOARD_AREA && this._squares[nx] === PC_X) {
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

// | 盤
// |
// +--------

// +--------
// | 棋譜
// |

// なし

// | 棋譜
// |
// +--------
