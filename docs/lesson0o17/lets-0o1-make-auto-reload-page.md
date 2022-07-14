# 目的

待っていると　対局が付くページがほしい  

いきなり作るのは難しいので、まず 5秒毎に時刻の表示を更新するページ から作る  

# はじめに

この記事は Lesson0 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    ├── 📂 host_local1                   # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    ├── 📂 host1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized    # アプリケーション
    │   │   ├── 📂 portal                # アプリケーション
    │   │   ├── 📂 practice              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 v0o0o1
    │   │   │           └── 📄 m_room.py
    │   │   ├── 📂 tic_tac_toe_v1        # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2        # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o0o1
    │   │       │           └── 📂 think
    │   │       │               ├── 📄 concepts.js
    │   │       │               ├── 📄 engine.js
    │   │       │               ├── 📄 judge_ctrl.js
    │   │       │               ├── 📄 position.js
    │   │       │               ├── 📄 things.js
    │   │       │               └── 📄 user_ctrl.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o0o1
    │   │       │           └── 📂 think
    │   │       │               └── 📄 engine_manual.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 v2o0o1
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
    └── 📄 .gitignore
```

# Step 1. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. 機能強化 - clock.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice                  # アプリケーション
                └── 📂 static
                    └── 📂 practice          # アプリケーションと同名
                        └── 📂 v0o0o1
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

# Step 3. 機能強化 - reloader.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice                  # アプリケーション
                └── 📂 static
                    └── 📂 practice          # アプリケーションと同名
                        └── 📂 v0o0o1
                            ├── 📄 clock.js
👉                          └── 📄 reloader.js
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

# Step 4. 画面編集 - v0o0o1/reloader.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice
                │       └── 📂 v0o0o1
                │           ├── 📄 clock.js
                │           └── 📄 reloader.js
                └── 📂 templates
                    └── 📂 practice          # アプリケーションと同名
                        └── 📂 v0o0o1
👉                          └── 📄 reloader.html
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

        <script src="{% static 'practice/v0o0o1/clock.js' %}"></script>
        <script src="{% static 'practice/v0o0o1/reloader.js' %}"></script>
        <!--                    ===========================
            `host1/apps1/practice/static/practice/v0o0o1/reloader.js`
                                         ===========================
        -->

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
                },
            });
        </script>
    </body>
</html>
```

# Step 5. ビュー モジュール作成 - reloader フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice
                │       └── 📂 v0o0o1
                │           ├── 📄 clock.js
                │           └── 📄 reloader.js
                ├── 📂 templates
                │   └── 📂 practice          # アプリケーションと同名
                │       └── 📂 v0o0o1
                │           └── 📄 reloader.html
                └── 📂 views
                    └── 📂 v0o0o1
                        └── 📂 reloader
👉                          └── 📄 __init__.py
```

```py
class ReloaderV():
    """自動再読込ビュー"""

    # 自動再読込ページ
    _path_of_reloader_page = "practice/v0o0o1/reloader.html"
    #                         -----------------------------
    #                         1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/reloader.html` を取得
    #                                    -----------------------------

    @staticmethod
    def render_reloader(request):
        """描画 - 自動再読込"""

        # 以下のファイルはあとで作ります
        from .v_reloader import render_reloader
        #    -----------        ---------------
        #    1                  2
        # 1. `host1/apps1/practice/views/v0o0o1/reloader/v_reloader.py`
        #                                                ----------
        # 2. `1.` に含まれる関数

        return render_reloader(request, ReloaderV._path_of_reloader_page)
```

# Step 6. ビュー モジュール作成 - v_reloader ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice
                │       └── 📂 v0o0o1
                │           ├── 📄 clock.js
                │           └── 📄 reloader.js
                ├── 📂 templates
                │   └── 📂 practice          # アプリケーションと同名
                │       └── 📂 v0o0o1
                │           └── 📄 reloader.html
                └── 📂 views
                    └── 📂 v0o0o1
                        └── 📂 reloader
                            ├──📄 __init__.py
👉                          └──📄 v_reloader.py
```

```py
from django.shortcuts import render


def render_reloader(request, path_of_reloader_page):
    """描画 - 自動再読込"""

    context = {
    }

    return render(request, path_of_reloader_page, context)
```

# Step 7. ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice                  # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 practice
        │       │       └── 📂 v0o0o1
        │       │           ├── 📄 clock.js
        │       │           └── 📄 reloader.js
        │       ├── 📂 templates
        │       │   └── 📂 practice
        │       │       └── 📂 v0o0o1
        │       │           └── 📄 reloader.html
        │       └── 📂 views
        │           └── 📂 v0o0o1
        │               └── 📂 reloader
        │                   ├──📄 __init__.py
        │                   └──📄 v_reloader.py
        └── 📂 project1                      # プロジェクト
👉          └── 📄 urls_practice.py
```

```py
# ...略...


from apps1.practice.views.v0o0o1.reloader import ReloaderV
#    ----- -------- ---------------------        ---------
#    1     2        3                            4
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


urlpatterns = [
    # ...略...


    # 自動再読込
    path('practice/reloader/', ReloaderV.render_reloader,
         # -----------------   -------------------------
         # 1                   2
         name='practice_reloader'),
    #          -----------------
    #          3
    #
    # 1. 例えば `http://example.com/practice/reloader/` のような URL のパスの部分
    #                              ------------------
    # 2. ReloaderV クラスの render_reloader メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_reloader' %} のような形でURLを取得するのに使える
]
```

# Step 8. Web画面へアクセス

📖 [http://localhost:8000/practice/reloader/](http://localhost:8000/practice/reloader/)  

# Step 9. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice                      # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 practice
        │       │       └── 📂 v0o0o1
        │       │           ├── 📄 clock.js
        │       │           └── 📄 reloader.js
        │       ├── 📂 templates
        │       │   └── 📂 practice
        │       │       └── 📂 v0o0o1
        │       │           └── 📄 reloader.html
        │       └── 📂 views
        │           └── 📂 v0o0o1
        │               └── 📂 reloader
        │                   ├──📄 __init__.py
        │                   └──📄 v_reloader.py
        └── 📂 project1                          # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/reloader/,自動再読込
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoで自動リダイレクトするページを作ろう！](https://qiita.com/muzudho1/items/aea9be36422763f082e9)  
