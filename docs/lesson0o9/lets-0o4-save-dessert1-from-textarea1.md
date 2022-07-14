# 目的

データをJSON形式で渡して、サーバーへ記憶させたい  

# はじめに

この記事は Lesson0 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key         | Value                                     |
| ----------- | ----------------------------------------- |
| OS          | Windows10                                 |
| Container   | Docker                                    |
| Auth        | allauth                                   |
| Frontend    | Vuetify                                   |
| Data format | JSON                                      |
| Editor      | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 host1
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized    # アプリケーション
    │   │   ├── 📂 portal                # アプリケーション
    │   │   └── 📂 practice              # アプリケーション
    │   │       ├── 📂 management
    │   │       ├── 📂 migrations
    │   │       ├── 📂 models
    │   │       ├── 📂 static
    │   │       │   └── 📂 practice
    │   │       │       └── 📂 v0o0o1
    │   │       │           └── 📂 data
    │   │       │               └── 📄 desserts1.json
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice          # アプリケーションと同名
    │   │       │       └── 📂 v0o0o1
    │   │       │           ├── 📂 prefecture
    │   │       │           └── 📂 vuetify
    │   │       │               ├── 📄 textarea1_base.html
    │   │       │               └── 📄 desserts1.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 v0o0o1
    │   │       │       ├── 📂 prefecture
    │   │       │       └── 📂 vuetify
    │   │       │           ├── 📄 __init__.py
    │   │       │           └── 📄 v_textarea1.py
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

# Step 1. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. モデル作成 - m_dessert.py ファイル

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
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice                  # アプリケーション
                └── 📂 models
                    └── 📂 v0o0o1
👉                      └── 📄 m_dessert.py
```

```py
# See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92
from django.db import models


class Dessert(models.Model):
    """デザート"""

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

# Step 3. モデル登録 - admin.py ファイル

👇 以下の既存ファイルに追記してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice                  # アプリケーション
                ├── 📂 models
                │   └── 📂 v0o0o1
                │       └── 📄 m_dessert.py
👉              └── admin.py
```

```py
# See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92
from django.contrib import admin

from .models.v0o0o1.m_dessert import Dessert
#    ------------------------        -------
#    1                               2
#
# 1. このファイルと同じディレクトリにある `models/v0o0o1/m_dessert.py` ファイルの拡張子抜き
#                                      --------------------------
# 2. クラス名

# Register your models here.
#   └── * 管理画面にモデルが表示されるようになる
#       └── * `manage.py makemigrations` コマンドの実行対象になる


# ...略...


# 以下を追加
admin.site.register(Dessert)
```

# Step 4. マイグレーション ファイル作成 - コマンド実行＜その１＞

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
# cd host1

docker-compose run --rm web python3 manage.py makemigrations practice --settings project1.settings
#                                                            --------            -----------------
#                                                            1                   2
# 1. アプリケーション名
# 2. `host1/project1/settings.py`
#           -----------------
```

以下のディレクトリーとファイルが生成される  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice
                ├── 📂 migrations
                │   ├── 📄 __init__.py
                │   ├── ...略...
👉              │   └── 📄 0002_dessert.py       # 名前は異なることがある
                ├── 📂 models
                │   └── 📂 v0o0o1
                │       └── 📄 m_dessert.py
                └── admin.py
```

👆 この生成されたファイルは マイグレーション ファイル と呼ぶらしい  

まだ マイグレーション作業は完了していない  

# Step 5. コマンド実行＜その２＞

```shell
docker-compose run --rm web python manage.py migrate --settings project1.settings
#                                                               -----------------
#                                                               1
# 1. `host1/project1/settings.py`
#           -----------------
```

👆 ここまでやって マイグレーション という作業が終わるらしい  

# Step 6. スーパーユーザーでWebの管理画面へアクセス

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

# Step 7. Dessert を３つほど追加してほしい

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

# Step 8. 登録した Prefecture を確認してほしい

`Desserts` ラベルをクリックすると、一覧画面が出てくる  

# Step 9. 規定値の作成 - desserts1-placeholder.json ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice          # アプリケーション
                ├── 📂 migrations
                │   ├── 📄 __init__.py
                │   ├── ...略...
                │   └── 📄 0002_dessert.py
                ├── 📂 models
                │   └── 📂 v0o0o1
                │       └── 📄 m_dessert.py
                ├── 📂 static
                │   └── 📂 practice      # アプリケーションと同名
                │       └── 📂 v0o0o1
                │           └── 📂 data
👉              │               └── 📄 desserts1-placeholder.json
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

# Step 10. 画面作成 - textarea1_to_model.html.txt ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice          # アプリケーション
                ├── 📂 migrations
                │   ├── 📄 __init__.py
                │   ├── ...略...
                │   └── 📄 0002_dessert.py
                ├── 📂 models
                │   └── 📂 v0o0o1
                │       └── 📄 m_dessert.py
                ├── 📂 static
                │   └── 📂 practice
                │       └── 📂 v0o0o1
                │           └── 📂 data
                │               └── 📄 desserts1-placeholder.json
                ├── 📂 templates
                │   └── 📂 practice      # アプリケーションと同名
                │       └── 📂 v0o0o1
                │           └── 📂 vuetify
👉              │               └── 📄 textarea1_to_model.html.txt
                └── admin.py
```

