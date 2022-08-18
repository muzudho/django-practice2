// OAAA1001o1o0ga13o_9o0

/**
 * 盤を動的生成
 */
class DynamicHtmlBoard {
    /**
     *
     * @param {number} boardIndex - 盤の番号
     */
    constructor(boardIndex) {
        this._boardIndex = boardIndex;
    }

    /**
     * テーブルを動的生成
     */
    installTable() {
        let lifeGameCanvas = document.getElementById(`life_game_canvas${this._boardIndex}`);
        let sq = 0;

        // 盤について
        // 縦に並べる
        for (let y = 0; y < vue1.engine.position.boards[this._boardIndex].height; y++) {
            // 横に並べる
            for (let x = 0; x < vue1.engine.position.boards[this._boardIndex].width; x++) {
                let span = document.createElement("span");
                let cellId = `b${this._boardIndex}_sq${sq}`;
                span.setAttribute("id", cellId);
                sq++;
                span.setAttribute("class", "dead");
                // 正方形に近い文字
                span.textContent = "■";

                span.setAttribute("onClick", `vue1.onCellClicked("${cellId}"); return false;`);
                // span.setAttribute("onClick", "alert('test'); return false;");

                lifeGameCanvas.appendChild(span);
            }

            // 改行
            let br = document.createElement("br");
            lifeGameCanvas.appendChild(br);
        }
    }

    /**
     * テーブルを削除
     */
    uninstallTable() {
        let lifeGameCanvas = document.getElementById(`life_game_canvas${this._boardIndex}`);

        // 子要素を全て削除
        var child = lifeGameCanvas.lastElementChild;
        while (child) {
            lifeGameCanvas.removeChild(child);
            child = lifeGameCanvas.lastElementChild;
        }
    }
}
