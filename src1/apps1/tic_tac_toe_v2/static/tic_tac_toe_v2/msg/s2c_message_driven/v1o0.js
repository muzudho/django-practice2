// BOF OA16o3o0g3o0

/**
 * 受信メッセージ駆動
 */
class S2cMessageDriven {
    constructor() {
        this._handlers = {};
    }

    addHandler(eventName, handler) {
        this._handlers[eventName] = handler;
    }

    /**
     * サーバーからクライアントへ送られてきたメッセージをセットする関数を返します
     * @returns 関数
     */
    execute(message) {
        // `s2c_` は サーバーからクライアントへ送られてきた変数の目印
        // イベント名
        let eventName = message["s2c_event"];
        console.log(`[S2cMessageDriven execute] サーバーからのメッセージを受信しました eventName:${eventName}`);

        if (eventName in this._handlers) {
            // 実行
            const execute2 = this._handlers[eventName];
            execute2(message);
        } else {
            // Undefined behavior
            console.log(`[S2cMessageDriven execute] ignored. eventName=[${eventName}]`);
        }
    }
}

// EOF OA16o3o0g3o0
