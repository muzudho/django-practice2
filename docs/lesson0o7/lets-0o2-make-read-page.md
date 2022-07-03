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

この記事は Lesson0 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    ├── 📂host1
    │   ├── 📂apps1
    │   │   ├── 📂allauth_customized    # アプリケーション
    │   │   ├── 📂portal                # アプリケーション
    │   │   └── 📂practice              # アプリケーション
    │   │       ├── 📂management
    │   │       ├── 📂migrations
    │   │       ├── 📂models
    │   │       ├── 📂static
    │   │       ├── 📂templates
    │   │       │   └── 📂practice          # アプリケーションと同名
    │   │       │       └── 📂v0o0o1
    │   │       │           └── 📂prefecture
    │   │       │               └── 📄list.html
    │   │       ├── 📂views
    │   │       │   └── 📂v0o0o1
    │   │       │       └── 📂prefecture
    │   │       │           ├── 📄__init__.py
    │   │       │           └── 📄v_list.py
    │   │       ├── 📄__init__.py
    │   │       ├── 📄admin.py
    │   │       ├── 📄apps.py
    │   │       └── 📄tests.py
    │   ├── 📂data
    │   ├── 📂project1                  # プロジェクト
    │   │   ├── 📄__init__.py
    │   │   ├── 📄asgi.py
    │   │   ├── 📄settings_secrets_example.txt
    │   │   ├── 📄settings.py
    │   │   ├── 📄urls_accounts.py
    │   │   ├── 📄urls_practice.py
    │   │   ├── 📄urls.py
    │   │   └── 📄wsgi.py
    │   ├── 📂project2                  # プロジェクト
    │   ├── 🐳docker-compose-project2.yml
    │   ├── 🐳docker-compose.yml
    │   ├── 🐳Dockerfile
    │   ├── 📄manage.py
    │   └── 📄requirements.txt
    └── 📄.gitignore
```

# Step 1. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. 画面作成 - read.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                      # アプリケーション
                └── 📂templates
                    └── 📂practice              # アプリケーションと同名
                        └── 📂v0o0o1                # ただのフォルダー
                            └── 📂prefecture            # ただのフォルダー
👉                              └── 📄read.html
```

```html
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<!-- See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92 -->
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <!--                                                ===================
                                                            1
            1. Example: `http://example.com/static/favicon.ico`
                                            ==================
        -->
        <!-- 覚えなくていい : Bootstrap -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />
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
            <a href="{% url 'prefecture_list' %}" class="btn btn-default btn-sm">戻る</a>
        </div>
        <!-- 覚えなくていい : jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- 覚えなくていい : Include all compiled plugins (below), or include individual files as needed -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
</html>
```

# Step 3. ビュー作成- v_read.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                      # アプリケーション
                ├── 📂templates
                │   └── 📂practice              # アプリケーションと同名
                │       └── 📂v0o0o1                # ただのフォルダー
                │           └── 📂prefecture            # ただのフォルダー
                │               └── 📄read.html
                └── 📂views
                    └── 📂v0o0o1                # ただのフォルダー
                        └── 📂prefecture            # ただのフォルダー
👉                          └── 📄v_read.py
```

```py
from django.http import HttpResponse
from django.template import loader

from apps1.practice.models.m_prefecture import Prefecture
#    ----- -------- ------ ------------        ----------
#    1     2        3      4                   5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


def render_read(request, id=id):
    """描画

    Parameters
    ----------
    request : object
        リクエスト
    id : str
        URLのGETストリングの ?id= の値
    """

    template = loader.get_template('practice/v0o0o1/prefecture/read.html')
    #                               ------------------------------------
    #                               1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/prefecture/read.html` を取得
    #                                    ------------------------------------

    context = {
        # GETストリングのidと、Prefectureテーブルのpkが一致するものを取得
        'prefecture': Prefecture.objects.get(pk=id),
    }
    return HttpResponse(template.render(context, request))
```

# Step 4. ビュー編集 - prefecture モジュール

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                      # アプリケーション
                ├── 📂templates
                │   └── 📂practice
                │       └── 📂v0o0o1
                │           └── 📂prefecture
                │               └── 📄read.html
                └── 📂views
                    └── 📂v0o0o1
                        └── 📂prefecture
👉                          ├── 📄__init__.py
                            └── 📄v_read.py
```

```py
class PrefectureV(object):
    """都道府県のビュー"""


    # ..略..


    # 以下を追加
    from .v_read import render_read
```

# Step 5. ルート編集 - urls.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂practice                      # アプリケーション
        │       ├── 📂templates
        │       │   └── 📂practice
        │       │       └── 📂v0o0o1
        │       │           └── 📂prefecture
        │       │               └── 📄read.html
        │       └── 📂views
        │           └── 📂v0o0o1
        │               └── 📂prefecture
        │                   ├── 📄__init__.py
        │                   └── 📄v_read.py
        └── 📂project1                          # プロジェクト
👉          ├── 📄urls_practice.py              # こちら
❌          └── 📄urls.py                       # これではない
```

```py
from django.urls import path


# ...略...


from apps1.practice.views.v0o0o1.prefecture import PrefectureV
#    ----- -------- -----------------------        -----------
#    1     2        3                              4
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


urlpatterns = [


    # ...略...


    # 都道府県の詳細
    path('practice/prefectures/read/<int:id>/',
         # ----------------------------------
         # 1
         PrefectureV.render_read, name='prefecture_read'),
    #    -----------------------        ---------------
    #    2                              3
    #
    # 1. 例えば `http://example.com/practice/prefectures/read/<数字列>/` のような URL のパスの部分
    #                              -----------------------------------
    #    数字列は `2.` のメソッドの引数に `=id` と指定することで取得できる
    # 2. PrefectureV クラスの render_read メソッド
    # 3. HTMLテンプレートの中で {% url 'prefecture_read' %} のような形でURLを取得するのに使える
]
```

# Step 6. Web画面へアクセス

📖 [http://localhost:8000/practice/prefectures/read/1/](http://localhost:8000/practice/prefectures/read/1/)  

# 次の記事

📖 [Djangoでモデルのインスタンスの削除ページを作成しよう！](https://qiita.com/muzudho1/items/32694c883331c75ef059)  
