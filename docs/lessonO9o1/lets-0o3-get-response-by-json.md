# 目的

サーバーからデータをJSON形式で受信したい  

# はじめに

この記事は LessonO2o1 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key         | Value                                     |
| ----------- | ----------------------------------------- |
| OS          | Windows10                                 |
| Container   | Docker                                    |
| Auth        | allauth                                   |
| Frontend    | Vuetify                                   |
| Data format | JSON                                      |
| Editor      | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 host1
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   └── 📂 practice_v1              # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       │   └── 📂 practice_v1
    │   │       │       └── 📂 o2o1
    │   │       │           └── 📂 data
    │   │       │               └── 📄 desserts1.json
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1          # アプリケーションと同名
    │   │       │       └── 📂 o2o1
    │   │       │           ├── 📂 prefecture
    │   │       │           └── 📂 vuetify
    │   │       │               ├── 📄 textarea1_base.html
    │   │       │               └── 📄 desserts1.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 o2o1
    │   │       │       ├── 📂 prefecture
    │   │       │       └── 📂 vuetify
    │   │       │           ├── 📄 __init__.py
    │   │       │           └── 📄 v_textarea1.py
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
    │   │   ├── 📄 urls_accounts.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2                  # プロジェクト
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

# Step 2. データの再利用 - desserts.json ファイル

👇 以下の記事で掲載した JSON ファイルを再利用してほしい  

* 📖 [Django のビューの Python スクリプトで JSON ファイルを読み込んで HTML に埋め込んでいる JavaScript にデータを渡そう！](https://qiita.com/muzudho1/items/b3b0c25fc329eb9bc0c1)

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 static
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 o2o1
                            └── 📂 data
👉                              └── 📄 desserts1.json
```

# Step 3. ビュー編集 - v_desserts1_as_json.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 o2o1
                │           └── 📂 data
                │               └── 📄 desserts1.json
                └── 📂 views
                    └── 📂 o2o1
                        └── 📂 vuetify
👉                          └── 📄 v_desserts1_as_json.py
```

```py
import json
from django.http import JsonResponse


def render_desserts1_as_json(request):
    """JSON形式でデザート１描画"""

    with open('apps1/practice_v1/static/practice_v1/o2o1/data/desserts1.json', mode='r', encoding='utf-8') as f:
        #      -------------------------------------------------------------
        #      1
        # 1. `host1/apps1/practice_v1/static/practice_v1/o2o1/data/desserts1.json` を取得
        #           -------------------------------------------------------------
        doc = json.load(f)

    return JsonResponse(doc)
```

# Step 4. ビュー編集 - VuetifyV モジュール

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 o2o1
                │           └── 📂 data
                │               └── 📄 desserts1.json
                └── 📂 views
                    └── 📂 o2o1
                        └── 📂 vuetify
👉                          ├── 📄 __init__.py
                            └── 📄 v_desserts1_as_json.py
```

```py
class VuetifyV(object):
    """ビューティファイの練習のビュー"""

    # ..略..


    # 以下を追加
    from .v_desserts1_as_json import render_desserts1_as_json
```

# Step 5. ルート編集 - urls.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o2o1
        │       │           └── 📂 data
        │       │               └── 📄 desserts1.json
        │       └── 📂 views
        │           └── 📂 o2o1
        │               └── 📂 vuetify
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_desserts1_as_json.py
        └── 📂 project1                          # プロジェクト
👉          ├── 📄 urls_practice.py              # こちら
❌          └── 📄 urls.py                       # これではない
```

```py
from django.urls import path


# ...略...


# 都道府県ビュー
from apps1.practice_v1.views.o2o1.vuetify import VuetifyV
#          -----------            -------        --------
#          11                     12             2
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [


    # ...略...


    # ビューティファイでJSON形式のデザート１
    path('practice/v1/vuetify/desserts1-as-json',
         # ------------------------------------
         # 1
         VuetifyV.render_desserts1_as_json, name='practice_v1_vuetify_desserts1_as_json'),
    #    ---------------------------------        -------------------------------------
    #    2                                        3
    # 1. 例えば `http://example.com/practice/v1/vuetify/desserts1-as-json` のような URL のパスの部分
    #                              -------------------------------------
    # 2. VuetifyV クラスの render_desserts1_as_json 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_vuetify_desserts1_as_json' %} のような形でURLを取得するのに使える
]
```

# Step 6. Web画面へアクセス

📖 [http://localhost:8000/practice/v1/vuetify/desserts1-as-json](http://localhost:8000/practice/v1/vuetify/desserts1-as-json)  

# Step 7. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o2o1
        │       │           └── 📂 data
        │       │               └── 📄 desserts1.json
        │       └── 📂 views
        │           └── 📂 o2o1
        │               └── 📂 vuetify
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_desserts1_as_json.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/vuetify/desserts1-as-json,ビューティファイでJSON形式のデザート１
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DjangoでデータをサーバーへJSON形式で渡して、記憶させよう！](https://qiita.com/muzudho1/items/ed0ea262aaa327a2d12b)  
