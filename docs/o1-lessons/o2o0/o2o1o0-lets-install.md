# 目標

開発環境を用意する  

# 情報

| What is    | This is                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------- |
| 連載の目次 | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is   | This is                                   |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Editor    | Visual Studio Code （以下 VSCode と表記） |
| Database  | PostgreSQL                                |

一番参考になる元記事は 📖[Quickstart: Compose and Django](https://docs.docker.com/samples/django/) だ。  
わたしの記事は単に **やってみた** ぐらいの位置づけだ  

# 手順

## Step O2o1o0g1o0 エディターのインストール - Visual Studio Code

👇 以下のリンクから、がんばって Visual Studio Code をインストールしてほしい  

📖 [Visual Studio Code](https://code.visualstudio.com/)  

## Step O2o1o0g2o0 リポジトリの用意 - Git

がんばって Git を使ったソース管理を覚えてきてほしい  

👇 参考サイト  

* 📖 [Git Hub](https://github.com/)
    * 📖 [Git Hub Desktop](https://desktop.github.com/)
* 📖 [Git Lab](https://gitlab.com/gitlab-org/gitlab)

## Step O2o1o0g3o0 仮想コンテナの用意 - Docker

がんばって Docker と docker-compose を覚えてきてほしい  

## Step O2o1o0g4o0 開発環境の確認

VSCode のターミナルで以下のコマンドを叩いていって、あなたのPCと この記事の環境が似ているか確認してほしい  

```shell
python -V
```

`Python 3.9.13`  

```shell
docker --version
```

`Docker version 20.10.10, build b485636`  

```shell
docker-compose -version
```

`docker-compose version 1.29.2, build 5becea4c`  

```shell
# pip を最新に
python -m pip install --upgrade pip
```

## Step O2o1o0g5o0 Pythonパッケージ インストール指定 - requirements.txt ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1                   # あなたの開発用ディレクトリー。任意の名前
👉      └── 📄 requirements.txt
```

```plaintext
# Dockerは2022年時点で Django 4 に対応してないから Django 3 を指定する
Django>=3.0,<4.0

# PostgreSQLへ接続するためのドライバ
psycopg2>=2.8
```

## Step O2o1o0g6o0 ドッカーファイル作成 - Dockerfile ファイル

以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
👉      ├── 🐳 Dockerfile
        └── 📄 requirements.txt
```

```Dockerfile
# See also: https://docs.docker.com/samples/django/

FROM python:3

# Pythonのキャッシュファイル（__pycache__ディレクトリや.pycファイル）を作成するのを止めます
ENV PYTHONDONTWRITEBYTECODE=1

# 出力をPythonでバッファリングせずにターミナルに直接送信します
ENV PYTHONUNBUFFERED=1

# コンテナに /code ディレクトリを作成し、以降、 /code ディレクトリで作業します
WORKDIR /code

# requirements.txtを /code/ ディレクトリへコピーします
ADD requirements.txt /code/

# requirements.txtに従ってpip installします
RUN pip install -r requirements.txt

# 開発環境のファイルを /code/ へコピーします
COPY . /code/
```

## Step O2o1o0g7o0 ドッカーコンポーズファイル作成 - docker-compose.yml ファイル

以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
👉      ├── 🐳docker-compose.yml
        ├── 🐳Dockerfile
        └── 📄requirements.txt
```

```yaml
version: "3.9"

services:
  # データベース
  db:
    image: postgres
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

  # Djangoアプリ
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000 --settings=project1.settings
    #                                   ------- ----            -----------------
    #                                   1       2               3
    # 1. Dockerコンテナ内のサーバーは localhost ではなく 0.0.0.0 と書く
    # 2. Dockerコンテナ内のWebアプリケーションのポート番号
    # 3. Django設定のPythonモジュール。分からなければ、Djangoの設定ファイル（src1/project1/settings.py）の拡張子抜きのドット区切りと考えればよい
    #                                                                        -----------------
    #    例えばレッスンの最初に project1 プロジェクトを作成したなら、
    #    デフォルトでは project1 プロジェクトの --settings=project1.settings を指定するようハードコーディングされる。
    #    この Django設定 を差し替えたくなったら、ここを変えればよい
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    environment:
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    depends_on:
      - db
```

## Step O2o1o0g8o0 プロジェクト作成 - startproject 管理コマンド

以下の説明は なんとことだか分からないだろうが、自分の頭で考えてほしい  

Django では 設定ファイルを入れるフォルダーを **プロジェクト フォルダー** と呼んでいて、あなたの環境に複数作ることができる。  
使い方は任意で、テスト環境、ステージング環境、本番環境　のように分けてもいいし、分けなくてもいい  

以上で説明を終わる  

あなたの開発用ディレクトリーへ移動してほしい  

```shell
cd src1
```

そして、以下のコマンドを１回だけ叩いてほしい  

```shell
docker-compose run web django-admin.py startproject project1 .
#                                                   -------- -
#                                                   1        2
# 1. 任意のDjangoプロジェクト フォルダー名
# 2. パス。 "." は コマンドを叩いたディレクトリにプロジェクトフォルダーを作る
```

Output:  

```plaintext
Creating src1_web_run ... done
/usr/local/bin/django-admin.py:17: RemovedInDjango40Warning: django-admin.py is deprecated in favor of django-admin.
  warnings.warn(
```

👇 すると、あなたの開発用ディレクトリーの下に、プロジェクト フォルダーと、 manage.py ファイルが自動生成される  

```plaintext
    └── 📂 src1
        ├── 📂 project1
        │   ├── 📄 __init__.py
        │   ├── 📄 asgi.py
        │   ├── 📄 settings.py
        │   ├── 📄 urls.py
        │   └── 📄 wsgi.py
        └── 📄 manage.py
```

## Step O2o1o0g9o0 セキュリティ対策 - SECRET_KEY 変数

プロジェクトを作成した直後には問題がある。だから対応する。  

👇 以下のファイルを作成してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 project1
        │   ├── 📄 __init__.py
        │   ├── 📄 asgi.py
👉      │   ├── 📄 settings_secrets.py
        │   ├── 📄 settings.py
        │   ├── 📄 urls.py
        │   └── 📄 wsgi.py
        ├── 🐳 docker-compose.yml
        ├── 🐳 Dockerfile
        ├── 📄 manage.py
        └── 📄 requirements.txt
```

👇 次に、 `📄 settings.py` から２つの変数を探してテキストを切り取り、`📄 settings_secrets.py` へ貼り付けてほしい  

```plaintext
    └── 📂 src1
        ├── 📂 project1
        │   ├── 📄 __init__.py
        │   ├── 📄 asgi.py
👉      │   ├── 📄 settings_secrets.py   # こっちへ貼り付ける
👉      │   ├── 📄 settings.py           # こっちから切り取る
        │   ├── 📄 urls.py
        │   └── 📄 wsgi.py
        ├── 🐳 docker-compose.yml
        ├── 🐳 Dockerfile
        ├── 📄 manage.py
        └── 📄 requirements.txt
```

```py
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<シークレット>'
```

```py
ALLOWED_HOSTS = []
```

👇 以下のファイルが無ければ新規作成、あれば編集してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets.py
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
👉  └── 📄 .gitignore
```

👇 例えば、 `📄 .gitignore` の冒頭あたりにでも 追加してほしい  

```plaintext
# Django practice
#   |
#   +-- Secret
src1/project1/settings_secrets.py
src1/project2/settings_secrets.py
```

👇 以下のファイルを編集してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets.py
👉  │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

👇 冒頭のあたりにでも追加してほしい  

```py
from .settings_secrets import SECRET_KEY, ALLOWED_HOSTS
#    -----------------        -------------------------
#    1                        2
# 1. `src1/project1/settings_secrets.py` を指しています
#                   ----------------
# 2. このファイル内では使われていませんが、このファイルを使う側から使われます
```

👇 以下のファイルを新規作成してほしい

```plaintext
    ├── 📂 src1
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
👉  │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings_secrets.py
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

```plaintxt
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<シークレット>'

ALLOWED_HOSTS = []
#               --
#               1
# 1. 例えば レンタルサーバーを借りたときなどは、ここに IPアドレス や ホスト名 を入れないと、外部からWebサイトが見れないだろう
```

## Step O2o1o0g9o1o0 プロジェクト名の一般化

## Step O2o1o0g9o1o1o0 asgi.py

👇 以下のファイルを編集してほしい

```plaintext
    ├── 📂 src1
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
👉  │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings_secrets.py
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

```py
# ...略... import文など


# vvvv 追加ここから
# O2o1o0g9o1o1o0 プロジェクト名の一般化
from .settings import PROJECT_NAME
#    ]--------        ------------
#    12               3
# 1. 同じディレクトリー
# 2. `src1/projectN/settings.py`
#                   --------
# 3. 変数

# * 変更前
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')
# * O2o1o0g9o1o1o0 プロジェクト名の一般化
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{PROJECT_NAME}.settings')
#                                                 -----------------------
#                                                 1
# 1. 設定モジュール名 `src1/projectN/settings.py`
#                         -----------------
# ^^^^ 追加ここまで


# ...略... application変数の設定など
```

## Step O2o1o0g9o1o2o_9o0 settings.py

👇 以下のファイルを編集してほしい

```plaintext
    ├── 📂 src1
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings_secrets.py
👉  │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

```py
# ...略...


# * 変更前
# WSGI_APPLICATION = 'project1.wsgi.application'
# * O2o1o0g9o1o2o_9o0 プロジェクト名の一般化
WSGI_APPLICATION = f'{PROJECT_NAME}.wsgi.application'
#                    -------------------------------
#                    1
# 1. DjangoのWSGI設定の大元となるグローバル変数。
#    `src1/projectN/wsgi.py` ファイルの中の application 変数を指している
#          -------------


# ...略...
```

## Step O2o1o0g9o1o2o0 urls.py

## Step O2o1o0g9o1o3o0 wsgi.py

👇 以下のファイルを編集してほしい

```plaintext
    ├── 📂 src1
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings_secrets.py
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls.py
👉  │   │   └── 📄 wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

```py
# ...略...


# O2o1o0g9o1o3o0 プロジェクト名の一般化
from .settings import PROJECT_NAME
#    ]--------        ------------
#    12               3
# 1. 同じディレクトリー
# 2. `src1/projectN/settings.py`
#                   --------
# 3. 変数


# ...略...


# * 変更前
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')
# * 変更後
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{PROJECT_NAME}.settings')
#                                                 -----------------------
#                                                 1
# 1. 設定モジュール名 `src1/projectN/settings.py`
#                         -----------------


# ...略...
```

## Step O2o1o0gA10o0 コメント - manage.py ファイル

👇 以下のファイルに、コメントを書き入れてもいいし、書き入れなくてもよい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings_secrets.py
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
👉  │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

```py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')
    #                                                -----------------
    #                                                1
    # 1. Django設定のPythonモジュール。分からなければ、Djangoの設定ファイル（src1/project1/settings.py）の拡張子抜きのドット区切りと考えればよい
    #                                                                        -----------------
    #    例えばレッスンの最初に project1 プロジェクトを作成したなら、
    #    デフォルトでは project1 プロジェクトの settings.py ファイルを指定するようハードコーディングされる。
    #    コマンドライン引数で設定ファイルを指定できるので、ここを編集する必要はない
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

## Step O2o1o0gA11o0 コメント - urls.py ファイル

👇 以下のファイルに、コメントを書き入れてもいいし、書き入れなくてもよい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings_secrets.py
    │   │   ├── 📄 settings.py
👉  │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

```py
"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # 最初から Django の管理画面は用意されている
    path('admin/', admin.site.urls),
    #     ------   ---------------
    #     1        2
    # 1. 例えば `http://example.com/admin/` のような URLのパスの部分
    #                              -------
    # 2. 例えば `http://example.com/admin/login/?next=/admin/` のように admin.site.urls モジュールに含まれる urlpatterns を `1.` にぶら下げる
    #                                    --------------------
    #
    # もしあなたが、あとで Django アプリケーションを作ったなら、以下のように追加することになるだろう
    # path('', include('app1.urls')),
    #      --           ---------
    #      1            2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `src1/app1/urls.py` の urlpatterns を `1.` にぶら下げる
    #          ---------
]
```

## Step O2o1o0gA12o0 設定変更 - settings.py ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings_secrets.py
👉  │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

### import

👇 冒頭のあたりに追加  

```py
import os


# ...略...
```

### PROJECT_NAME

👇 BASE_DIR の設定の下あたりに追加  

```py
# ...略...


# プロジェクト名を親ディレクトリー名から取得
PROJECT_NAME = os.path.basename(Path(__file__).resolve().parent)
print(f"PROJECT_NAME:{PROJECT_NAME}")


# ...略...
```

### ROOT_URLCONF

```py
# ...略...


# * 変更前
# ROOT_URLCONF = 'project1.urls'
# * 変更後
ROOT_URLCONF = f'{PROJECT_NAME}.urls'


# ...略...
```

### DATABASES

👇 探して変更してほしい

```py
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# * 変更前
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}
# * 変更後
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

## Step O2o1o0gA13o0 コメント - settings.py ファイル

👇 以下のファイルに、コメントを書き入れてもいいし、書き入れなくてもよい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 project1
    │   │   ├── 📄__init__.py
    │   │   ├── 📄asgi.py
    │   │   ├── 📄settings_secrets_example.txt
    │   │   ├── 📄settings_secrets.py
👉  │   │   ├── 📄settings.py
    │   │   ├── 📄urls.py
    │   │   └── 📄wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

👇 抜粋  

```py
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#                        ------------------------
#                        1
# 1. 例えば `src1/project1/settings.py` ファイルから見て
#    .resolve()               は `code/project1/settings.py` （`src1` は見えず `code` に差し変わっている）
#    .resolve().parent        は `code/project1/`
#    .resolve().parent.parent は `code/`
#    となっていて、つまり BASE_DIR は あなたの開発用ディレクトリーを指している
```

```py
ROOT_URLCONF = f'{PROJECT_NAME}.urls'
#                -------------------
#                1
# 1. DjangoのURL設定の大元となるPythonモジュール。
#    `src1/project1/urls.py` を指している
#          -------------
```

## Step O2o1o0gA14o0 コメント - settings_secrets.py ファイル

👇 以下のファイルに、コメントを書き入れてもいいし、書き入れなくてもよい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
👉  │   │   ├── 📄 settings_secrets.py
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

```py
ALLOWED_HOSTS = []
#               --
#               1
# 1. 例えば レンタルサーバーを借りたときなどは、ここに IPアドレス や ホスト名 を入れないと、外部からWebサイトが見れないだろう
```

## Step O2o1o0gA15o0 ギット設定 - .gitignore ファイル

👇 （もしgitを使っているなら）以下のファイルを編集してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings_secrets.py
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
👉  └── 📄 .gitignore
```

👇 例えば、冒頭あたりにでも 追加してほしい  

```plaintext
# Django practice
#   |
#   +-- Winmerge
*.bak
#   |
#   +-- Database
src1/data/db
```

## Step O2o1o0gA16o0 ドッカーコンテナ起動 - docker-compose コマンド

👇 以下のコマンドを叩いてほしい  

```shell
docker-compose up
```

👇 このとき、以下の巨大なフォルダーが作成される  

```plaintext
    ├── 📂 src1
    │   ├── 📂 data
    │   │   └── 📂 db
👉  │   │       └── （たくさんのもの）
    │   ├── 📂 project1
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings_secrets.py
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 🐳 docker-compose.yml
    │   ├── 🐳 Dockerfile
    │   ├── 📄 manage.py
    │   └── 📄 requirements.txt
    └── 📄 .gitignore
```

## Step O2o1o0gA17o0 Webページへアクセス

次に、ブラウザで以下のURLにアクセスしてほしい  

[http://localhost:8000](http://localhost:8000)  

これで、ロケットが飛んでいるページが出てくれば　インストールは完了だ。  
`[Ctrl]+[C]` キーでWebサーバーを停めることができる  

## Step O2o1o0gA18o0 Dockerコンテナの停止の練習

Dockerコンテナの停止の練習をしてほしい。そんなん知ってるという人はパスして構わない  

例えば 何を言っているか分からないかもしれないが、  
ターミナルのフォアグラウンドで動いていれば `[Ctrl] + [C]` キーを打鍵したり、  
ターミナルのバックグラウンドで動いていれば `docker-compose down` コマンドを打鍵するといいだろう  

# 次の記事

📖 [Djangoの本番環境のプロジェクトの作り方を予習しよう！](https://qiita.com/muzudho1/items/e9b8c1cefa5ddaa21ab2)  

# 参考にした記事

📖 [Django: SECRET_KEY を GitHub に晒さない](https://blog.kyanny.me/entry/2021/01/27/032342)  
