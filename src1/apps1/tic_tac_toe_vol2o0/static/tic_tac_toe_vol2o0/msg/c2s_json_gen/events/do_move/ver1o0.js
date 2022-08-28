// BOF OA16o3o_1o0g_1o__10o0

/**
 * イベント
 *
 * * 自分のターンに駒を置いたとき
 */
class EvtDoMove {
    /**
     * メッセージ新規作成
     * @param {int} sq - 升番号
     * @param {string} pieceMoved - 駒を置いたプレイヤー。 X か O
     * @returns メッセージ
     */
    createMessage(sq, pieceMoved) {
        return new MovedC2sMessage(sq, pieceMoved);
    }
}

// EOF OA16o3o_1o0g_1o__10o0
