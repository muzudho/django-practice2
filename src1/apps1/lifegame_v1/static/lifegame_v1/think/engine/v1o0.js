// OAAA1001o1o0ga12o_4o0

/**
 * 思考エンジン
 */
class Engine {
    /**
     * 生成
     * @param {UserCtrl} userCtrl - ユーザーコントロール
     * @param {number} boardsCount - 盤の数
     */
    constructor(userCtrl, boardsCount) {
        // 局面
        this._position = new Position(boardsCount);

        // ユーザーコントロール
        this._userCtrl = userCtrl;

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
        // ログ
        let log = "";
        let textOfBoards = ["", ""];

        // 盤の表示
        // Example: `board 0`
        //           ----- -
        //           0     1
        this._parser.onBoardPrint = (tokens) => {
            let boardIndex = parseInt(tokens[1]);
            log += this._position.boards[boardIndex].toHumanPresentableText();
        };

        // 盤の横幅設定
        // Example: `board 0 width 64`
        //           ----- - ----- --
        //           0     1 2     3
        this._parser.onBoardWidth = (tokens) => {
            let boardIndex = parseInt(tokens[1]);
            let width = parseInt(tokens[3]);
            console.log(`board width change: boardIndex:${boardIndex} width:${width} curr:${this._position.boards[boardIndex].width}`);
            this._position.boards[boardIndex].width = width;
        };

        // 盤の縦幅設定
        // Example: `board 0 height 16`
        //           ----- - ------ --
        //           0     1 2      3
        this._parser.onBoardHeight = (tokens) => {
            let boardIndex = parseInt(tokens[1]);
            let height = parseInt(tokens[3]);
            this._position.boards[boardIndex].height = height;
        };

        // 盤の設定（複数行）開始
        // Example: `board 0 """`
        //           ----- - ---
        //           0     1 2
        this._parser.onBoardStart = (tokens) => {
            let boardIndex = parseInt(tokens[1]);
            textOfBoards[boardIndex] = "";
        };

        // Example: `....X....` in board multi-line
        //           ---------
        //           1
        // 1. line
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
            //             console.log(`dstBoardIndex:${dstBoardIndex}
            // dstX:${dstX}
            // dstY:${dstY}
            // srcBoardIndex:${srcBoardIndex}
            // srcX:${srcX}
            // srcY:${srcY}
            // srcWidth:${srcWidth}
            // srcHeight:${srcHeight}`);

            let vec = srcBoard.cropRect(srcX, srcY, srcWidth, srcHeight);
            let cropText1 = vec.map((n) => pc_to_label(n)).join("");
            // console.log(`cropText1:${cropText1}`);

            dstBoard.pasteRect(vec, srcWidth, srcHeight, dstX, dstY);
        };

        // Example: `step board 0`
        //           ---- ----- -
        //           0    1     2
        this._parser.onStep = (tokens) => {
            let boardIndex = parseInt(tokens[2]);

            this._userCtrl.doMove(this._position, boardIndex);
            // Ok
            log += "=\n.\n";
        };

        this._parser.onReadLine = (line) => {
            log += line;
        };

        this._parser.execute(command);

        return log;
    }

    dump(indent) {
        return `
${indent}Engine
${indent}------
${indent}${this._position.dump(indent + "    ")}`;
    }
}
