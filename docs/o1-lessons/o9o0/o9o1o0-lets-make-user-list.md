# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1.0/user-list/ver1.0/)  

# 目標

管理者でなくても、会員（メンバー，会員登録しているユーザー）の一覧を見たい  

管理者は、管理画面から会員一覧を見れる  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is   | This is                                   |
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

## Step [O9o1o0g1o0] Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step [O9o1o0g2o0] テンプレート編集 - user_list/ver1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_vol1o0          # アプリケーションと同名
                        └── 📂 user_list
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
        <title>会員登録ユーザー一覧</title>
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
                        <h3>会員登録ユーザー一覧</h3>
                        <v-simple-table>
                            <template v-slot:default>
                                <thead>
                                    <tr>
                                        <th>ID</th>
                                        <th>ユーザー名</th>
                                        <th>アクティブか</th>
                                        <th>最終ログイン</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="user in vu_userDic" :key="user.pk">
                                        {% comment %} Vue で二重波括弧（braces）は変数の展開に使っていることから、 Python のテンプレートに二重波括弧を変数の展開に使わないよう verbatim で指示します。 {% endcomment %} {% verbatim %}
                                        <td>{{ user.pk }}</td>
                                        <td>{{ user.username }}</td>
                                        <td>{{ user.is_active }}</td>
                                        <td>{{ user.last_login }}</td>
                                        {% endverbatim %}
                                    </tr>
                                </tbody>
                            </template>
                        </v-simple-table>
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
                    vu_userDic: JSON.parse("{{ dj_user_dic|escapejs }}"),
                },
            });
        </script>
    </body>
</html>
```

## Step [O9o1o0g3o0] モデルヘルパー モジュール作成 - user/ver1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 ver1o0
👉              │           └── 📄 __init__.py
                └── 📂 templates
                    └── 📂 practice_vol1o0
                        └── 📂 user_list
                            └── 📄 ver1o0.html
```

```py
class MhUser():
    """O9o1o0g3o0 ユーザー モデルヘルパー"""

    # O9o1o0g3o0 以下のファイルはあとで作ります
    from .mh_get_user_dic import get_user_dic
    #    ----------------        ------------
    #    1                       2
    # 1. `src1/apps1/practice_vol1o0/model_helper/user/ver1o0/mh_get_user_dic.py`
    #                                                         ---------------
    # 2. `1.` に含まれる関数
```

## Step [O9o1o0g4o0] モデルヘルパー モジュール作成 - mh_get_user_dic.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 ver1o0
                │           ├── 📄 __init__.py
👉              │           └── 📄 mh_get_user_dic.py
                └── 📂 templates
                    └── 📂 practice_vol1o0
                        └── 📂 user_list
                            └── 📄 ver1o0.html
```

```py
from django.contrib.auth import get_user_model  # カスタムした User
# from django.contrib.auth.models import User # デフォルトの User


def get_user_dic():
    """O9o1o0g4o0 会員登録ユーザー一覧"""
    User = get_user_model()

    # 会員登録ユーザー一覧
    user_resultset = User.objects.all()

    # 使いやすい形に変換します
    user_dic = dict()
    for user in user_resultset:

        if user.last_login is None:
            # まだ一度もログインしていないとき
            last_login1 = ""
        else:
            # 日付型はJSONに変換できないので、先に文字列に変換しておく
            last_login1 = user.last_login.strftime("%Y-%m-%d %H:%M:%S")

        user_dic[user.pk] = {
            "pk": user.pk,
            "last_login": last_login1,
            "username": user.username,
            "is_active": user.is_active,
        }

    return user_dic
```

## Step [O9o1o0g5o0] ビュー作成 - user_list/ver1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 ver1o0
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_user_dic.py
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 user_list
                │           └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 user_list
                        └── 📂 ver1o0
👉                          └── 📄 __init__.py
```

```py
class UserListV():
    """O9o1o0g5o0 練習1.0巻 会員一覧1.0版"""

    # そのページ
    _path_of_this_page = "practice_vol1o0/user_list/ver1o0.html"
    #                     -------------------------------------
    #                     1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/user_list/ver1o0.html` を取得
    #                                          -------------------------------------

    @staticmethod
    def render(request):
        """O9o1o0g5o0 練習1.0巻 会員一覧1.0版 描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_user_list
        #    ---------        ----------------
        #    1                2
        # 1. `src1/apps1/practice_vol1o0/views/user_list/ver1o0/v_render.py`
        #                                                       --------
        # 2. `1.` に含まれる関数

        return render_user_list(request, UserListV._path_of_this_page)
```

## Step [O9o1o0g6o0] ビュー作成 - user_list/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 ver1o0
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_user_dic.py
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 user_list
                │           └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 user_list
                        └── 📂 ver1o0
                            ├── 📄 __init__.py
👉                          └── 📄 v_render.py       # 頭の `v_` は、これはビューだと分かるよう目印に付けているだけなので、無くてもいい
```

```py
# BOF O9o1o0g6o0

import json
from django.shortcuts import render

# 練習1.0巻 ユーザー モデルヘルパー1.0版
from apps1.practice_vol1o0.models_helper.user.ver1o0 import MhUser
#          ---------------                    ------        ------
#          11                                 12            2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_user_list(request, user_list_tp):
    """O9o1o0g6o0 練習1.0巻 会員一覧1.0版 - 描画

    Parameters
    ----------
    user_list_tp : str
        Template path
    """

    context = {
        # * `dj_` - 「Djangoがレンダーに埋め込む変数」 の目印
        # * Vue に渡すときは、 JSON オブジェクトではなく、 JSON 文字列
        'dj_user_dic': json.dumps(MhUser.get_user_dic())
    }

    return render(request, user_list_tp, context)

# EOF O9o1o0g6o0
```

## ~~Step [O9o1o0g7o0]~~

Merged to O9o1o0g7o1o0  

## Step [O9o1o0g7o1o0] ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_vol1o0                  # アプリケーション
    │           ├── 📂 models_helper
    │           │   └── 📂 user
    │           │       └── 📂 ver1o0
    │           │           ├── 📄 __init__.py
    │           │           └── 📄 mh_get_user_dic.py
    │           ├── 📂 templates
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 user_list
    │           │           └── 📄 ver1o0.html
    │           └── 📂 views
    │               └── 📂 o1o0
    │                   └── 📂 user_list
    │                       ├── 📄 __init__.py
    │                       └── 📄 v_render.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/user-list/ver1.0/,,"O9o1o0g7o1o0 練習1.0巻 会員一覧1.0版",apps1.practice_vol1o0.views.user_list.ver1o0,UserListV,,render
```

## Step [O9o1o0g7o2o0] ルート編集 - コマンド打鍵

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

## Step [O9o1o0g8o0] Web画面へアクセス

📖 [http://localhost:8000/practice/vol1.0/user-list/ver1.0/](http://localhost:8000/practice/vol1.0/user-list/ver1.0/)  

## Step [O9o1o0g9o0] ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                    # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_vol1o0                  # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 mh_user
        │       │       └── 📂 ver1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 mh_get_user_dic.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 user_list
        │       │           └── 📄 ver1o0.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 user_list
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_render.py
        └── 📂 project1                      # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/vol1.0/user-list/ver1.0/,O9o1o0g9o0 練習1.0巻 会員一覧1.0版
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DjangoでUserモデルを拡張しよう！](https://qiita.com/muzudho1/items/2d182729f625234f0eff)  
