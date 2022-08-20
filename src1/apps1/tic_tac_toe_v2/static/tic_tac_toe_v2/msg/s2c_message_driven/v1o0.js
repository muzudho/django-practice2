// BOF OA16o3o0g3o0

/**
 * 受信メッセージ駆動
 */
class S2cMessageDriven {
    /**
     * サーバーからクライアントへ送られてきたメッセージをセットする関数を返します
     * @returns 関数
     */
    setMessageFromServer(message) {
        // `s2c_` は サーバーからクライアントへ送られてきた変数の目印
        // イベント
        let event = message["s2c_event"];
        console.log(`[S2cMessageDriven setMessageFromServer] サーバーからのメッセージを受信しました event:${event}`);

        switch (event) {
            case "S2C_Start":
                this.start(message);
                break;

            case "S2C_End":
                this.end(message);
                break;

            case "S2C_Moved":
                this.moved(message);
                break;

            default:
                // Undefined behavior
                console.log(`[S2cMessageDriven setMessageFromServer] ignored. event=[${event}]`);
        }
    }

    set onStart(value) {
        this._onStart = value;
    }

    set onEnd(value) {
        this._onEnd = value;
    }

    set onMoved(value) {
        this._onMoved = value;
    }

    /**
     * 対局開始時
     *
     * @param {*} message
     */
    start(message) {
        if (this._onStart == null) {
            // undefined も null も弾きます
            return;
        }

        console.log(`[S2cMessageDriven start]`);
        this._onStart(message);
    }

    /**
     * 対局終了時
     *
     * @param {*} message
     */
    end(message) {
        if (this._onEnd == null) {
            return;
        }

        this._onEnd(message);
    }

    /**
     * 指し手受信時
     *
     * @param {*} message
     */
    moved(message) {
        if (this._onMoved == null) {
            return;
        }

        this._onMoved(message);
    }
}

// EOF OA16o3o0g3o0
