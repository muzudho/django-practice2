# 目的

（※いわゆる CRUD の R）  

`http://localhost:8000/prefectures/read/1/` へアクセスすると、  
pk が 1 の都道府県を表示したい  

表示例:  

```plaintext
都道府県の詳細情報

連番
1

名前
東京
```

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

参考にした元記事は 📖[DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92) だ。  
わたしの記事は単に **やってみた** ぐらいの位置づけだ  

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 host1
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1        # アプリケーション
    │   │   ├── 📂 portal_v1                    # アプリケーション
    │   │   └── 📂 practice_v1                  # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1          # アプリケーションと同名
    │   │       │       └── 📂 o1o0
    │   │       │           └── 📂 prefecture
    │   │       │               └── 📄 list.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 o1o0
    │   │       │       └── 📂 prefecture
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

# Step O1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step O2o0 画面作成 - read.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 o1o0                # ただのフォルダー
                            └── 📂 prefecture            # ただのフォルダー
👉                              └── 📄 read.html
```

```html
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
            <a href="{% url 'practice_v1_prefectures' %}" class="btn btn-default btn-sm">戻る</a>
        </div>
        <!-- 覚えなくていい : jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- 覚えなくていい : Include all compiled plugins (below), or include individual files as needed -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
</html>
```

# Step O3o0 ビュー作成- v_read.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1              # アプリケーションと同名
                │       └── 📂 o1o0                # ただのフォルダー
                │           └── 📂 prefecture            # ただのフォルダー
                │               └── 📄 read.html
                └── 📂 views
                    └── 📂 o1o0                # ただのフォルダー
                        └── 📂 prefecture            # ただのフォルダー
👉                          └── 📄 v_read.py
```

```py
from django.http import HttpResponse
from django.template import loader

# 都道府県モデル
from apps1.practice_v1.models.o1o0.m_prefecture import Prefecture
#          -----------             ------------        ----------
#          11                      12                  2
#    ------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_read(request, id=id):
    """詳細画面の描画

    Parameters
    ----------
    request : object
        リクエスト
    id : str
        URLのGETストリングの ?id= の値
    """

    template = loader.get_template('practice_v1/o1o0/prefecture/read.html')
    #                               -------------------------------------
    #                               1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o1o0/prefecture/read.html` を取得
    #                                       -------------------------------------

    context = {
        # GETストリングのidと、Prefectureテーブルのpkが一致するものを取得
        'prefecture': Prefecture.objects.get(pk=id),
    }
    return HttpResponse(template.render(context, request))
```

# Step O4o0 ビュー編集 - prefecture モジュール

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o1o0
                │           └── 📂 prefecture
                │               └── 📄 read.html
                └── 📂 views
                    └── 📂 o1o0
                        └── 📂 prefecture
👉                          ├── 📄 __init__.py
                            └── 📄 v_read.py
```

```py
class PrefectureV(object):
    """都道府県のビュー"""


    # ..略..


    # 以下を追加
    from .v_read import render_read
```

# Step O5o0 ルート編集 - urls.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📂 prefecture
        │       │               └── 📄 read.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 prefecture
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_read.py
        └── 📂 project1                          # プロジェクト
👉          ├── 📄 urls_practice.py              # こちら
❌          └── 📄 urls.py                       # これではない
```

```py
from django.urls import path


# ...略...


# 都道府県
from apps1.practice_v1.views.o1o0.prefecture import PrefectureV
#          -----------            ----------        -----------
#          11                     12                2
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [


    # ...略...


    # 都道府県の詳細
    path('practice/v1/prefectures/read/<int:id>/',
         # -------------------------------------
         # 1
         PrefectureV.render_read, name='practice_v1_prefectures_read'),
    #    -----------------------        ----------------------------
    #    2                              3
    #
    # 1. 例えば `http://example.com/practice/v1/prefectures/read/<数字列>/` のような URL のパスの部分
    #                              --------------------------------------
    #    数字列は `2.` のメソッドの引数 id で取得できる
    # 2. PrefectureV クラスの render_read 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_prefectures_read' %} のような形でURLを取得するのに使える
]
```

# Step O6o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/prefectures/read/1/](http://localhost:8000/practice/v1/prefectures/read/1/)  

# Step O7o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
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
/practice/v1/prefectures/read/1/,都道府県(1)の詳細
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでモデルのインスタンスの削除ページを作成しよう！](https://qiita.com/muzudho1/items/32694c883331c75ef059)  
