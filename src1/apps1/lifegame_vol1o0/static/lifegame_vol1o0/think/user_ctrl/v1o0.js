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
