# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/v1/auto_reload/)  

# 目標

待っていると　対局が付くページがほしい  

いきなり作るのは難しいので、まず 5秒毎に時刻の表示を更新するページ から作る  

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
    ├── 📂 src1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 room
    │   │   │           └── 📄 v1o0.py
    │   │   ├── 📂 tic_tac_toe_v1        # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2        # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       ├── 📂 gui
    │   │       │       └── 📂 think
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       ├── 📂 gui
    │   │       │       └── 📂 think
    │   │       ├── 📂 views
    │   │       │   ├── 📂 gui
    │   │       │   └── 📂 think
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
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📄 urls.py
    ├── 📂 src2_local                   # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# 手順

## Step OA21o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA21o1o0g2o0 機能強化 - clock/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 static
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 clock
👉                          └── 📄 v1o0.js
```

```js
// OA21o1o0g2o0

/**
 *
 * @returns 現在時刻の文字列
 */
function getTimeStamp() {
    const weekStr = ["日", "月", "火", "水", "木", "金", "土"];

    // 現在時刻
    const now = new Date();

    const year = now.getFullYear(); // 年
    const month = now.getMonth() + 1; // 月
    const day = now.getDate(); // 日
    const weekday = weekStr[now.getDay()]; // 曜日
    const hour = now.getHours(); // 時
    const minite = now.getMinutes(); // 分
    const second = now.getSeconds(); // 秒
    const millisecond = now.getMilliseconds(); // ミリ秒

    const text = `${year}年 ${month}月 ${day}日 （${weekday}） ${hour}時 ${minite}分 ${second}秒 ${millisecond}ミリ秒`;

    console.log(`time stamp=[${text}]`);

    return text;
}
```

## Step OA21o1o0g3o0 機能強化 - auto_reload/v1o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 static
                    └── 📂 practice_v1          # アプリケーションと同名
                        ├── 📂 auto_reload
👉                      │   └── 📄 v1o0.js
                        └── 📂 clock
                            └── 📄 v1o0.js
```

```js
// OA21o1o0g3o0

/**
 * @param {number} intervalMilliseconds
 */
function startReloadingAutomatically(intervalMilliseconds) {
    setInterval(() => {
        location.reload();
    }, intervalMilliseconds);
}
```

## Step OA21o1o0g4o0 画面編集 - auto_reload/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       ├── 📂 auto_reload
                │       │   └── 📄 v1o0.js
                │       └── 📂 clock
                │           └── 📄 v1o0.js
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 auto_reload
👉                          └── 📄 v1o0.html
```

```html
{# OA21o1o0g4o0 #}
<!-- -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<!-- See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92 -->
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>対局待合室</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <!-- v-app-bar に app プロパティを指定しないなら、背景画像を付けてほしい -->
                <v-app-bar app dense elevation="4">
                    <v-app-bar-nav-icon></v-app-bar-nav-icon>
                    <v-toolbar-title>ゲーム対局サーバー</v-toolbar-title>
                </v-app-bar>
                <v-main>
                    <v-container>
                        <h3>対局待合室</h3>
                        <!-- ここに時計 -->
                        {% comment %} Vue で二重波括弧（braces）は変数の展開に使っていることから、 Python のテンプレートに二重波括弧を変数の展開に使わないよう verbatim で指示します。 {% endcomment %}
                        <!-- -->
                        {% verbatim %} {{vu_timeStamp}} {% endverbatim %}
                    </v-container>
                </v-main>
            </v-app>
        </div>

        {% block script_src %}
        <script src="{% static 'practice_v1/clock/v1o0.js' %}"></script>
        <script src="{% static 'practice_v1/auto_reload/v1o0.js' %}"></script>
        <!--            =======================================
            `src1/apps1/practice_v1/static/practice_v1/auto_reload/v1o0.js`
                                    ======================================
        -->
        {% endblock script_src %}

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            let vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                // page loaded
                mounted: () => {
                    // ここで Vue の準備完了後の処理ができる。
                    // ただし、まだ this は初期化されてない

                    // 5秒毎にリロード
                    startReloadingAutomatically(5000);
                },
                data: {
                    // "vu_" は 「vue1.dataのメンバー」 の目印
                    vu_timeStamp: getTimeStamp(),
                    {% block data_trailing %}
                    {% endblock data_trailing %}
                },
                methods: {
                    {% block methods_trailing %}
                    {% endblock methods_trailing %}
                },
            });
        </script>
    </body>
