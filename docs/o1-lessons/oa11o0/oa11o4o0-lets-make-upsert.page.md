# サンプルを見る

📖 [この記事のゴール：新規作成](http://tic.warabenture.com:8000/practice/vol1o0/prefectures/create/ver1o0/)  
📖 [この記事のゴール：更新](http://tic.warabenture.com:8000/practice/vol1o0/prefectures/update/ver1o0/4/) - IDは適宜変えてほしい  

# 目標

（※いわゆる CRUD の C と U）  

`http://localhost:8000/members/upsert/4/` へアクセスすると、  
主キーが 4 のメンバーが存在しないときは新規作成を、  
主キーが 4 のメンバーが既に存在するなら更新をしたい  

## 詳細

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
    │   │   ├── 📂 accounts_vol1o0    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   └── 📂 practice_vol1o0              # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_vol1o0          # アプリケーションと同名
    │   │       │       └── 📂 prefecture
    │   │       │           └── 📂 ver1o0
    │   │       │               ├── 📄 delete.html
    │   │       │               ├── 📄 list.html
    │   │       │               └── 📄 read.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 prefecture
    │   │       │       └── 📂 ver1o0
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

## Step OA11o4o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA11o4o0g2o0 画面作成 - upsert.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                      # アプリケーション
                └── 📂 templates
                    └── 📂 practice_vol1o0              # アプリケーションと同名
                        └── 📂 prefecture           # ただのフォルダー
                            └── 📂 ver1o0             # ただのフォルダー
👉                              └── 📄 upsert.html
```

```html
{# OA11o4o0g2o0 #}
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

## Step OA11o4o0g3o0 入力フォーム作成 - f_prefecture.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                      # アプリケーション
                ├── 📂 forms                        # ただのフォルダー
👉              │   └── 📄 f_prefecture.py
                └── 📂 templates
                    └── 📂 practice_vol1o0              # アプリケーションと同名
                        └── 📂 prefecture           # ただのフォルダー
                            └── 📂 ver1o0             # ただのフォルダー
                                └── 📄 upsert.html
```

```py
from django.forms import ModelForm

# 都道府県モデル
from apps1.practice_v1.models.prefecture.v1o0 import Prefecture
#          -----------                   ----        ----------
#          11                            12          2
#    ----------------------------------------
#    10
# 10. ディレクトリー
# 11 アプリケーション
# 12. Pythonファイル名 拡張子抜き
# 2. クラス


class PrefectureForm(ModelForm):
    """OA11o4o0g3o0 都道府県フォーム"""

    class Meta:
        model = Prefecture  # モデル指定
        fields = ('seq', 'name',)  # フィールド指定
```

👆 HTMLタグの `<form>～</form>` の子要素を自動的に埋めてくれる  

## Step OA11o4o0g4o0 ビュー編集 - v_upsert.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                      # アプリケーション
                ├── 📂 forms                        # ただのフォルダー
                │   └── 📄 f_prefecture.py
                ├── 📂 templates
                │   └── 📂 practice_vol1o0              # アプリケーションと同名
                │       └── 📂 prefecture           # ただのフォルダー
                │           └── 📂 ver1o0             # ただのフォルダー
                │               └── 📄 upsert.html
                └── 📂 views
                    └── 📂 prefecture               # ただのフォルダー
                        └── 📂 ver1o0                 # ただのフォルダー
👉                          └── 📄 v_upsert.py
```

```py
# BOF OA11o4o0g4o0

from django.shortcuts import render, get_object_or_404, redirect

# 都道府県モデル
from apps1.practice_v1.models.prefecture.v1o0 import Prefecture
#          -----------                   ----        ----------
#          11                            12          2
#    ------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 都道府県フォーム
from apps1.practice_v1.forms.f_prefecture import PrefectureForm
#          -----------       ------------        --------------
#          11                12                  2
#    ------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_upsert(request, id=None):
    """OA11o4o0g4o0 新規作成または更新の画面の描画"""

    if id:  # idがあるとき（更新の時）
        # idで検索して、結果を戻すか、404エラー
        prefecture = get_object_or_404(Prefecture, pk=id)
    else:  # idが無いとき（作成の時）
        prefecture = Prefecture()

    # POSTの時（作成であれ更新であれ送信ボタンが押されたとき）
    if request.method == 'POST':
        # フォームを生成
        form = PrefectureForm(request.POST, instance=prefecture)

        # Valid なら保存して一覧画面へ
        if form.is_valid():
            prefecture = form.save(commit=False)
            prefecture.save()
            return redirect('practice_v1_prefectures')

        # Invalid ならフォームを引き継いで再び同じ画面表示へ

    else:  # GETの時（フォームを生成）
        form = PrefectureForm(instance=prefecture)

    # 作成・更新画面を表示
    # Template path
    prefecture_upsert_tp = 'practice_v1/prefecture/v1o0/upsert.html'
    #                       ---------------------------------------
    #                       1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/prefecture/v1o0/upsert.html` を取得
    #                                      ---------------------------------------

    return render(request, prefecture_upsert_tp, dict(form=form, id=id))

# EOF OA11o4o0g4o0
```

## Step OA11o4o0g5o0 ビュー編集 - prefecture/v1o0 フォルダー

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                      # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 prefecture
                │           └── 📂 ver1o0
                │               └── 📄 upsert.html
                └── 📂 views
                    └── 📂 prefecture
                        └── 📂 ver1o0
👉                          ├── 📄 __init__.py
                            └── 📄 v_upsert.py
```

```py
class PrefectureV(object):
    """OA11o1o0g4o0 都道府県のビュー"""


    # ..略..


    # 以下を追加
    # OA11o4o0g5o0 新規作成，更新画面
    from .v_upsert import render_upsert
```

## ~~Step OA11o4o0g6o0~~

Merged to OA11o4o0g6o1o0  

## Step OA11o4o0g6o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_vol1o0                      # アプリケーション
    │           ├── 📂 forms
    │           │   └── 📄 f_prefecture.py
    │           ├── 📂 templates
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 prefecture
    │           │           └── 📂 ver1o0
    │           │               └── 📄 delete.html
    │           └── 📂 views
    │               └── 📂 prefecture
    │                   └── 📂 ver1o0
    │                       └── 📄 v_delete.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/prefectures/create/ver1.0/,practice_v1_prefectures_create,"OA11o4o0g6o1o0 練習1.0巻 都道府県の新規作成 1.0版",apps1.practice_v1.views.prefecture.v1o0,PrefectureV,,render_upsert
../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/prefectures/update/ver1.0/<int:id>/,practice_v1_refectures_update,"OA11o4o0g6o1o0 練習1.0巻 都道府県の更新 1.0版",apps1.practice_v1.views.prefecture.v1o0,PrefectureV,,render_upsert
```

## Step OA11o4o0g6o2o0 ルート編集 - コマンド打鍵

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

## Step OA11o4o0g7o0 Web画面へアクセス

👇 作成するとき、IDは付けるな  

📖 [http://localhost:8000/practice/vol1o0/prefectures/create/ver1o0/](http://localhost:8000/practice/vol1o0/prefectures/create/ver1o0/)  

👇 更新するとき、IDを付けろ。 IDは適宜変えてほしい  

📖 [http://localhost:8000/practice/vol1o0/prefectures/update/ver1o0/4/](http://localhost:8000/practice/vol1o0/prefectures/update/ver1o0/4/)  

## Step OA11o4o0g8o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_vol1o0                      # アプリケーション
        │       ├── 📂 forms
        │       │   └── 📄 f_prefecture.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 prefecture
        │       │           └── 📂 ver1o0
        │       │               └── 📄 delete.html
        │       └── 📂 views
        │           └── 📂 prefecture
        │               └── 📂 ver1o0
        │                   └── 📄 v_delete.py
        └── 📂 project1                             # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/vol1.0/prefectures/create/ver1o0/,OA11o4o0g8o0 練習1.0巻 都道府県の新規作成1.0版
/practice/vol1.0/prefectures/update/ver1o0/4/,OA11o4o0g8o0 練習1.0巻 都道府県の更新1.0版 id=4
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [DjangoでフロントエンドにVuetifyを使おう！](https://qiita.com/muzudho1/items/e80a72b027249daa4d41)

# 参考にした記事

📖 [DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92)
