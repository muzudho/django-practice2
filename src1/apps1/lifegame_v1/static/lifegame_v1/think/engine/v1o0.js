// OAAA1001o1o0ga12o_4o0

/**
 * 思考エンジン
 */
class Engine {
    /**
     * 生成
     * @param {UserCtrl} userCtrl - ユーザーコントロール
     */
    constructor(userCtrl) {
        // 局面
        this._position = new Position();

        // ユーザーコントロール
        this._userCtrl = userCtrl;
    }

    /**
     * 局面
     */
    get position() {
        return this._position;
    }

    /**
     * ユーザーコントロール
     */
    get userCtrl() {
        return this._userCtrl;
    }

    /**
     * 対局開始時
     */
    start() {
        // 局面の初期化
        this._position = new Position();
    }

    /**
     * コマンドの実行
     */
    execute(command) {
        let log = "";

        const lines = command.split(/\r?\n/);
        for (const line of lines) {
            // 空行はパス
            if (line.trim() === "") {
                continue;
            }

            // One line command
            log += "# " + line + "\n";

            const tokens = line.split(" ");
            switch (tokens[0]) {
                case "board":
                    {
                        // Example: `board`
                        log += this._position.toBoardString();
                    }
                    break;

                case "play":
                    {
                        // Example: `play`
                        this._userCtrl.doMove(this._position);
                        // Ok
                        log += "=\n.\n";
                    }
                    break;

                default:
                    // ignored
                    break;
            }
        }

        return log;
    }

    dump(indent) {
        return `
${indent}Engine
${indent}------
${indent}${this._position.dump(indent + "    ")}`;
    }
}
