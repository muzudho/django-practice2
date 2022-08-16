// OAAA1001o1o0ga12o_4o_A99o0

/**
 * パーサー
 */
class Parser {
    /**
     * 生成
     */
    constructor() {
        // 実行時の現在のエグゼキューター
        this._executeCurr = null;

        this._onBoard = null;
        this._onPlay = null;
        this._onPosition = null;
        this._onPositionBody = null;
        this._onPositionEnd = null;
    }

    set onBoard(action) {
        this._onBoard = action;
    }

    set onPlay(action) {
        this._onPlay = action;
    }

    set onPosition(action) {
        this._onPosition = action;
    }

    set onPositionBody(action) {
        this._onPositionBody = action;
    }

    set onPositionEnd(action) {
        this._onPositionEnd = action;
    }

    /**
     * コマンドの実行
     */
    execute(command) {
        let executePosition = (line) => {
            switch (line) {
                case '"""':
                    this._onPositionEnd();
                    this._executeCurr = executeMain;
                    break;

                default:
                    this._onPositionBody(line);
                    break;
            }
        };
        let executeMain = (line) => {
            const tokens = line.split(" ");
            switch (tokens[0]) {
                case "board":
                    this._onBoard();
                    break;

                case "play":
                    this._onPlay();
                    break;

                case 'position"""':
                    this._onPosition();
                    this._executeCurr = executePosition;
                    break;

                default:
                    // ignored
                    break;
            }
        };
        this._executeCurr = executeMain;

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
    }
}