```html
{% extends "practice/v0o0o1/vuetify/textarea1_base.html" %}
{#          -------------------------------------------
            1
1. host1/apps1/practice/templates/practice/v0o0o1/vuetify/textarea1_base.html
                                  -------------------------------------------
#}

{% block form_signature %}
    <form method="POST" action="save-desserts1-from-textarea1">
        <!--                    =============================
                                1
        1. 宛先を間違えないように
            `http://example.com/practice/vuetify/save-desserts1-from-textarea1`
                                                =============================
        -->
{% endblock form_signature %}
```

# Step 11. ビュー作成 - v_textarea1_to_model.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice          # アプリケーション
                ├── 📂 migrations
                │   ├── 📄 __init__.py
                │   ├── ...略...
                │   └── 📄 0002_dessert.py
                ├── 📂 models
                │   └── 📂 v0o0o1
                │       └── 📄 m_dessert.py
                ├── 📂 static
                │   └── 📂 practice
                │       └── 📂 v0o0o1
                │           └── 📂 data
                │               └── 📄 desserts1-placeholder.json
                ├── 📂 templates
                │   └── 📂 practice      # アプリケーションと同名
                │       └── 📂 v0o0o1
                │           └── 📂 vuetify
                │               └── 📄 textarea2.html
                ├── 📂 views
                │   └── 📂 v0o0o1
                │       └── 📂 vuetify
👉              │           └── 📄 v_textarea1_to_model.py
                └── admin.py
```

```py
import json
from django.http import HttpResponse, JsonResponse
from django.template import loader

from apps1.practice.models.v0o0o1.m_dessert import Dessert
#    ---------------------------- ---------        -----
#    1                            2                3
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き
# 3. クラス名


def render_textarea1_to_model(request):
    """ビューティファイのテキストエリア１ to model"""

    template = loader.get_template(
        'practice/v0o0o1/vuetify/textarea1_to_model.html.txt')
    #    ---------------------------------------------------
    #    1
    # 1. `host1/apps1/practice/templates/practice/v0o0o1/vuetify/textarea1_to_model.html.txt` を取得
    #                                    ---------------------------------------------------

    with open('apps1/practice/static/practice/v0o0o1/data/desserts1-placeholder.json', mode='r', encoding='utf-8') as f:
        #      ---------------------------------------------------------------------
        #      1
        # 1. `host1/apps1/practice/static/practice/v0o0o1/data/desserts1-placeholder.json` を取得
        #           ---------------------------------------------------------------------
        doc = json.load(f)

    context = {
        'dessertsStr': json.dumps(doc)
    }
    return HttpResponse(template.render(context, request))


def render_save_result_of_desserts1_from_textarea1(request):
    """ビューティファイのデザート１ . テキストエリア１から . 保存結果"""

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
```

# Step 12. ビュー編集 - VuetifyV モジュール

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice          # アプリケーション
                ├── 📂 migrations
                │   ├── 📄 __init__.py
                │   ├── ...略...
                │   └── 📄 0002_dessert.py
                ├── 📂 models
                │   └── 📂 v0o0o1
                │       └── 📄 m_dessert.py
                ├── 📂 static
                │   └── 📂 practice
                │       └── 📂 v0o0o1
                │           └── 📂 data
                │               └── 📄 desserts1-placeholder.json
                ├── 📂 templates
                │   └── 📂 practice      # アプリケーションと同名
                │       └── 📂 v0o0o1
                │           └── 📂 vuetify
                │               └── 📄 textarea2.html
                ├── 📂 views
                │   └── 📂 v0o0o1
                │       └── 📂 vuetify
👉              │           ├── 📄 __init__.py
                │           └── 📄 v_textarea1_to_model.py
                └── admin.py
