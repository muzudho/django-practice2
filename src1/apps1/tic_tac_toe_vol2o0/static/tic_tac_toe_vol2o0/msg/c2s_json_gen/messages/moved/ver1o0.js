// BOF OA16o3o_1o0g_1o__10o___101o0

/**
 * クライアントからサーバーへ送るメッセージ
 *
 * * 駒の移動を表す
 */
class MovedC2sMessage {
    /**
     * 設定
     * @param {*} sq - マス番号
     * @param {*} pieceMoved - 動かした駒
     */
    constructor(sq, pieceMoved) {
        this._sq = sq;
        this._pieceMoved = pieceMoved;
    }

    /**
     * JSObject形式で取得
     * @returns JSObject形式
     */
    asJsObject() {
        return {
            event: "C2S_Moved", // Client to server
            sq: this._sq,
            piece: this._pieceMoved,
        };
    }
}

// EOF OA16o3o_1o0g_1o__10o___101o0
