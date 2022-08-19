# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/v1/buttom_for_member/)  

# 目標

ログインしていない人には見えず、  
ログインしている人には見えるボタンを作ろう！  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

# 始める前に

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
    │   │   ├── 📂 allauth_customized_v1        # アプリケーション
    │   │   ├── 📂 portal_v1                    # アプリケーション
    │   │   └── 📂 practice_v1                  # アプリケーション
    │   ├── 📂 data
    │   ├── 📂 project1                         # プロジェクト
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_accounts.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2
    │   ├── 🐳 docker-compose-project2.yml
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

# Step O8o3o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step O8o3o0g2o0 HTMLファイルの作成

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 button_for_member
👉                          └── 📄 v1o0.html
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

# Step O8o3o0g3o0 ビュー作成 - button_for_member/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 button_for_member
                │           └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 button_for_member
                        └── 📂 v1o0
👉                          └── 📄 __init__.py
```

```py
class ButtonForMember():
    """O8o3o0g3o0 会員にだけ見えるボタンを説明するページ"""

    # そのページ
    _path_of_this_page = "practice_v1/button_for_member/v1o0.html"
    #                     ---------------------------------------
    #                     1
    # 1. src1/apps1/practice_v1/templates/practice_v1/button_for_member/v1o0.html を取得
    #                                     ---------------------------------------

    # 既存のポータルページ
    _path_of_portal = "/"
    #                  -
    #                  1
    # 1. http://example.com:8000/ を取得
    #                           -

    # 既存のログイン必須ページ
    _path_of_login_required = "/practice/v1/login-required"
    #                          ---------------------------
    #                          1
    # 1. http://example.com/practice/v1/login-required
    #                      ---------------------------

    # 既存のログイン ページ
    _path_of_login = "/accounts/v1/login/"
    #                 -------------------
    #                 1
    # 1. http://example.com/accounts/v1/login/
    #                      -------------------

    # 既存のログアウト ページ
    _path_of_logout = "/accounts/v1/logout/"
    #                  --------------------
    #                  1
    # 1. http://example.com/accounts/v1/logout/
    #                      --------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_button_for_member
        #    ---------        ------------------------
        #    1                2
        # 1. `src1/apps1/practice_v1/views/button_for_member/v1o0/v_render.py`
        #                                                         --------
        # 2. `1.` に含まれる関数

        return render_button_for_member(request, ButtonForMember._path_of_this_page, ButtonForMember._path_of_portal, ButtonForMember._path_of_login_required, ButtonForMember._path_of_login, ButtonForMember._path_of_logout)
```

# Step O8o3o0g4o0 ビュー作成 - button_for_member/v1o0/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 button_for_member
                │           └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 button_for_member
                        └── 📂 v1o0
                            ├── 📄 __init__.py
👉                          └── 📄 v_render.py       # 頭の `v_` は、これはビューだと分かるよう目印に付けているだけなので、無くてもいい
```

```py
from django.shortcuts import render


def render_button_for_member(request, lp_button_for_member_page, path_of_portal, path_of_login_required, path_of_login, path_of_logout):
    """O8o3o0g4o0 描画 - 会員にだけ見えるボタンを説明するページ

    Parameters
    ----------
    lp_button_for_member_page : str
        ローカルパス
    """

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        'dj_user': request.user,
        'dj_path_of_portal': path_of_portal,
        'dj_path_of_login_required': path_of_login_required,
        'dj_path_of_login': path_of_login,
        'dj_path_of_logout': path_of_logout,
    }
    return render(request, lp_button_for_member_page, context)
```

# Step O8o3o0g5o0 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 button_for_member
        │       │           └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 button_for_member
        │               └── 📂 v1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_render.py
        └── 📂 project1                      # プロジェクト
👉          └── 📄 urls_practice.py
```

```py
# ...略...


# O8o3o0g5o0 会員用ボタン
from apps1.practice_v1.views.button_for_member.v1o0 import ButtonForMember
#          -----------                         ----        ---------------
#          11                                  12          2
#    ----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [
    # ...略...


    # O8o3o0g5o0 会員にだけ見えるボタンを説明するページ
    path('practice/v1/buttom_for_member/',
         # -----------------------------
         # 1
         ButtonForMember.render),
    #    ----------------------
    #    2
    # 1. 例えば `http://example.com/practice/v1/buttom_for_member/` のような URL のパスの部分
    #                              ------------------------------
    # 2. ButtonForMember クラスの render 静的メソッド
]
```

# Step O8o3o0g6o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/buttom_for_member/](http://localhost:8000/practice/v1/buttom_for_member/)  

# Step O8o3o0g7o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                    # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 button_for_member
        │       │           └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 button_for_member
        │               └── 📂 v1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_render.py
        └── 📂 project1                      # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/buttom_for_member/,会員にだけ見えるボタンを説明するページ
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoで会員登録ユーザーを一覧しよう！](https://qiita.com/muzudho1/items/13c15be5b9070dab1770)  
