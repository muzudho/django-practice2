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
        let boardText = "";

        // [`board`] - 盤の表示
        this._parser.onBoard = () => {
            this._log += this._position.board.toString();
        };

        // [`boardWidth`] - 盤の横幅設定
        this._parser.onBoardWidth = (tokens) => {
            let width = parseInt(tokens[1]);
            this._position.board.width = width;
        };

        // [`boardHeight`] - 盤の横幅設定
        this._parser.onBoardHeight = (tokens) => {
            let height = parseInt(tokens[1]);
            this._position.board.height = height;
        };

        // [`board"""`]
        this._parser.onBoardStart = () => {
            boardText = "";
        };

        // [`board"""`][*]
        this._parser.onBoardBody = (line) => {
            boardText += `${line}`;
        };

        // [`board"""`][`"""`]
        this._parser.onBoardEnd = () => {
            this.position.board.parse(boardText);
            boardText = "";
        };

        // [`play`]
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
