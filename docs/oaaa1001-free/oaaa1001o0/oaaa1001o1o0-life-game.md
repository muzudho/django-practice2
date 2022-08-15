# 目的

ライフゲームを作る

# はじめに

この記事は 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) のレッスン編を読み終えた人を対象とする  

# Step OAAA1001o1o0g1o0 Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step OAAA1001o1o0g2o0 フォルダー作成 - apps1/lifegame_v1 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1                # 複数のアプリケーションを入れるフォルダー
            └── 📂 lifegame_v1      # アプリケーション
```

# Step OAAA1001o1o0g3o0 アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp lifegame_v1 ./apps1/lifegame_v1 --settings=project1.settings
#                                                     ----------- -------------------            -----------------
#                                                     1           2                              3
# 1. 任意のDjangoアプリケーション名
# 2. アプリケーション フォルダーへのパス
# 3. `src1/project1/settings.py` 設定ファイルに従う
#          -----------------
```

👇 以下のようなディレクトリー、ファイルが自動生成される  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 lifegame_v1              # アプリケーション
👉              ├── 📂 migrations
👉              │   └── 📄 __init__.py
👉              ├── 📄 __init__.py
👉              ├── 📄 admin.py
👉              ├── 📄 apps.py
👉              ├── 📄 models.py
👉              ├── 📄 tests.py
👉              └── 📄 views.py
```

# Step OAAA1001o1o0g4o0 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1              # アプリケーション名
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
                ├── 📄 apps.py
👉              ├── 📄 models.py
                ├── 📄 tests.py
👉              └── 📄 views.py
```

# Step OAAA1001o1o0g5o0 アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 lifegame_v1              # アプリケーション
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
👉              ├── 📄 apps.py
                └── 📄 tests.py
```

```py
from django.apps import AppConfig


class LifegameV1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    # name = 'lifegame_v1'
    # * OAAA1001o1o0g5o0 変更後
    name = 'apps1.lifegame_v1'
    #       -----------------
    #       1
    # 1. `src1/apps1/lifegame_v1/apps.py`
    #          -----------------
```

# Step OAAA1001o1o0g6o0 アプリケーション登録 - settings.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1              # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
👉          └── 📄 settings.py
```

```py
# ...略...


INSTALLED_APPS = [
    # ...略...
    # あなたが追加したアプリケーション
    # ...略...


    # OAAA1001o1o0g6o0 ライフゲーム v1
    'apps1.lifegame_v1',


    # ...略...
    # Djangoの標準アプリケーション
    # ...略...
]


# ...略...
```

# Step OAAA1001o1o0g7o0 画面作成 - board/v0o1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1              # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1      # アプリケーションと同名
        │       │       └── 📂 board
👉      │       │           └── 📄 v0o1o0.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```html
<!-- OAAA1001o1o0g7o0 -->
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
        </style>
    </head>
    <body>
        {% block body %}
        <!-- -->
        ここに本体を書く
        <!-- -->
        {% endblock body %}
    </body>
</html>
```

# Step OAAA1001o1o0g8o0 設定変更 - settings.py ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1              # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1      # アプリケーションと同名
        │       │       └── 📂 board
        │       │           └── 📄 v0o1o0.html
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
👉          └── 📄 settings.py
```

👇 変更するのは `TEMPLATES[0]["DIRS"]` 変数  

```py
TEMPLATES = [
    {
        # ...略... 'BACKEND'


        'DIRS': [
            # ...略...


            # OAAA1001o1o0g8o0 ライフゲーム v1
            os.path.join(BASE_DIR, 'apps1/lifegame_v1/templates'),
            #                       ---------------------------
            #                       10
            # Example: /src1/apps1/lifegame_v1/templates/lifegame_v1/board/v0o1o0.html
            #                      -----------          ------------
            #                      11                   2
            #                ---------------------------
            #                10
            # 10. テンプレート ディレクトリーへのパス
            # 11. アプリケーション
            # 2. まるで `http://example.com/lifegame_v1` という素材フォルダーがあるかのように扱われる
            #                             ------------
        ],


        # ...略... 'APP_DIRS' や 'OPTIONS'
    },
]
```

# Step OAAA1001o1o0g9o0 ビュー作成 - board/v0o1 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1              # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1      # アプリケーションと同名
        │       │       └── 📂 board
        │       │           └── 📄 v0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v0o1o0
👉      │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
from django.shortcuts import render


class BoardView():
    """OAAA1001o1o0g9o0 盤"""

    @staticmethod
    def render(request):
        """描画"""

        # * `_lp` - Local path
        this_page_lp = 'lifegame_v1/board/v0o1o0.html'
        #               -----------------------------
        #               1
        # 1. `src1/apps1/lifegame_v1/templates/lifegame_v1/board/v0o1o0.html` を取得
        #                                      -----------------------------

        context = {}
        return render(request, this_page_lp, context)
```

