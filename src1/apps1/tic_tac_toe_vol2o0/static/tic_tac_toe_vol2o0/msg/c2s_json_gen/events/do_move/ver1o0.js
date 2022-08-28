// BOF OA16o3o_1o0g_1o__10o0

/**
 * イベント
 *
 * * 自分のターンに駒を置いたとき
 */
class EvtDoMove {
    constructor(getArgs) {
        this._getArgs = getArgs;
    }

    /**
     * メッセージ新規作成
     * @returns メッセージ
     */
    createMessage() {
        // {int} sq - 升番号
        // {string} pieceMoved - 駒を置いたプレイヤー。 X か O
        const [sq, pieceMoved] = this._getArgs();
        return new MovedC2sMessage(sq, pieceMoved);
    }
}

// EOF OA16o3o_1o0g_1o__10o0
