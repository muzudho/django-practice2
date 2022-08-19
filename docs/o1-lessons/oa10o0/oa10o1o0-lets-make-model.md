# 目標

（クライアント側ではなく）サーバー側に、データを記憶したい  

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
    │   │   ├── 📂 allauth_customized_v1        # アプリケーション名
    │   │   ├── 📂 portal_v1                    # アプリケーション名
    │   │   └── 📂 practice_v1                  # アプリケーション名
    │   ├── 📂 data
    │   ├── 📂 project1                         # プロジェクト名
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

# 手順

## Step OA10o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA10o1o0g2o0 モデル作成 - prefecture/v1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1          # アプリケーション フォルダー
                └── 📂 models
                    └── 📂 prefecture
👉                      └── 📄 v1o0.py
```

```py
# See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92
from django.db import models


class Prefecture(models.Model):
    """OA10o1o0g2o0 都道府県"""

    # プロパティの仕様を決める感じで
    seq = models.AutoField('連番', primary_key=True)
    name = models.CharField('名前', max_length=4)
    # email = models.CharField('E-Mail', max_length=255)
    # age = models.IntegerField('年齢', blank=True, default=0)
    # stateInPark = models.IntegerField('状態1', blank=False, default=0)

    def __str__(self):
        """このオブジェクトを文字列にしたとき返るもの"""
        return f"{self.name} prefecture"
```

## Step OA10o1o0g3o0 モデル登録 - admin.py ファイル

👇 以下の既存ファイルに追記してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1          # アプリケーション
👉              └── 📄 admin.py
```

```py
# ...略...


# OA10o1o0g3o0 都道府県
from .models.prefecture.v1o0 import Prefecture
#    -----------------------        ----------
#    1                              2
# 1. このファイルと同じディレクトリにある `models/prefecture/v1o0.py` ファイルの拡張子抜き
#                                      ----------------------
# 2. クラス


# ...略...


# Register your models here.
#   └── * 管理画面にモデルが表示されるようになる
#       └── * `manage.py makemigrations` コマンドの実行対象になる


# ...略...


# OA10o1o0g3o0 都道府県
admin.site.register(Prefecture)
```

👆 管理画面に Prefecture オブジェクトが表示されるようにしている  

## Step OA10o1o0g4o0 マイグレーション ファイル生成 - コマンド実行＜その１＞

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
# cd src1

docker-compose run --rm web python3 manage.py makemigrations practice_v1
#                                                            -----------
#                                                            1
# 1. アプリケーション名
#    settings.py に `apps1.practice_v1` と 書いていても、ここには `practice_v1` と書く
```

以下のディレクトリーとファイルが生成される  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1          # アプリケーション
                └── 📂 migrations
                    ├── 📄 __init__.py
                    └── 📄 0001_initial.py
```

👆 この生成されたファイルは マイグレーション ファイル と呼ぶらしい  

まだ マイグレーション作業は完了していない  

## Step OA10o1o0g5o0 マイグレーション - コマンド実行＜その２＞

```shell
docker-compose run --rm web python manage.py migrate
```

👆 ここまでやって マイグレーション という作業が終わるらしい  

## Step OA10o1o0g6o0 スーパーユーザーでWebの管理画面へアクセス

👇 スーパーユーザーでログインすること  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

👇 画面左に以下のように表示されていればOK  

```plain
+----------------------------------+
| PRACTICE                         |
+-------------+--------+-----------+
| Prefecuters | ➕ Add | 🖊 Change |
+-------------+--------+-----------+
```

## Step OA10o1o0g7o0 Prefecture を３つほど追加してほしい

Prefectures ラベルの右横の `➕ Add` リンクをクリックしてほしい  

```plaintext
名前:
     ----------------

                [Save and add another] [Save and continue editing] [SAVE]
```

👆 入力フォームが出てくるから、３件ほど適当に追加してほしい。  
`[SAVE]` が追加ボタンのようだ  

## Step OA10o1o0g8o0 登録した Prefecture を確認してほしい

`Prefectures` ラベルをクリックすると、一覧画面が出てくる  

# 次の記事

📖 [Djangoでモデルの中身をダンプ出力しよう！](https://qiita.com/muzudho1/items/5db218ed0f12bae43d18)  

# 参考にした記事

📖 [Django model data types and fields list](https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/)  
