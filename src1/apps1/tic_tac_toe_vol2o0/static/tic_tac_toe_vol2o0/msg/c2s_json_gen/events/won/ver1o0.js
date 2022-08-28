// BOF OA16o3o_1o0g_1o__13o0

/**
 * イベント
 *
 * * 勝ったことに納得したとき
 */
class EvtWon {
    constructor(getArgs) {
        this._getArgs = getArgs;
    }

    /**
     * メッセージ新規作成
     * @returns メッセージ
     */
    createMessage() {
        // {string} winner - 勝者。 "X" か "O"
        const winner = this._getArgs();
        return new EndC2sMessage(winner);
    }
}

// EOF OA16o3o_1o0g_1o__13o0
