// OAAA1001o1o0ga12o_4o_A10o0

/**
 * パーサー
 */
class Parser {
    /**
     * 生成
     */
    constructor() {
        // 実行時の現在のパーサー
        this._parseCurr = null;

        // 盤コマンドのイベントハンドラー
        this._onBoardWidth = null;
        this._onBoardHeight = null;
        this._onBoardPrint = null;
        this._onBoardStart = null;
        this._onBoardBody = null;
        this._onBoardEnd = null;
        this._onBoardCopyFrom = null;

        this._onPlay = null;
    }

    set onBoardWidth(action) {
        this._onBoardWidth = action;
    }

    set onBoardHeight(action) {
        this._onBoardHeight = action;
    }

    set onBoardPrint(action) {
        this._onBoardPrint = action;
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

    set onBoardCopyFrom(action) {
        this._onBoardCopyFrom = action;
    }

    set onPlay(action) {
        this._onPlay = action;
    }

    /**
     * コマンドの実行
     */
    execute(command) {
        // 内部状態
        let boardIndex = 0;

        let parseBoard = (line) => {
            switch (line) {
                case '"""':
                    {
                        this._onBoardEnd(boardIndex);
                        this._parseCurr = parseMain;
                    }
                    break;

                default:
                    {
                        this._onBoardBody(boardIndex, line);
                    }
                    break;
            }
        };
        let parseMain = (line) => {
            const tokens = line.split(" ");
            switch (tokens[0]) {
                case "board":
                    // Example: `board 0`
                    // Example: `board 0 width 64`
                    // Example: `board 0 """
                    //           ....X....
                    //           """`
                    // Example: `board 0 xy 3 3 copy_from board 1 rect 0 0 5 5`
                    boardIndex = parseInt(tokens[1]);

                    if (tokens.length < 3) {
                        this._onBoardPrint(tokens);
                        return;
                    }

                    let subCommand = tokens[2];
                    switch (subCommand) {
                        case "width":
                            this._onBoardWidth(tokens);
                            break;

                        case "height":
                            this._onBoardHeight(tokens);
                            break;

                        case "xy":
                            this._onBoardCopyFrom(tokens);
                            break;

                        case '"""':
                            this._onBoardStart(tokens);
                            this._parseCurr = parseBoard;
                            break;

                        default:
                            // Error
                            throw new Error(`subCommand:${subCommand} in line:${line}`);
                    }
                    break;

                case "play":
                    // Example: `play`
                    this._onPlay();
                    break;

                default:
                    // ignored
                    break;
            }
        };
        this._parseCurr = parseMain;

        const lines = command.split(/\r?\n/);
        for (const line of lines) {
            // 空行はパス
            if (line.trim() === "") {
                continue;
            }

            // Echo for Single line.
            this._log += `# ${line}\n`;

            this._parseCurr(line);
        }

        this._parseCurr = null;
    }
}
