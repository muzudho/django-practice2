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
        // メッセージ名 (Server to client)
        let message_name = message["message_name"];

        let description = `[Server] ${message_name}`;
        const keys = Object.keys(message);
        keys.forEach((key) => {
            if (key != "message_name" && key != "type") {
                description += ` ${key}:${message[key]}`;
            }
        });
        console.log(description);

        if (message_name in this._messageListeners) {
            // 実行
            const execute2 = this._messageListeners[message_name];
            execute2(message);
        } else {
            // Undefined behavior
            console.log(`(ignored) [Server] ${message_name}`);
        }
    }
}

// EOF [OA16o3o0g3o0]
