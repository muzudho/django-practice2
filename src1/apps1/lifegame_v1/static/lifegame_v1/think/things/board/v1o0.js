// OAAA1001o1o0ga12o_2o_A10o0

/*
 * SQ は Square （マス）の略です
 * 64x64サイズの例
 * +----------------------+
 * |    0     1  ...   63 |
 * |   64    65  ...  127 |
 * |  ...                 |
 * | 4032  4033  ... 4095 |
 * +----------------------+
 */

/**
 * 盤
 */
class Board {
    constructor() {
        // 盤の横幅
        this._width = 0;
        // 盤の縦幅
        this._height = 0;

        // 盤サイズ変更
        this.resize();
    }

    /**
     * 盤の横幅
     * @type {number}
     */
    get width() {
        return this._width;
    }

    set width(value) {
        this._width = value;

        // 盤サイズ変更
        this.resize();
    }

    /**
     * 盤の縦幅
     * @type {number}
     */
    get height() {
        return this._height;
    }

    set height(value) {
        this._height = value;

        // 盤サイズ変更
        this.resize();
    }

    /**
     * 盤上の升の数
     * @type {number}
     */
    get area() {
        return this._width * this._height;
    }

    /**
     * 各マスについて変換
     * @param {function} convertCell - (sq, cellValue)
     */
    convertEachSq(convertCell) {
        let nextBoard = Array(this.area);

        for (let sq = 0; sq < this.area; sq++) {
            let cell = convertCell(sq, this._squares[sq]);
            nextBoard[sq] = cell;
        }

        this._squares = nextBoard;
    }

    /**
     * 各マスについてアクション
     * @param {function} setCell - (sq, cellValue)
     */
    eachSq(setCell) {
        for (let sq = 0; sq < this.area; sq++) {
            setCell(sq, this._squares[sq]);
        }
    }

    /**
     * 周囲８近傍の生命の数
     * @param {*} sq
     * @returns
     */
    getLifeCountAround(sq) {
        let count = 0;

        // 上を北、右を東とする
        const north = -this._width; // 北
        const east = 1; // 東
        const south = this._width; // 南
        const west = -1; // 西

        let dirs = [];

        let isEastEnd = sq % this._width == this._width - 1; // 東端だ
        let isNorthernEnd = sq / this._width == 0; // 北端だ
        let isWestEnd = sq % this._width == 0; // 西端だ
        let isSouthEnd = sq / this._width == this._height - 1; // 南端だ

        if (!isEastEnd) {
            // 盤の東端でなければ
            //  |
            // -+* 東
            //  |
            dirs.push(east);

            if (!isNorthernEnd) {
                // かつ、盤の北端でもなければ
                //  |* 北東
                // -+-
                //  |
                dirs.push(north + east);
            }
        }

        if (!isNorthernEnd) {
            // 盤の北端でなければ
            //  * 北
            // -+-
            //  |
            dirs.push(north);

            if (!isWestEnd) {
                // かつ、盤の西端でもなければ
                // *| 北西
                // -+-
                //  |
                dirs.push(north + west);
            }
        }

        if (!isWestEnd) {
            // 盤の西端でなければ
            //  |
            // *+- 西
            //  |
            dirs.push(west);

            if (!isSouthEnd) {
                // かつ、盤の南端でもなければ
                //  |
                // -+-
                // *|  南西
                dirs.push(south + west);
            }
        }

        if (!isSouthEnd) {
            // 盤の南端でなければ
            //  |
            // -+-
            //  *  南
            dirs.push(south);

            if (!isEastEnd) {
                // かつ、盤の東端でもなければ
                //  |
                // -+-
                //  |* 南東
                dirs.push(south + east);
            }
        }

        for (const dir of dirs) {
            if (this._squares[sq + dir] === PC_X) {
                count += 1;
            }
        }

        return count;
    }

    /**
     * 盤上のマス番号で示して、駒を取得
     * @param {number} sq - マス番号
     */
    getPieceBySq(sq) {
        return this._squares[sq];
    }

    /**
     * 盤サイズ変更
     */
    resize() {
        // 各マス
        this._squares = Array(this.area);

        // 空マスで埋める
        this._squares.fill(PC_EMPTY);
    }

    /**
     * 盤上のマスに駒を上書きします
     *
     * @param {*} sq - マス番号
     * @param {*} piece - 駒
     */
    setPiece(sq, piece) {
        this._squares[sq] = piece;
    }

    /**
     *
     * @returns コピー配列
     */
    toArray() {
        // スプレッド構文
        return [...this._squares];
    }

    /**
     * 変換
     * @param {*} x
     * @param {*} y
     * @returns マス番号
     */
    toSq(x, y) {
        return y * this._width + x;
    }

    /**
     * データ用の部分数列
     *
     * * 矩形で部分指定
     * * シリアライズ = 改行を含まない
     */
    cropRect(ox, oy, width, height) {
        let vec = [];

        let x2 = ox + width;
        let y2 = oy + height;

        if (this._width < x2) {
            x2 = this._width;
        }

        if (this._height < y2) {
            y2 = this._height;
        }

        // 各行
        for (let y = oy; y < y2; y++) {
            for (let x = ox; x < x2; x++) {
                vec.push(this._squares[this.toSq(x, y)]);
            }
        }

        return vec;
    }

    /**
     * データ用の文字列貼り付け, 矩形
     */
    pasteRect(srcVec, width, height, dstX, dstY) {
        // 各行
        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                let srcSq = y * width + x;
                let dstSq = this.toSq(dstX + x, dstY + y);

                this._squares[dstSq] = label_to_pc(srcVec[srcSq]);
            }
        }
    }

    /**
     * 表示用の文字列　枠付き
     * @returns
     */
    toHumanPresentableText() {
        let s = "";

        // 上辺の横線
        s += "+";
        for (let x = 0; x < this._width; x++) {
            s += "-";
        }
        s += "+\n";

        // 各行
        let vec = this.cropRect(0, 0, this._width, this._height);
        let i = 0;
        for (let y = 0; y < this._height; y++) {
            let row = vec.slice(i, i + this._width);
            line = row.map((n) => pc_to_label(n)).join("");
            s += `|${line}|\n`;
            i += this._width;
        }

        // 下辺の横線
        s += "+";
        for (let x = 0; x < this._width; x++) {
            s += "-";
        }
        s += "+\n";

        return s;
    }

    /**
     * 盤面を設定します
     *
     * @param {*} token - Example: `..X.X....`
     */
    parse(token) {
        this._squares = token.split("").map((x) => label_to_pc(x));
    }

    /**
     * ダンプ
     */
    dump(indent) {
        s = `
${indent}Board
${indent}-----`;

        for (let y = 0; y < this._height; y++) {
            s += `
${indent}`;
            for (let x = 0; x < this._width; x++) {
                s += `${this._squares[this.toSq(x, y)]}`;
            }
        }

        return s;
    }
}
