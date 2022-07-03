# 目的

（※いわゆる CRUD の C と U）  

`http://localhost:8000/members/upsert/4/` へアクセスすると、  
主キーが 4 のメンバーが存在しないときは新規作成を、  
主キーが 4 のメンバーが既に存在するなら更新をしたい  

👇 表示例（新規作成のとき）:  

```plaintext
都道府県の作成

名前:
      --------------------

送信
戻る
```

👇 表示例（更新のとき）:  

```plaintext
都道府県の更新

氏名: 福岡
      --------------------

送信
戻る
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
    │   │       │               ├── 📄delete.html
    │   │       │               ├── 📄list.html
    │   │       │               └── 📄read.html
    │   │       ├── 📂views
    │   │       │   └── 📂v0o0o1
    │   │       │       └── 📂prefecture
    │   │       │           ├── 📄__init__.py
    │   │       │           ├── 📄v_delete.py
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

# Step 2. 画面作成 - upsert.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                      # アプリケーション
                └── 📂templates
                    └── 📂practice              # アプリケーションと同名
                        └── 📂v0o0o1                # ただのフォルダー
                            └── 📂prefecture            # ただのフォルダー
👉                              └── 📄upsert.html
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
        <title>都道府県の新規作成/更新</title>
    </head>
    <body>
        <div class="container">

            {% if id %}
            <h3 class="page-header">都道府県の更新</h3>
            <form action="{% url 'prefecture_update' id=id %}" method="post" class="form-horizontal" role="form">
            {% else %}
            <h3 class="page-header">都道府県の新規作成</h3>
            <form action="{% url 'prefecture_create' %}" method="post" class="form-horizontal" role="form">
            {% endif %}

                {% csrf_token %}
                {{ form }}

                <div class="form-group">
                    <div class="col-sm-offset-2 col-sm-10">
                        <button type="submit" class="btn btn-primary">送信</button>
                    </div>
                </div>

            </form>
            <a href="{% url 'prefecture_list' %}" class="btn btn-default btn-sm">戻る</a>
        </div>
        <!-- 覚えなくていい : jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- 覚えなくていい : Include all compiled plugins (below), or include individual files as needed -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
</html>
```

# Step 3. 入力フォーム作成 - f_prefecture.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                      # アプリケーション
                ├── 📂forms                         # ただのフォルダー
👉              │   └── 📄f_prefecture.py
                └── 📂templates
                    └── 📂practice              # アプリケーションと同名
                        └── 📂v0o0o1                # ただのフォルダー
                            └── 📂prefecture            # ただのフォルダー
                                └── 📄upsert.html
```

```py
from django.forms import ModelForm

from apps1.practice.models.m_prefecture import Prefecture
#    ----- -------- ------ ------------        ----------
#    1     2        3      4                   5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


class PrefectureForm(ModelForm):
    class Meta:
        model = Prefecture  # モデル指定
        fields = ('seq', 'name',)  # フィールド指定
```

👆 HTMLタグの `<form>～</form>` の子要素を自動的に埋めてくれる  

# Step 4. ビュー編集 - v_upsert.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                      # アプリケーション
                ├── 📂forms                         # ただのフォルダー
                │   └── 📄f_prefecture.py
                ├── 📂templates
                │   └── 📂practice              # アプリケーションと同名
                │       └── 📂v0o0o1                # ただのフォルダー
                │           └── 📂prefecture            # ただのフォルダー
                │               └── 📄upsert.html
                └── 📂views
                    └── 📂v0o0o1                # ただのフォルダー
                        └── 📂prefecture            # ただのフォルダー
👉                          └── 📄v_upsert.py
```

```py
from django.shortcuts import render, get_object_or_404, redirect

from apps1.practice.models.v0o0o1.m_prefecture import Prefecture
#    ----- -------- ------------- ------------        ----------
#    1     2        3             4                   5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

from apps1.practice.forms.f_prefecture import PrefectureForm
#    ----- -------- ----- ------------        --------------
#    1     2        3     4                   5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


def render_upsert(request, id=None):
    """新規作成または更新の画面の描画"""

    if id:  # idがあるとき（更新の時）
        # idで検索して、結果を戻すか、404エラー
        prefecture = get_object_or_404(Prefecture, pk=id)
    else:  # idが無いとき（作成の時）
        prefecture = Prefecture()

    # POSTの時（作成であれ更新であれ送信ボタンが押されたとき）
    if request.method == 'POST':
        # フォームを生成
        form = PrefectureForm(request.POST, instance=prefecture)
        if form.is_valid():  # バリデーションがOKなら保存
            prefecture = form.save(commit=False)
            prefecture.save()
            return redirect('prefecture_list')
    else:  # GETの時（フォームを生成）
        form = PrefectureForm(instance=prefecture)

    # 作成・更新画面を表示
    return render(request, 'practice/v0o0o1/prefecture/upsert.html', dict(form=form, id=id))
    #                       --------------------------------------
    #                       1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/prefecture/upsert.html` を取得
    #                                    --------------------------------------
```

# Step 5. ビュー編集 - prefecture モジュール

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                      # アプリケーション
                ├── 📂templates
                │   └── 📂practice
                │       └── 📂v0o0o1
                │           └── 📂prefecture
                │               └── 📄upsert.html
                └── 📂views
                    └── 📂v0o0o1
                        └── 📂prefecture
👉                          ├── 📄__init__.py
                            └── 📄v_upsert.py
```

```py
class PrefectureV(object):
    """都道府県のビュー"""


    # ..略..


    # 以下を追加
    from .v_upsert import render_upsert
```

# Step 6. ルート編集 - urls.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂practice                      # アプリケーション
        │       ├── 📂forms
        │       │   └── 📄f_prefecture.py
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


from apps1.practice.views.v0o0o1.prefecture import PrefectureV
#    ----- -------- -----------------------        -----------
#    1     2        3                              4
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


urlpatterns = [


    # ...略...


    # 都道府県の新規作成
    path('practice/prefecture/create/',
         # --------------------------
         # 1
         PrefectureV.render_upsert, name='prefecture_create'),
    #    -------------------------        -----------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/prefecture/create/` のような URL のパスの部分
    #                              ----------------------------
    # 2. PrefectureV クラスの render_upsert メソッド
    # 3. HTMLテンプレートの中で {% url 'prefecture_create' %} のような形でURLを取得するのに使える

    # 都道府県の更新
    path('practice/prefecture/update/<int:id>/',
         # -----------------------------------
         # 1
         PrefectureV.render_upsert, name='prefecture_update'),
    #    -------------------------        -----------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/prefecture/update/<数字列>/` のような URL のパスの部分
    #                              ------------------------------------
    #    数字列は `2.` のメソッドの引数に `=id` と指定することで取得できる
    # 2. PrefectureV クラスの render_upsert メソッド
    # 3. HTMLテンプレートの中で {% url 'prefecture_update' %} のような形でURLを取得するのに使える
]
```

# Step 7. Web画面へアクセス

👇 作成するとき、IDは付けるな  

📖 [http://localhost:8000/practice/prefecture/create/](http://localhost:8000/practice/prefecture/create/)  

👇 更新するとき、IDを付けろ。 IDは適宜変えてほしい  

📖 [http://localhost:8000/practice/prefecture/update/4/](http://localhost:8000/practice/prefecture/update/4/)  

# 次の記事

📖 [DjangoでフロントエンドにVuetifyを使おう！](https://qiita.com/muzudho1/items/e80a72b027249daa4d41)

# 参考にした記事

📖 [DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92)
