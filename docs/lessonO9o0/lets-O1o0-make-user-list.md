# 目的

管理者でなくても、会員（メンバー，会員登録しているユーザー）の一覧を見たい  

管理者は、管理画面から会員一覧を見れる  

# 知識

Django では、サインアップした口座を User と呼んでいる。  
従って、「会員登録しているユーザー」と、「ユーザー」は同義だ  

「会員登録していないユーザー」とは、Django では、単に口座に紐づかないアクセスに過ぎない  

名称を User ではなく Member にしてほしかった  

# はじめに

この記事は LessonO[1 0] から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key       | Value                                     |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Auth      | allauth                                   |
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 host1
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   │   ├── 📂 data
    │   │   │   │   └── 📄 finished-lesson.csv
    │   │   │   ├── 📂 migrations
    │   │   │   │   └── 📄 __init__.py
    │   │   │   ├── 📂 static
    │   │   │   │   └── 🚀 favicon.ico
    │   │   │   ├── 📂 templates
    │   │   │   │   └── 📂 portal_v1
    │   │   │   │       └── 📂 o2o1
    │   │   │   │           └── 📄 portal_base.html
    │   │   │   └── 📂 views
    │   │   │       └── 📂 o2o1
    │   │   │           └── 📄 pages.py
    │   │   └── 📂 practice_v1              # アプリケーション
    │   │       └── 📂 templates
    │   │           ├── 📂 practice_v1
    │   │           │   └── 📂 o2o1
    │   │           │       └── 📄 login_required.html
    │   │           └── 📂 views
    │   │               └── 📄 v_login_required.py
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト
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

# Step O[1 0] Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step O[2 0] テンプレート編集 - user-list.html ファイル

以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 o2o1
👉                          └── 📄 user_list.html
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

# Step O[3 0] モデルヘルパー作成 - mh_user フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 o2o1
                │       └── 📂 mh_user               # 頭の `mh_` は models helper の頭文字を目印にしたもの。無くてもいい
👉              │           └── 📄 __init__.py
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 o2o1
                            └── 📄 user_list.html
```

```py
class MhUser():
    """ユーザー モデルヘルパー"""

    # * 以下を追加
    # 以下のファイルはあとで作ります
    from .mh_get_user_dic import get_user_dic
    #    ----------------        ------------
    #    1                       2
    # 1. `host1/apps1/practice_v1/model_helper/o2o1/mh_user/mh_get_user_dic.py`
    #                                                         ---------------
    # 2. `1.` に含まれる関数
```

# Step O[4 0] モデルヘルパー モジュール作成 - mh_get_user_dic.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 o2o1
                │       └── 📂 mh_user
                │           ├── 📄 __init__.py
👉              │           └── 📄 mh_get_user_dic.py
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 o2o1
                            └── 📄 user_list.html
```

```py
from django.contrib.auth import get_user_model  # カスタムした User
# from django.contrib.auth.models import User # デフォルトの User


@staticmethod
def get_user_dic():
    """会員登録ユーザー一覧"""
    User = get_user_model()

    # 会員登録ユーザー一覧
    user_resultset = User.objects.all()

    # 使いやすい形に変換します
    user_dic = dict()
    for user in user_resultset:
        user_dic[user.pk] = {
            "pk": user.pk,
            # 日付型はJSONに変換できないので、先に文字列に変換しておく
            "last_login": user.last_login.strftime("%Y-%m-%d %H:%M:%S"),
            "username": user.username,
            "is_active": user.is_active,
        }

    return user_dic
```

# Step O[5 0] ビュー モジュール作成 - user_list フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 o2o1
                │       └── 📂 mh_user
                │           └── 📄 __init__.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o2o1
                │           └── 📄 user_list.html
                └── 📂 views
                    └── 📂 o2o1
                        └── 📂 user_list
👉                          └── 📄 __init__.py
```

```py
class UserListV():
    """会員一覧ビュー"""

    # そのページ
    _path_of_this_page = "practice_v1/o2o1/user_list.html"
    #                     ---------------------------------
    #                     1
    # 1. host1/apps1/practice_v1/templates/practice_v1/o2o1/user_list.html を取得
    #                                        ---------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_user_list
        #    ---------        ----------------
        #    1                2
        # 1. `host1/apps1/practice_v1/views/o2o1/user_list/v_render.py`
        #                                                    --------
        # 2. `1.` に含まれる関数

        return render_user_list(request, UserListV._path_of_this_page)
```

# Step O[6 0] ビュー モジュール作成 - user_list/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models_helper
                │   └── 📂 o2o1
                │       └── 📂 mh_user
                │           └── 📄 __init__.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o2o1
                │           └── 📄 user_list.html
                └── 📂 views
                    └── 📂 o2o1
                        └── 📂 user_list
                            ├── 📄 __init__.py
👉                          └── 📄 v_render.py       # 頭の `v_` は、これはビューだと分かるよう目印に付けているだけなので、無くてもいい
```

```py
import json
from django.http import HttpResponse
from django.template import loader

# ユーザー モデルヘルパー
from apps1.practice_v1.models_helper.o2o1.mh_user import MhUser
#          -------------                    -------        ------
#          11                               12             2
#    ----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_user_list(request, path_of_this_page):
    """描画 - 会員一覧"""

    template = loader.get_template(path_of_this_page)

    context = {
        # * `dj_` - 「Djangoがレンダーに埋め込む変数」 の目印
        # * Vue に渡すときは、 JSON オブジェクトではなく、 JSON 文字列
        'dj_user_dic': json.dumps(MhUser.get_user_dic())
    }

    return HttpResponse(template.render(context, request))
```

# Step O[7 0] ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 o2o1
        │       │       └── 📂 mh_user
        │       │           └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o2o1
        │       │           └── 📄 user_list.html
        │       └── 📂 views
        │           └── 📂 o2o1
        │               └── 📂 user_list
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_render.py
        └── 📂 project1                      # プロジェクト
👉          └── 📄 urls_practice.py
```

```py
# ...略...


# 会員一覧
from apps1.practice_v1.views.o2o1.user_list import UserListV
#          -------------            ---------        ---------
#          11                       12               2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [
    # ...略...


    # 会員一覧
    path('practice/v1.0/user-list/',
         # ---------------------
         # 1
         UserListV.render, name='practice_v1_user_list'),
    #    ----------------        -----------------------
    #    2                       3
    # 1. 例えば `http://example.com/practice/v1.0/user-list/` のような URL のパスの部分
    #                              ----------------------
    # 2. UserListV クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_user_list' %} のような形でURLを取得するのに使える
]
```

# Step O[8 0] Web画面へアクセス

📖 [http://localhost:8000/practice/v1.0/user-list/](http://localhost:8000/practice/v1.0/user-list/)  

# Step O[9 0] ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                    # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 models_helper
        │       │   └── 📂 o2o1
        │       │       └── 📂 mh_user
        │       │           └── 📄 __init__.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o2o1
        │       │           └── 📄 user_list.html
        │       └── 📂 views
        │           └── 📂 o2o1
        │               └── 📂 user_list
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_render.py
        └── 📂 project1                      # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1.0/user-list/,会員一覧
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでアクティブユーザーの一覧を作ろう！](https://qiita.com/muzudho1/items/bea77e8a69c5c805e1d7)  
