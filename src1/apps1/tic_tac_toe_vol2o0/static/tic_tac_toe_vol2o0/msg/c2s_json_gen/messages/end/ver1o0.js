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
            // `c2s_` は クライアントからサーバーへ送る変数の目印
            c2s_type: "C2S_End",
            c2s_winner: this._winner,
        };
    }
}

// EOF OA16o3o_1o0g_1o__11o___102o0
