# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1.0/vuetify/textarea1-to-model/ver1.0/)  

# 目標

データをJSON形式で渡して、サーバーへ記憶させたい  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is     | This is                                   |
| ----------- | ----------------------------------------- |
| OS          | Windows10                                 |
| Container   | Docker                                    |
| Auth        | allauth                                   |
| Frontend    | Vuetify                                   |
| Data format | JSON                                      |
| Editor      | Visual Studio Code （以下 VSCode と表記） |

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
    │   │       │   └── 📂 practice_vol1o0
    │   │       │       └── 📂 data
    │   │       │           └── 📂 desserts1
    │   │       │               └── 📄 ver1o0.json
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_vol1o0          # アプリケーションと同名
    │   │       │       ├── 📂 prefecture
    │   │       │       └── 📂 vuetifies
    │   │       ├── 📂 views
    │   │       │   ├── 📂 prefecture
    │   │       │   └── 📂 vuetifies
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

## Step [OA13o4o0g1o0] Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step [OA13o4o0g2o0] モデル作成 - dessert/ver1o0.py ファイル

JSONのデータを受け入れられる形をサーバー側で定義しておく必要がある。  
おおまかに言って以下のような形だ。  

モデルの表示名: `Dessert (100g serving)`

| キー名   | 表示名      | サイズ               | デフォルト | ブランク | Example    |
| -------- | ----------- | -------------------- | ---------- | -------- | ---------- |
| name     | Name        | 最大32文字程度で十分 |            | 不可     | "Lollipop" |
| calories | Calories    | 自然数3桁程度        | 0          | 可       | 392        |
| fat      | Fat (g)     | 0.0～100.0程度       | 0          | 可       | 0.2        |
| carbs    | Carbs (g)   | 自然数2桁程度        | 0          | 可       | 98         |
| protein  | Protein (g) | 0.0～10.0程度        | 0          | 可       | 0          |
| iron     | Iron (%)    | 最大4文字程度で十分  |            | v"2%"    |

以上から、以下のコードを記述してほしい。  
ファイルは既存だろうから、マージしてほしい。  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                └── 📂 models
                    └── 📂 dessert
👉                      └── 📄 ver1o0.py
```

```py
# See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92
from django.db import models


class Dessert(models.Model):
    """OA13o4o0g2o0 デザート"""

    # プロパティの仕様を決める感じで
    name = models.CharField('Name', max_length=32)
    calories = models.IntegerField('Calories', blank=True, default=0)
    fat = models.FloatField('Fat (g)', blank=True, default=0)
    carbs = models.IntegerField('Carbs (g)', blank=True, default=0)
    protein = models.FloatField('Protein (g)', blank=True, default=0)
    iron = models.CharField('Iron (%)', max_length=4, blank=True)

    # このオブジェクトを文字列にしたとき返るもの
    def __str__(self):
        """このオブジェクトを文字列にしたとき返るもの"""
        return f"{self.name} dessert"
```

## Step [OA13o4o0g3o0] モデル登録 - admin.py ファイル

👇 以下の既存ファイルに追記してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 models
                │   └── 📂 dessert
                │       └── 📄 ver1o0.py
👉              └── admin.py
```

```py
# ...略...


# OA13o4o0g3o0 練習1.0巻 デザート1.0版
from .models.dessert.ver1o0 import Dessert
#    ----------------------        -------
#    1                             2
# 1. このファイルと同じディレクトリにある `models/dessert/ver1o0.py` ファイルの拡張子抜き
#                                      ---------------------
# 2. クラス


# ...略...


# Register your models here.
#   └── * 管理画面にモデルが表示されるようになる
#       └── * `manage.py makemigrations` コマンドの実行対象になる


# ...略...


# * 以下を追加
# OA13o4o0g3o0 デザート
admin.site.register(Dessert)
```

## Step [OA13o4o0g4o0] マイグレーション ファイル作成 - コマンド実行＜その１＞

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
# cd src1

