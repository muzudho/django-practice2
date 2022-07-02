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

この記事は Lesson01 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    │   │       │               ├── 📄list.html
    │   │       │               └── 📄read.html
    │   │       ├── 📂views
    │   │       │   └── 📂v0o0o1
    │   │       │       └── 📂prefecture
    │   │       │           ├── 📄__init__.py
    │   │       │           ├── 📄v_list.py
    │   │       │           └── 📄v_read.py
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

# Step 2. 画面作成 - delete.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                      # アプリケーション
                └── 📂templates
                    └── 📂practice              # アプリケーションと同名
                        └── 📂v0o0o1                # ただのフォルダー
                            └── 📂prefecture            # ただのフォルダー
👉                              └── 📄delete.html
```

```html
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<!-- See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92 -->
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <!--                                                ===================
                                                            1
            1. Example: `http://example.com/static/favicon.ico`
                                            ==================
        -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>都道府県の削除</title>
        <!-- 覚えなくていい : Bootstrap -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />
    </head>
    <body>
        <div class="container">
            <h3>都道府県の削除</h3>
            <div class="card" style="width: 18rem">「{{ prefecture.name }}」を削除しました。</div>
            <a href="{% url 'prefecture_list' %}" class="btn btn-default btn-sm">戻る</a>
        </div>
        <!-- 覚えなくていい : jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- 覚えなくていい : Include all compiled plugins (below), or include individual files as needed -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
</html>
```

# Step 3. ビュー編集 - v_delete.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                      # アプリケーション
                ├── 📂templates
                │   └── 📂practice              # アプリケーションと同名
                │       └── 📂v0o0o1                # ただのフォルダー
                │           └── 📂prefecture            # ただのフォルダー
                │               └── 📄delete.html
                └── 📂views
                    └── 📂v0o0o1                # ただのフォルダー
                        └── 📂prefecture            # ただのフォルダー
👉                          └── 📄v_delete.py
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


class PrefectureDeleteV():
    """都道府県の削除ビュー"""

    def render(request, id=id):
        """描画

        Parameters
        ----------
        request : object
            リクエスト
        id : str
            URLのGETストリングの ?id= の値
        """

        template = loader.get_template(
            'practice/v0o0o1/prefecture/delete.html')
        #    --------------------------------------
        #    1
        # 1. `host1/apps1/practice/templates/practice/v0o0o1/prefecture/delete.html` を取得
        #                                    --------------------------------------

        # GETストリングのidと、Prefectureテーブルのpkが一致するものを取得
        prefecture = Prefecture.objects.get(pk=id)
        name = prefecture.name  # 名前だけまだ使う
        prefecture.delete()
        # すでに削除されたデータを使うために以下のようにする
        context = {
            'prefecture': {
                'name': name
            }
        }
        return HttpResponse(template.render(context, request))
```

# Step 4. ルート編集 - urls.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂practice                      # アプリケーション
        │       ├── 📂templates
        │       │   └── 📂practice
        │       │       └── 📂v0o0o1
        │       │           └── 📂prefecture
        │       │               └── 📄delete.html
        │       └── 📂views
        │           └── 📂v0o0o1
        │               └── 📂prefecture
        │                   └── 📄v_delete.py
        └── 📂project1                          # プロジェクト
👉          ├── 📄urls_practice.py              # こちら
❌          └── 📄urls.py                       # これではない
```

```py
from django.urls import path


# ...略...


from apps1.practice.views.v0o0o1.prefecture.v_delete import PrefectureDeleteV
#    ----- -------- ----------------------- --------        -----------------
#    1     2        3                       4               5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


urlpatterns = [


    # ...略...


    # 都道府県の削除
    path('practice/prefectures/delete/<int:id>/',
         # ------------------------------------
         # 1
         PrefectureDeleteV.render, name='prefecture_delete'),
    #    ------------------------        -----------------
    #    2                               3
    #
    # 1. 例えば `http://example.com/practice/prefectures/delete/<数字列>/` のような URL のパスの部分
    #                              -------------------------------------
    #    数字列は `2.` のメソッドの引数に `=id` と指定することで取得できる
    # 2. PrefectureDeleteV クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'prefecture_delete' %} のような形でURLを取得するのに使える
]
```

# Step 4. Web画面へアクセス

👇 IDの番号は適宜変えてほしい。  

📖 [http://localhost:8000/practice/prefectures/delete/2/](http://localhost:8000/practice/prefectures/delete/2/)  

# 次の記事

📖 [Djangoでモデルのインスタンスの作成／更新ページを作成しよう！](https://qiita.com/muzudho1/items/806ecdba1654ae169f37)  
