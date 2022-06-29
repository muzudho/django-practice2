# 目的

ログインしているユーザーには 見え、  
そうでないユーザーには ログイン ページが出るような  
ページを作る練習をする  

見えるページは、以下のように 自分のユーザー情報が出るよう、考えている  

```
Login user.

* id: 1
* username: Muzudho
* email: admin@example.com
```

# 手段

allauth アプリケーションの機能を使う　　

# はじめに

この記事は Lesson01 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    ├── 📂host1
    │   ├── 📂apps1
    │   │   ├── 📂allauth_customized    # アプリケーション名
    │   │   ├── 📂portal                # アプリケーション名
    │   │   │   ├── 📂data
    │   │   │   │   └── 📄finished-lesson.csv
    │   │   │   ├── 📂migrations
    │   │   │   │   └── 📄__init__.py
    │   │   │   ├── 📂static
    │   │   │   │   └── 🚀favicon.ico
    │   │   │   ├── 📂templates
    │   │   │   │   └── 📂portal
    │   │   │   │       └── 📂v0o0o1
    │   │   │   │           └── 📄portal_base.html
    │   │   │   └── 📂views
    │   │   │       └── 📂v0o0o1
    │   │   │           └── 📄pages.py
    │   │   └── 📂practice              # アプリケーション名
    │   ├── 📂data
    │   ├── 📂project1                  # プロジェクト名
    │   │   ├── 📄__init__.py
    │   │   ├── 📄asgi.py
    │   │   ├── 📄settings_secrets_example.txt
    │   │   ├── 📄settings.py
    │   │   ├── 📄urls_accounts.py
    │   │   ├── 📄urls_practice.py
    │   │   ├── 📄urls.py
    │   │   └── 📄wsgi.py
    │   ├── 📂project2
    │   ├── 🐳docker-compose-project2.yml
    │   ├── 🐳docker-compose.yml
    │   ├── 🐳Dockerfile
    │   ├── 📄manage.py
    │   └── 📄requirements.txt
    └── 📄.gitignore
```

# Step 1. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. HTMLファイルを置く

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1                 # あなたの開発用ディレクトリー。任意の名前
        └── 📂apps1
            └── 📂practice              # アプリケーション
                └── 📂templates
                    └── 📂practice              # アプリケーションと同名
                        └── 📂v0o0o1
👉                          └── 📄login_required.html
```

```html
<html>
    <body>
        Login user.
        <ul>
            <li>id: {{ id }}</li>
            <li>username: {{ username }}</li>
            <li>email: {{ email }}</li>
        </ul>
    </body>
</html>
```

# Step 3. ビュー作成 - v_login_required.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice              # アプリケーション
                └── 📂templates
                    ├── 📂practice
                    │   └── 📂v0o0o1
                    │       └── 📄login_required.html
                    └── 📂views
👉                      └── 📄v_login_required.py
```

```py
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import redirect


class LoggingIn():
    """ログイン中"""

    _path_of_html = "practice/v0o0o1/login_required.html"
    #                -----------------------------------
    #                1
    # 1. host1/apps1/practice/templates/practice/v0o0o1/login_required.html を取得
    #                                   -----------------------------------

    # 👇 このデコレーターを付けると、ログインしていないなら、 settings.py の LOGIN_URL で指定した URL に飛ばします。
    # インスタンスのメソッドや、クラスメソッドには付けられません。
    # 第一引数が self や clazz でないことに注意してください
    @login_required
    def render(request):
        """描画"""
        return loggingIn_render(request, LoggingIn._path_of_html)


class LoggingOut():
    """ログアウト中"""

    def render(request):
        """描画"""
        return loggingOut_render(request)


# 以下、関数


def loggingIn_render(request, path_of_html):
    """ログイン中 - 描画"""
    template = loader.get_template(path_of_html)

    user = request.user
    context = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }
    return HttpResponse(template.render(context, request))


def loggingOut_render(request):
    """ログアウト中 - 描画"""
    logout(request)  # Django の認証機能のログアウトを使う
    return redirect('home')  # ホームに戻る
```

# Step 4. ルート編集 - urls.py ファイル

👇 以下のファイルの該当箇所を追記してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂practice              # アプリケーション
        │       └── 📂templates
        │           ├── 📂practice
        │           │   └── 📂v0o0o1
        │           │       └── 📄login_required.html
        │           └── 📂views
        │               └── 📄v_login_required.py
        └── 📂project1
👉          ├── 📄urls_practice.py          # こちら
❌          └── 📄urls.py                   # これではない
```

```py
# ...略...


from apps1.practice.views.v0o0o1 import v_login_required
#    ---------------------------        ----------------
#    1                                  2
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き


# ...略...


urlpatterns = [
    # ...略...


    # ログイン中
    path('practice/login-required', v_login_required.LoggingIn.render,
         # ----------------------   ---------------------------------
         # 1                        2
         name='practiceLoginRequired'),
    #          ---------------------
    #          3
    # 1. 例えば `http://example.com/practice/login-required` のような URL のパスの部分
    #                              -----------------------
    # 2. v_login_required.py ファイルの LoggingIn クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practiceLoginRequired' %} のような形でURLを取得するのに使える

    # ログアウト中
    path('practice/logout', v_login_required.LoggingOut.render,
         # --------------   ----------------------------------
         # 1                2
         name='practiceLogout'),
    #          --------------
    #          3
    # 1. 例えば `http://example.com/practice/logout` のような URL のパスの部分
    #                              ---------------
    # 2. v_login_required.py ファイルの LoggingOut クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practiceLogout' %} のような形でURLを取得するのに使える
]
```

# Step 5. Webページへアクセス

👇　ログインしているときは、ログイン情報が見えます。  
　　ログインしていないときは、ログイン画面が出ます

📖 [http://localhost:8000/practice/login-required](http://localhost:8000/practice/login-required)  

👇 ログアウトするにはこちら  

📖 [http://localhost:8000/practice/logout](http://localhost:8000/practice/logout)  

# Step 6. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   ├── 📂portal                # アプリケーション
        │   │   └── 📂data
👉      │   │       └── 📄finished-lessons.csv
        │   └── 📂practice              # アプリケーション
        │       └── 📂templates
        │           ├── 📂practice
        │           │   └── 📂v0o0o1
        │           │       └── 📄login_required.html
        │           └── 📂views
        │               └── 📄v_login_required.py
        └── 📂project1
            ├── 📄urls_practice.py
            └── 📄urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/login-required,ログイン必須
/practice/logout,ログアウト
```

# 次の記事

📖 [Djangoでスーパーユーザーを追加しよう！](https://qiita.com/muzudho1/items/cf21fa75e23e1f987153)  

# 関連する記事

📖 [Using the Django authentication system](https://docs.djangoproject.com/en/3.1/topics/auth/default/)  
📖 [Djangoメモ(25) : login_requiredデコレータでビューをログイン済みユーザーのみに制限](https://wonderwall.hatenablog.com/entry/2018/03/25/180000)  
