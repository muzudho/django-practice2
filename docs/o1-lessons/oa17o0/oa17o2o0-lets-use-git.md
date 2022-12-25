DjangoとDocker練習[O17o2o0] gitでソースをクローンしよう！

Git を使ってソースをデプロイする方法を説明する  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

# 用語解説

* `レポジトリ` - ソースを置いているディレクトリー

# 手順

## 本題に入る前に

Git Hub にレポジトリを作っておいてほしい  

## git をインストールする

📖 [1.5 使い始める - Gitのインストール](https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)  

git は Dockerコンテナの外側のOSにインストールしたい  

👇 Ubuntu を使っているときは、以下のコマンドを打鍵してほしい  

```shell
sudo apt-get install git-all
```

## ソースをクローンしたいディレクトリーに移動する

👇 例えば 以下の場所にソースを置きたいとする  
ディレクトリーは作成しておいてほしい  

```plaintext
    📂 /
        └── 📂 home
            └── 📂 ubuntu
👉              └── 📂 repos  この中にソースを置きたい
```

```shell
cd /home/ubuntu/repos
```

## ソースをクローンする

URLは適宜変えてほしい  

👇 1回目は、イニシャライズしてクローン  

```shell
git init

git clone https://github.com/muzudho/django-practice2.git
#         -----------------------------------------------
#         1
# 1. Git Hub の レポジトリのURL
#
# ここまでは1回行うだけでよい
```

👇 2回目以降は、プルしてフェッチ（この操作でサーバーが壊れる。あとで説明する）  

```shell
# （慎重）ローカルの変更をすべて破棄したいなら
git restore .

# 取得
git pull https://github.com/muzudho/django-practice2.git
git fetch https://github.com/muzudho/django-practice2.git
```

以下の２つを説明する  

* パーミッションが変わってるかもしれない
* Docker が止まっているかもしれない

これでディレクトリー構成はクローンされる。  
👇 例えば以下のように  

```plaintext
    📂 /
        └── 📂 home
            └── 📂 ubuntu
                └── 📂 repos
                    └── 📂 django-practice2     # レポジトリ
                        ├── 📂 docs
                        ├── 📂 src1
                        ├── 📂 src2_local
                        ├── 📄 .gitignore
                        ├── 📄 LICENSE
                        └── 📄 README.md
```

## fetch したらデータベースが壊れてるかも

👇 マイグレーションすると直るかもしれないが、何をやってるのか　さっぱり分からない  

```shell
docker-compose run --rm web python3 manage.py migrate sites
docker-compose run --rm web python3 manage.py migrate
```

## パーミッション

Windows に無くて Linux に有るのが ファイルのパーミッション。  
👇 確認してほしい  

Input:  

```shell
ll
```

Output:  

```plaintext
total 12
drwxrwxr-x 3 ubuntu ubuntu 4096 Aug 14 20:05 ./
drwxr-xr-x 7 ubuntu ubuntu 4096 Aug 14 20:05 ../
drwxrwxr-x 6 ubuntu ubuntu 4096 Aug 14 20:05 django-practice2/
```

さくらのVPS を借りると ubuntu というユーザーだったので、そうする  

```shell
# 指定のフォルダー以下のすべてのファイル、ディレクトリーのパーミッションの変更（上書き）の例
sudo chown -R ubuntu:ubuntu django-practice2
# サーバーのパスワードを入力
```

👇 docker-compose は ルート権限で実行しないといけないかもしれない  

```
sudo docker-compose up
```

## DEBUG フラグ

* settings.py の DEBUGフラグは下げてほしい

## .env ファイルをアプロードしてほしい

このファイルの内容は秘密にすること  

```plaintext
    📂 /
        └── 📂 home
            └── 📂 ubuntu
                └── 📂 repos
                    └── 📂 django-practice2     # レポジトリ
                        ├── 📂 docs
                        ├── 📂 src1
                        ├── 📂 src2_local
👉                      ├── 📄 .env
                        ├── 📄 .gitignore
                        ├── 📄 LICENSE
                        └── 📄 README.md
```

# 次の記事

* 📖 [[OA17o3o0] さくらのVPS 備忘録](https://qiita.com/muzudho1/items/c34c8cf93a091e25cc59)
