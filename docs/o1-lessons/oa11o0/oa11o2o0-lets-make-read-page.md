# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1.0/prefectures/read/ver1.0/1/)  

# 目標

（※いわゆる CRUD の R）  

`http://localhost:8000/prefectures/read/1/` へアクセスすると、  
pk が 1 の都道府県を表示したい  

## 詳細

表示例:  

```plaintext
都道府県の詳細情報

連番
1

名前
東京
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
    │   │   └── 📂 practice_vol1o0                  # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_vol1o0          # アプリケーションと同名
    │   │       │       └── 📂 prefecture
    │   │       │           └── 📂 ver1o0
    │   │       │               └── 📄 list.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 prefecture
    │   │       │       └── 📂 ver1o0
    │   │       │           ├── 📄 __init__.py
    │   │       │           └── 📄 v_list.py
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

## Step [OA11o2o0g1o0] Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step [OA11o2o0g2o0] 画面作成 - read.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                      # アプリケーション
                └── 📂 templates
                    └── 📂 practice_vol1o0              # アプリケーションと同名
                        └── 📂 prefecture           # ただのフォルダー
                            └── 📂 ver1o0             # ただのフォルダー
👉                              └── 📄 read.html
```

```html
<!-- BOF OA11o2o0g2o0 -->
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
        <title>都道府県の詳細</title>
    </head>
    <body>
        <div class="container">
            <h3>都道府県の詳細</h3>
            <div class="card" style="width: 18rem">
                <div class="card-body">
                    <h5 class="card-title">主キー</h5>
                    <p class="card-text">{{ prefecture.pk }}</p>
                </div>
                <div class="card-body">
                    <h5 class="card-title">連番</h5>
                    <p class="card-text">{{ prefecture.seq }}</p>
                </div>
                <div class="card-body">
                    <h5 class="card-title">名前</h5>
                    <p class="card-text">{{ prefecture.name }}</p>
                </div>
            </div>
            <a href="{% url 'practice_vol1o0_prefectures' %}" class="btn btn-default btn-sm">戻る</a>
        </div>
        <!-- 覚えなくていい : jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- 覚えなくていい : Include all compiled plugins (below), or include individual files as needed -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
</html>
<!-- EOF OA11o2o0g2o0 -->
```

## Step [OA11o2o0g3o0] ビュー作成- v_read.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                      # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_vol1o0              # アプリケーションと同名
                │       └── 📂 prefecture
                │           └── 📂 ver1o0
                │               └── 📄 read.html
                └── 📂 views
                    └── 📂 prefecture               # ただのフォルダー
                        └── 📂 ver1o0                 # ただのフォルダー
👉                          └── 📄 v_read.py
```

```py
# BOF OA11o2o0g3o0

from django.shortcuts import render, get_object_or_404

# 練習1.0巻 都道府県モデル1.0版
from apps1.practice_vol1o0.models.prefecture.ver1o0 import Prefecture
#          ---------------                   ------        ----------
#          11                                12            2
#    ----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_read(request, id=id):
    """OA11o2o0g3o0 詳細画面の描画

    Parameters
    ----------
    request : object
        リクエスト
    id : str
        URLのGETストリングの ?id= の値
    """

    # Template path
    prefecture_read_tp = 'practice_vol1o0/prefecture/ver1o0/read.html'
    #                     -------------------------------------------
    #                     1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/prefecture/ver1o0/read.html` を取得
    #                                          -------------------------------------------

    # GETストリングのidと、Prefectureテーブルのpkが一致するものを取得。無ければ 404 画面へ飛ぶ
    prefecture = get_object_or_404(Prefecture, pk=id)
    # * 以下の書き方だと、 404 画面に飛ばない
    # prefecture = Prefecture.objects.get(pk=id)

    context = {
        'prefecture': prefecture,
    }
    return render(request, prefecture_read_tp, context)

# EOF OA11o2o0g3o0
```

## Step [OA11o2o0g4o0] ビュー編集 - prefecture モジュール

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                      # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 o1o0
                │           └── 📂 prefecture
                │               └── 📄 read.html
                └── 📂 views
                    └── 📂 prefecture
                        └── 📂 ver1o0
👉                          ├── 📄 __init__.py
                            └── 📄 v_read.py
```

```py
class PrefectureV(object):
    """OA11o1o0g4o0 都道府県のビュー"""


    # ...略...


    # * 以下を追加
    # OA11o2o0g4o0 詳細
    from .v_read import render_read
```

## ~~Step [OA11o2o0g5o0]~~

Merged to OA11o2o0g5o1o0  

## Step [OA11o2o0g5o1o0] ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_vol1o0                      # アプリケーション
    │           ├── 📂 templates
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 prefecture
    │           │           └── 📂 ver1o0
    │           │               └── 📄 read.html
    │           └── 📂 views
    │               └── 📂 prefecture
    │                   └── 📂 ver1o0
    │                       ├── 📄 __init__.py
    │                       └── 📄 v_read.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/prefectures/read/ver1.0/<int:id>/,practice_vol1o0_prefectures_read,"OA11o2o0g5o1o0 練習1.0巻 都道府県の詳細1.0版",apps1.practice_vol1o0.views.prefecture.ver1o0,PrefectureV,,render_read
```

## Step [OA11o2o0g5o2o0] ルート編集 - コマンド打鍵

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

## Step [OA11o2o0g6o0] Web画面へアクセス

📖 [http://localhost:8000/practice/vol1.0/prefectures/read/ver1.0/1/](http://localhost:8000/practice/vol1.0/prefectures/read/ver1.0/1/)  

## Step [OA11o2o0g7o0] ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_vol1o0                      # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 o1o0
        │       │           └── 📂 prefecture
        │       │               └── 📄 read.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 prefecture
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_read.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/vol1.0/prefectures/read/ver1.0/1/,OA11o2o0g7o0 練習1.0巻 都道府県の詳細1.0版 Id=1
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでモデルのインスタンスの削除ページを作成しよう！](https://qiita.com/muzudho1/items/32694c883331c75ef059)  
