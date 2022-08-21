# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/v1/active-user-list/)  

# 目標

（会員登録ユーザーではなく）現在、サーバーに接続されていると思われるユーザー（≒アクティブ・ユーザー）を一覧したい  

* ログインしたまま サーバーから離れていて、まだセッション期限切れをしていないユーザーを数えてしまっても構わないものとする  

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
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📄 urls.py
    └── 📄 .gitignore
```

# 手順

## Step O9o3o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step O9o3o0g2o0 画面作成 - active_user_list/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 active_user_list
👉                          └── 📄 v1o0.html
```

```html
{# O9o3o0g2o0 #}
<!-- -->
{% load static %} {# 👈 あとで static "URL" を使うので load static します #}
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
        <title>アクティブ ユーザー一覧</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <v-main>
                    <v-container>
                        <h3>アクティブ ユーザー一覧</h3>
                    </v-container>
                    <v-container>
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
                                    <tr v-for="user in vu_users" :key="user.pk">
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
                    vu_users: JSON.parse("{{ dj_users|escapejs }}"),
                },
                methods: {
                    createRoomsReadPath(id) {
                        return `${this.vu_readRoomPath}${id}`;
                    },
                },
            });
        </script>
    </body>
</html>
```

## Step O9o3o0g3o0 モデル関連作成 - session/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 session
                │       └── 📂 v1o0
👉              │           └── 📄 __init__.py
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 active_user_list
                            └── 📄 v1o0.html
```

```py
class MhSession():
    """O9o3o0g3o0 セッション ヘルパー"""

    # O9o3o0g3o0 以下のファイルはあとで作ります
    from .v_get_all_logged_in_users import get_all_logged_in_users
    #    --------------------------        -----------------------
    #    1                                 2
    # 1. `src1/apps1/practice_v1/model_helper/sesion/v1o0/v_get_all_logged_in_users.py`
    #                                                     -------------------------
    # 2. `1.` に含まれる関数
```

## Step O9o3o0g4o0 ビュー作成 - session/v1o0/v_get_all_logged_in_users.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 session
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
👉              │           └── 📄 v_get_all_logged_in_users.py
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 active_user_list
                            └── 📄 v1o0.html
```

```py
# See also: 📖[How to get the list of the authenticated users?](https://stackoverflow.com/questions/2723052/how-to-get-the-list-of-the-authenticated-users)
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone


def get_all_logged_in_users():
    """O9o3o0g4o0 接続が切れていないセッションを絞りこみます。
    ログアウトせず２週間放置しているセッションが含まれる場合があります
    """

    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # セッション一覧を、ユーザーID一覧に変換します
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    user_resultset = User.objects.filter(id__in=uid_list)
    """
web_1  | user_table_doc=[
web_1  |     {
web_1  |         "model": "auth.user",
web_1  |         "pk": 1,
web_1  |         "fields": {
web_1  |             "password": "pbkdf2_sha256$260000$tOSdFO6BqvafBgtFgE1qYS$+rv007MKnAy8j+krixlQuogvi46Xl8fZf87xn4lAU+0=",
web_1  |             "last_login": "2022-05-14T03:09:21.968Z",
web_1  |             "is_superuser": false,
web_1  |             "username": "kifuwarabe",
web_1  |             "first_name": "",
web_1  |             "last_name": "",
web_1  |             "email": "muzudho1@gmail.com",
web_1  |             "is_staff": false,
web_1  |             "is_active": true,
web_1  |             "date_joined": "2022-03-13T05:45:26.368Z",
web_1  |             "groups": [],
web_1  |             "user_permissions": []
web_1  |         }
web_1  |     }
web_1  | ]
"""
    # print(f"user_table_doc={json.dumps(user_table_doc, indent=4)}")

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

## Step O9o3o0g5o0 ビュー作成 - session/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 session
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
                │           └── 📄 v_get_all_logged_in_users.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 active_user_list
                │           └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 session
                        └── 📂 v1o0
👉                          └── 📄 __init__.py
```

