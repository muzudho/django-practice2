# サンプルを見る

📖 [http://tic.warabenture.com:8000/lifegame/v0.3/board](http://tic.warabenture.com:8000/lifegame/v0.3/board)  

# オススメ動画

👇 以下の６分程度の動画９本を全部見れば１時間でライフゲームの見所の知識が入る  

📖 [THE RECURSIVE COSMOS: Conway's Game of Life ライフゲームの世界](https://www.youtube.com/playlist?list=PLZC7Zqdh0Qb3wOpit5dewit3q2-Mqg9vC)  

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

# Step OAAA1001o1o0ga12o_1o__10o0 Webページにアクセスする

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
// OAAA1001o1o0ga12o_1o0

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
const PC_X_LABEL = "x";

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

/**
 * 駒の有無を反転
 * @param {*} pc
 * @returns
 */
function flip_pc(pc) {
    switch (pc) {
        case PC_EMPTY:
            return PC_X;
        case PC_X:
            return PC_EMPTY;
        default:
            return pc;
    }
}

// |
// | 駒
// +--------
```

# Step OAAA1001o1o0ga12o_2o_1o0 盤の定義 - think/things/board/v1o0.js ファイル

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
        │       │               ├── 📂 board
👉      │       │               │   └── 📄 v1o0.js
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
// OAAA1001o1o0ga12o_2o_1o0

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
     *
     * @param {number} boardsCount - 盤の数
     */
    constructor(boardsCount) {
        // 各盤
        this._boards = Array(boardsCount);

        // 全要素の初期化（.fill()は参照渡しなので使いません）
        for (let i = 0; i < this._boards.length; i++) {
            this._boards[i] = new Board();
        }
    }

    /**
     * 盤配列
     */
    get boards() {
        return this._boards;
    }

    /**
     * ダンプ
     */
    dump(indent) {
        let s = `
${indent}Position
${indent}--------`;

        for (let boardIndex = 0; boardIndex < this._boards.length; boardIndex++) {
            s += `
${indent}${this._boards[boardIndex].dump(indent + "    ")}`;
        }
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
     * @param {number} boardIndex - 盤番号
     */
    doMove(position, boardIndex) {
        this._position = position;
        // 盤[0] について
        // セルの変化
        this._position.boards[boardIndex].convertEachSq((sq, cellValue) => {
            let count = this._position.boards[boardIndex].getLifeCountAround(sq);

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

# Step OAAA1001o1o0ga12o_4o_1o0 エンジン作成 - think/engine/parser/v1o0.js ファイル

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
        │       │           │   └── 📂 parser
👉      │       │           │       └── 📄 v1o0.js
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
// OAAA1001o1o0ga12o_4o_1o0

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

    set onReadLine(action) {
        this._onReadLine = action;
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
            this._onReadLine(`# ${line}\n`);

            this._parseCurr(line);
        }

        this._parseCurr = null;
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
        │       │           │   ├── 📂 parser
        │       │           │   │   └── 📄 v1o0.js
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

        // Example: `play`
        this._parser.onPlay = () => {
            this._userCtrl.doMove(this._position);
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
            const vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // 入力
                    inputText: {
                        value: `# 盤[0]サイズ
board 0 width 64
board 0 height 32
# グライダー
board 0 """
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
board 0
play
board 0
play
board 0
play
board 0
play
board 0
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
                            Original: 📖 <a href="https://conwaylife.com/">https://conwaylife.com/</a>
                        </div>
                    </v-container>
                    <v-container>
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
                    <v-container>
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

                        // 再生する
                        this.playVu();
                    }
                },
                methods: {
                    // 関数名の末尾の Vu は vue1 のメソッドであることを表す目印
                    /**
                     * po_input 欄のコマンドを入力します
                     */
                    enterVu() {
                        // this.inputText.enabled = false;
                        // this.enterButton.enabled = false;

                        this.enteredText = vue1.inputText.value;
                        vue1.inputText.value = "";
                    },
                    /**
                     * 画面更新
                     */
                    updateVu() {
                        if (this.enteredText !== null) {
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
                        } else {
                            // 盤[0]を動かす。それ以外の盤は動かさない
                            let boardIndex = 0;
                            vue1.engine.userCtrl.doMove(vue1.engine.position, boardIndex);
                        }

                        this.repaintVu();
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

# 参考にした記事

## ライフゲーム

📖 [ライフゲーム Akihide Hanaki](http://math.shinshu-u.ac.jp/~hanaki/lifegame/)  
📖 [ライフゲームの数理 里村孔明](http://nalab.mind.meiji.ac.jp/2018/2019-satomura.pdf)  

## Vue.js

📖 [【Vue.js】ページ読み込み完了後・離脱時に処理を実行する](https://into-the-program.com/vue-page-onload-leave/)  
📖 [Vue.js v-show ディレクティブで要素の表示非表示を切り替える](https://anteku.jp/blog/develop/vue-js-v-show-%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%86%E3%82%A3%E3%83%96%E3%81%A7%E8%A6%81%E7%B4%A0%E3%81%AE%E8%A1%A8%E7%A4%BA%E9%9D%9E%E8%A1%A8%E7%A4%BA%E3%82%92%E5%88%87%E3%82%8A%E6%9B%BF/)  

## Vuetify

📖 [Colors](https://vuetifyjs.com/en/styles/colors/#material-colors)  

## Java Script

📖 [How to Stop setInterval() Call in JavaScript](https://www.tutorialrepublic.com/faq/how-to-stop-setinterval-call-in-javascript.php)  
📖 [Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)  

### 正規表現

📖 [正規表現](https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Regular_Expressions)  
