# 目標

〇×ゲーム（Tic tac toe）の通信対戦をしたい。  
その前に、サーバーとクライアント間で通信するメッセージを取り決めておく  

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

## Step Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA16o3o_1o0g1o0 画面作成

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                └── 📂 templates
                    └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                        └── 📂 msg
                            └── 📂 tester
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
                        <h1>Tic Tac Toe Message Test</h1>
                        <v-form method="POST">
                            {% csrf_token %}

                            <!-- `po_` は POST送信するパラメーター名の目印 -->
                            <!-- 入力 -->
                            <v-textarea name="po_input" required v-model="inputText.value" label="Input"></v-textarea>

                            <v-btn block elevation="2" v-on:click="enterVu()"> Execute </v-btn>

                            <!-- 出力 -->
                            <v-textarea name="po_output" required v-model="outputText.value" label="Output"></v-textarea>
                        </v-form>
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            const vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // 入力
                    inputText: {
                        value: `# W.I.P`,
                    },
                    // 出力
                    outputText: {
                        value: 'Please push "Execute" button.',
                    },
                },
                methods: {
                    // 関数名の末尾の Vu は vue1 のメソッドであることを表す目印
                    /**
                     * po_input 欄のコマンドを入力します
                     */
                    enterVu() {
                        // console.log(`[methods enterVu]`);
                    },
                },
            });
        </script>
    </body>
</html>
{# EOF OA16o3o_1o0g1o0 #}
```

## Step OA16o3o_1o0g2o0 ビュー作成 - msg/tester/v1o0/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                │       └── 📂 msg
                │           └── 📂 tester
                │               └── 📄 v1o0.html
                └── 📂 views
                        └── 📂 msg
                            └── 📂 tester
                                └── 📂 v1o0
👉                                  └── 📄 v_render.py
```

```py
# BOF OA16o3o_1o0g2o0

from django.shortcuts import render, redirect


def render_tester(request, room_name, template_path, on_open, on_sent):
    """OA16o3o_1o0g2o0 テスター - 描画

    Parameters
    ----------
    tester_tp : str
        Template path
    """
    if request.method == "POST":
        # 送信後
        on_sent(request)

        # `po_` は POST送信するパラメーター名の目印
        po_room_name = request.POST.get("po_room_name")
        # 自分の番。 "X" か "O"。 機能拡張も想定
        my_turn = request.POST.get("po_my_turn")

        # TODO バリデーションチェックしたい

        return redirect(template_path.format(po_room_name, my_turn))

    # 訪問後
    context = on_open(request)

    turn = request.GET.get("myturn")

    return render(request, template_path.format(room_name, turn), context)

# EOF OA16o3o_1o0g2o0
```

## Step OA16o3o_1o0g3o0 ビュー作成 - msg/tester/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 tic_tac_toe_v2    # アプリケーション
                ├── 📂 templates
                │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
                │       └── 📂 msg
                │           └── 📂 tester
                │               └── 📄 v1o0.html
                └── 📂 views
                        └── 📂 msg
                            └── 📂 tester
                                └── 📂 v1o0
👉                                  └── 📄 __init__.py
```

```py
# BOF OA16o3o_1o0g3o0

import json


class TesterV():
    """OA16o3o_1o0g3o0 テスター ビュー"""

    # 対局申込 - 訪問後
    open_context = {
        # `dj_` は Djangoでレンダーするパラメーター名の目印
        # 入場者データ
        "dj_visitor_value": "X",
        # Python と JavaScript 間で配列データを渡すために JSON 文字列形式にします
        "dj_visitor_select": json.dumps([
            {"text": "X", "value": "X"},
            {"text": "O", "value": "O"},
        ]),
    }

    template_path = "tic_tac_toe_v2/msg/tester/v1o0.html"
    #                             ^two
    #                -----------------------------------
    #                1
    # 1. src1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/msg/tester/v1o0.html
    #                                        -----------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_tester
        #    ---------        -------------
        #    1                2
        # 1. `src1/apps1/tic_tac_toe_v2/views/msg/tester/v1o0/v_render.py`
        #                                                     --------
        # 2. `1.` に含まれる関数

        return render_tester(
            request,
            kw_room_name,
            TesterV.template_path,
            TesterV.on_open,
            TesterV.on_sent)

    @staticmethod
    def on_open(request):
        """訪問後

        Returns
        -------
        context : dict
            context
        """
        return TesterV.open_context

    @staticmethod
    def on_sent(request):
        """送信後"""
        pass

# EOF OA16o3o_1o0g3o0
```

## Step OA16o3o_1o0g4o0 ルート編集 - urls_tic_tac_toe_v2.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 tic_tac_toe_v2    # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 tic_tac_toe_v2    # アプリケーションと同名
        │       │       └── 📂 msg
        │       │           └── 📂 tester
        │       │               └── 📄 v1o0.html
        │       └── 📂 views
        │               └── 📂 msg
        │                   └── 📂 tester
        │                       └── 📂 v1o0
        │                           └── 📄 __init__.py
        └── 📂 project1                      # プロジェクト
👉          └── 📄 urls_tic_tac_toe_v2.py
```

```py
# ...略...


# OA16o3o_1o0g4o0 〇×ゲーム v2 メッセージ テスター
from apps1.tic_tac_toe_v2.views.msg.tester.v1o0 import TesterV as MsgTesterV
#          --------------                  ----        -------    ----------
#          11                              12          2          3
#    ------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


urlpatterns = [
    # ...略...


    # OA16o3o_1o0g4o0 〇×ゲーム v2 メッセージ テスター
    path('tic-tac-toe/v2/msg-test/<str:kw_room_name>/',
         # ------------------------------------------
         # 1
         MsgTesterV.render),
    #    -----------------
    #    2
    # 1. 例えば `http://example.com/tic-tac-toe/v2/msg-test/<部屋名>/` のような URL のパスの部分。
    #                              ---------------------------------
    #    <部屋名> に入った文字列は kw_room_name 変数に渡されます
    # 2. MsgTesterV クラスの render 静的メソッド
]
```

## Step Web画面へアクセス

👇 適宜、部屋名，自分が持つ手番 を付けてアクセスしてほしい  

📖 [http://localhost:8000/tic-tac-toe/v2/msg-test/Elephant/?&myturn=X](http://localhost:8000/tic-tac-toe/v2/msg-test/Elephant/?&myturn=X)  
