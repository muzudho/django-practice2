# 目標

シナリオ:  

Djangoサーバーのデータベースが壊れてしまった。  
プログラムは残っている  

アクション:  

データが初期状態から Djangoサーバーを再開できるようにしたい  

## 詳細

シナリオ:  

既存のデータベースはフォルダーごと削除し、初期状態のデータベースを自動生成した。  
しかし Django フレームワークはエラーを起こし、サーバーが起動しないようだ。  
その原因としては、  
allauthなど、他のDjangoサーバーのアプリケーションを混ぜると、データベースを１から作り直すだけでは  
再開できないケースが出てくるのかもしれないが、よくわからない  

アクション:  

なんだかよくわからないが、やってみて直ったケースを　逐一　覚えていくことにする  

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
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   └── 📂 practice_vol1o0              # アプリケーション
    │   ├── 📂 data
    │   ├── 📂 project1                     # プロジェクト
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

# 手順

## Step [O7o1o0g1o0] バックアップを残しておけ

関連するすべてのフォルダーまるごと、 **バックアップを残しておけ**  

このレッスンは　異常時からの復旧の練習だ。  
データを損失するし、復旧できるとも限らない  

## Step [O7o1o0g2o0] Dockerコンテナ停止

Dockerコンテナが動いていれば、停止させてほしい  

## Step [O7o1o0g3o0] data フォルダーを消そう

👇 以下のフォルダーを消してほしい。 Webサイトのデータが全部飛ぶ  

```plaintext
    └── 📂 src1
👉      └── 📂 data
```

## Step [O7o1o0g4o0] Dockerコンテナの起動

👇 Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
# cd src1

# Docker コンテナ起動
docker-compose up
```

## Step [O7o1o0g5o0] コマンドの打鍵 - migrate

👇 以下のコマンドを打鍵してほしい。何をやっているかは分からない  

```shell
docker-compose run --rm web python3 manage.py migrate sites
docker-compose run --rm web python3 manage.py migrate
```

（マイグレーションをしているのは分かるが、何でこうなるのか　よく分からない）  

## Step [O7o1o0g6o0] Webページへアクセス

📖 [http://localhost:8000/accounts/vol1.0/signup/](http://localhost:8000/accounts/vol1.0/signup/)  

👆 allauth など、正常に動いているか　確認してほしい。  
もし動いていなければ Webサイト は破壊してしまった。 連載を１からやり直してほしい  

## Step [O7o1o0g7o0] やりなおし

今までにデータベースに登録した内容は消えているので、連載をやり直してほしい  

* Super-user の作成

# 次の記事

📖 [Djangoでサインイン（利用開始）のページを作ろう！](https://qiita.com/muzudho1/items/1d34d64562ff07f1742a)  

# 参考にした記事

📖 [Django: relation "django_site" does not exist](https://stackoverflow.com/questions/23925726/django-relation-django-site-does-not-exist)  
