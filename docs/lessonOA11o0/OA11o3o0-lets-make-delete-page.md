# サンプルを見る

📖 [http://tic.warabenture.com:8000/practice/v1/prefectures/delete/2/](http://tic.warabenture.com:8000/practice/v1/prefectures/delete/2/) - IDは適宜変えてほしい  

# 目的

（※いわゆる CRUD の D）  

`http://localhost:8000/members/delete/2/` へアクセスすると、  
id が 2 のメンバーを削除したい。  

表示例:  

```plaintext
都道府県の削除

「大阪」を削除しました。

戻る
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
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   └── 📂 practice_v1              # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1          # アプリケーションと同名
    │   │       │       └── 📂 prefecture
    │   │       │           └── 📂 v1o0
    │   │       │               ├── 📄 list.html
    │   │       │               └── 📄 read.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 prefecture
    │   │       │       └── 📂 v1o0
    │   │       │           ├── 📄 __init__.py
    │   │       │           ├── 📄 v_list.py
    │   │       │           └── 📄 v_read.py
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

# Step OA11o3o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step OA11o3o0g2o0 画面作成 - delete.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 prefecture           # ただのフォルダー
                            └── 📂 v1o0             # ただのフォルダー
👉                              └── 📄 delete.html
```

```html
{# OA11o3o0g2o0 #}
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
        <title>都道府県の削除</title>
    </head>
    <body>
        <div class="container">
            <h3>都道府県の削除</h3>
            <div class="card" style="width: 18rem">「{{ prefecture.name }}」を削除しました。</div>
            <a href="{% url 'practice_v1_prefectures' %}" class="btn btn-default btn-sm">戻る</a>
        </div>
        <!-- 覚えなくていい : jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- 覚えなくていい : Include all compiled plugins (below), or include individual files as needed -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
</html>
```

# Step OA11o3o0g3o0 ビュー編集 - v_delete.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1              # アプリケーションと同名
                │       └── 📂 prefecture           # ただのフォルダー
                │           └── 📂 v1o0             # ただのフォルダー
                │               └── 📄 delete.html
                └── 📂 views
                    └── 📂 prefecture               # ただのフォルダー
                        └── 📂 v1o0                 # ただのフォルダー
👉                          └── 📄 v_delete.py
```

```py
from django.shortcuts import render, get_object_or_404

# 都道府県モデル
from apps1.practice_v1.models.prefecture.v1o0 import Prefecture
#          -----------                   ----        ----------
#          11                            12          2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_delete(request, id=id):
    """OA11o3o0g3o0 削除画面の描画

    Parameters
    ----------
    request : object
        リクエスト
    id : str
        URLのGETストリングの ?id= の値
    """

    # * `lp_` - Local path
    lp_prefecture_delete = 'practice_v1/prefecture/v1o0/delete.html'
    #                       ---------------------------------------
    #                       1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/prefecture/v1o0/delete.html` を取得
    #                                      ---------------------------------------

    # GETストリングのidと、Prefectureテーブルのpkが一致するものを取得。無ければ 404 画面へ飛ぶ
    prefecture = get_object_or_404(Prefecture, pk=id)

    name = prefecture.name  # 名前だけまだ使う
    prefecture.delete()
    # すでに削除されたデータを使うために以下のようにする
    context = {
        'prefecture': {
            'name': name
        }
    }
    return render(request, lp_prefecture_delete, context)
```

# Step OA11o3o0g4o0 ビュー編集 - prefecture モジュール

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 prefecture
                │           └── 📂 v1o0
                │               └── 📄 delete.html
                └── 📂 views
                    └── 📂 prefecture
                        └── 📂 v1o0
👉                          ├── 📄 __init__.py
                            └── 📄 v_delete.py
```

```py
class PrefectureV(object):
    """OA11o1o0g4o0 都道府県のビュー"""


    # ..略..


    # 以下を追加
    # OA11o3o0g4o0 削除画面
    from .v_delete import render_delete
```

# Step OA11o3o0g5o0 ルート編集 - urls.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 prefecture
        │       │           └── 📂 v1o0
        │       │               └── 📄 delete.html
        │       └── 📂 views
        │           └── 📂 prefecture
        │               └── 📂 v1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_delete.py
        └── 📂 project1                          # プロジェクト
👉          ├── 📄 urls_practice.py              # こちら
❌          └── 📄 urls.py                       # これではない
```

```py
# ...略...


urlpatterns = [


    # ...略...


    # OA11o3o0g5o0 都道府県の削除
    path('practice/v1/prefectures/delete/<int:id>/',
         # ---------------------------------------
         # 1
         PrefectureV.render_delete, name='practice_v1_prefectures_delete'),
    #    -------------------------        ------------------------------
    #    2                                3
    #
    # 1. 例えば `http://example.com/practice/v1/prefectures/delete/<数字列>/` のような URL のパスの部分
    #                              ----------------------------------------
    #    数字列は `2.` のメソッドの引数 id で取得できる
    # 2. PrefectureV クラスの render_delete メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_prefectures_delete' %} のような形でURLを取得するのに使える
]
```

# Step OA11o3o0g6o0 Web画面へアクセス

👇 IDの番号は適宜変えてほしい。  

📖 [http://localhost:8000/practice/v1/prefectures/delete/2/](http://localhost:8000/practice/v1/prefectures/delete/2/)  

# Step OA11o3o0g7o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

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
        │       │               └── 📄 delete.html
        │       └── 📂 views
        │           └── 📂 prefecture
        │               └── 📂 v1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_delete.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/prefectures/delete/2/,都道府県(2)の削除
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでモデルのインスタンスの作成／更新ページを作成しよう！](https://qiita.com/muzudho1/items/806ecdba1654ae169f37)  
