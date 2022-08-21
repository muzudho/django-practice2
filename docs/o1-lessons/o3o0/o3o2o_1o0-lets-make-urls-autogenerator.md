# 目標

URLの設定はめんどうだ。自動化しよう  

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
    │   │   └── 📂 practice_v1              # アプリケーション名
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1
    │   │       │       └── 📂 page_the_hello
    │   │       │           └── 📄 v1o0.html
    │   │       └── 📂 views
    │   │           └── 📂 page_the_hello
    │   │               └── 📂 v1o0
    │   │                   └── 📄 __init__.py
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト名
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets.py
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

## Step. Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step o3o2o_1o0g1o0 データ作成 - src1_meta/data/urls.csv ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1     # 既存
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
file,path,name,comment,module,class,alias,method
../src1/project1/urls_practice_autogen.py,practice/v1/page-the-hello,page_the_hello,"O3o1o0gA10o0 こんにちわページ",apps1.practice_v1.views.page_the_hello.v1o0,PageTheHello,,render
```

## Step o3o2o_1o0g2o0 スクリプト作成 - src1_meta/scripts/auto_generators/urls.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1     # 既存
    └── 📂 src1_meta
        ├── 📂 data
        │   └── 📄 urls.csv
        └── 📂 scripts
            └── 📂 auto_generators
                └── 📄 urls.py
```

```py
```


```shell
# ディレクトリーを移動してほしい
# cd src1_meta

python -m scripts.auto_generators.urls
```
