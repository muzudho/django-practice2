// BOF [OA16o3o0g3o0]

/**
 * 受信メッセージ駆動
 */
class S2cMessageDriven {
    constructor() {
        this._handlers = {};
    }

    addHandler(s2c_type, handler) {
        this._handlers[s2c_type] = handler;
    }

    /**
     * サーバーからクライアントへ送られてきたメッセージをセットする関数を返します
     * @returns 関数
     */
    execute(message) {
        // `s2c_` は サーバーからクライアントへ送られてきた変数の目印
        // イベント名
        let s2c_type = message["s2c_type"];
        console.log(`[S2cMessageDriven execute] サーバーからのメッセージを受信しました s2c_type:${s2c_type}`);

        if (s2c_type in this._handlers) {
            // 実行
            const execute2 = this._handlers[s2c_type];
            execute2(message);
        } else {
            // Undefined behavior
            console.log(`[S2cMessageDriven execute] ignored. s2c_type=[${s2c_type}]`);
        }
    }
}

// EOF [OA16o3o0g3o0]
