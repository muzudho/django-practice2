# 目標

| What is        | This is                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------- |
| この連載の目的 | 連続名（Consecutive name）ツール を作る                                                  |
| この記事の目標 | いきなり 連続名（Consecutive name）ツール を作るのは難しいから、まずマスターデータを作る |

# 情報

👇 この記事はレッスン編と前回の記事を読み終えた人を対象とする  

| What is    | This is                                                                                                          |
| ---------- | ---------------------------------------------------------------------------------------------------------------- |
| レッスン編 | 📖 [[O1o1o0] DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |
| 前回の記事 | 📖 [[OAAA1001o2o0] 連続名ツールを作ろう！](https://qiita.com/muzudho1/items/0ae87ae14ee28ccbb08e)                 |

👇 Step の変な数字の説明  

📖 [電脳向量表記](https://qiita.com/muzudho1/items/fdbf31e41dd8c247081f)  

# 手順

## Step [OAAA1001o2o1o0g1o0] Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step [OAAA1001o2o1o0g2o0] マスターデータ作成 - events/ver1o0.json ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                └── 📂 static
                    └── 📂 consecutive_name_vol1o0      # アプリケーションと同名
                        └── 📂 data
                            └── 📂 events
👉                              └── 📄 ver1o0.json
```

```json
{
    "events": [
        {
            "id": "1",
            "display_name": "2020春",
            "sort": 1.1
        },
        {
            "id": "2",
            "display_name": "2020冬",
            "sort": 1.2
        },
        {
            "id": "3",
            "display_name": "2021春",
            "sort": 1.3
        },
        {
            "id": "4",
            "display_name": "2021冬",
            "sort": 1.4
        },
        {
            "id": "5",
            "display_name": "2022春",
            "sort": 1.5
        },
        {
            "id": "6",
            "display_name": "2022冬",
            "sort": 1.6
        }
    ]
}
```

## Step [OAAA1001o2o1o0g3o0] モデル作成 - events/ver1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                └── 📂 models
                    └── 📂 events
                        └── 📄 ver1o0.py
```

```py
# BOF [OAAA1001o2o1o0g3o0]

# See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92
from django.db import models


class Event(models.Model):
    """[OAAA1001o2o1o0g3o0] イベント"""

    # プロパティの仕様を決める感じで
    id = models.AutoField('Id', primary_key=True)
    display_name = models.CharField('表示名', max_length=32)
    sort = models.IntegerField('順番', blank=True, default=0)

    def __str__(self):
        """このオブジェクトを文字列にしたとき返るもの"""
        return f"{self.display_name} event"

# EOF [OAAA1001o2o1o0g3o0]
```

## Step [OAAA1001o2o1o0g3o0] モデル登録 - admin.py ファイル

👇 以下の既存ファイルに追記してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0          # アプリケーション
👉              └── 📄 admin.py
```

```py
# ...略...


# OA10o1o0g3o0 練習1.0巻 都道府県1.0版
from .models.prefecture.ver1o0 import Prefecture
#    -------------------------        ----------
#    1                                2
# 1. このファイルと同じディレクトリにある `models/prefecture/ver1o0.py` ファイルの拡張子抜き
#                                      ------------------------
# 2. クラス


# ...略...


# Register your models here.
#   └── * 管理画面にモデルが表示されるようになる
#       └── * `manage.py makemigrations` コマンドの実行対象になる


# ...略...


# OA10o1o0g3o0 練習1.0巻 都道府県1.0版
admin.site.register(Prefecture)
```
