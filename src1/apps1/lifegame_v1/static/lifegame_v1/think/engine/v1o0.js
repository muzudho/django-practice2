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

        // 実行ログ
        this._log = "";
        // 実行時の現在のエグゼキューター
        this._executeCurr = null;
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
        let positionText = "";
        let executePosition = (line) => {
            switch (line) {
                case '"""':
                    {
                        this.position.board.parse(positionText);
                        positionText = "";

                        this._executeCurr = executeMain;
                    }
                    break;

                default:
                    {
                        positionText += `${line}`;
                    }
                    break;
            }
        };
        let executeMain = (line) => {
            const tokens = line.split(" ");
            switch (tokens[0]) {
                case "board":
                    {
                        // Example: `board`
                        this._log += this._position.toBoardString();
                    }
                    break;

                case "play":
                    {
                        // Example: `play`
                        this._userCtrl.doMove(this._position);
                        // Ok
                        this._log += "=\n.\n";
                    }
                    break;

                case 'position"""':
                    {
                        positionText = "";
                        this._executeCurr = executePosition;
                    }
                    break;

                default:
                    // ignored
                    break;
            }
        };
        this._executeCurr = executeMain;
        this._log = "";

        const lines = command.split(/\r?\n/);
        for (const line of lines) {
            // 空行はパス
            if (line.trim() === "") {
                continue;
            }

            // Echo for Single line.
            this._log += `# ${line}\n`;

            this._executeCurr(line);
        }

        this._executeCurr = null;

        let logTemp = this._log;
        this._log = "";
        return logTemp;
    }

    dump(indent) {
        return `
${indent}Engine
${indent}------
${indent}${this._position.dump(indent + "    ")}`;
    }
}
