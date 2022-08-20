# 目標

〇×ゲーム（Tic tac toe）の通信対戦をしたい  

いきなり作るのは難しいので その前に、クライアントからサーバーへ送るメッセージを取り決めておく  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is          | This is                                   |
| ---------------- | ----------------------------------------- |
| OS               | Windows10                                 |
| Container        | Docker                                    |
| Database         | Postgresql, (Redis)                       |
| Program Language | Python 3                                  |
| Web framework    | Django                                    |
| Auth             | allauth                                   |
| Frontend         | Vuetify                                   |
| Data format      | JSON                                      |
| Others           | (Socket), Web socket                      |
| Editor           | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1                            # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   ├── 📂 tic_tac_toe_v1           # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2           # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 think
    │   │       │           ├── 📂 concepts
    │   │       │           │   └── 📄 v1o0.js
    │   │       │           ├── 📂 engine
    │   │       │           │   └── 📄 v1o0.js
    │   │       │           ├── 📂 judge_ctrl
    │   │       │           │   └── 📄 v1o0.js
    │   │       │           ├── 📂 position
    │   │       │           │   └── 📄 v1o0.js
    │   │       │           ├── 📂 things
    │   │       │           │   └── 📄 v1o0.js
    │   │       │           └── 📂 user_ctrl
    │   │       │               └── 📄 v1o0.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 think
    │   │       │           └── 📂 engine_manual
    │   │       │               └── 📄 v1o0.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 think
    │   │       │       └── 📂 engine_manual
    │   │       │           └── 📂 v1o0
    │   │       │               ├── 📄 __init__.py
    │   │       │               └── 📄 v_render.py
    │   │       ├── 📄 __init__.py
    │   │       ├── 📄 admin.py
    │   │       ├── 📄 apps.py
    │   │       └── 📄 tests.py
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_accounts.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls_tic_tac_toe_v1.py
    │   │   ├── 📄 urls_tic_tac_toe_v2.py
    │   │   ├── 📄 urls.py
    │   │   ├── 📄 ws_urls_tic_tac_toe_v1.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2                  # プロジェクト
    │   ├── 🐳 docker-compose-project2.yml
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    ├── 📂 src2_local                      # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# 手順

## Step. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA16o3o_1o0g_1o0 クライアントからサーバーへ送るメッセージ実装 - msg/c2s_json_gen/v1o0.js ファイル

Moved from OA16o3o0g2o0  

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                └── 📂 static
                    └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                        └── 📂 msg
                            └── 📂 c2s_json_gen
👉                              └── 📄 v1o0.js
```

```js
// BOF OA16o3o_1o0g_1o0

/**
 * 送信JSONジェネレーター
 *
 * * クライアントからサーバーへ送る
 */
class C2sJsonGen {
    /**
     * どちらかのプレイヤーが駒を置いたとき
     * @param {int} sq - 升番号
     * @param {string} pieceMoved - 駒を置いたプレイヤー。 X か O
     * @returns メッセージ
     */
    createDoMove(sq, pieceMoved) {
        // `c2s_` は クライアントからサーバーへ送る変数の目印
        console.log(`[C2sJsonGen createDoMove] sq=${sq} pieceMoved=${pieceMoved}`);
        return {
            c2s_event: "C2S_Moved",
            c2s_sq: sq,
            c2s_pieceMoved: pieceMoved,
        };
    }

    /**
     * 引き分けたとき、とりあえず両方のプレイヤーが、サーバーへ対局終了メッセージを送ります
     * @returns メッセージ
     */
    createDraw() {
        // `c2s_` は クライアントからサーバーへ送る変数の目印
        return {
            c2s_event: "C2S_End",
            c2s_winner: PC_EMPTY_LABEL,
        };
    }

    /**
     * 対局を開始したとき
     * @returns メッセージ
     */
    createStart() {
        // `c2s_` は クライアントからサーバーへ送る変数の目印
        return {
            c2s_event: "C2S_Start",
        };
    }

