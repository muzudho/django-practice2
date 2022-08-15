Git を使ってソースをデプロイする方法を説明する  

# はじめに

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

# 用語解説

* `レポジトリ` - ソースを置いているディレクトリー

# 本題に入る前に

Git Hub にレポジトリを作っておいてほしい  

# git をインストールする

📖 [1.5 使い始める - Gitのインストール](https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)  

git は Dockerコンテナの外側のOSにインストールしたい  

👇 Ubuntu を使っているときは、以下のコマンドを打鍵してほしい  

```shell
sudo apt-get install git-all
```

# ソースをクローンしたいディレクトリーに移動する

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

# ソースをクローンする

👇 URLは適宜変えてほしい  

```shell
git init

git clone https://github.com/muzudho/django-practice2.git
#         -----------------------------------------------
#         1
# 1. Git Hub の レポジトリのURL
#
# ここまでは1回行うだけでよい

# 2回目以降は、プルしてフェッチ
# git pull https://github.com/muzudho/django-practice2.git
# git fetch https://github.com/muzudho/django-practice2.git
```

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

# パーミッション

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

# 次の記事

📖 [Djangoでゲーム対局部屋のモデルを定義しよう！](https://qiita.com/muzudho1/items/e1cf253dd6929bcd708d)  
