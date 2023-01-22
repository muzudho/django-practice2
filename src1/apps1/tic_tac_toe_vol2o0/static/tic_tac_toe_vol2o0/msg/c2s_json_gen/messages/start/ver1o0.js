// BOF OA16o3o_1o0g_1o__11o___103o0

/**
 * クライアントからサーバーへ送るメッセージ
 *
 * * 対局開始を表す
 */
class StartC2sMessage {
    constructor() {}

    /**
     * JSObject形式で取得
     * @returns JSObject形式
     */
    asJsObject() {
        return {
            event: "C2S_Start", // Client to server
        };
    }
}

// EOF OA16o3o_1o0g_1o__11o___103o0
