# 目的

サーバー側に記憶したデータを一覧したい  

表示例:  

```plaintext
一覧表示
主キー  連番  名前
------  ----  ----
1       1     東京
2       2     大阪
3       3     愛知
```

# はじめに

この記事は LessonO[1 0] から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション名
    │   │   ├── 📂 portal_v1                # アプリケーション名
    │   │   │   ├── 📂 data
    │   │   │   ├── 📂 migrations
    │   │   │   ├── 📂 static
    │   │   │   ├── 📂 templates
    │   │   │   └── 📂 views
    │   │   └── 📂 practice_v1              # アプリケーション名
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
    │   ├── 📂 project1                  # プロジェクト名
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets_example.txt
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_accounts.py
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

# Step [1] Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step [2] 画面作成 - list.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 o2o1                # ただのフォルダー
                            └── 📂 prefecture            # ただのフォルダー
👉                              └── 📄 list.html
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

# Step [3] ビュー作成 - v_list.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o2o1
                │           └── 📂 prefecture
                │               └── 📄 list.html
                └── 📂 views
                    └── 📂 o2o1                # ただのフォルダー
                        └── 📂 prefecture            # ただのフォルダー
👉                          └── 📄 v_list.py
```

```py
from django.http import HttpResponse
from django.template import loader

# 都道府県モデル
from apps1.practice_v1.models.o2o1.m_prefecture import Prefecture
#    ----- ----------- ----------- ------------        ----------
#    1     2           3           4                   5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


def render_list(request):
    """一覧画面の描画"""

    template = loader.get_template('practice_v1/o2o1/prefecture/list.html')
    #                               -------------------------------------
    #                               1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o2o1/prefecture/list.html` を取得
    #                                       -------------------------------------

    context = {
        'prefectures': Prefecture.objects.all().order_by('pk'),  # pk順にメンバーを全部取得
    }
    return HttpResponse(template.render(context, request))
```

# Step [4] ビュー作成 - prefecture モジュール

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o2o1
                │           └── 📂 prefecture
                │               └── 📄 list.html
                └── 📂 views
                    └── 📂 o2o1
                        └── 📂 prefecture
👉                          ├── 📄 __init__.py
                            └── 📄 v_list.py
```

```py
class PrefectureV(object):
    """都道府県のビュー"""

    from .v_list import render_list
```

# Step [5] ルート編集 - urls.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o2o1
        │       │           └── 📂 prefecture
        │       │               └── 📄 list.html
        │       └── 📂 views
        │           └── 📂 o2o1
        │               └── 📂 prefecture
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_list.py
        └── 📂 project1                          # プロジェクト
👉          ├── 📄 urls_practice.py              # こちら
❌          └── 📄 urls.py                       # これではない
```

```py
from django.urls import path


# ...略...


# 都道府県
from apps1.practice_v1.views.o2o1.prefecture import PrefectureV
#          -----------            ----------        -----------
#          11                     12                2
#    ---------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [


    # ...略...


    # 都道府県の一覧
    path('practice/v1/prefectures/',
         # -----------------------
         # 1
         PrefectureV.render_list, name='practice_v1_prefectures'),
    #    -----------------------        -----------------------
    #    2                              3
    # 1. 例えば `http://example.com/practice/v1/prefectures/` のような URL のパスの部分
    #                              ------------------------
    # 2. PrefectureV クラスの render_list 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_prefectures' %} のような形でURLを取得するのに使える
]
```

# Step [6] Web画面へアクセス

📖 [http://localhost:8000/practice/v1/prefectures/](http://localhost:8000/practice/v1/prefectures/)  

# Step [7] ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

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
        │       │       └── 📂 o2o1
        │       │           └── 📂 prefecture
        │       │               └── 📄 list.html
        │       └── 📂 views
        │           └── 📂 o2o1
        │               └── 📂 prefecture
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

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでモデルのインスタンスの読取ページを作成しよう！](https://qiita.com/muzudho1/items/ae362f53a670e265a7e4)  
