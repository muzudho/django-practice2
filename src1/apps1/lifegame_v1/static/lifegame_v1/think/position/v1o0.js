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

        // 全要素の初期化（fillは参照渡しなので使いません）
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
