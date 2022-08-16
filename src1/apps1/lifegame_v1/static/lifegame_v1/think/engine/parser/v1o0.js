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
        this._onBoardStart = null;
        this._onBoardBody = null;
        this._onBoardEnd = null;
        this._onPlay = null;
    }

    set onBoard(action) {
        this._onBoard = action;
    }

    set onBoardStart(action) {
        this._onBoardStart = action;
    }

    set onBoardBody(action) {
        this._onBoardBody = action;
    }

    set onBoardEnd(action) {
        this._onBoardEnd = action;
    }

    set onPlay(action) {
        this._onPlay = action;
    }

    /**
     * コマンドの実行
     */
    execute(command) {
        let executePosition = (line) => {
            switch (line) {
                case '"""':
                    this._onBoardEnd();
                    this._executeCurr = executeMain;
                    break;

                default:
                    this._onBoardBody(line);
                    break;
            }
        };
        let executeMain = (line) => {
            const tokens = line.split(" ");
            switch (tokens[0]) {
                case "board":
                    this._onBoard();
                    break;

                case 'board"""':
                    this._onBoardStart();
                    this._executeCurr = executePosition;
                    break;

                case "play":
                    this._onPlay();
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
