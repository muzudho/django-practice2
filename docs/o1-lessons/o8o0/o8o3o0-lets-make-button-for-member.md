# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1.0/buttom_for_member/ver1.0/)  

# 目標

ログインしていない人には見えず、  
ログインしている人には見えるボタンを作ろう！  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| Key       | Value                                     |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Auth      | allauth                                   |
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   ├── 📂 accounts_vol1o0        # アプリケーション
    │   │   ├── 📂 portal_v1                    # アプリケーション
    │   │   └── 📂 practice_vol1o0                  # アプリケーション
    │   ├── 📂 data
    │   ├── 📂 project1                         # プロジェクト
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_accounts_vol1o0.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2
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
    └── 📄 .gitignore
```

# 手順

## Step [O8o3o0g1o0] Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step [O8o3o0g2o0] HTMLファイルの作成

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_vol1o0          # アプリケーションと同名
                        └── 📂 button_for_member
👉                          └── 📄 ver1o0.html
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
        <title>会員専用のボタン</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container>
                        <v-row class="my-2">
                            <h3>みんなのボタン</h3>
                        </v-row>
                        <v-row class="my-2">
                            <v-btn :href="createPortalUrl()">ポータルへ移動する</v-btn>
                        </v-row>
                        {% if user.is_authenticated %}
                        <v-row class="my-2">
                            <h3>会員専用のボタン</h3>
                        </v-row>
                        <v-row class="my-2">
                            <v-btn :href="createLoginRequiredUrl()">ログイン必須ページ</v-btn>
                        </v-row>
                        <v-row class="my-2">
                            <v-btn :href="createLogoutUrl()">ログアウト</v-btn>
                        </v-row>
                        {% else %}
                        <v-row class="my-2">
                            <v-btn :href="createLoginUrl()">ログイン／会員登録</v-btn>
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
                    // * `vu_` - 「vue1.dataのメンバー」 の目印
                    // * `dj_` - 「Djangoがレンダーに埋め込む変数」 の目印
                    vu_pathOfPortal: "{{ dj_path_of_portal }}",
                    vu_pathOfLogin: "{{ dj_path_of_login }}",
                    vu_pathOfLoginRequired: "{{ dj_path_of_login_required }}",
                    vu_pathOfLogout: "{{ dj_path_of_logout }}",
                },
                methods: {
                    createPortalUrl() {
                        let url = `${location.protocol}//${location.host}${this.vu_pathOfPortal}`;
                        //         --------------------  ---------------]-----------------------
                        //         1                     2               3
                        // 1. protocol
                        // 2. host
                        // 3. path
                        console.log(`portal url=[${url}]`);
                        return url;
                    },
                    createLoginUrl() {
                        let url = `${location.protocol}//${location.host}${this.vu_pathOfLogin}`;
                        console.log(`login url=[${url}]`);
                        return url;
                    },
                    createLoginRequiredUrl() {
                        let url = `${location.protocol}//${location.host}${this.vu_pathOfLoginRequired}`;
                        console.log(`loginRequired url=[${url}]`);
                        return url;
                    },
                    createLogoutUrl() {
                        let url = `${location.protocol}//${location.host}${this.vu_pathOfLogout}`;
                        console.log(`logout url=[${url}]`);
                        return url;
                    },
                },
            });
        </script>
    </body>
</html>
```

## Step [O8o3o0g3o0] ビュー作成 - button_for_member/ver1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 button_for_member
                │           └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 button_for_member
                        └── 📂 ver1o0
👉                          └── 📄 __init__.py
```

