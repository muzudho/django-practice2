# 目的

本番環境の用意の仕方を予習しておく  

# はじめに

この記事のアーキテクチャ:  

| Key       | Value                                     |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Editor    | Visual Studio Code （以下 VSCode と表記） |
| Database  | PostgreSQL                                |

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
この連載の最初のページ: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1
    │   ├── 📂 data
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

# Step O2o2o0g1o0 Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step O2o2o0g2o0 プロジェクトのコピー - project2 フォルダー

👇 以下のフォルダーをコピー＆ペーストして  

```plaintext
    └── 📂 src1
👉      └── 📂 project1
```

👇 名前を変えたものを作ってほしい  

```plaintext
    └── 📂 src1
        ├── 📂 project1
👉      └── 📂 project2
```

# Step O2o2o0g3o0 設定変更 - settings.py ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 project1
        └── 📂 project2
👉          └── 📄 settings.py
```

👇 抜粋  

```py
# SECURITY WARNING: don't run with debug turned on in production!
#
# * 変更前
# DEBUG = True
# * 変更後
DEBUG = False
```

* `📂 project2` の settings.py などに `project1` という文字が含まれていれば `project2` に変えてほしい

# Step O2o2o0g4o0 設定変更 - settings_secrets.py ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 project1
        └── 📂 project2
👉          ├── 📄 settings_secrets.py
            └── 📄 settings.py
```

👇 抜粋  

```py
# * 変更前
# ALLOWED_HOSTS = []
# * 変更後
ALLOWED_HOSTS = [
    "localhost",
    "127,0,0,1",
    # --------
    # 1
    #
    # 1. 例えば レンタルサーバーを借りたときなどは、ここに IPアドレス や ホスト名 を入れないと、外部からWebサイトが見れないだろう
]
```

# Step O2o2o0g5o0 本番用ドッカーコンポーズ ファイル作成 - docker-compose-project2.yml ファイル

👇 以下のフォルダーをコピー＆ペーストして  

```plaintext
    └── 📂 src1
        ├── 📂 project1
        ├── 📂 project2
        │   ├── 📄 settings_secrets.py
        │   └── 📄 settings.py
👉      └── 🐳 docker-compose.yml
```

👇 名前を変えたものを作ってほしい  

```plaintext
    └── 📂 src1
        ├── 📂 project1
        ├── 📂 project2
        │   ├── 📄 settings_secrets.py
        │   └── 📄 settings.py
        ├── 🐳 docker-compose.yml
👉      └── 🐳 docker-compose-project2.yml
```

# Step O2o2o0g6o0 本番用ドッカーコンポーズ ファイル編集 - docker-compose-project2.yml ファイル

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 project1
        ├── 📂 project2
        │   ├── 📄 settings_secrets.py
        │   └── 📄 settings.py
        ├── 🐳 docker-compose.yml
👉      └── 🐳 docker-compose-project2.yml
```

👇 抜粋  

```yaml
  # Djangoアプリ
  web:


    # ...中略...


    # * 変更前
    # command: python manage.py runserver 0.0.0.0:8000 --settings=project2.settings
    # * 変更後
    command: python manage.py runserver 0.0.0.0:8000 --settings=project2.settings
    #                                                                  ^two
```

# Step O2o2o0g7o0 ドッカーコンテナの停止～起動 - docker-compose コマンド

👇 以下のコマンドを叩いてほしい  

```shell
docker-compose down
```

👇 以下のコマンドを叩いてほしい  

```shell
docker-compose -f docker-compose-project2.yml up
#              ------------------------------
#              1
# 1. ドッカーコンポーズ ファイルを指定
```

# Step O2o2o0g8o0 Webページへアクセス

次に、ブラウザで以下のURLにアクセスしてほしい  

[http://localhost:8000](http://localhost:8000)  

まだ Webページを作っていないので、 `Not Found`, `The requested resource was not found on this server.` と出てくるだろう。  
これで、本番環境のプロジェクトの作り方の練習は完了だ。  
`[Ctrl]+[C]` キーでWebサーバーを停めることができる  

# 次の記事

📖 [DjangoでWebページを追加しよう！](https://qiita.com/muzudho1/items/06fe071c1147b4b8f062)  