docker-compose run --rm web python3 manage.py makemigrations practice_vol1o0 --settings project1.settings
#                                                            ---------------            -----------------
#                                                            1                          2
# 1. アプリケーション
# 2. `src1/project1/settings.py`
#          -----------------
```

以下のディレクトリーとファイルが生成される  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0
                ├── 📂 migrations
                │   ├── 📄 __init__.py
                │   ├── ...略...
👉              │   └── 📄 0002_dessert.py       # 名前は異なることがある
                ├── 📂 models
                │   └── 📂 dessert
                │       └── 📄 ver1o0.py
                └── admin.py
```

👆 この生成されたファイルは マイグレーション ファイル と呼ぶらしい  

まだ マイグレーション作業は完了していない  

## Step [OA13o4o0g5o0] コマンド実行＜その２＞

```shell
docker-compose run --rm web python manage.py migrate --settings project1.settings
#                                                               -----------------
#                                                               1
# 1. `src1/project1/settings.py`
#          -----------------
```

👆 ここまでやって マイグレーション という作業が終わるらしい  

## Step [OA13o4o0g6o0] スーパーユーザーでWebの管理画面へアクセス

👇 スーパーユーザーでログインすること  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

👇 画面左に以下のように表示されていればOK  

```plain
+----------------------------------+
| PRACTICE                         |
+-------------+--------+-----------+
| Desserts    | ➕ Add | 🖊 Change |
+-------------+--------+-----------+
| Prefecuters | ➕ Add | 🖊 Change |
+-------------+--------+-----------+
```

## Step [OA13o4o0g7o0] Dessert を３つほど追加してほしい

Desserts ラベルの右横の `➕ Add` リンクをクリックしてほしい  

```plaintext
Name:
      ----------------

Calories:
          ----

Fat (g):
         ----

Carbs (g):
           ----

Protein (g):
             ----

Iron (%):
          ----

                [Save and add another] [Save and continue editing] [SAVE]
```

👆入力フォームが出てくるから、３件ほど適当に追加してほしい。  
`[SAVE]` が追加ボタンのようだ  

## Step [OA13o4o0g8o0] 登録した Prefecture を確認してほしい

`Desserts` ラベルをクリックすると、一覧画面が出てくる  

## Step [OA13o4o0g9o0] 規定値の作成 - desserts1_placeholder/ver1o0.json ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0          # アプリケーション
                ├── 📂 migrations
                │   ├── 📄 __init__.py
                │   ├── ...略...
                │   └── 📄 0002_dessert.py
                ├── 📂 models
                │   └── 📂 dessert
                │       └── 📄 ver1o0.py
                ├── 📂 static
                │   └── 📂 practice_vol1o0      # アプリケーションと同名
                │       └── 📂 data
                │           └── 📂 desserts1_placeholder
👉              │               └── 📄 ver1o0.json
                └── admin.py
```

```json
{
    "name": "",
    "calories": 0,
    "fat": 0,
    "carbs": 0,
    "protein": 0,
    "iron": "0%"
}
```

👆 入力フォームの規定値にする  

## Step [OA13o4o0gA10o0] 画面作成 - vuetifies/textarea1_to_model/ver1o0.html.txt ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0          # アプリケーション
                ├── 📂 migrations
                │   ├── 📄 __init__.py
                │   ├── ...略...
                │   └── 📄 0002_dessert.py
                ├── 📂 models
                │   └── 📂 dessert
                │       └── 📄 ver1o0.py
                ├── 📂 static
                │   └── 📂 practice_vol1o0
                │       └── 📂 o1o0
                │           └── 📂 desserts1_placeholder
                │               └── 📄 ver1o0.json
                ├── 📂 templates
                │   └── 📂 practice_vol1o0      # アプリケーションと同名
                │       └── 📂 vuetifies
                │           └── 📂 textarea1_to_model
👉              │               └── 📄 ver1o0.html.txt
                └── admin.py
```

