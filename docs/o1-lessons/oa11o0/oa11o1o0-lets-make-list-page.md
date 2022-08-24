# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/v1/prefectures/)  

# 目標

サーバー側に記憶したデータを一覧したい  

## 詳細

表示例:  

```plaintext
一覧表示
主キー  連番  名前
------  ----  ----
1       1     東京
2       2     大阪
3       3     愛知
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

参考にした元記事は 📖[DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92) だ。  
わたしの記事は単に **やってみた** ぐらいの位置づけだ  

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   ├── 📂 accounts_vol1o0        # アプリケーション
    │   │   ├── 📂 portal_v1                    # アプリケーション
    │   │   │   ├── 📂 data
    │   │   │   ├── 📂 migrations
    │   │   │   ├── 📂 static
    │   │   │   ├── 📂 templates
    │   │   │   └── 📂 views
    │   │   └── 📂 practice_v1                  # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       ├── 📂 templates
    │   │       ├── 📂 views
    │   │       ├── 📄 __init__.py
    │   │       ├── 📄 admin.py
    │   │       ├── 📄 apps.py
    │   │       └── 📄 tests.py
    │   ├── 📂 data
    │   ├── 📂 project1                         # プロジェクト
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_accounts_vol1o0.py
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

## Step OA11o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA11o1o0g2o0 画面作成 - list.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 prefecture           # ただのフォルダー
                            └── 📂 v1o0             # ただのフォルダー
👉                              └── 📄 list.html
```

```html
{# OA11o1o0g2o0 #}
<!-- -->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<!-- See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92 -->
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <!-- 覚えなくていい : Bootstrap -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <!--                                                ===================
                                                            1
            1. Example: `http://example.com/static/favicon.ico`
                                            ==================
        -->
        <title>都道府県の一覧</title>
    </head>
    <body>
        <div class="container">
            <h3>都道府県の一覧</h3>

            <table class="table table-striped table-bordered">
                <thead>
                    <tr>
                        <th>主キー</th>
                        <th>連番</th>
                        <th>名前</th>
                    </tr>
                </thead>
                <tbody>
                    {% for prefecture in prefectures %}
                    <tr>
                        <td>{{ prefecture.pk }}</td>
                        <td>{{ prefecture.seq }}</td>
                        <td>{{ prefecture.name }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>

        <!-- 覚えなくていい : jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- 覚えなくていい : Include all compiled plugins (below), or include individual files as needed -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
</html>
```

## Step OA11o1o0g3o0 ビュー作成 - v_list.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 prefecture
                │           └── 📂 v1o0
                │               └── 📄 list.html
                └── 📂 views
                    └── 📂 prefecture               # ただのフォルダー
                        └── 📂 v1o0                 # ただのフォルダー
👉                          └── 📄 v_list.py
```

```py
# BOF OA11o1o0g3o0

from django.shortcuts import render

# 都道府県モデル
from apps1.practice_v1.models.prefecture.v1o0 import Prefecture
#          -----------                   ----        ----------
#          11                            12          2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_list(request):
    """OA11o1o0g3o0 一覧画面の描画"""

    # Template path
    prefecture_list_tp = 'practice_v1/prefecture/v1o0/list.html'
    #                     -------------------------------------
    #                     1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/prefecture/v1o0/list.html` を取得
    #                                      -------------------------------------

    context = {
        'prefectures': Prefecture.objects.all().order_by('pk'),  # pk順にメンバーを全部取得
    }
    return render(request, prefecture_list_tp, context)

# EOF OA11o1o0g3o0
```

## Step OA11o1o0g4o0 ビュー作成 - prefecture モジュール

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 prefecture
                │           └── 📂 v1o0
                │               └── 📄 list.html
                └── 📂 views
                    └── 📂 prefecture
                        └── 📂 v1o0
👉                          ├── 📄 __init__.py
                            └── 📄 v_list.py
```

```py
class PrefectureV(object):
    """OA11o1o0g4o0 都道府県のビュー"""

    # OA11o1o0g4o0 一覧
    from .v_list import render_list
```

## ~~Step OA11o1o0g5o0~~

Merged to OA11o1o0g5o1o0  

## Step OA11o1o0g5o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_v1                      # アプリケーション
    │           ├── 📂 templates
    │           │   └── 📂 practice_v1
    │           │       └── 📂 prefecture
    │           │           └── 📂 v1o0
    │           │               └── 📄 list.html
    │           └── 📂 views
    │               └── 📂 prefecture
    │                   └── 📂 v1o0
    │                       ├── 📄 __init__.py
    │                       └── 📄 v_list.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_vol1o0_autogen.py,practice/v1/prefectures/,practice_v1_prefectures,"OA11o1o0g5o1o0 都道府県",apps1.practice_v1.views.prefecture.v1o0,PrefectureV,,render_list
```

## Step OA11o1o0g5o2o0 ルート編集 - コマンド打鍵

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

## Step OA11o1o0g6o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/prefectures/](http://localhost:8000/practice/v1/prefectures/)  

## Step OA11o1o0g7o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 prefecture
        │       │           └── 📂 v1o0
        │       │               └── 📄 list.html
        │       └── 📂 views
        │           └── 📂 prefecture
        │               └── 📂 v1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_list.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/prefectures/,都道府県の一覧
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでモデルのインスタンスの読取ページを作成しよう！](https://qiita.com/muzudho1/items/ae362f53a670e265a7e4)  
