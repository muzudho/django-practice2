// BOF OA16o3o_1o0g_1o__11o___102o0

/**
 * クライアントからサーバーへ送るメッセージ
 *
 * * 対局終了を表す
 */
class EndC2sMessage {
    constructor(winner) {
        this._winner = winner;
    }

    /**
     * JSObject形式で取得
     * @returns JSObject形式
     */
    asJsObject() {
        return {
            event: "C2S_End", // Client to server
            winner: this._winner,
        };
    }
}

// EOF OA16o3o_1o0g_1o__11o___102o0
