# サンプルを見る

📖 [http://tic.warabenture.com:8000/practice/v1/auto_reload/](http://tic.warabenture.com:8000/practice/v1/auto_reload/)  

# 目的

待っていると　対局が付くページがほしい  

いきなり作るのは難しいので、まず 5秒毎に時刻の表示を更新するページ から作る  

# はじめに

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key              | Value                                     |
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
    │   │   │       └── 📂 o1o0
    │   │   │           └── 📄 m_room.py
    │   │   ├── 📂 tic_tac_toe_v1        # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2        # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o1o0
    │   │       │           └── 📂 think
    │   │       │               ├── 📄 concepts.js
    │   │       │               ├── 📄 engine.js
    │   │       │               ├── 📄 judge_ctrl.js
    │   │       │               ├── 📄 position.js
    │   │       │               ├── 📄 things.js
    │   │       │               └── 📄 user_ctrl.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o1o0
    │   │       │           └── 📂 think
    │   │       │               └── 📄 engine_manual.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 o1o0
    │   │       │       └── 📂 think
    │   │       │           └── 📂 engine_manual
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
    ├── 📂 src2_local                   # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# Step OA21o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step OA21o1o0g2o0 機能強化 - clock.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 static
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 o1o0
👉                          └── 📄 clock.js
```

```js
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

# Step OA21o1o0g3o0 機能強化 - auto_reload.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 static
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 o1o0
                            ├── 📄 clock.js
👉                          └── 📄 auto_reload.js
```

```js
/**
 * @param {number} intervalMilliseconds
 */
function startReloadingAutomatically(intervalMilliseconds) {
    setInterval(() => {
        location.reload();
    }, intervalMilliseconds);
}
```

# Step OA21o1o0g4o0 画面編集 - v0o0o1/auto_reload.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 o1o0
                │           ├── 📄 clock.js
                │           └── 📄 auto_reload.js
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 o1o0
👉                          └── 📄 auto_reload.html
```

```html
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
        <script src="{% static 'practice_v1/o1o0/clock.js' %}"></script>
        <script src="{% static 'practice_v1/o1o0/auto_reload.js' %}"></script>
        <!--            =======================================
            `src1/apps1/practice_v1/static/practice_v1/o1o0/auto_reload.js`
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

# Step OA21o1o0g5o0 ビュー作成 - reloader フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 o1o0
                │           ├── 📄 clock.js
                │           └── 📄 auto_reload.js
                ├── 📂 templates
                │   └── 📂 practice_v1          # アプリケーションと同名
                │       └── 📂 o1o0
                │           └── 📄 auto_reload.html
                └── 📂 views
                    └── 📂 o1o0
                        └── 📂 auto_reload
👉                          └── 📄 __init__.py
```

```py
class AutoReloadV():
    """自動再読込ビュー"""

    # 自動再読込ページ
    _path_of_auto_reload_page = "practice_v1/o1o0/auto_reload.html"
    #                            ---------------------------------
    #                            1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/o1o0/auto_reload.html` を取得
    #                                      ---------------------------------

    @staticmethod
    def render_auto_reload(request):
        """描画 - 自動再読込"""

        # 以下のファイルはあとで作ります
        from .v_auto_reload import render_auto_reload
        #    --------------        ------------------
        #    1                     2
        # 1. `src1/apps1/practice_v1/views/o1o0/auto_reload/v_auto_reload.py`
        #                                                   -------------
        # 2. `1.` に含まれる関数

        return render_auto_reload(request, AutoReloadV._path_of_auto_reload_page)
```

# Step OA21o1o0g6o0 ビュー作成 - v_auto_reload ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 o1o0
                │           ├── 📄 clock.js
                │           └── 📄 auto_reload.js
                ├── 📂 templates
                │   └── 📂 practice_v1          # アプリケーションと同名
                │       └── 📂 o1o0
                │           └── 📄 auto_reload.html
                └── 📂 views
                    └── 📂 o1o0
                        └── 📂 auto_reload
                            ├──📄 __init__.py
👉                          └──📄 v_auto_reload.py
```

```py
from django.shortcuts import render


def render_auto_reload(request, path_of_reloader_page):
    """描画 - 自動再読込"""

    context = {
    }

    return render(request, path_of_reloader_page, context)
```

# Step OA21o1o0g7o0 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           ├── 📄 clock.js
        │       │           └── 📄 auto_reload.js
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📄 auto_reload.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 auto_reload
        │                   ├──📄 __init__.py
        │                   └──📄 v_auto_reload.py
        └── 📂 project1                      # プロジェクト
👉          └── 📄 urls_practice.py
```

```py
# ...略...


# 自動リロード ビュー
from apps1.practice_v1.views.o1o0.auto_reload import AutoReloadV
#          -----------            -----------        -----------
#          11                     12                 2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [
    # ...略...


    # 自動再読込
    path('practice/v1/auto_reload/', AutoReloadV.render_auto_reload,
         # -----------------------   ------------------------------
         # 1                         2
         name='practice_v1_auto_reload'),
    #          -----------------------
    #          3
    #
    # 1. 例えば `http://example.com/practice/v1/auto_reload/` のような URL のパスの部分
    #                              ------------------------
    # 2. AutoReloadV クラスの render_auto_reload 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_auto_reload' %} のような形でURLを取得するのに使える
]
```

# Step OA21o1o0g8o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/auto_reload/](http://localhost:8000/practice/v1/auto_reload/)  

# Step OA21o1o0g9o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

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
        │       │       └── 📂 o1o0
        │       │           ├── 📄 clock.js
        │       │           └── 📄 auto_reload.js
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📄 auto_reload.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 auto_reload
        │                   ├──📄 __init__.py
        │                   └──📄 v_auto_reload.py
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
