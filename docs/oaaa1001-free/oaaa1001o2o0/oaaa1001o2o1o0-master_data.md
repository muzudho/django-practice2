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

## Step [OAAA1001o2o1o0g2o0] マスターデータ作成 - data/event/ver1o0.json ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                └── 📂 static
                    └── 📂 consecutive_name_vol1o0      # アプリケーションと同名
                        └── 📂 data
                            └── 📂 event
👉                              └── 📄 ver1o0.json
```

```json
{
    "events": [
        {
            "id": "1",
            "event": "ダミーデータを扱う大会",
            "event_s": "ダミー大会",
            "sort": 1.1
        },
        {
            "id": "2",
            "event": "予備データを眺める選手権",
            "event_s": "予備デー選手権",
            "sort": 1.2
        }
    ]
}
```

## Step [OAAA1001o2o1o0g2o1o0] マスターデータ作成 - data/volume/ver1o0.json ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                └── 📂 static
                    └── 📂 consecutive_name_vol1o0      # アプリケーションと同名
                        └── 📂 data
                            └── 📂 volume
👉                              └── 📄 ver1o0.json
```

```json
{
    "events": [
        {
            "event_id": "1",
            "id": "1",
            "volume": "2020年スプリング杯",
            "volume_s": "2020春",
            "sort": 1.1
        },
        {
            "event_id": "1",
            "id": "2",
            "volume": "2020年ウィンター杯",
            "volume_s": "2020冬",
            "sort": 1.2
        },
        {
            "event_id": "1",
            "id": "3",
            "volume": "2021年スプリング杯",
            "volume_s": "2021春",
            "sort": 1.3
        },
        {
            "event_id": "1",
            "id": "4",
            "volume": "2021年ウィンター杯",
            "volume_s": "2021冬",
            "sort": 1.4
        },
        {
            "event_id": "1",
            "id": "5",
            "volume": "2022春スプリング杯",
            "volume_s": "2022春",
            "sort": 1.5
        },
        {
            "event_id": "1",
            "id": "6",
            "volume": "2022冬スプリング杯",
            "volume_s": "2022冬",
            "sort": 1.6
        }
    ]
}
```

## Step [OAAA1001o2o1o0g3o0] モデル作成 - event/ver1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                └── 📂 models
                    └── 📂 event
                        └── 📄 ver1o0.py
```

```py
# BOF [OAAA1001o2o1o0g3o0]

# See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92
from django.db import models


class Event(models.Model):
    """[OAAA1001o2o1o0g3o0] 催事種別"""

    # プロパティの仕様を決める感じで
    id = models.AutoField('Id', primary_key=True)
    name = models.CharField('名称', max_length=32, blank=True, null=True)
    name_s = models.CharField('名称_短縮', max_length=16, blank=True, null=True)
    sort = models.IntegerField('順番', blank=True, default=0)

    def __str__(self):
        """このオブジェクトを文字列にしたとき返るもの"""
        return f"{self.display_name} event"

# EOF [OAAA1001o2o1o0g3o0]
```

## Step [OAAA1001o2o1o0g3o1o0] モデル作成 - event_volume/ver1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                └── 📂 models
                    ├── 📂 event
                    │   └── 📄 ver1o0.py
                    └── 📂 event_volume
👉                      └── 📄 ver1o0.py
```

```py
# BOF [OAAA1001o2o1o0g3o1o0]

# See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92
from django.db import models


class EventVolume(models.Model):
    """[OAAA1001o2o1o0g3o1o0] 催事巻"""

    # プロパティの仕様を決める感じで
    id = models.AutoField('Id', primary_key=True)
    event_id = models.IntegerField('催事種別Id', blank=True, default=0)
    name = models.CharField('名称', max_length=64, blank=True, null=True)
    name_s = models.CharField('名称_短縮', max_length=16, blank=True, null=True)
    sort = models.IntegerField('順番', blank=True, default=0)

    def __str__(self):
        """このオブジェクトを文字列にしたとき返るもの"""
        return f"{self.display_name} event-volume"

# EOF [OAAA1001o2o1o0g3o1o0]
```

## Step [OAAA1001o2o1o0g4o0] モデル登録 - admin.py ファイル

👇 以下の既存ファイルに追記してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                ├── 📂 models
                │   └── 📂 event
                │       └── 📄 ver1o0.py
👉              └── 📄 admin.py
```

```py
# ...略... from django.contrib import admin


# [OAAA1001o2o1o0g4o0] 連続名1.0巻 催事種別1.0版
from .models.event.ver1o0 import Event
#    --------------------        -----
#    1                           2
# 1. このファイルと同じディレクトリにある `models/event/ver1o0.py` ファイルの拡張子抜き
#                                      ----------------------
# 2. クラス

# [OAAA1001o2o1o0g4o0] 連続名1.0巻 催事巻1.0版
from .models.event_volume.ver1o0 import EventVolume


# ...略...


# Register your models here.
#   └── * 管理画面にモデルが表示されるようになる
#       └── * `manage.py makemigrations` コマンドの実行対象になる


# ...略...


# [OAAA1001o2o1o0g4o0] 連続名1.0巻 催事種別1.0版
admin.site.register(Event)

# [OAAA1001o2o1o0g4o0] 連続名1.0巻 催事巻1.0版
admin.site.register(EventVolume)
```

👆 管理画面に EventVolume オブジェクトが表示されるようにしている  

## Step [OAAA1001o2o1o0g5o0] マイグレーション ファイル生成 - コマンド実行

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
# cd src1

docker-compose run --rm web python3 manage.py makemigrations consecutive_name_vol1o0
#                                                            -----------------------
#                                                            1
# 1. アプリケーション
#    settings.py に `apps1.consecutive_name_vol1o0` と 書いていても、ここには `consecutive_name_vol1o0` と書く
```

👇 以下のファイルが生成される  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0              # アプリケーション
                ├── 📂 migrations
                │   ├── 📄 __init__.py
👉              │   └── 📄 0001_initial.py
                ├── 📂 models
                │   └── 📂 event
                │       └── 📄 ver1o0.py
👉              └── 📄 admin.py
```

👆 この生成されたファイルは マイグレーション ファイル と呼ぶらしい  

まだ マイグレーション作業は完了していない  

## Step [OAAA1001o2o1o0g6o0] マイグレーション - コマンド実行

```shell
docker-compose run --rm web python manage.py migrate
```

👆 ここまでやって マイグレーション という作業が終わるらしい  

## Step [OAAA1001o2o1o0g7o0] スーパーユーザーでWebの管理画面へアクセス

👇 スーパーユーザーでログインすること  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

👇 画面左に以下のように表示されていればOK  

```plain
+----------------------------------+
| CONSECUTIVE_NAME_VOL1O0          |
+-------------+--------+-----------+
| Events      | ➕ Add | 🖊 Change |
+-------------+--------+-----------+
```

## Step [OAAA1001o2o1o0g8o0] EventVolume を３つほど追加してほしい

Events ラベルの右横の `➕ Add` リンクをクリックしてほしい  

```plaintext
表示名:
       ----------------
順番:   0
       ----------------

                [Save and add another] [Save and continue editing] [SAVE]
```

👆 入力フォームが出てくるから、３件ほど適当に追加してほしい。  
`[SAVE]` が追加ボタンのようだ  