# Step OAAA1001o1o0ga10o0 サブ ルート作成 - urls_lifegame.py

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1              # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1      # アプリケーションと同名
        │       │       └── 📂 board
        │       │           └── 📄 v0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v0o1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
👉          ├── 📄 urls_lifegame.py          # 新規作成
❌          └── 📄 urls.py                   # これではない
```

```py
from django.urls import path

# OAAA1001o1o0g9o0 ライフゲーム v0.1 の盤
from apps1.lifegame_v1.views.board.v0o1o0 import BoardView as BoardViewV0o1o0
#          -----------             ------        ---------    ---------------
#          11                      12            2            3
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [

    # OAAA1001o1o0ga10o0 ライフゲーム v0.1 の盤
    path('lifegame/v0.1/board',
         # ------------------
         # 1
         BoardViewV0o1o0.render, name='lifegame_v0o1o0_board'),
    #    ----------------------        ---------------------
    #    2                             3
    # 1. 例えば `http://example.com/lifegame/v0.1/board` のようなURLのパスの部分
    #                              -------------------
    # 2. BoardViewV0o1o0 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'lifegame_v0o1o0_board' %} のような形でURLを取得するのに使える
]
```

# Step OAAA1001o1o0ga11o0 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1
        │       │       └── 📂 board
        │       │           └── 📄 v0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v0o1o0
        │       │           └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
            ├── 📄 settings.py
❌          ├── 📄 urls_lifegame.py          # これではない
👉          └── 📄 urls.py                   # こっち
```

```py
# ...略...


urlpatterns = [
    # ...略...


    # OAAA1001o1o0ga11o0 ライフゲーム
    path('', include(f'{PROJECT_NAME}.urls_lifegame')),
    #    --            ----------------------------
    #    1             2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `src1/projectN/urls_lifegame.py` の urlpatterns を `1.` にぶら下げる
    #          ----------------------
]
```

# Step OAAA1001o1o0ga12o_1o__99o0 Webページにアクセスする

👇 接続の確認だけしてほしい  

