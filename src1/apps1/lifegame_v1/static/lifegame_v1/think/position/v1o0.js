// OAAA1001o1o0ga12o_2o0

/**
 * 局面
 */
class Position {
    /**
     * 初期化
     *
     * * 対局開始時
     */
    constructor() {
        // 盤面
        this._board = new Board();

        // 棋譜
        // なし

        // 番
        // なし
    }

    /**
     * 盤
     */
    get board() {
        return this._board;
    }

    toBoardString() {
        // 各マス
        const label_of_squares = this._board.toArray().map((n) => pc_to_label(n));

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
                s += label_of_squares[this._board.toSq(x, y)];
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
     * ダンプ
     */
    dump(indent) {
        return `
${indent}Position
${indent}--------
${indent}${this._board.dump(indent + "    ")}`;
    }
}