</html>
```

## Step OA21o1o0g5o0 ビュー作成 - auto_reload/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       ├── 📂 auto_reload
                │       │   └── 📄 v1o0.js
                │       └── 📂 clock
                │           └── 📄 v1o0.js
                ├── 📂 templates
                │   └── 📂 practice_v1          # アプリケーションと同名
                │       └── 📂 auto_reload
                │           └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 auto_reload
                        └── 📂 v1o0
👉                          └── 📄 __init__.py
```

```py
class AutoReloadV():
    """OA21o1o0g5o0 自動再読込ビュー"""

    # 自動再読込ページ
    _path_of_auto_reload_page = "practice_v1/auto_reload/v1o0.html"
    #                            ---------------------------------
    #                            1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/auto_reload/v1o0.html` を取得
    #                                      ---------------------------------

    @staticmethod
    def render_auto_reload(request):
        """描画 - 自動再読込"""

        # 以下のファイルはあとで作ります
        from .v_auto_reload import render_auto_reload
        #    --------------        ------------------
        #    1                     2
        # 1. `src1/apps1/practice_v1/views/auto_reload/v1o0/v_auto_reload.py`
        #                                                   -------------
        # 2. `1.` に含まれる関数

        return render_auto_reload(request, AutoReloadV._path_of_auto_reload_page)
```

## Step OA21o1o0g6o0 ビュー作成 - auto_reload/v1o0/v_auto_reload.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       ├── 📂 auto_reload
                │       │   └── 📄 v1o0.js
                │       └── 📂 clock
                │           └── 📄 v1o0.js
                ├── 📂 templates
                │   └── 📂 practice_v1          # アプリケーションと同名
                │       └── 📂 auto_reload
                │           └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 auto_reload
                        └── 📂 v1o0
                            ├── 📄 __init__.py
👉                          └── 📄 v_auto_reload.py
```

```py
# BOF OA21o1o0g6o0

from django.shortcuts import render


def render_auto_reload(request, auto_reload_tp):
    """OA21o1o0g6o0 描画 - 自動再読込

    Parameters
    ----------
    auto_reload_tp : str
        Template path
    """

    context = {}
    return render(request, auto_reload_tp, context)

# EOF OA21o1o0g6o0
```

## ~~Step OA21o1o0g7o0~~

Merged to OA21o1o0g7o1o0  

## Step OA21o1o0g7o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_v1                  # アプリケーション
    │           ├── 📂 static
    │           │   └── 📂 practice_v1
    │           │       ├── 📂 auto_reload
    │           │       │   └── 📄 v1o0.js
    │           │       └── 📂 clock
    │           │           └── 📄 v1o0.js
    │           ├── 📂 templates
    │           │   └── 📂 practice_v1
    │           │       └── 📂 auto_reload
    │           │           └── 📄 v1o0.html
    │           └── 📂 views
    │               └── 📂 auto_reload
    │                   └── 📂 v1o0
    │                       ├── 📄 __init__.py
    │                       └── 📄 v_auto_reload.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_autogen.py,practice/v1/auto_reload/,practice_v1_auto_reload,"OA21o1o0g7o1o0 自動リロードページ",apps1.practice_v1.views.auto_reload.v1o0,AutoReloadV,,render_auto_reload
```

## Step OA21o1o0g7o2o0 ルート編集 - コマンド打鍵

👇 以下のコマンドを打鍵してほしい  

```shell
cd ../src1_meta
python -m scripts.auto_generators.urls
cd ../src1
docker-compose restart
```

* ディレクトリーは、がんばって移動してほしい
* スクリプトについて See also: O3o2o_1o0g2o0
* 設定ファイルを変更したら、サーバーの再起動が必要

## Step OA21o1o0g8o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/auto_reload/](http://localhost:8000/practice/v1/auto_reload/)  

## Step OA21o1o0g9o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 practice_v1
        │       │       ├── 📂 auto_reload
        │       │       │   └── 📄 v1o0.js
        │       │       └── 📂 clock
        │       │           └── 📄 v1o0.js
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 auto_reload
        │       │           └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 auto_reload
        │               └── 📂 v1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_auto_reload.py
        └── 📂 project1                          # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/auto_reload/,自動再読込
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoで自動リダイレクトするページを作ろう！](https://qiita.com/muzudho1/items/aea9be36422763f082e9)  