📖 [http://localhost:8000/lifegame/v0.1/board](http://localhost:8000/lifegame/v0.1/board)  

# Step OAAA1001o1o0ga12o_1o0 物の定義 - think/things/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_v1          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           └── 📂 things
👉      │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1
        │       │       └── 📂 board
        │       │           └── 📄 v0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v0o1o0
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
// OAAA1001o1o0ga12o_9o0

// +--------
// | 駒
// |

/**
 * PC は Piece （駒）の略です
 * @type {number}
 */
const PC_EMPTY = 0; // セルに何も置いていないことを表します
const PC_X = 1; // 塗りつぶしたセルを表します

/**
 * ラベル
 * @type {string}
 */
const PC_EMPTY_LABEL = ".";
const PC_X_LABEL = "X";

/**
 * 定数をラベルに変換
 *
 * @param {int} pc
 * @returns {str} label
 */
function pc_to_label(pc) {
    switch (pc) {
        case PC_EMPTY:
            return PC_EMPTY_LABEL;
        case PC_X:
            return PC_X_LABEL;
        default:
            return pc;
    }
}

/**
 * ラベルを定数に変換
 *
 * @param {str} - label
 * @returns {int} - pc
 */
function label_to_pc(label) {
    switch (label) {
        case PC_EMPTY_LABEL:
            return PC_EMPTY;
        case PC_X_LABEL:
            return PC_X;
        default:
            return label;
    }
}

// |
// | 駒
// +--------

// +--------
// | 盤
// |

/**
 * 盤の横幅
 * @type {number}
 */
const BOARD_WIDTH = 64;

/**
 * 盤の縦幅
 * @type {number}
 */
const BOARD_HEIGHT = 64;

/**
 * 盤上の升の数
 * @type {number}
 */
const BOARD_AREA = BOARD_WIDTH * BOARD_HEIGHT;

/*
 * SQ は Square （マス）の略です
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
        // 各マス
        this._squares = Array(BOARD_AREA);
        this._squares.fill(PC_EMPTY);
    }

    /**
     * 各マスについて変換
     * @param {function} convertCell - (sq, cellValue)
     */
    convertEachSq(convertCell) {
        let nextBoard = Array(BOARD_AREA);

        for (let sq = 0; sq < BOARD_AREA; sq++) {
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
        for (let sq = 0; sq < BOARD_AREA; sq++) {
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

        const north = -BOARD_WIDTH; // 北
        const east = 1; // 東
        const south = BOARD_WIDTH; // 南
        const west = -1; // 西
        const next = [
            sq + north, // 北
            sq + north + east, // 北東
            sq + east, // 東
            sq + south + east, // 南東
            sq + south, // 南
            sq + south + west, // 南西
            sq + west, // 西
            sq + north + west, // 北西
        ];

        for (const nx of next) {
            if (0 <= nx && nx < BOARD_AREA && this._squares[nx] === PC_X) {
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
        return y * BOARD_WIDTH + x;
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

        for (let y = 0; y < BOARD_HEIGHT; y++) {
            s += `
${indent}`;
            for (let x = 0; x < BOARD_WIDTH; x++) {
                s += `${this._squares[this.toSq(x, y)]}`;
            }
        }

        return s;
    }
}

// | 盤
// |
// +--------

// +--------
// | 棋譜
// |

// なし

// | 棋譜
// |
// +--------
```

# Step OAAA1001o1o0ga12o_2o0 局面作成 - think/position/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_v1          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           ├── 📂 position
👉      │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 things
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1
        │       │       └── 📂 board
        │       │           └── 📄 v0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v0o1o0
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
// OAAA1001o1o0ga12o_2o0

/**
 * 局面
 */
class Position {
    /**
     * 初期化
     *
     * * 対局開始時
     */
    constructor() {
        // 盤面
        this._board = new Board();

        // 棋譜
        // なし

        // 番
        // なし
    }

    /**
     * 盤
     */
    get board() {
        return this._board;
    }

    toBoardString() {
        // 各マス
        const label_of_squares = this._board.toArray().map((n) => pc_to_label(n));

        let s = "";

        // 上辺の横線
        s += "+";
        for (let x = 0; x < BOARD_WIDTH; x++) {
            s += "-";
        }
        s += "+\n";

        // 各行
        for (let y = 0; y < BOARD_HEIGHT; y++) {
            s += "|";
            for (let x = 0; x < BOARD_WIDTH; x++) {
                s += label_of_squares[this._board.toSq(x, y)];
            }
            s += "|\n";
        }

        // 下辺の横線
        s += "+";
        for (let x = 0; x < BOARD_WIDTH; x++) {
            s += "-";
        }
        s += "+\n";

        return s;
    }

    /**
     * ダンプ
     */
    dump(indent) {
        return `
${indent}Position
${indent}--------
${indent}${this._board.dump(indent + "    ")}`;
    }
}
```

# Step OAAA1001o1o0ga12o_3o0 ユーザーコントロール作成 - think/user_ctrl/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_v1          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
👉      │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1
        │       │       └── 📂 board
        │       │           └── 📄 v0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v0o1o0
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
// OAAA1001o1o0ga12o_3o0

/**
 * ユーザーコントロール
 */
class UserCtrl {
    /**
     * 時間を１つ進めます
     *
     * @param {Position} position - 局面
     */
    doMove(position) {
        this._position = position;
        // セルの変化
        this._position.board.convertEachSq((sq, cellValue) => {
            let count = this._position.board.getLifeCountAround(sq);

            switch (cellValue) {
                case PC_EMPTY: // 生命のいない場所
                    // 周囲８近傍に生命が３個あれば、ここに生命が誕生
                    if (count === 3) {
                        return PC_X;
                    }
                    return cellValue;

                case PC_X: // 生命のいる場所
                    // 周囲８近傍に生命が２個または３個あるケース以外では、この生命は消滅
                    if (count === 2 || count === 3) {
                        return cellValue;
                    }
                    return PC_EMPTY;

                default:
                    throw `Unexpected piece:${cellValue} sq:${sq}`;
            }
        });
        this._position = null;
    }
}
```

# Step OAAA1001o1o0ga12o_4o0 エンジン作成 - think/engine/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_v1          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           ├── 📂 engine
👉      │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 position
        │       │           │   └── 📄 v1o0.js
        │       │           ├── 📂 things
        │       │           │   └── 📄 v1o0.js
        │       │           └── 📂 user_ctrl
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 lifegame_v1
        │       │       └── 📂 board
        │       │           └── 📄 v0o1o0.html
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v0o1o0
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
        // 実行時の現在のエグゼキューター
        this._executeCurr = null;
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
        let positionText = "";
        let executePosition = (line) => {
            switch (line) {
                case '"""':
                    {
                        this.position.board.parse(positionText);
                        positionText = "";

                        this._executeCurr = executeMain;
                    }
                    break;

                default:
                    {
                        positionText += `${line}`;
                    }
                    break;
            }
        };
        let executeMain = (line) => {
            const tokens = line.split(" ");
            switch (tokens[0]) {
                case "board":
                    {
                        // Example: `board`
                        this._log += this._position.toBoardString();
                    }
                    break;

                case "play":
                    {
                        // Example: `play`
                        this._userCtrl.doMove(this._position);
                        // Ok
                        this._log += "=\n.\n";
                    }
                    break;

                case 'position"""':
                    {
                        positionText = "";
                        this._executeCurr = executePosition;
                    }
                    break;

                default:
                    // ignored
                    break;
            }
        };
        this._executeCurr = executeMain;
        this._log = "";

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
```

# Step OAAA1001o1o0ga12o_5o0 画面作成 - board/v0o2o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_v1          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           ├── 📂 engine
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
👉      │       │           └── 📄 v0o2o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 board
        │       │       └── 📂 v0o1o0
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
{# OAAA1001o1o0ga12o_5o0 #}
<!-- -->
{% extends "lifegame_v1/board/v0o1o0.html" %}
{#          -----------------------------
            1
1. src1/apps1/lifegame_v1/templates/lifegame_v1/board/v0o1o0.html
                                    -----------------------------
#}
{% load static %} {# 👈あとで static "URL" を使うので load static します #}

{% block body %}
        <div id="app">
            <v-app>
                <v-main>
                    <v-container fluid>
                        <h1>Life game Engine Test</h1>
                        <v-form method="POST">
                            {% csrf_token %}

                            <!-- `po_` は POST送信するパラメーター名の目印 -->
                            <!-- 入力 -->
                            <v-textarea name="po_input" required v-model="inputText.value" label="Input"></v-textarea>

                            <v-btn block elevation="2" v-on:click="executeVu()"> Execute </v-btn>

                            <!-- 出力 -->
                            <v-textarea name="po_output" required v-model="outputText.value" label="Output"></v-textarea>
                        </v-form>
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="{% static 'lifegame_v1/think/engine/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/think/position/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/think/things/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/think/user_ctrl/v1o0.js' %}"></script>
        <!--            ===========================================
                        1
        1. src1/apps1/lifegame_v1/static/lifegame_v1/think/user_ctrl/v1o0.js
                                  ==========================================
        -->

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            const vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // 入力
                    inputText: {
                        value: `
# 64x64 グライダー
position"""
................................................................
................................................................
....X...........................................................
.....X..........................................................
...XXX..........................................................
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
board
play
board
play
board
play
board
play
board
`,
                    },
                    // 出力
                    outputText: {
                        value: 'Please push "Execute" button.',
                    },
                    // 思考エンジン
                    engine: new Engine(
                        // ユーザーコントロール
                        new UserCtrl()
                    ),
                },
                methods: {
                    // 関数名の末尾の Vu は vue1 のメソッドであることを表す目印
                    /**
                     * po_input 欄のコマンドを入力します
                     */
                    executeVu() {
                        // console.log(`[methods executeVu]`);
                        vue1.outputText.value = vue1.engine.execute(vue1.inputText.value);
                    },
                },
            });
        </script>
{% endblock body %}
```

# Step OAAA1001o1o0ga12o_6o0 ビュー作成 - board/v0o2o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_v1          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           ├── 📂 engine
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
    """OAAA1001o1o0ga12o_6o0 盤"""

    @staticmethod
    def render(request):
        """描画"""

        # * `_lp` - Local path
        this_page_lp = 'lifegame_v1/board/v0o2o0.html.txt'
        #               ---------------------------------
        #               1
        # 1. `src1/apps1/lifegame_v1/templates/lifegame_v1/board/v0o2o0.html.txt` を取得
        #                                      ---------------------------------

        context = {}
        return render(request, this_page_lp, context)
```

# Step OAAA1001o1o0ga12o_7o0 サブ ルート作成 - urls_lifegame.py

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 lifegame_v1                  # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📂 static
        │       │   └── 📂 lifegame_v1          # アプリケーションと同名
        │       │       └── 📂 think
        │       │           ├── 📂 engine
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

```py
# ...略...


# OAAA1001o1o0ga12o_7o0 ライフゲーム v0.2 の盤
from apps1.lifegame_v1.views.board.v0o2o0 import BoardView as BoardViewV0o2o0
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


    # OAAA1001o1o0ga12o_7o0 ライフゲーム v0.2 の盤
    path('lifegame/v0.2/board',
         # ------------------
         # 1
         BoardViewV0o2o0.render, name='lifegame_v0o2o0_board'),
    #    ----------------------        ---------------------
    #    2                             3
    # 1. 例えば `http://example.com/lifegame/v0.2/board` のようなURLのパスの部分
    #                              -------------------
    # 2. BoardViewV0o2o0 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'lifegame_v0o2o0_board' %} のような形でURLを取得するのに使える
]
```

# Step OAAA1001o1o0ga12o0 Webページにアクセスする

📖 [http://localhost:8000/lifegame/v0.2/board](http://localhost:8000/lifegame/v0.2/board)  

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
        │       │       └── 📂 think
        │       │           ├── 📂 engine
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
        </style>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container fluid>
                        <h1>Life game Engine Test</h1>
                        <v-form method="POST">
                            {% csrf_token %}

                            <!-- `po_` は POST送信するパラメーター名の目印 -->
                            <!-- 入力 -->
                            <v-textarea name="po_input" required v-model="inputText.value" label="Input"></v-textarea>

                            <v-btn block elevation="2" v-on:click="executeVu()"> Execute </v-btn>

                            <!-- 出力 -->
                            <v-textarea name="po_output" required v-model="outputText.value" label="Output"></v-textarea>
                            <v-btn
                                elevation="1"
                                tile
                                x-small
                            ></v-btn>
                        </v-form>
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="{% static 'lifegame_v1/think/engine/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/think/position/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/think/things/v1o0.js' %}"></script>
        <script src="{% static 'lifegame_v1/think/user_ctrl/v1o0.js' %}"></script>
        <!--            ===========================================
                        1
        1. src1/apps1/lifegame_v1/static/lifegame_v1/think/user_ctrl/v1o0.js
                                  ==========================================
        -->

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            const vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // 入力
                    inputText: {
                        value: `
# 64x64 グライダー
position"""
................................................................
................................................................
....X...........................................................
.....X..........................................................
...XXX..........................................................
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
`,
                    },
                    // 出力
                    outputText: {
                        value: 'Please push "Execute" button.',
                    },
                    // 思考エンジン
                    engine: new Engine(
                        // ユーザーコントロール
                        new UserCtrl()
                    ),
                },
                methods: {
                    // 関数名の末尾の Vu は vue1 のメソッドであることを表す目印
                    /**
                     * po_input 欄のコマンドを入力します
                     */
                    executeVu() {
                        let firstPositionText = vue1.inputText.value;

                        let _log = vue1.engine.execute(firstPositionText);

                        // 動かす
                        vue1.engine.userCtrl.doMove(vue1.engine.position);

                        // 盤面表示
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
        │       │       └── 📂 think
        │       │           ├── 📂 engine
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
        │       │       └── 📂 think
        │       │           ├── 📂 engine
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

# 参考にした記事

📖 [http://math.shinshu-u.ac.jp/~hanaki/lifegame/](http://math.shinshu-u.ac.jp/~hanaki/lifegame/)  
