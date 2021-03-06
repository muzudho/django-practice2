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

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    │   │   ├── 📂 allauth_customized_v1        # アプリケーション
    │   │   ├── 📂 portal_v1                    # アプリケーション
    │   │   └── 📂 practice_v1                  # アプリケーション
    │   ├── 📂 data
    │   ├── 📂 project1                         # プロジェクト名
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

# Step 1. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. 画面作成 - login_required.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1                 # あなたの開発用ディレクトリー。任意の名前
        └── 📂 apps1
            └── 📂 practice_v1              # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 o1o0
👉                          └── 📄 login_required.html
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

# Step 3. ビュー モジュール作成 - login_required フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1              # アプリケーション
                └── 📂 templates
                    ├── 📂 practice_v1
                    │   └── 📂 o1o0
                    │       └── 📄 login_required.html
                    └── 📂 views
                        └── 📂 o1o0
                            └── 📂 login_required
👉                              └── 📄 __init__.py
```

```py
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import redirect


class LoggingIn():
    """ログイン中"""

    path_of_html = "practice_v1/o1o0/login_required.html"
    #               ------------------------------------
    #               1
    # 1. host1/apps1/practice_v1/templates/practice_v1/o1o0/login_required.html を取得
    #                                      ------------------------------------

    # 👇 このデコレーターを付けると、ログインしていないなら、 settings.py の LOGIN_URL で指定した URL に飛ばします。
    # インスタンスのメソッドや、クラスメソッドには付けられません。
    # 第一引数が self や clazz でないことに注意してください
    @login_required
    def render(request):
        """描画"""
        return loggingIn_render(request, LoggingIn.path_of_html)


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

# Step 4. ルート編集 - urls_practice.py ファイル

👇 以下のファイルの該当箇所を追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1              # アプリケーション
        │       └── 📂 templates
        │           ├── 📂 practice_v1
        │           │   └── 📂 o1o0
        │           │       └── 📄 login_required.html
        │           └── 📂 views
        │               └── 📂 o1o0
        │                   └── 📂 login_required
        │                       └── 📄 __init__.py
        └── 📂 project1
👉          ├── 📄 urls_practice.py          # こちら
❌          └── 📄 urls.py                   # これではない
```

```py
# ...略...


# ログイン必須ページ
from apps1.practice_v1.views.o1o0.login_required import LoggingIn, LoggingOut
#          -----------            --------------        ---------------------
#          11                     12                    2
#    -------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


# ...略...


urlpatterns = [
    # ...略...


    # ログイン中
    path('practice/v1/login-required', LoggingIn.render,
         # -------------------------   ----------------
         # 1                           2
         name='practice_v1_login_required'),
    #          --------------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/login-required` のような URL のパスの部分
    #                              --------------------------
    # 2. LoggingIn クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_login_required' %} のような形でURLを取得するのに使える

    # ログアウト中
    path('practice/v1/logout', LoggingOut.render,
         # -----------------   -----------------
         # 1                   2
         name='practice_v1_logout'),
    #          ------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/logout` のような URL のパスの部分
    #                              ------------------
    # 2. LoggingOut クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_logout' %} のような形でURLを取得するのに使える
]
```

# Step 5. Webページへアクセス

👇　ログインしているときは、ログイン情報が見えます。  
　　ログインしていないときは、ログイン画面が出ます

📖 [http://localhost:8000/practice/v1/login-required](http://localhost:8000/practice/v1/login-required)  

👇 ログアウトするにはこちら  

📖 [http://localhost:8000/practice/v1/logout](http://localhost:8000/practice/v1/logout)  

# Step 6. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1              # アプリケーション
        │       └── 📂 templates
        │           ├── 📂 practice_v1
        │           │   └── 📂 o1o0
        │           │       └── 📄 login_required.html
        │           └── 📂 views
        │               └── 📂 o1o0
        │                   └── 📄 v_login_required.py
        └── 📂 project1
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/login-required,ログイン必須
/practice/v1/logout,ログアウト
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでログインしていない人には見えず、ログインしている人には見えるボタンを作ろう！](https://qiita.com/muzudho1/items/0c59f3ce7aa6bef2a91f)  

# 関連する記事

📖 [Using the Django authentication system](https://docs.djangoproject.com/en/3.1/topics/auth/default/)  
📖 [Djangoメモ(25) : login_requiredデコレータでビューをログイン済みユーザーのみに制限](https://wonderwall.hatenablog.com/entry/2018/03/25/180000)  

## User関連

📖 [Django check if a related object exists error: RelatedObjectDoesNotExist](https://stackoverflow.com/questions/27064206/django-check-if-a-related-object-exists-error-relatedobjectdoesnotexist)  
