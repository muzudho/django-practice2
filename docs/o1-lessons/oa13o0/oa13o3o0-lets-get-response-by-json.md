# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1.0/vuetify/desserts1-as-json/ver1.0/)  

# 目標

サーバーからデータをJSON形式で受信したい  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is     | This is                                   |
| ----------- | ----------------------------------------- |
| OS          | Windows10                                 |
| Container   | Docker                                    |
| Auth        | allauth                                   |
| Frontend    | Vuetify                                   |
| Data format | JSON                                      |
| Editor      | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   ├── 📂 accounts_vol1o0    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   └── 📂 practice_vol1o0              # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       │   └── 📂 practice_vol1o0
    │   │       │       └── 📂 data
    │   │       │           └── 📂 desserts1
    │   │       │               └── 📄 ver1o0.json
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_vol1o0          # アプリケーションと同名
    │   │       │       ├── 📂 prefecture
    │   │       │       └── 📂 vuetifies
    │   │       ├── 📂 views
    │   │       │   ├── 📂 prefecture
    │   │       │   └── 📂 vuetifies
    │   │       ├── 📄 __init__.py
    │   │       ├── 📄 admin.py
    │   │       ├── 📄 apps.py
    │   │       └── 📄 tests.py
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_accounts_vol1o0.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2                  # プロジェクト
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

## Step OA13o3o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA13o3o0g2o0 データの再利用 - desserts.json ファイル

👇 以下の記事で掲載した JSON ファイルを再利用してほしい  

* 📖 [Django のビューの Python スクリプトで JSON ファイルを読み込んで HTML に埋め込んでいる JavaScript にデータを渡そう！](https://qiita.com/muzudho1/items/b3b0c25fc329eb9bc0c1)

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                └── 📂 static
                    └── 📂 practice_vol1o0              # アプリケーションと同名
                        └── 📂 data
                            └── 📂 desserts1
👉                              └── 📄 ver1o0.json
```

## Step OA13o3o0g3o0 ビュー編集 - vuetifies/desserts1_as_json/ver1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_vol1o0
                │       └── 📂 data
                │           └── 📂 desserts1
                │               └── 📄 ver1o0.json
                └── 📂 views
                    └── 📂 vuetifies
                        └── 📂 desserts1_as_json
👉                          └── 📄 ver1o0.py
```

```py
# BOF OA13o3o0g3o0

import json
from django.http import JsonResponse


def render_desserts1_as_json(request):
    """OA13o3o0g3o0 JSON形式でデザート１描画"""

    with open('apps1/practice_vol1o0/static/practice_vol1o0/data/desserts1/ver1o0.json', mode='r', encoding='utf-8') as f:
        #      -----------------------------------------------------------------------
        #      1
        # 1. `src1/apps1/practice_vol1o0/static/practice_vol1o0/data/desserts1/ver1o0.json` を取得
        #          -----------------------------------------------------------------------
        doc = json.load(f)

    return JsonResponse(doc)

# EOF OA13o3o0g3o0
```

## Step OA13o3o0g4o0 ビュー編集 - VuetifyV モジュール

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_vol1o0
                │       └── 📂 data
                │           └── 📂 desserts1
                │               └── 📄 ver1o0.json
                └── 📂 views
                    └── 📂 vuetifies
                        ├── 📂 desserts1_as_json
                        │   └── 📄 ver1o0.py
👉                      └── 📄 __init__.py
```

```py
class VuetifyV(object):
    """OA12o1o0g4o0 ビューティファイの練習のビュー"""


    # ..略..


    # * 以下を追加
    # OA13o3o0g4o0 JSONでデザート１
    from .desserts1_as_json.ver1o0 import render_desserts1_as_json
```

## ~~Step OA13o3o0g5o0~~

Merged to OA13o3o0g5o1o0

## Step OA13o3o0g5o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_vol1o0                  # アプリケーション
    │           ├── 📂 static
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 data
    │           │           └── 📂 desserts1
    │           │               └── 📄 ver1o0.json
    │           └── 📂 views
    │               └── 📂 vuetifies
    │                   ├── 📂 desserts1_as_json
    │                   │   └── 📄 ver1o0.py
    │                   └── 📄 __init__.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/vuetify/desserts1-as-json/ver1.0/,,"OA13o3o0g5o1o0 練習1.0巻 ビューティファイでJSON形式のデザート１ 1.0版",apps1.practice_vol1o0.views.vuetifies,VuetifyV,,render_desserts1_as_json
```

## Step OA13o3o0g5o2o0 ルート編集 - コマンド打鍵

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

## Step OA13o3o0g6o0 Web画面へアクセス

📖 [http://localhost:8000/practice/vol1.0/vuetify/desserts1-as-json/ver1.0/](http://localhost:8000/practice/vol1.0/vuetify/desserts1-as-json/ver1.0/)  

## Step OA13o3o0g7o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_vol1o0                  # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 data
        │       │           └── 📂 desserts1
        │       │               └── 📄 ver1o0.json
        │       └── 📂 views
        │           └── 📂 vuetifies
        │               ├── 📂 desserts1_as_json
        │               │   └── 📄 ver1o0.py
        │               └── 📄 __init__.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/vol1.0/vuetify/desserts1-as-json/ver1.0/,OA13o3o0g7o0 練習1.0巻 ビューティファイでJSON形式のデザート１ 1.0版
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DjangoでデータをサーバーへJSON形式で渡して、記憶させよう！](https://qiita.com/muzudho1/items/ed0ea262aaa327a2d12b)  
