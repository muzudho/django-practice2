# 前回の記事

📖 [DjangoとDocker自由課題OAAA1001o1o0 ライフゲームを作ろう！](https://qiita.com/muzudho1/items/a2c90f8d3dfaad849211)  

# Step OAAA1001o1o0ga13o__10o0 画面作成 - gui/cell_id_helper/v1o0.js ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_v1          # アプリケーションと同名
        │       │       ├── 📂 gui
        │       │       │   └── 📂 cell_id_helper
👉      │       │       │       └── 📄 v1o0.js
        │       │       └── 📂 think
        │       │           ├── 📂 engine
        │       │           │   ├── 📂 parser
        │       │           │   │   └── 📄 v1o0.js
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1
        │       │       └── 📂 board
        │       │           ├── 📄 v0o1o0.html
        │       │           └── 📄 v0o2o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       ├── 📂 v0o1o0
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 v0o2o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
👉          ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```js
// OAAA1001o1o0ga13o__10o0

class CellIdHelper {
    /**
     * IDを作成します
     * @param {*} boardIndex - 盤番号
     * @param {*} sq - セル番号
     */
    static createId(boardIndex, sq) {
        return `b${boardIndex}_sq${sq}`;
    }

    static destructuringId(id) {
        const re = /b(\d+)_sq(\d+)/;
        const result = id.match(re);

        return [parseInt(result[1]), parseInt(result[2])];
    }
}
```

# Step OAAA1001o1o0ga13o_1o0 画面作成 - gui/dynamic_html_board/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_v1          # アプリケーションと同名
        │       │       ├── 📂 gui
        │       │       │   └── 📂 dynamic_html_board
👉      │       │       │       └── 📄 v1o0.js
        │       │       └── 📂 think
        │       │           ├── 📂 engine
        │       │           │   ├── 📂 parser
        │       │           │   │   └── 📄 v1o0.js
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1
        │       │       └── 📂 board
        │       │           ├── 📄 v0o1o0.html
        │       │           └── 📄 v0o2o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       ├── 📂 v0o1o0
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 v0o2o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
            ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```js
// OAAA1001o1o0ga13o_1o0

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
                let cellId = CellIdHelper.createId(this._boardIndex, sq);
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
```

# Step OAAA1001o1o0ga13o0 画面作成 - board/v0o3o0.html.txt ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_v1          # アプリケーションと同名
        │       │       ├── 📂 gui
        │       │       │   └── 📂 dynamic_html_board
        │       │       │       └── 📄 v1o0.js
        │       │       └── 📂 think
        │       │           ├── 📂 engine
        │       │           │   ├── 📂 parser
        │       │           │   │   └── 📄 v1o0.js
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1
        │       │       └── 📂 board
        │       │           ├── 📄 v0o1o0.html
        │       │           ├── 📄 v0o2o0.html.txt
👉      │       │           └── 📄 v0o3o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       ├── 📂 v0o1o0
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 v0o2o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
            ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```html
<!-- OAAA1001o1o0ga13o0 -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<html>
    <head>
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui" />
        <title>Life game</title>
        <style>
            /* 等幅 */
            .v-textarea textarea {
                font-family: monospace, monospace;
            }
            /* 生きているセル */
            .live {
                font-family: monospace, monospace;
                color:#FFC107; /* amber */
                background-color:#FFC107; /* amber */
                border:solid 1px black;
            }
            /* 死んでいるセル */
            .dead {
                font-family: monospace, monospace;
                color:#607D8B; /* blue-gray */
                background-color:#607D8B; /* blue-gray */
                border:solid 1px black;
            }
            /* エラーのセル */
            .error {
                font-family: monospace, monospace;
                color:red;
                background-color:red;
                border:solid 1px black;
            }
        </style>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container fluid>
                        <h1>Life game</h1>
                        <div>
                            Original: 📖 <a href="https://conwaylife.com/">https://conwaylife.com/</a><br/>
                            Tutorial Video: 📺 <a href="https://www.youtube.com/playlist?list=PLZC7Zqdh0Qb3wOpit5dewit3q2-Mqg9vC">THE RECURSIVE COSMOS: Conway's Game of Life ライフゲームの世界</a>
                        </div>
                    </v-container>
                    <!--
                        ディスプレイ部
                        横幅いっぱい広げるために fluid を指定
                    -->
                    <v-container fluid>
                        <!-- 盤０ -->
                        <v-card
                            elevation="2"
                        >
                            <v-card-title>board 0</v-card-title>
                            <v-card-text>
                                <!-- Example: <span id="b0_sq0" class="live">■</span><span id="b0_sq1" class="dead">■</span> -->
                                <div id="life_game_canvas0" style="line-height:1;"></div>
                                <!-- 再生ボタン -->
                                <v-btn block elevation="2" v-on:click="playVu()" v-show="playButton.isShow" :disabled="!playButton.enabled"> ▶ Play </v-btn>
                                <!-- 一時停止ボタン -->
                                <v-btn block elevation="2" v-on:click="pauseVu()" v-show="pauseButton.isShow" :disabled="!pauseButton.enabled"> ▮▮ Pause </v-btn>
                                <div>Pause, then click a cell.</div>
                            </v-card-text>
                        </v-card>

                        <!-- 盤１ -->
                        <v-card
                            elevation="2"
                        >
                            <v-card-title>board 1</v-card-title>
                            <v-card-text>
                                <div id="life_game_canvas1" style="line-height:1;"></div>
                            </v-card-text>
                        </v-card>

                        <!-- 盤２ -->
                        <v-card
                            elevation="2"
                        >
                            <v-card-title>board 2</v-card-title>
                            <v-card-text>
                                <div id="life_game_canvas2" style="line-height:1;"></div>
                            </v-card-text>
                        </v-card>
                    </v-container>
                    <!-- テキストエディター部 -->
                    <v-container fluid>
                        <v-form method="POST">
                            {% csrf_token %}

                            <!-- `po_` は POST送信するパラメーター名の目印 -->
                            <!-- 入力 -->
                            <v-textarea name="po_input" required rows="6" v-model="inputText.value" label="Input" :disabled="!inputText.enabled" background-color="#263238" dark></v-textarea>

                            <!-- 入力ボタン -->
                            <v-btn block elevation="2" v-on:click="enterVu()" :disabled="!enterButton.enabled"> Enter </v-btn>

                            <!-- 出力 -->
                            <v-textarea name="po_output" rows="1" disabled v-model="outputText.value" label="Output"></v-textarea>
                        </v-form>
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="{% static 'lifegame_v1/gui/cell_id_helper/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/gui/dynamic_html_board/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/think/engine/parser/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/think/engine/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/think/position/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/think/things/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/think/things/board/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/think/user_ctrl/v1o0.js' %}"></script>
        <!--            ===========================================
                        1
        1. src1/apps1/lifegame_v1/static/lifegame_v1/think/user_ctrl/v1o0.js
                                  ==========================================
        -->

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            /**
             * 盤の数
             */
            let BOARDS_COUNT = 3;

            // 盤を動的生成
            let dynamicHtmlBoards = Array(BOARDS_COUNT);

            // 全要素の初期化（.fill()は参照渡しなので使いません）
            for (let i = 0; i < BOARDS_COUNT; i++) {
                dynamicHtmlBoards[i] = new DynamicHtmlBoard(i);
            }

            const vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // 入力
                    inputText: {
                        enabled: true,
                        value: `# 盤[0] ムービー
# サイズ
board 0 width 64
board 0 height 32
# 点描
board 0 """
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
................................................................
"""

# 盤[1] 停止
# サイズ
board 1 width 64
board 1 height 6
# 点描
#    5     11   16   21    27 30    36    42    48
board 1 """
................................................................
.xx...xx...xx....xx...xx...x...xx...xx.....x.....x..............
.xx..x..x..x.x..x.x..x..x..x..x.....x......x.x....x.............
......xx....x...xx...x..x..x.....x.....x..x.x...xxx.............
......................xx.......xx.....xx....x...................
................................................................
"""

# 盤[2] 停止
# サイズ
board 2 width 64
board 2 height 7
# 点描
board 2 """
................................................................
.xxx...xxx...xxx..xxx..xxx...x...x..xxx.........................
.x..x..x....x.....x....x..x..x...x..x...........................
.xxx...xxx...xx...xxx..xxx...x...x..xxx.........................
.x..x..x.......x..x....x..x...x.x...x...........................
.x..x..xxx..xxx...xxx..x..x....x....xxx.........................
................................................................
"""

# コピー
# グライダー
board 0 xy 1 1 copy_from board 1 rect 48 1 3 3
# ブロック
board 0 xy 10 3 copy_from board 1 rect 1 1 2 2
# 蜂の巣
board 0 xy 17 5 copy_from board 1 rect 5 1 4 3
# ボート
board 0 xy 24 3 copy_from board 1 rect 11 1 3 3
# 船
board 0 xy 31 6 copy_from board 1 rect 16 1 3 3
# 池
board 0 xy 38 2 copy_from board 1 rect 21 1 4 4
# ブリンカー
board 0 xy 45 5 copy_from board 1 rect 27 1 1 3
# ヒキガエル
board 0 xy 52 8 copy_from board 1 rect 30 1 4 4
# ビーコン
board 0 xy 57 3 copy_from board 1 rect 36 1 4 4
# 時計
board 0 xy 46 15 copy_from board 1 rect 42 1 4 4
`,
                    },
                    // 出力
                    outputText: {
                        value: 'Please push "Enter" button.',
                    },
                    // 思考エンジン
                    engine: new Engine(
                        // ユーザーコントロール
                        new UserCtrl(),
                        // 盤の数
                        BOARDS_COUNT
                    ),
                    // 入力ボタン
                    enterButton: {
                        enabled: true,
                    },
                    // 再生ボタン
                    playButton: {
                        enabled: false,
                        isShow: true,
                    },
                    // 一時停止ボタン
                    pauseButton: {
                        enabled: true,
                        isShow: false,
                    },
                    // 入力されたテキスト
                    enteredText : null,
                    // タイマー
                    timer: {
                        // 停止するのに使う
                        id: null,
                        // 再生間隔（ミリ秒）
                        intervalMilliseconds: 100,
                    },
                },
                mounted() {
                    window.onload = ()=>{
                        console.log('ページが読み込まれました！');

                        // 初期状態を設定
                        let boardIndex = 0;
                        vue1.engine.position.boards[boardIndex].width = 24;
                        vue1.engine.position.boards[boardIndex].height = 24;
                        vue1.engine.position.boards[boardIndex].parse(`........................
........................
........................
........................
........................
........................
........................
........................
........................
........................
........................
.........x....x.........
.......xx.xxxx.xx.......
.........x....x.........
........................
........................
........................
........................
........................
........................
........................
........................
........................
........................`.replace(/\r?\n/g, ''));

                        // GUIに反映
                        dynamicHtmlBoards[boardIndex].uninstallTable();
                        dynamicHtmlBoards[boardIndex].installTable();

                        // 初期状態を描画
                        this.repaintVu();

                        // 自動再生する
                        this.playVu();
                    }
                },
                methods: {
                    // 関数名の末尾の Vu は vue1 のメソッドであることを表す目印
                    /**
                     * po_input 欄のコマンドを入力します
                     */
                    enterVu() {
                        console.log("入力ボタンをクリックした");

                        // this.inputText.enabled = false;
                        // this.enterButton.enabled = false;

                        this.enteredText = vue1.inputText.value;
                        vue1.inputText.value = "";

                        // 入力テキストを処理
                        // * タイマーの処理が走っているときに、この処理がどう割り込むのか分からない
                        this.processingTextVu();
                    },
                    /**
                     * 画面更新
                     */
                    updateVu() {
                        if (this.enteredText !== null) {
                            // 入力テキストを処理
                            this.processingTextVu();
                        } else {
                            // 盤[0]を動かす。それ以外の盤は動かさない
                            let boardIndex = 0;
                            vue1.engine.userCtrl.doMove(vue1.engine.position, boardIndex);
                        }

                        this.repaintVu();
                    },
                    /**
                     * 入力テキストを処理
                     */
                    processingTextVu(){
                        // 盤のサイズを一時記憶
                        let widthOfBoards = new Array(BOARDS_COUNT);
                        widthOfBoards.fill(0);
                        let heightOfBoards = new Array(BOARDS_COUNT);
                        heightOfBoards.fill(0);
                        for(let boardIndex=0; boardIndex<BOARDS_COUNT; boardIndex++){
                            widthOfBoards[boardIndex] = vue1.engine.position.boards[boardIndex].width;
                            heightOfBoards[boardIndex] = vue1.engine.position.boards[boardIndex].height;
                        }

                        // コマンドを実行
                        let log = vue1.engine.execute(this.enteredText);
                        this.enteredText = null;

                        this.outputText.value = log;

                        // 盤のサイズが変わっていれば作り直し
                        for(let boardIndex=0; boardIndex<BOARDS_COUNT; boardIndex++){
                            if (widthOfBoards[boardIndex] !== vue1.engine.position.boards[boardIndex].width ||
                                heightOfBoards[boardIndex] !== vue1.engine.position.boards[boardIndex].height) {
                                dynamicHtmlBoards[boardIndex].uninstallTable();
                                dynamicHtmlBoards[boardIndex].installTable();
                            }
                        }
                    },
                    /**
                     * 再描画
                     */
                    repaintVu(){
                        // 盤表示
                        for(let boardIndex=0; boardIndex<BOARDS_COUNT; boardIndex++){
                            vue1.engine.position.boards[boardIndex].eachSq((sq, cellValue) => {
                                const cellId = CellIdHelper.createId(boardIndex, sq);
                                let cell = document.getElementById(cellId);
                                switch(cellValue) {
                                    case PC_X:
                                        cell.setAttribute("class", "live");
                                        break;

                                    case PC_EMPTY:
                                        cell.setAttribute("class", "dead");
                                        break;

                                    default:
                                        cell.setAttribute("class", "error");
                                        break;
                                }
                            })
                        }
                    },
                    /**
                     * 再生ボタンをクリックした
                     */
                    playVu(){
                        // console.log("再生ボタンをクリックした");

                        this.playButton.enabled = false;
                        this.playButton.isShow = false;

                        // タイマー開始
                        this.timer.id = setInterval(() => {
                            this.updateVu();
                        }, this.timer.intervalMilliseconds);

                        this.pauseButton.enabled = true;
                        this.pauseButton.isShow = true;
                    },
                    /**
                     * 停止ボタンをクリックした
                     */
                    pauseVu(){
                        // console.log("停止ボタンをクリックした");

                        this.pauseButton.enabled = false;
                        this.pauseButton.isShow = false;

                        // タイマー停止
                        clearInterval(this.timer.id);

                        this.playButton.enabled = true;
                        this.playButton.isShow = true;
                    },
                    /**
                     * セルクリック時
                     */
                    onCellClicked(cellId){
                        const [boardIndex, sq] = CellIdHelper.destructuringId(cellId);

                        // Reverse piece
                        const revPc = flip_pc(vue1.engine.position.boards[boardIndex].getPieceBySq(sq));
                        // alert(`cell clicked id:${cellId} board:${boardIndex} sq:${sq} revPc:${revPc}`);

                        vue1.engine.position.boards[boardIndex].setPiece(sq, revPc);

                        // 再生中に１セル塗っても、すぐ消える。
                        // 一時停止中に塗る。
                        // 一時停止中は描画されないので、明示的に再描画する
                        this.repaintVu();
                    },
                },
            });
        </script>
    </body>
</html>
```

# Step OAAA1001o1o0ga14o0 ビュー作成 - board/v0o3o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_v1          # アプリケーションと同名
        │       │       ├── 📂 gui
        │       │       │   └── 📂 dynamic_html_board
        │       │       │       └── 📄 v1o0.js
        │       │       └── 📂 think
        │       │           ├── 📂 engine
        │       │           │   ├── 📂 parser
        │       │           │   │   └── 📄 v1o0.js
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1
        │       │       └── 📂 board
        │       │           ├── 📄 v0o1o0.html
        │       │           ├── 📄 v0o2o0.html.txt
        │       │           └── 📄 v1o0o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       ├── 📂 v0o1o0
        │       │       │   └── 📄 __init__.py
        │       │       ├── 📂 v0o2o0
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 v0o3o0
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
            ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```py
from django.shortcuts import render


class BoardView():
    """OAAA1001o1o0ga14o0 盤"""

    @staticmethod
    def render(request):
        """描画"""

        # * `_lp` - Local path
        this_page_lp = 'lifegame_v1/board/v0o3o0.html.txt'
        #               ---------------------------------
        #               1
        # 1. `src1/apps1/lifegame_v1/templates/lifegame_v1/board/v0o3o0.html.txt` を取得
        #                                      ---------------------------------

        context = {}
        return render(request, this_page_lp, context)
```

# Step OAAA1001o1o0ga15o0 サブ ルート作成 - urls_lifegame.py

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_v1          # アプリケーションと同名
        │       │       ├── 📂 gui
        │       │       │   └── 📂 dynamic_html_board
        │       │       │       └── 📄 v1o0.js
        │       │       └── 📂 think
        │       │           ├── 📂 engine
        │       │           │   ├── 📂 parser
        │       │           │   │   └── 📄 v1o0.js
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1
        │       │       └── 📂 board
        │       │           ├── 📄 v0o1o0.html
        │       │           ├── 📄 v0o2o0.html.txt
        │       │           └── 📄 v1o0o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       ├── 📂 v0o1o0
        │       │       │   └── 📄 __init__.py
        │       │       ├── 📂 v0o2o0
        │       │       │   └── 📄 __init__.py
        │       │       └── 📂 v0o3o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
👉          ├── 📄 urls_lifegame.py
            └── 📄 urls.py
```

```py
# ...略...


# OAAA1001o1o0ga15o0 ライフゲーム v0.3 の盤
from apps1.lifegame_v1.views.board.v0o3o0 import BoardView as BoardViewV0o3o0
#          -----------             ------        ---------    ---------------
#          11                      12            2            3
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [
    # ...略...


    # OAAA1001o1o0ga15o0 ライフゲーム v0.3 の盤
    path('lifegame/v0.3/board',
         # ------------------
         # 1
         BoardViewV0o3o0.render, name='lifegame_v0o3o0_board'),
    #    ----------------------        ---------------------
    #    2                             3
    # 1. 例えば `http://example.com/lifegame/v0.3/board` のようなURLのパスの部分
    #                              -------------------
    # 2. BoardViewV0o3o0 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'lifegame_v0o3o0_board' %} のような形でURLを取得するのに使える
]
```

# Step OAAA1001o1o0ga16o0 Webページにアクセスする

📖 [http://localhost:8000/lifegame/v0.3/board](http://localhost:8000/lifegame/v0.3/board)  
