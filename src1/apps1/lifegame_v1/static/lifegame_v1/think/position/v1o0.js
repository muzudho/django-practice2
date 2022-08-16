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
        // 盤
        this._board = new Board();

        // 盤２
        this._board2 = new Board();
    }

    /**
     * 盤
     */
    get board() {
        return this._board;
    }

    /**
     * 盤２
     */
    get board2() {
        return this._board2;
    }

    /**
     * ダンプ
     */
    dump(indent) {
        return `
${indent}Position
${indent}--------
${indent}${this._board.dump(indent + "    ")}
${indent}${this._board2.dump(indent + "    ")}`;
    }
}
