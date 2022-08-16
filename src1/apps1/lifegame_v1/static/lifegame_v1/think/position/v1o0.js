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
        // ２つの盤
        this._boards = [new Board(), new Board()];
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
        return `
${indent}Position
${indent}--------
${indent}${this._boards[0].dump(indent + "    ")}
${indent}${this._boards[1].dump(indent + "    ")}`;
    }
}