```html
<!-- BOF OA13o4o0gA10o0 -->
<!-- -->
{% extends "practice_vol1o0/vuetifies/textarea1/ver1o0.html" %}
{#          -----------------------------------------------
            1
1. src1/apps1/practice_vol1o0/templates/practice_vol1o0/vuetifies/textarea1/ver1o0.html
                                        -----------------------------------------------
#}

{% block form_signature %}
    <form method="POST" action="{% url 'practice1o0_vuetify_save_desserts_from_textarea1o0' %}">
        <!--                    ==============================================================
                                1
        1. urls_*.py ファイルで pathへ指定したname属性
            `http://example.com/{url}`
                                =====
        -->
{% endblock form_signature %}
<!-- EOF OA13o4o0gA10o0 -->
```

## Step [OA13o4o0gA11o0] ビュー作成 - v_textarea1_to_model.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0          # アプリケーション
                ├── 📂 migrations
                │   ├── 📄 __init__.py
                │   ├── ...略...
                │   └── 📄 0002_dessert.py
                ├── 📂 models
                │   └── 📂 dessert
                │       └── 📄 ver1o0.py
                ├── 📂 static
                │   └── 📂 practice_vol1o0
                │       └── 📂 o1o0
                │           └── 📂 desserts1_placeholder
                │               └── 📄 ver1o0.json
                ├── 📂 templates
                │   └── 📂 practice_vol1o0      # アプリケーションと同名
                │       └── 📂 vuetifies
                │           └── 📂 textarea1_to_model
                │               └── 📄 ver1o0.html.txt
                ├── 📂 views
                │   └── 📂 vuetifies
                │       └── 📂 textarea1_to_model
👉              │           └── 📄 ver1o0.py
                └── admin.py
```

```py
# BOF OA13o4o0gA11o0

import json
from django.http import JsonResponse
from django.shortcuts import render

# 練習1.0巻 デザート1.0版
from apps1.practice_vol1o0.models.dessert.ver1o0 import Dessert
#          ---------------                ------        -------
#          11                             12            2
#    -------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_textarea1_to_model(request):
    """OA13o4o0gA11o0 練習1.0巻 ビューティファイのテキストエリア１ 1.0版"""

    # Template path
    textarea1_to_model_tp = 'practice_vol1o0/vuetifies/textarea1_to_model/ver1o0.html.txt'
    #                        ------------------------------------------------------------
    #                        1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/vuetifies/textarea1_to_model/ver1o0.html.txt` を取得
    #                                          ------------------------------------------------------------

    with open('apps1/practice_vol1o0/static/practice_vol1o0/data/desserts1_placeholder/ver1o0.json', mode='r', encoding='utf-8') as f:
        #      -----------------------------------------------------------------------------------
        #      1
        # 1. `src1/apps1/practice_vol1o0/static/practice_vol1o0/data/desserts1_placeholder/ver1o0.json` を取得
        #          -----------------------------------------------------------------------------------
        doc = json.load(f)

    context = {
        'dessertsStr': json.dumps(doc)
    }
    return render(request, textarea1_to_model_tp, context)


def render_save_result_of_desserts1_from_textarea1(request):
    """OA13o4o0gA11o0 ビューティファイのデザート１ . テキストエリア１から . 保存結果"""

    form1Textarea1 = request.POST["textarea1"]
    doc = json.loads(form1Textarea1)  # Dessert

    dessert = Dessert(
        name=doc["name"],
        calories=doc["calories"],
        fat=doc["fat"],
        carbs=doc["carbs"],
        protein=doc["protein"],
        iron=doc["iron"])
    dessert.save()

    doc2 = {
        'result': "Success"
    }
    return JsonResponse(doc2)

# EOF OA13o4o0gA11o0
```

## Step [OA13o4o0gA12o0] ビュー編集 - VuetifyV モジュール

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0          # アプリケーション
                ├── 📂 migrations
                │   ├── 📄 __init__.py
                │   ├── ...略...
                │   └── 📄 0002_dessert.py
                ├── 📂 models
                │   └── 📂 dessert
                │       └── 📄 ver1o0.py
                ├── 📂 static
                │   └── 📂 practice_vol1o0
                │       └── 📂 o1o0
                │           └── 📂 desserts1_placeholder
                │               └── 📄 ver1o0.json
                ├── 📂 templates
                │   └── 📂 practice_vol1o0      # アプリケーションと同名
                │       └── 📂 vuetifies
                │           └── 📂 textarea1_to_model
                │               └── 📄 ver1o0.html.txt
                ├── 📂 views
                │   └── 📂 vuetifies
                │       ├── 📂 textarea1_to_model
                │       │   └── 📄 ver1o0.py
👉              │       └── 📄 __init__.py
                └── admin.py
```

