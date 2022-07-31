# サンプルを見る

📖 [http://tic.warabenture.com:8000/practice/v1/prefectures/create/](http://tic.warabenture.com:8000/practice/v1/prefectures/create/) - 作成  
📖 [http://tic.warabenture.com:8000/practice/v1/prefectures/update/4/](http://tic.warabenture.com:8000/practice/v1/prefectures/update/4/) - 更新。IDは適宜変えてほしい  

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
    │   │       │       └── 📂 o1o0
    │   │       │           └── 📂 prefecture
    │   │       │               ├── 📄 delete.html
    │   │       │               ├── 📄 list.html
    │   │       │               └── 📄 read.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 o1o0
    │   │       │       └── 📂 prefecture
    │   │       │           ├── 📄 __init__.py
    │   │       │           ├── 📄 v_delete.py
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

# Step OA11o4o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step OA11o4o0g2o0 画面作成 - upsert.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 o1o0                # ただのフォルダー
                            └── 📂 prefecture            # ただのフォルダー
👉                              └── 📄 upsert.html
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
            <form action="{% url 'practice_v1_refectures_update' id=id %}" method="post" class="form-horizontal" role="form">
            {% else %}
            <h3 class="page-header">都道府県の新規作成</h3>
            <form action="{% url 'practice_v1_prefectures_create' %}" method="post" class="form-horizontal" role="form">
            {% endif %}

                {% csrf_token %}
                {{ form }}

                <div class="form-group">
                    <div class="col-sm-offset-2 col-sm-10">
                        <button type="submit" class="btn btn-primary">送信</button>
                    </div>
                </div>

            </form>
            <a href="{% url 'practice_v1_prefectures' %}" class="btn btn-default btn-sm">戻る</a>
        </div>
        <!-- 覚えなくていい : jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- 覚えなくていい : Include all compiled plugins (below), or include individual files as needed -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
</html>
```

# Step OA11o4o0g3o0 入力フォーム作成 - f_prefecture.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                ├── 📂 forms                        # ただのフォルダー
👉              │   └── 📄 f_prefecture.py
                └── 📂 templates
                    └── 📂 practice_v1              # アプリケーションと同名
                        └── 📂 o1o0                   # ただのフォルダー
                            └── 📂 prefecture       # ただのフォルダー
                                └── 📄 upsert.html
```

```py
from django.forms import ModelForm

# 都道府県モデル
from apps1.practice_v1.models.o1o0.m_prefecture import Prefecture
#          -----------             ------------        ----------
#          1.1                     2                   3
#    ------------------------------------------
#    1
# 1. ディレクトリー
# 1.1 アプリケーション
# 2. Pythonファイル名 拡張子抜き
# 3. クラス名


class PrefectureForm(ModelForm):
    class Meta:
        model = Prefecture  # モデル指定
        fields = ('seq', 'name',)  # フィールド指定
```

👆 HTMLタグの `<form>～</form>` の子要素を自動的に埋めてくれる  

# Step OA11o4o0g4o0 ビュー編集 - v_upsert.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                ├── 📂 forms                         # ただのフォルダー
                │   └── 📄 f_prefecture.py
                ├── 📂 templates
                │   └── 📂 practice_v1              # アプリケーションと同名
                │       └── 📂 o1o0                # ただのフォルダー
                │           └── 📂 prefecture            # ただのフォルダー
                │               └── 📄 upsert.html
                └── 📂 views
                    └── 📂 o1o0                # ただのフォルダー
                        └── 📂 prefecture            # ただのフォルダー
👉                          └── 📄 v_upsert.py
```

```py
from django.shortcuts import render, get_object_or_404, redirect

# 都道府県モデル
from apps1.practice_v1.models.o1o0.m_prefecture import Prefecture
#          -----------             ------------        ----------
#          11                      12                  2
#    ------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 都道府県フォーム
from apps1.practice_v1.forms.f_prefecture import PrefectureForm
#          -----------       ------------        ----------
#          11                12                  2
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


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
            return redirect('practice_v1_prefectures')
    else:  # GETの時（フォームを生成）
        form = PrefectureForm(instance=prefecture)

    # 作成・更新画面を表示
    return render(request, 'practice_v1/o1o0/prefecture/upsert.html', dict(form=form, id=id))
    #                       ---------------------------------------
    #                       1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/o1o0/prefecture/upsert.html` を取得
    #                                      ---------------------------------------
```

# Step OA11o4o0g5o0 ビュー編集 - prefecture モジュール

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o1o0
                │           └── 📂 prefecture
                │               └── 📄 upsert.html
                └── 📂 views
                    └── 📂 o1o0
                        └── 📂 prefecture
👉                          ├── 📄 __init__.py
                            └── 📄 v_upsert.py
```

```py
class PrefectureV(object):
    """都道府県のビュー"""


    # ..略..


    # 以下を追加
    from .v_upsert import render_upsert
```

# Step OA11o4o0g6o0 ルート編集 - urls.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 forms
        │       │   └── 📄 f_prefecture.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📂 prefecture
        │       │               └── 📄 delete.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 prefecture
        │                   └── 📄 v_delete.py
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


    # 都道府県の新規作成
    path('practice/v1/prefectures/create/',
         # ------------------------------
         # 1
         PrefectureV.render_upsert, name='practice_v1_prefectures_create'),
    #    -------------------------        ------------------------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/v1/prefectures/create/` のような URL のパスの部分
    #                              -------------------------------
    # 2. PrefectureV クラスの render_upsert 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_prefectures_create' %} のような形でURLを取得するのに使える

    # 都道府県の更新
    path('practice/v1/prefectures/update/<int:id>/',
         # ---------------------------------------
         # 1
         PrefectureV.render_upsert, name='practice_v1_refectures_update'),
    #    -------------------------        -----------------------------
    #    2                                3
    # 1. 例えば `http://example.com/practice/v1/prefectures/update/<数字列>/` のような URL のパスの部分
    #                              ----------------------------------------
    #    数字列は `2.` のメソッドの引数 id で取得できる
    # 2. PrefectureV クラスの render_upsert 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_refectures_update' %} のような形でURLを取得するのに使える
]
```

# Step OA11o4o0g7o0 Web画面へアクセス

👇 作成するとき、IDは付けるな  

📖 [http://localhost:8000/practice/v1/prefectures/create/](http://localhost:8000/practice/v1/prefectures/create/)  

👇 更新するとき、IDを付けろ。 IDは適宜変えてほしい  

📖 [http://localhost:8000/practice/v1/prefectures/update/4/](http://localhost:8000/practice/v1/prefectures/update/4/)  

# Step OA11o4o0g8o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 forms
        │       │   └── 📄 f_prefecture.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📂 prefecture
        │       │               └── 📄 delete.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 prefecture
        │                   └── 📄 v_delete.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/prefectures/create/,都道府県の新規作成
/practice/v1/prefectures/update/4/,都道府県(4)の更新
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DjangoでフロントエンドにVuetifyを使おう！](https://qiita.com/muzudho1/items/e80a72b027249daa4d41)

# 参考にした記事

📖 [DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92)
