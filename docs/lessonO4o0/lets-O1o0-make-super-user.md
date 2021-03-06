# 目的

Djangoサーバー支配下のすべてのアプリケーションを調整できるユーザー（*1）を作る  

`*1.` - スーパーユーザー  

その際、サーバーの乗っ取りを防ぐため、スーパーユーザーを勝手に作られないようにする  

# 手段

最初のサーバー管理者を作る機能は そのシステムの内部に用意しない。  
最初のサーバー管理者は、そのシステムの外部からコマンドを叩いて作る  

# 練習内容

最初の管理者を作る。  
そして Django の管理画面に入る

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
    │   │   └── 📂 practice_v1              # アプリケーション名
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1
    │   │       │       ├── 📂 o1o0
    │   │       │       │   └── 📄 page_the_hello.html
    │   │       │       │   └── 📄 page_to_be_added.html
    │   │       │       ├── 📂 o2o0
    │   │       │       │   └── 📄 page_to_be_added.html.txt
    │   │       │       └── 📂 o3o0
    │   │       │           └── 📄 page_to_be_added.html.txt
    │   │       └── 📂 views
    │   │           ├── 📂 o1o0
    │   │           │   └── 📂 page_the_hello
    │   │           │       └── 📄 __init__.py
    │   │           ├── 📂 o2o0
    │   │           │   └── 📂 page_to_be_added
    │   │           │       └── 📄 __init__.py
    │   │           └── 📂 o3o0
    │   │               └── 📂 page_to_be_added
    │   │                   └── 📄 __init__.py
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト名
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings.py
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

# Step 2. スーパーユーザーを作るコマンドを用意する

以下のようにディレクトリとファイルを作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1          # 既存のアプリケーション
                └── 📂 management        # ただのフォルダー
                    └── 📂 commands          # ただのフォルダー
👉                      └── 📄 custom_createsuperuser.py
```

```py
# See also: https://jumpyoshim.hatenablog.com/entry/how-to-automate-createsuperuser-on-django
from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


class Command(createsuperuser.Command):
    help = 'Create a superuser with a password non-interactively'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '--password', dest='password', default=None,
            help='Specifies the password for the superuser.',
        )

    def handle(self, *args, **options):
        options.setdefault('interactive', False)
        username = options.get('username')
        email = options.get('email')
        password = options.get('password')
        database = options.get('database')

        if not (username and email and password):
            raise CommandError(
                '--username, --email and --password are required options')

        user_data = {
            'username': username,
            'email': email,
            'password': password,
        }

        exists = self.UserModel._default_manager.db_manager(
            database).filter(username=username).exists()
        if not exists:
            self.UserModel._default_manager.db_manager(
                database).create_superuser(**user_data)
```

# Step 3. 名前，E-mailアドレス，パスワードを考えておけ

スーパーユーザーの名前，スーパーユーザーのE-mailアドレス，スーパーユーザーのパスワードを考えておいてほしい  

忘れっぽければ、以下のファイルにメモ書きしておいてもいいが、そのローカルPCにログインされると見えてしまうので パスワードを保管するソフトの使い方をセキュリティに詳しい人から聞いてほしい  

```plaintext
    ├── 📂 host1
    │   ├── 📂 apps1
    │   │   └── 📂 practice_v1          # 既存のアプリケーション
    │   │       └── 📂 management        # ただのフォルダー
    │   │           └── 📂 commands          # ただのフォルダー
    │   │               └── 📄 custom_createsuperuser.py
👉  │   └── 📄 .env              # このファイルを Git Hub などにプッシュするとサーバーが乗っ取られてしまう原因になるので注意
    └── 📄 .gitignore            # Gitレポジトリに .env ファイルをプッシュしないように設定をここに書いておくこと
```

```shell
# シャープで始まる行はコメント
#
# 以下はただのメモ書き
#
# * `aaaa` - スーパーユーザーの名前
# * `aaaa@example.com` - スーパーユーザーのE-mailアドレス
# * `bbbb` - スーパーユーザーのパスワード
```

# Step 4. スーパーユーザー作成

👇 以下のコマンドを打鍵してほしい。Dockerコンテナの中で動いているサーバーアプリケーションにスーパーユーザーが追加される。タイプミスしないように注意してほしい  

```shell
docker-compose run --rm web python3 manage.py custom_createsuperuser --username <スーパーユーザー名> --email <スーパーユーザーのEmailアドレス> --password <スーパーユーザーのパスワード>
```

👆 恐らく `host1/data` フォルダー下のデータベースに格納され永続的に保存されるのかもしれない。このコマンドを実行するのは１回だけでいいと思う  

# Step 5. Webの管理画面へアクセス

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

👆 Django のアプリケーション作成時に自動生成される urls.py ファイルに最初から `/admin` の設定は書かれているので、URLの設定は要らない  

# 次の記事

📖 [Djangoでポータルページを作成しよう！](https://qiita.com/muzudho1/items/ad2299cf94a9a5b1c254)  

# 参考にした記事

📖 [Django 管理画面の利用](https://python.keicode.com/django/admin-site-enabling.php)  
📖 [【Django】ワンライナーでスーパーユーザーを作成する方法](https://jumpyoshim.hatenablog.com/entry/how-to-automate-createsuperuser-on-django)  

## トラブルシューティング

📖 [【Django】”ProgrammingError: relation “django_session” does not exist・・・”みたいなエラーに怒られたときの対処法](https://yukituna.com/2745/)  