    /**
     * 勝った方のプレイヤーが、サーバーに対局終了メッセージを送ります
     * @param {*} winner - 勝者。 "X" か "O"
     * @returns メッセージ
     */
    createWon(winner) {
        // `c2s_` は クライアントからサーバーへ送る変数の目印
        return {
            c2s_event: "C2S_End",
            c2s_winner: winner,
        };
    }
}

// EOF OA16o3o_1o0g_1o0
```

## Step OA16o3o_1o0g1o0 画面作成 - msg/c2s_json_gen/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       └── 📂 msg
                │           └── 📂 c2s_json_gen
                │               └── 📄 v1o0.js
                └── 📂 templates
                    └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                        └── 📂 msg
                            └── 📂 c2s_json_gen
👉                              └── 📄 v1o0.html
```

```html
{# BOF OA16o3o_1o0g1o0 #}
<!-- -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<html>
    <head>
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui" />
        <title>Tic Tac Toe</title>
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
                        <h1>Tic Tac Toe - C2S Json Generator</h1>
                        <v-form method="POST">
                            {% csrf_token %}

                            <!-- `po_` は POST送信するパラメーター名の目印 -->

                            <!-- リスト -->
                            <v-select v-model="c2sMessageTypeListbox.value" :items="c2sMessageTypeItems" label="クライアントからサーバーへ送るメッセージの種類一覧"></v-select>
                            <v-select v-model="sqListbox.value" :items="sqItems" label="マス番号一覧"></v-select>
                            <v-select v-model="playerListbox.value" :items="playerItems" label="プレイヤー一覧"></v-select>

                            <!-- ボタン -->
                            <v-btn block elevation="2" v-on:click="postVu()"> Generate JSON </v-btn>

                            <!-- 出力 -->
                            <v-textarea name="po_output" required v-model="outputTextbox.value" label="Output" rows="10"></v-textarea>
                        </v-form>
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="{% static 'tic_tac_toe_v2/think/things/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/think/concepts/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/think/position/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/think/user_ctrl/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/think/judge_ctrl/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/think/engine/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/msg/s2c_messages/v1o0.js' %}"></script>
        <script src="{% static 'tic_tac_toe_v2/msg/c2s_json_gen/v1o0.js' %}"></script>
        <!--            ===============================================
                        1
        1. src1/apps1/tic_tac_toe_v2/static/tic_tac_toe_v2/msg/c2s_json_gen/v1o0.js
                                     ==============================================
        -->

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            // クライアントからサーバーへ送るメッセージを生成できる
            const c2sJsonGen1 = new C2sJsonGen();

            const vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // 出力
                    outputTextbox: {
                        value: 'Please push "Execute" button.',
                    },
                    // メッセージの種類リストボックス
                    c2sMessageTypeListbox: {
                        value: "DoMove",
                    },
                    // マス番号リストボックス
                    sqListbox: {
                        value: "",
                    },
                    // プレイヤーリストボックス
                    playerListbox: {
                        value: "",
                    },
                    // メッセージの種類一覧
                    c2sMessageTypeItems: ["DoMove", "Draw", "Start", "Won"],
                    // マス番号の一覧
                    sqItems: ["", 0, 1, 2, 3, 4, 5, 6, 7, 8],
                    // プレイヤーの一覧
                    playerItems: ["", "X", "O"],
                },
                methods: {
                    // 関数名の末尾の Vu は vue1 のメソッドであることを表す目印
                    /**
                     * po_input 欄のコマンドを入力します
                     */
                    postVu() {
                        // console.log(`[methods postVu]`);
                        let doc = null;
                        switch (this.c2sMessageTypeListbox.value) {
                            case "DoMove":
                                {
                                    const sq = this.sqListbox.value;
                                    const myTurn = this.playerListbox.value;
                                    doc = c2sJsonGen1.createDoMove(sq, myTurn);
                                }
                                break;

                            case "Draw":
                                doc = c2sJsonGen1.createDraw();
                                break;

                            case "Start":
                                doc = c2sJsonGen1.createStart();
                                break;

                            case "Won":
                                const winner = this.playerListbox.value;
                                doc = c2sJsonGen1.createWon(winner);
                                break;

                            default:
                                doc = {};
                                break;
                        }

                        this.outputTextbox.value = JSON.stringify(doc, null, "    ");
                    },
                },
            });
        </script>
    </body>
</html>
{# EOF OA16o3o_1o0g1o0 #}
```

