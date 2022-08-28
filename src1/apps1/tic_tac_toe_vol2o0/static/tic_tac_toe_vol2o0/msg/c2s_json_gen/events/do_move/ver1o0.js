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
        return new MessageC2S({
            // `c2s_` は クライアントからサーバーへ送る変数の目印
            c2s_event: "C2S_Moved",
            c2s_sq: sq,
            c2s_pieceMoved: pieceMoved,
        });
    }
}

// EOF OA16o3o_1o0g_1o__10o0