```

```py
class VuetifyV(object):
    """ビューティファイの練習のビュー"""

    # ..略..


    # 以下を追加
    from .v_textarea1_to_model import render_textarea1_to_model, render_save_result_of_desserts1_from_textarea1
```

# Step 13. ルート編集 - urls.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice          # アプリケーション
        │       ├── 📂 migrations
        │       │   ├── 📄 __init__.py
        │       │   ├── ...略...
        │       │   └── 📄 0002_dessert.py
        │       ├── 📂 models
        │       │   └── 📂 v0o0o1
        │       │       └── 📄 m_dessert.py
        │       ├── 📂 static
        │       │   └── 📂 practice
        │       │       └── 📂 v0o0o1
        │       │           └── 📂 data
        │       │               └── 📄 desserts1-placeholder.json
        │       ├── 📂 templates
        │       │   └── 📂 practice
        │       │       └── 📂 v0o0o1
        │       │           └── 📂 vuetify
        │       │               └── 📄 textarea2.html
        │       ├── 📂 views
        │       │   └── 📂 v0o0o1
        │       │       └── 📂 vuetify
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_textarea1_to_model.py
        │       └── admin.py
        └── 📂 project1                          # プロジェクト
👉          ├── 📄 urls_practice.py              # こちら
❌          └── 📄 urls.py                       # これではない
```

```py
from django.urls import path


# ...略...


from apps1.practice.views.v0o0o1.vuetify import VuetifyV
#    ----- -------- --------------------        --------
#    1     2        3                           4
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


urlpatterns = [


    # ...略...


    # ビューティファイでテキストエリア１ . 保存用
    path('practice/vuetify/textarea1-to-model',
         # ----------------------------------
         # 1
         VuetifyV.render_textarea1_to_model, name='vuetify_textarea1_to_model'),
    #    ----------------------------------        --------------------------
    #    2                                         3
    # 1. 例えば `http://example.com/practice/vuetify/textarea1-to-model` のような URL のパスの部分
    #                              -----------------------------------
    # 2. VuetifyV クラスの render_textarea1_to_model メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_textarea1_to_model' %} のような形でURLを取得するのに使える

    # ビューティファイでデザート１ . テキストエリア１から . 保存付き
    path('practice/vuetify/save-desserts1-from-textarea1',
         # ---------------------------------------------
         # 1
         VuetifyV.render_save_result_of_desserts1_from_textarea1,
         # -----------------------------------------------------
         # 2
         name='vuetify_save_desserts1_from_textarea1'),
    #          -------------------------------------
    #          3
    # 1. 例えば `http://example.com/practice/vuetify/save-desserts1-from-textarea1` のような URL のパスの部分
    #                              ----------------------------------------------
    # 2. VuetifyV クラスの render_save_result_of_desserts1_from_textarea1 メソッド
    # 3. HTMLテンプレートの中で {% url 'vuetify_save_desserts1_from_textarea1' %} のような形でURLを取得するのに使える
]
```

# Step 12. Web画面へアクセス

👇 1件送信してほしい  

📖 [http://localhost:8000/practice/vuetify/textarea1-to-model](http://localhost:8000/practice/vuetify/textarea1-to-model)  

# Step 13. スーパーユーザーでWebの管理画面へアクセス

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

# Step 14. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice                      # アプリケーション
        │       ├── 📂 migrations
        │       │   ├── 📄 __init__.py
        │       │   ├── ...略...
        │       │   └── 📄 0002_dessert.py
        │       ├── 📂 models
        │       │   └── 📂 v0o0o1
        │       │       └── 📄 m_dessert.py
        │       ├── 📂 static
        │       │   └── 📂 practice
        │       │       └── 📂 v0o0o1
        │       │           └── 📂 data
        │       │               └── 📄 desserts1-placeholder.json
        │       ├── 📂 templates
        │       │   └── 📂 practice
        │       │       └── 📂 v0o0o1
        │       │           └── 📂 vuetify
        │       │               └── 📄 textarea2.html
        │       ├── 📂 views
        │       │   └── 📂 v0o0o1
        │       │       └── 📂 vuetify
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_textarea1_to_model.py
        │       └── admin.py
        └── 📂 project1                          # プロジェクト
            ├── 📄 urls_practice.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/vuetify/textarea1-to-model,ビューティファイでテキストエリア１ . 保存用
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [ソケットを使おう！](https://qiita.com/muzudho1/items/7a6501f7dbafbaa9b96c)  