## Step OA16o3o_1o0g2o0 ビュー作成 - msg/c2s_json_gen/v1o0/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       └── 📂 msg
                │           └── 📂 c2s_json_gen
                │               └── 📄 v1o0.js
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                │       └── 📂 msg
                │           └── 📂 c2s_json_gen
                │               └── 📄 v1o0.html
                └── 📂 views
                        └── 📂 msg
                            └── 📂 c2s_json_gen
                                └── 📂 v1o0
👉                                  └── 📄 v_render.py
```

```py
# BOF OA16o3o_1o0g2o0

from django.shortcuts import render


def render_main(request, template_path):
    """OA16o3o_1o0g2o0 C2S JSON ジェネレーター - 描画

    Parameters
    ----------
    template_path : str
        Template path
    """

    context = {}

    return render(request, template_path, context)

# EOF OA16o3o_1o0g2o0
```

## Step OA16o3o_1o0g3o0 ビュー作成 - msg/c2s_json_gen/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 static
                │   └── 📂 tic_tac_toe_v2
                │       └── 📂 msg
                │           └── 📂 c2s_json_gen
                │               └── 📄 v1o0.js
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                │       └── 📂 msg
                │           └── 📂 c2s_json_gen
                │               └── 📄 v1o0.html
                └── 📂 views
                        └── 📂 msg
                            └── 📂 c2s_json_gen
                                └── 📂 v1o0
👉                                  └── 📄 __init__.py
```

```py
# BOF OA16o3o_1o0g3o0

class TesterV():
    """OA16o3o_1o0g3o0 テスター ビュー"""

    template_path = "tic_tac_toe_v2/msg/c2s_json_gen/v1o0.html"
    #                             ^two
    #                -----------------------------------------
    #                1
    # 1. src1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/msg/c2s_json_gen/v1o0.html
    #                                        -----------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_main
        #    ---------        -----------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_v2/views/msg/c2s_json_gen/v1o0/v_render.py`
        #                                                           --------
        # 2. `1.` に含まれる関数

        return render_main(
            request,
            TesterV.template_path)

# EOF OA16o3o_1o0g3o0
```

## Step OA16o3o_1o0g4o0 ルート編集 - urls_tic_tac_toe_v2.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v2    # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 tic_tac_toe_v2
        │       │       └── 📂 msg
        │       │           └── 📂 c2s_json_gen
        │       │               └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
        │       │       └── 📂 msg
        │       │           └── 📂 c2s_json_gen
        │       │               └── 📄 v1o0.html
        │       └── 📂 views
        │               └── 📂 msg
        │                   └── 📂 c2s_json_gen
        │                       └── 📂 v1o0
        │                           └── 📄 __init__.py
        └── 📂 project1                      # プロジェクト
👉          └── 📄 urls_tic_tac_toe_v2.py
```

```py
# ...略...


# OA16o3o_1o0g4o0 〇×ゲーム v2 C2S JSON ジェネレーター
from apps1.tic_tac_toe_v2.views.msg.c2s_json_gen.v1o0 import TesterV as MsgTesterV
#          --------------                        ----        -------    ----------
#          11                                    12          2          3
#    ------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [
    # ...略...


    # OA16o3o_1o0g4o0 〇×ゲーム v2 C2S JSON ジェネレーター
    path('tic-tac-toe/v2/c2s-json-gen/',
         # ---------------------------
         # 1
         MsgTesterV.render),
    #    -----------------
    #    2
    # 1. 例えば `http://example.com/tic-tac-toe/v2/c2s-json-gen/` のような URL のパスの部分
    #                              -----------------------------
    # 2. MsgTesterV クラスの render 静的メソッド
]
```

## Step. Web画面へアクセス

📖 [http://localhost:8000/tic-tac-toe/v2/c2s-json-gen/](http://localhost:8000/tic-tac-toe/v2/c2s-json-gen/)  

# 参考にした記事

## Vuetify

📖 [Set initial vuetify v-select value](https://stackoverflow.com/questions/51392719/set-initial-vuetify-v-select-value)  