```py
# BOF O8o3o0g3o0

class ButtonForMember():
    """O8o3o0g3o0 会員にだけ見えるボタンを説明するページ"""

    # そのページ
    _path_of_this_page = "practice_vol1o0/button_for_member/ver1o0.html"
    #                     ---------------------------------------------
    #                     1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/button_for_member/ver1o0.html` を取得
    #                                          ---------------------------------------------

    # 既存のポータルページ
    _path_of_portal = "/"
    #                  -
    #                  1
    # 1. http://example.com:8000/ を取得
    #                           -

    # 既存のログイン必須ページ
    _path_of_login_required = "/practice/vol1.0/login-required/ver1.0/"
    #                          ---------------------------------------
    #                          1
    # 1. `http://example.com/practice/vol1.0/login-required/ver1.0/`
    #                       ---------------------------

    # 既存のログイン ページ
    _path_of_login = "/accounts/vol1.0/login/"
    #                 -----------------------
    #                 1
    # 1. http://example.com/accounts/vol1.0/login/
    #                      -----------------------

    # 既存のログアウト ページ
    _path_of_logout = "/accounts/vol1.0/logout/"
    #                  ------------------------
    #                  1
    # 1. http://example.com/accounts/vol1.0/logout/
    #                      ------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_button_for_member
        #    ---------        ------------------------
        #    1                2
        # 1. `src1/apps1/practice_vol1o0/views/button_for_member/ver1o0/v_render.py`
        #                                                               --------
        # 2. `1.` に含まれる関数

        return render_button_for_member(request, ButtonForMember._path_of_this_page, ButtonForMember._path_of_portal, ButtonForMember._path_of_login_required, ButtonForMember._path_of_login, ButtonForMember._path_of_logout)

# EOF O8o3o0g3o0
```

## Step [O8o3o0g4o0] ビュー作成 - button_for_member/ver1o0/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 button_for_member
                │           └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 button_for_member
                        └── 📂 ver1o0
                            ├── 📄 __init__.py
👉                          └── 📄 v_render.py       # 頭の `v_` は、これはビューだと分かるよう目印に付けているだけなので、無くてもいい
```

```py
# BOF O8o3o0g4o0

from django.shortcuts import render


def render_button_for_member(request, button_for_member_page_tp, path_of_portal, path_of_login_required, path_of_login, path_of_logout):
    """O8o3o0g4o0 描画 - 会員にだけ見えるボタンを説明するページ

    Parameters
    ----------
    button_for_member_page_tp : str
        Template path
    """

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        'dj_user': request.user,
        'dj_path_of_portal': path_of_portal,
        'dj_path_of_login_required': path_of_login_required,
        'dj_path_of_login': path_of_login,
        'dj_path_of_logout': path_of_logout,
    }
    return render(request, button_for_member_page_tp, context)

# EOF O8o3o0g4o0
```

## ~~Step [O8o3o0g5o0]~~

Merged to O8o3o0g5o1o0  

## Step [O8o3o0g5o1o0] ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_vol1o0                  # アプリケーション
    │           ├── 📂 templates
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 button_for_member
    │           │           └── 📄 ver1o0.html
    │           └── 📂 views
    │               └── 📂 button_for_member
    │                   └── 📂 ver1o0
    │                       ├── 📄 __init__.py
    │                       └── 📄 v_render.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/buttom_for_member/ver1.0/,,"O8o3o0g5o1o0 練習1.0巻 会員にだけ見えるボタンを説明するページ1.0版",apps1.practice_vol1o0.views.button_for_member.ver1o0,ButtonForMember,,render
```

## Step [O8o3o0g5o2o0] ルート編集 - コマンド打鍵

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

## Step [O8o3o0g6o0] Web画面へアクセス

📖 [http://localhost:8000/practice/vol1.0/buttom_for_member/ver1.0/](http://localhost:8000/practice/vol1.0/buttom_for_member/ver1.0/)  

## Step [O8o3o0g7o0] ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                    # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_vol1o0                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 button_for_member
        │       │           └── 📄 ver1o0.html
        │       └── 📂 views
        │           └── 📂 button_for_member
        │               └── 📂 ver1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_render.py
        └── 📂 project1                      # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/vol1.0/buttom_for_member/ver1.0/,O8o3o0g7o0 練習1.0巻 会員にだけ見えるボタンを説明するページ1.0版
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoで会員登録ユーザーを一覧しよう！](https://qiita.com/muzudho1/items/13c15be5b9070dab1770)  
