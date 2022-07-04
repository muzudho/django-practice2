/**
 * 思考エンジン
 */
class Engine {
    /**
     * 生成
     * @param {string} myTurn - 自分の手番。 "X" か "O"。 部屋に入ると変えることができない
     * @param {UserCtrl} userCtrl - ユーザーコントロール
     * @param {JudgeCtrl} judgeCtrl - 審判コントロール
     */
    constructor(myTurn, userCtrl, judgeCtrl) {
        console.log(`[Engine constructor] 自分の手番=${myTurn}`);

        // あれば勝者 "X", "O" なければ空文字列
        this._winner = "";

        // 局面
        this._position = new Position(myTurn);

        // ゲームオーバー集合
        this._gameoverSet = new GameoverSet(GameoverSet.none);

        // ユーザーコントロール
        this._userCtrl = userCtrl;

        // 審判コントロール
        this._judgeCtrl = judgeCtrl;
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
     * 審判コントロール
     */
    get judgeCtrl() {
        return this._judgeCtrl;
    }

    /**
     * 勝者
     */
    get winner() {
        return this._winner;
    }

    set winner(value) {
        this._winner = value;
    }

    /**
     * ゲームオーバー集合
     */
    get gameoverSet() {
        return this._gameoverSet;
    }

    set gameoverSet(value) {
        this._gameoverSet = value;
    }

    /**
     * 対局開始時
     */
    start() {
        console.log(`[Engine start] 自分の手番=${this._position.turn.me}`);

        // 勝者のクリアー
        this._winner = "";

        // ゲームオーバー状態のクリアー
        this._gameoverSet = new GameoverSet(GameoverSet.none);

        // 局面の初期化
        this._position = new Position(this._position.turn.me);
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

                case "judge":
                    {
                        // Example: `judge`
                        const gameoverSet = this._judgeCtrl.doJudge(this._position);
                        log += gameoverSet.toString();
                    }
                    break;

                case "play":
                    {
                        // Example: `play X 2`
                        const isOk = this._userCtrl.doMove(this._position, tokens[1], parseInt(tokens[2]));
                        if (isOk) {
                            log += "=\n.\n";
                        } else {
                            log += "? this engine couldn't play\n.\n";
                        }
                    }
                    break;

                case "position":
                    {
                        // Example: `position ..O.X.... next X moves 53`
                        //           -------- --------- ---- - ----- --
                        //           0        1         2    3 4     5
                        // 1. 初期局面
                        // 2. 次の番，手番
                        // 3. 初期局面からの棋譜
                        this._position.board.parse(tokens[1]);
                        this._position.turn.next = tokens[3];

                        // 棋譜の配列を作る
                        const arr = tokens[5].split("");
                        // 指定局面から指す，棋譜作成
                        this._position.record.clear();
                        for (const sq of arr) {
                            this._userCtrl.doMove(this._position, this._position.turn.next, sq);
                        }
                        log += `=\n.\n`;
                    }
                    break;

                case "undo":
                    {
                        // Example: `undo`
                        const isOk = this._userCtrl.undoMove(this._position);
                        if (isOk) {
                            log += "=\n.\n";
                        } else {
                            log += "? this engine couldn't undo\n.\n";
                        }
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
${indent}_winner:${this._winner}
${indent}${this._gameoverSet.dump(indent + "    ")}
${indent}${this._position.dump(indent + "    ")}`;
    }
}
