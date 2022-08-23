# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/v1/my/)  

# 目標

ゲーム対局サーバーと、ユーザーの間には サインアップを経て承諾した内容があるはずだ。  
ユーザーは時に その契約内容を変えたいし、 また 退会したい  

# 詳細

**マイページ** なるページを用意し、そこから 契約内容の変更や 退会が行えると 話しが早いだろう  

免責: この記事では 工事中のページを用意するだけで、契約内容の変更などの機能までは持たない  

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

参考にした元記事は 📖[DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92) だ。  
わたしの記事は単に **やってみた** ぐらいの位置づけだ  

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1                            # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 room
    │   │   │           └── 📄 v1o0.py
    │   │   ├── 📂 tic_tac_toe_v1           # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2           # アプリケーション
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
    ├── 📂 src2_local                      # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# 手順

## Step OA19o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA19o1o0g2o0 画面作成 - my/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 my
👉                          └── 📄 v1o0.html
```

```html
{# OA19o1o0g2o0 #}
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

## Step OA19o1o0g3o0 ビュー編集 - my/v1o0 フォルダー

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1          # アプリケーションと同名
                │       └── 📂 my
                │           └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 my
                        └── 📂 v1o0
👉                          └── 📄 __init__.py
```

```py
class MyV():
    """OA19o1o0g3o0 マイ ページ ビュー"""

    # マイ ページ
    _path_of_my_page = "practice_v1/my/v1o0.html"
    #                   ------------------------
    #                   1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/my/v1o0.html` を取得
    #                                      ------------------------

    @staticmethod
    def render_my(request):
        """OA19o1o0g3o0 描画 - マイ ページ"""

        # 以下のファイルはあとで作ります
        from .v_my import render_my
        #    -----        ---------
        #    1            2
        # 1. `src1/apps1/practice_v1/views/my/v1o0/v_my.py`
        #                                          ----
        # 2. `1.` に含まれる関数

        return render_my(request, MyV._path_of_my_page)
```

## Step OA19o1o0g4o0 ビュー作成 - v_my ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 my
                │           └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 my
                        └── 📂 v1o0
                            ├── 📄 __init__.py
👉                          └── 📄 v_my.py
```

```py
# BOF OA19o1o0g4o0

from django.shortcuts import render


def render_my(request, my_page_tp):
    """OA19o1o0g4o0 描画 - マイ ページ

    Parameters
    ----------
    my_page_tp : str
        Template path
    """

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

    return render(request, my_page_tp, context)

# EOF OA19o1o0g4o0
```

## ~~Step OA19o1o0g5o0~~

Merged to OA19o1o0g5o1o0  

## Step OA19o1o0g5o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_v1                  # アプリケーション
    │           ├── 📂 templates
    │           │   └── 📂 practice_v1
    │           │       └── 📂 my
    │           │           └── 📄 v1o0.html
    │           └── 📂 views
    │               └── 📂 my
    │                   └── 📂 v1o0
    │                       ├── 📄 __init__.py
    │                       └── 📄 v_my.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_autogen.py,practice/v1/my/,practice_v1_my,"OA19o1o0g5o1o0 マイページ ビュー",apps1.practice_v1.views.my.v1o0,MyV,,render_my
```

## Step OA11o4o0g6o2o0 ルート編集 - コマンド打鍵

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

## Step OA19o1o0g6o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/my/](http://localhost:8000/practice/v1/my/)  

## Step OA19o1o0g7o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
        │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 my
        │       │           └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 my
        │               └── 📂 v1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_my.py
        └── 📂 project1                          # プロジェクト
👉          └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/my/,マイ ページ
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでロビー（待合室）を作ろう！](https://qiita.com/muzudho1/items/57677b07854aca71b42d)  
