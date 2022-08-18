// OAAA1001o1o0ga13o__10o0

class CellIdHelper {
    /**
     * IDを作成します
     * @param {*} boardIndex - 盤番号
     * @param {*} sq - セル番号
     */
    static createId(boardIndex, sq) {
        return `b${boardIndex}_sq${sq}`;
    }

    static destructuringId(id) {
        const re = /b(\d+)_sq(\d+)/;
        const result = id.match(re);

        return [parseInt(result[1]), parseInt(result[2])];
    }
}
