# サンプルを見る

📖 [http://tic.warabenture.com:8000/practice/v1/my/](http://tic.warabenture.com:8000/practice/v1/my/)  

# 目的

ゲーム対局サーバーと、ユーザーの間には サインアップを経て承諾した内容があるはずだ。  
ユーザーは時に その契約内容を変えたいし、 また 退会したい  

# 手段

**マイページ** なるページを用意し、そこから 契約内容の変更や 退会が行えると 話しが早いだろう  

免責: この記事では 工事中のページを用意するだけで、契約内容の変更などの機能までは持たない  

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

参考にした元記事は 📖[DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92) だ。  
わたしの記事は単に **やってみた** ぐらいの位置づけだ  

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 host_local1                      # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    ├── 📂 host1                            # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 o1o0
    │   │   │           └── 📄 m_room.py
    │   │   ├── 📂 tic_tac_toe_v1           # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2           # アプリケーション
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
    └── 📄 .gitignore
```

# Step O1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step O2o0 画面作成 - my.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 o1o0
👉                          └── 📄 my.html
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
        <title>マイ ページ</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container>
                        <v-row class="my-2">
                            <h3>マイ ページ</h3>
                        </v-row>
                        <v-row class="my-2">
                            <v-btn :href="createLobbyPath()">ロビー（待合室）へ移動する</v-btn>
                        </v-row>
                        <v-row class="my-2">
                            <v-btn :href="createTicTacToePath()">〇×ゲーム</v-btn>
                        </v-row>
                        {% if user.is_authenticated %}
                        <v-row class="my-2">
                            <v-btn :href="createLogoutPath()">ログアウト</v-btn>
                        </v-row>
                        {% else %}
                        <v-row class="my-2">
                            <v-btn :href="createLoginPath()">ログイン／会員登録</v-btn>
                        </v-row>
                        {% endif %}
                    </v-container>
                </v-main>
            </v-app>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            let vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // "vu_" は 「vue1.dataのメンバー」 の目印
                    vu_lobbyPath: "{{ dj_lobbyPath }}",
                    vu_ticTacToePath: "{{ dj_ticTacToePath }}",
                    vu_loginPath: "{{ dj_loginPath }}",
                    vu_logoutPath: "{{ dj_logoutPath }}",
                },
                methods: {
                    createLobbyPath() {
                        let url = `${location.protocol}//${location.host}${this.vu_lobbyPath}`;
                        //          --------------------  --------------]--------------------
                        //          1                     2              3
                        // 1. protocol
                        // 2. host
                        // 3. path
                        console.log(`game url=[${url}]`);
                        return url;
                    },
                    createTicTacToePath() {
                        let url = `${location.protocol}//${location.host}${this.vu_ticTacToePath}`;
                        console.log(`game url=[${url}]`);
                        return url;
                    },
                    createLoginPath() {
                        let url = `${location.protocol}//${location.host}${this.vu_loginPath}`;
                        console.log(`login url=[${url}]`);
                        return url;
                    },
                    createLogoutPath() {
                        let url = `${location.protocol}//${location.host}${this.vu_logoutPath}`;
                        console.log(`logout url=[${url}]`);
                        return url;
                    },
                },
            });
        </script>
    </body>
</html>
```

# Step O3o0 ビュー モジュール編集 - my フォルダー

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1          # アプリケーションと同名
                │       └── 📂 o1o0
                │           └── 📄 my_page.html
                └── 📂 views
                    └── 📂 o1o0
                        └── 📂 my
👉                          └── 📄 __init__.py
```

```py
class MyV():
    """マイ ページ ビュー"""

    # マイ ページ
    _path_of_my_page = "practice_v1/o1o0/my.html"
    #                   ------------------------
    #                   1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o1o0/my.html` を取得
    #                                       ------------------------

    @staticmethod
    def render_my(request):
        """描画 - マイ ページ"""

        # 以下のファイルはあとで作ります
        from .v_my import render_my
        #    -----        ---------
        #    1            2
        # 1. `host1/apps1/practice_v1/views/o1o0/my/v_my.py`
        #                                           ----
        # 2. `1.` に含まれる関数

        return render_my(request, MyV._path_of_my_page)
```

# Step O4o0 ビュー モジュール作成 - v_my ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o1o0
                │           └── 📄 my_page.html
                └── 📂 views
                    └── 📂 o1o0
                        └── 📂 my
                            ├── 📄 __init__.py
👉                          └── 📄 v_my.py
```

```py
from django.http import HttpResponse
from django.template import loader


def render_my(request, path_of_my_page):
    """描画 - マイ ページ"""
    template = loader.get_template(path_of_my_page)

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        'dj_user': request.user,

        'dj_lobbyPath': '/practice/v1/lobby/',
        #                -------------------
        #                1
        # 1. http://example.com/practice/v1/lobby/
        #                      -------------------

        'dj_ticTacToePath': '/tic-tac-toe/v2/match-application/',
        #                    ----------------------------------
        #                    1
        # 1. http://example.com/tic-tac-toe/v2/match-application/
        #                      ----------------------------------

        'dj_loginPath': '/accounts/v1/login/',
        #                -------------------
        #                1
        # 1. http://example.com/accounts/v1/login/
        #                      -------------------

        'dj_logoutPath': '/accounts/v1/logout/',
        #                 --------------------
        #                 1
        # 1. http://example.com/accounts/v1/logout/
        #                      --------------------
    }

    return HttpResponse(template.render(context, request))
```

# Step O5o0 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📄 my_page.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 my
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_my.py
        └── 📂 project1                          # プロジェクト
👉          └── 📄 urls_practice.py
```

```py
# ...略...


# マイページ ビュー
from apps1.practice_v1.views.o1o0.my import MyV
#          -----------            --        ---
#          11                     12        2
#    -------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [
    # ...略...


    # マイ ページ
    path('practice/v1/my/', MyV.render_my, name='practice_v1_my'),
    #     ---------------   -------------        --------------
    #     1                 2                    3
    #
    # 1. 例えば `http://example.com/practice/v1/my/` のような URL のパスの部分
    #                              ---------------
    # 2. MyV クラスの render_my メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_my' %} のような形でURLを取得するのに使える
]
```

# Step O6o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/my/](http://localhost:8000/practice/v1/my/)  

# Step O7o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
        │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📄 my_page.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 my
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_my.py
        └── 📂 project1                          # プロジェクト
👉          └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/my/,マイ ページ
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでロビー（待合室）を作ろう！](https://qiita.com/muzudho1/items/57677b07854aca71b42d)  