```py
class VuetifyV(object):
    """OA12o1o0g4o0 ビューティファイの練習のビュー"""


    # ..略..


    # 以下を追加
    # OA13o4o0gA12o0 テキストエリア入力から保存まで
    from .textarea1_to_model.ver1o0 import render_textarea1_to_model, render_save_result_of_desserts1_from_textarea1
```

## ~~Step [OA13o4o0gA13o0]~~

## Step [OA13o4o0gA13o1o0] ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_vol1o0          # アプリケーション
    │           ├── 📂 migrations
    │           │   ├── 📄 __init__.py
    │           │   ├── ...略...
    │           │   └── 📄 0002_dessert.py
    │           ├── 📂 models
    │           │   └── 📂 dessert
    │           │       └── 📄 ver1o0.py
    │           ├── 📂 static
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 o1o0
    │           │           └── 📂 desserts1_placeholder
    │           │               └── 📄 ver1o0.json
    │           ├── 📂 templates
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 vuetifies
    │           │           └── 📂 textarea1_to_model
    │           │               └── 📄 ver1o0.html.txt
    │           ├── 📂 views
    │           │   └── 📂 vuetifies
    │           │       ├── 📂 textarea1_to_model
    │           │       │   └── 📄 ver1o0.py
    │           │       └── 📄 __init__.py
    │           └── admin.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/vuetify/textarea1-to-model/ver1.0/,,"OA13o4o0gA13o1o0 練習1.0巻 ビューティファイでテキストエリア入力から保存まで . 入力1.0版",apps1.practice_vol1o0.views.vuetifies,VuetifyV,,render_textarea1_to_model
../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/vuetify/save-desserts-from-textarea/ver1.0/,,"OA13o4o0gA13o1o0 練習1.0巻 ビューティファイでテキストエリア入力から保存まで . 保存1.0版",apps1.practice_vol1o0.views.vuetifies,VuetifyV,,render_save_result_of_desserts1_from_textarea1
```

## Step [OA13o4o0gA13o2o0] ルート編集 - コマンド打鍵

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

## Step [OA13o4o0gA14o0] Web画面へアクセス

👇 1件送信してほしい  

📖 [http://localhost:8000/practice/vol1.0/vuetify/textarea1-to-model/ver1.0/](http://localhost:8000/practice/vol1.0/vuetify/textarea1-to-model/ver1.0/)  

## Step [OA13o4o0gA15o0] スーパーユーザーでWebの管理画面へアクセス

👇 スーパーユーザーでログインすること  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

```plain
+----------------------------------+
| PRACTICE                         |
+-------------+--------+-----------+
| Desserts    | ➕ Add | 🖊 Change |
+-------------+--------+-----------+
| Prefecuters | ➕ Add | 🖊 Change |
+-------------+--------+-----------+
```

`Desserts` リンクをクリックして、データが追加されていることを確認できればOK  

## Step [OA13o4o0gA16o0] ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_vol1o0                   # アプリケーション
        │       ├── 📂 migrations
        │       │   ├── 📄 __init__.py
        │       │   ├── ...略...
        │       │   └── 📄 0002_dessert.py
        │       ├── 📂 models
        │       │   └── 📂 dessert
        │       │       └── 📄 ver1o0.py
        │       ├── 📂 static
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 o1o0
        │       │           └── 📂 desserts1_placeholder
        │       │               └── 📄 ver1o0.json
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 vuetifies
        │       │           └── 📂 textarea1_to_model
        │       │               └── 📄 ver1o0.html.txt
        │       ├── 📂 views
        │       │   └── 📂 vuetifies
        │       │       ├── 📂 textarea1_to_model
        │       │       │   └── 📄 ver1o0.py
        │       │       └── 📄 __init__.py
        │       └── admin.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/vol1.0/vuetify/textarea1-to-model/ver1.0/,OA13o4o0gA16o0 練習1.0巻 ビューティファイでテキストエリアから保存まで . 入力 1.0版
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [ソケットを使おう！](https://qiita.com/muzudho1/items/7a6501f7dbafbaa9b96c)  
