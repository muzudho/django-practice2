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
        let positionText = "";

        // [`board`]
        this._parser.onBoard = () => {
            this._log += this._position.toBoardString();
        };

        // [`play`]
        this._parser.onPlay = () => {
            this._userCtrl.doMove(this._position);
            // Ok
            this._log += "=\n.\n";
        };

        // [`position"""`]
        this._parser.onPosition = () => {
            positionText = "";
        };

        // [`position"""`][*]
        this._parser.onPositionBody = (line) => {
            positionText += `${line}`;
        };

        // [`position"""`][`"""`]
        this._parser.onPositionEnd = () => {
            this.position.board.parse(positionText);
            positionText = "";
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
