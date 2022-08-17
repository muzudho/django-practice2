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

        // パーサー
        this._parser = new Parser();
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
        // 変数
        this._log = "";
        let textOfBoards = ["", ""];

        // Example: `board 0` - 盤の表示
        this._parser.onBoardPrint = (boardIndex) => {
            this._log += this._position.boards[boardIndex].toHumanPresentableText();
        };

        // Example: `board 0 width 64` - 盤の横幅設定
        this._parser.onBoardWidth = (boardIndex, tokens) => {
            let width = parseInt(tokens[3]);
            this._position.boards[boardIndex].width = width;
        };

        // Example: `board 0 height 16` - 盤の縦幅設定
        this._parser.onBoardHeight = (boardIndex, tokens) => {
            let height = parseInt(tokens[3]);
            this._position.boards[boardIndex].height = height;
        };

        // Example: `board 0 """` - 盤の設定（複数行）開始
        this._parser.onBoardStart = (boardIndex) => {
            textOfBoards[boardIndex] = "";
        };

        // Example: `....X....` in board multi-line
        this._parser.onBoardBody = (boardIndex, line) => {
            textOfBoards[boardIndex] += line;
        };

        // Example: `"""` end of board multi-line
        this._parser.onBoardEnd = (boardIndex) => {
            this.position.boards[boardIndex].parse(textOfBoards[boardIndex]);
            textOfBoards[boardIndex] = "";
        };

        // 複写
        // Example: `board 0 xy 3 3 copy_from board 1 rect 0 0 5 5`
        //           ----- - -- - - --------- ----- - ---- - - - -
        //           0     1 2  3 4 5         6     7 8    9 101112
        this._parser.onBoardCopyFrom = (tokens) => {
            let dstBoardIndex = parseInt(tokens[1]);
            let dstX = parseInt(tokens[3]);
            let dstY = parseInt(tokens[4]);
            let srcBoardIndex = parseInt(tokens[7]);
            let srcX = parseInt(tokens[9]);
            let srcY = parseInt(tokens[10]);
            let srcWidth = parseInt(tokens[11]);
            let srcHeight = parseInt(tokens[12]);
            let dstBoard = this.position.boards[dstBoardIndex];
            let srcBoard = this.position.boards[srcBoardIndex];
            console.log(`dstBoardIndex:${dstBoardIndex}
dstX:${dstX}
dstY:${dstY}
srcBoardIndex:${srcBoardIndex}
srcX:${srcX}
srcY:${srcY}
srcWidth:${srcWidth}
srcHeight:${srcHeight}`);

            let vec = srcBoard.cropRect(srcX, srcY, srcWidth, srcHeight);
            let cropText1 = vec.map((n) => pc_to_label(n)).join("");
            console.log(`cropText1:${cropText1}`);

            dstBoard.pasteRect(vec, srcWidth, srcHeight, dstX, dstY);
        };

        // Example: `play`
        this._parser.onPlay = () => {
            this._userCtrl.doMove(this._position);
            // Ok
            this._log += "=\n.\n";
        };

        this._parser.execute(command);

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
