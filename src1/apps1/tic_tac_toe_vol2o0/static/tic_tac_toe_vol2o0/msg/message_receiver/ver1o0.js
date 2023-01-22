// BOF [OA16o3o0g3o0]

/**
 * メッセージ受信器
 */
class MessageReceiver {
    constructor() {
        this._messageListeners = {};
    }

    addMessageListener(name, setMessage) {
        this._messageListeners[name] = setMessage;
    }

    /**
     * サーバーからクライアントへ送られてきたメッセージをセットする関数を返します
     * @returns 関数
     */
    execute(message) {
        // イベント名 (Server to client)
        let event = message["event"];

        let description = `[Server] event:${event}`;
        const keys = Object.keys(message);
        keys.forEach((key) => {
            if (key != "event" && key != "type") {
                description += ` ${key}:${message[key]}`;
            }
        });
        description += ` type:${message["type"]}`;
        console.log(description);

        if (event in this._messageListeners) {
            // 実行
            const execute2 = this._messageListeners[event];
            execute2(message);
        } else {
            // Undefined behavior
            console.log(`(ignored) [Server] ${event}`);
        }
    }
}

// EOF [OA16o3o0g3o0]
