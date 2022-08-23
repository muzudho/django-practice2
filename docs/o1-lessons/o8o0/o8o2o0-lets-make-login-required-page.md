# サンプルを見る

📖 [この記事のゴール：ログインが必要なページ](http://localhost:8000/practice/v1/login-required)  
📖 [この記事のゴール：ログアウト](http://localhost:8000/practice/v1/logout)  

# 目標

ログインしているユーザーには 見え、  
そうでないユーザーには ログイン ページが出るような  
ページを作る練習をする  

## 詳細

とりあえず、見えるページは、以下のように 自分のユーザー情報を出す  

```
Login user.

* id: 1
* username: Muzudho
* email: admin@example.com
```

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
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📄 urls.py
    └── 📄 .gitignore
```

# 手順

## Step O8o2o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step O8o2o0g2o0 画面作成 - login_required/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1                 # あなたの開発用ディレクトリー。任意の名前
        └── 📂 apps1
            └── 📂 practice_v1              # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 login_required
👉                          └── 📄 v1o0.html
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

## Step O8o2o0g3o0 ビュー作成 - login_required フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1              # アプリケーション
                └── 📂 templates
                    ├── 📂 practice_v1
                    │   └── 📂 login_required
👉                  │       └── 📄 v1o0.html
                    └── 📂 views
                        └── 📂 login_required
                            └── 📂 v1o0
👉                              └── 📄 __init__.py
```

```py
# BOF O8o2o0g3o0

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


class LoggingIn():
    """O8o2o0g3o0 ログイン中"""

    # Template path
    login_required_tp = "practice_v1/login_required/v1o0.html"
    #                    ------------------------------------
    #                    1
    # 1. src1/apps1/practice_v1/templates/practice_v1/login_required/v1o0.html を取得
    #                                     ------------------------------------

    # 👇 このデコレーターを付けると、ログインしていないなら、 settings.py の LOGIN_URL で指定した URL に飛ばします。
    # インスタンスのメソッドや、クラスメソッドには付けられません。
    # 第一引数が self や clazz でないことに注意してください
    @login_required
    def render(request):
        """描画"""
        return loggingIn_render(request, LoggingIn.login_required_tp)


class LoggingOut():
    """O8o2o0g3o0 ログアウト中"""

    def render(request):
        """描画"""
        return loggingOut_render(request)


# 以下、関数


def loggingIn_render(request, login_required_tp):
    """O8o2o0g3o0 ログイン中 - 描画

    Parameters
    ----------
    request : object
        リクエスト
    login_required_tp : str
        Template path
    """

    user = request.user
    context = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }
    return render(request, login_required_tp, context)


def loggingOut_render(request):
    """O8o2o0g3o0 ログアウト中 - 描画"""
    logout(request)  # Django の認証機能のログアウトを使う
    return redirect('home')  # ホームに戻る

# EOF O8o2o0g3o0
```

## ~~Step O8o2o0g4o0~~

Merged to O8o2o0g4o1o0  

## Step O8o2o0g4o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_v1              # アプリケーション
    │           └── 📂 templates
    │               ├── 📂 practice_v1
    │               │   └── 📂 login_required
    │               │       └── 📄 v1o0.html
    │               └── 📂 views
    │                   └── 📂 login_required
    │                       └── 📂 v1o0
    │                           └── 📄 __init__.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_autogen.py,practice/v1/login-required,practice_v1_login_required,"O8o2o0g4o1o0 ログイン必須ページでログイン中",apps1.practice_v1.views.login_required.v1o0,LoggingIn,,render
../src1/project1/urls_practice_autogen.py,practice/v1/logout,practice_v1_logout,"O8o2o0g4o1o0 ログイン必須ページでログアウト中",apps1.practice_v1.views.login_required.v1o0,LoggingOut,,render
```

## Step O8o2o0g4o2o0 ルート編集 - コマンド打鍵

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

## Step O8o2o0g5o0 Webページへアクセス

👇　ログインしているときは、ログイン情報が見えます。  
　　ログインしていないときに（ページを開いたり、画面を再更新したりすると）、ログイン画面が出ます

📖 [http://localhost:8000/practice/v1/login-required](http://localhost:8000/practice/v1/login-required)  

👇 ログアウトするにはこちら  

📖 [http://localhost:8000/practice/v1/logout](http://localhost:8000/practice/v1/logout)  

## Step O8o2o0g6o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
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

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでログインしていない人には見えず、ログインしている人には見えるボタンを作ろう！](https://qiita.com/muzudho1/items/0c59f3ce7aa6bef2a91f)  

# 関連する記事

📖 [Using the Django authentication system](https://docs.djangoproject.com/en/3.1/topics/auth/default/)  
📖 [Djangoメモ(25) : login_requiredデコレータでビューをログイン済みユーザーのみに制限](https://wonderwall.hatenablog.com/entry/2018/03/25/180000)  

## User関連

📖 [Django check if a related object exists error: RelatedObjectDoesNotExist](https://stackoverflow.com/questions/27064206/django-check-if-a-related-object-exists-error-relatedobjectdoesnotexist)  