```py
class SessionV():
    """O9o3o0g5o0 セッション ビュー"""

    # そのページ
    _path_of_this_page = "practice_v1/active_user_list/v1o0.html"
    #                     --------------------------------------
    #                     1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/active_user_list/v1o0.html` を取得
    #                                      --------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_active_user_list
        #    ---------        -----------------------
        #    1                2
        # 1. `src1/apps1/practice_v1/views/session/v1o0/v_render.py`
        #                                               --------
        # 2. `1.` に含まれる関数

        return render_active_user_list(request, SessionV._path_of_this_page)
```

## Step O9o3o0g6o0 ビュー作成 - session/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 session
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
                │           └── 📄 v_get_all_logged_in_users.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 active_user_list
                │           └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 session
                        └── 📂 v1o0
                            ├── 📄 __init__.py
👉                          └── 📄 v_render.py
```

```py
import json
from django.shortcuts import render

# セッション モデルヘルパー
from apps1.practice_v1.models_helper.session.v1o0 import MhSession
#          -----------                       ----        ---------
#          11                                12          2
#    --------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. クラス


def render_active_user_list(request, path_of_this_page):
    """O9o3o0g6o0 描画 - アクティブ ユーザー一覧"""

    context = {
        # * `dj_` - 「Djangoがレンダーに埋め込む変数」 の目印
        # * Vue に渡すときは、 JSON オブジェクトではなく、 JSON 文字列
        'dj_users': json.dumps(MhSession.get_all_logged_in_users())
    }

    return render(request, path_of_this_page, context)
```

## ~~Step O9o3o0g7o0~~

Merged to O9o3o0g7o1o0  

## Step O9o3o0g7o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_v1                  # アプリケーション
    │           ├── 📂 models_helper
    │           │   └── 📂 session
    │           │       └── 📂 v1o0
    │           │           ├── 📄 __init__.py
    │           │           └── 📄 v_get_all_logged_in_users.py
    │           ├── 📂 templates
    │           │   └── 📂 practice_v1
    │           │       └── 📂 active_user_list
    │           │           └── 📄 v1o0.html
    │           └── 📂 views
    │               └── 📂 o1o0
    │                   └── 📂 session
    │                       ├── 📄 __init__.py
    │                       └── 📄 v_render_active_user_list.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_autogen.py,practice/v1/active-user-list/,practice_v1_active_user_list,"O9o3o0g7o1o0 アクティブユーザー一覧",apps1.practice_v1.views.session.v1o0,SessionV,,render
```

## Step O9o3o0g7o2o0 ルート編集 - コマンド打鍵

👇 以下のコマンドを打鍵してほしい  

```shell
# がんばって、ディレクトリーを移動してほしい
# cd ../src1_meta

# See also: O3o2o_1o0g2o0
python -m scripts.auto_generators.urls

# がんばって、ディレクトリーを移動してほしい
# cd ../src1

# 設定ファイルを変更したから、サーバーを再起動してほしい
docker-compose restart
```

## Step O9o3o0g8o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/active-user-list/](http://localhost:8000/practice/v1/active-user-list/)  

## Step O9o3o0g9o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                    # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 session
        │       │       └── 📂 v1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_get_all_logged_in_users.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 active_user_list
        │       │           └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 session
        │               └── 📂 v1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_render_active_user_list.py
        └── 📂 project1                      # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/active-user-list/,アクティブユーザー一覧
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでモデルを追加しよう！](https://qiita.com/muzudho1/items/2463cc006da69f5ed7b2)  

# 関連する記事

📖 [djangoでログイン状態を判定する機能](https://techpr.info/python/django-login-judge/)  
📖 [How to get the list of the authenticated users?](https://stackoverflow.com/questions/2723052/how-to-get-the-list-of-the-authenticated-users)  
📖 [Get List of Current Users](https://www.codingforentrepreneurs.com/blog/django-tutorial-get-list-of-current-users)  
