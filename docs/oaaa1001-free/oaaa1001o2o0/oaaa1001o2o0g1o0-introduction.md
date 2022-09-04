# 目標

| What is        | This is                                                                                       |
| -------------- | --------------------------------------------------------------------------------------------- |
| この連載の目的 | 連続名（Consecutive name）ツール を作る                                                       |
| この記事の目標 | いきなり 連続名（Consecutive name）ツール を作るのは難しいから、まず白紙のWebページを開設する |

# 情報

この記事はレッスン編を読み終えた人を対象とする  

| What is    | This is                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------- |
| レッスン編 | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

# 始める前に

👇 まず、継続（Continue）と 連続（Consecutive） の違いを説明する  

* 継続：　`１` → `１` → `１` → `１`
* 連続：　`１` → `２` → `３` → `４`

👇 連続名（Consecutive name）の分かりやすい例は以下を参考  

📖 [出世魚ってどんな魚？？](https://ikimall.ikimonopal.jp/blog/post-2324/)  
📖 [世界コンピュータ将棋選手権のプログラム別順位の推移](http://www.yss-aya.com/csa_all.html)  

👇 連続名（Consecutive name）の必要性は、主に 以下のことを決める需要からある  

* 何年連続出場というカウントを引き継ぐチーム
* 前年の順位のシード権を引き継ぐチーム
* 新人賞の候補となるチーム

👇 以下は「連続」。前と後ろで違うがつながっている。何と何が連続しているか判定する方法は人為的だ。このツールは記録と表示のみ行う  

* 去年 Apple という名前のチームが 今年は Banana という名前で出場している  
* 去年 Cherry という名前のチームが、今年は Durian と Eggfruit という名前で出場している  
* 去年 Fig と Grape という名前のチームが、今年は合体して Hernandia という名前で出場している  

👇 以下は「継続」。前と後ろで違わずつながっている。特に問題なし  

* 去年 Icaco という名前のチームが 今年も Icaco という名前で出場している  
* 数年ぶりに Jujube という名前のチームが出場している  

# Step OAAA1001o2o0g1o0 Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step OAAA1001o2o0g2o0 フォルダー作成 - apps1/consecutive_name_vol1o0 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1                            # 複数のアプリケーションを入れるフォルダー
            └── 📂 consecutive_name_vol1o0   # アプリケーション
```

# Step OAAA1001o2o0g3o0 アプリケーション作成

Dockerコンテナ を起動しているターミナルとは別のターミナルをもう１つ開き、  

👇 以下のコマンドを打鍵してほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# アプリケーション新規作成
docker-compose run --rm web python manage.py startapp consecutive_name_vol1o0 ./apps1/consecutive_name_vol1o0 --settings=project1.settings
#                                                     ----------------------- -------------------------------            -----------------
#                                                     1                       2                                          3
# 1. 任意のDjangoアプリケーション名
# 2. アプリケーション フォルダーへのパス
# 3. `src1/project1/settings.py` 設定ファイルに従う
#          -----------------
```

👇 以下のようなディレクトリー、ファイルが自動生成される  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0       # アプリケーション
👉              ├── 📂 migrations
👉              │   └── 📄 __init__.py
👉              ├── 📄 __init__.py
👉              ├── 📄 admin.py
👉              ├── 📄 apps.py
👉              ├── 📄 models.py
👉              ├── 📄 tests.py
👉              └── 📄 views.py
```

# Step OAAA1001o2o0g4o0 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0       # アプリケーション名
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
                ├── 📄 apps.py
👉              ├── 📄 models.py
                ├── 📄 tests.py
👉              └── 📄 views.py
```

# Step OAAA1001o2o0g5o0 アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 consecutive_name_vol1o0       # アプリケーション
                ├── 📂 migrations
                │   └── 📄 __init__.py
                ├── 📄 __init__.py
                ├── 📄 admin.py
👉              ├── 📄 apps.py
                └── 📄 tests.py
```

```py
from django.apps import AppConfig


class NameOfConsecutiveVol1O0Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    # name = 'consecutive_name_vol1o0'
    # * [OAAA1001o2o0g5o0] 変更後
    name = 'apps1.consecutive_name_vol1o0'
    #       -----------------------------
    #       1
    # 1. `src1/apps1/consecutive_name_vol1o0/apps.py`
    #          -----------------------------
```

# Step OAAA1001o2o0g6o0 アプリケーション登録 - settings.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 consecutive_name_vol1o0       # アプリケーション
        │       ├── 📂 migrations
        │       │   └── 📄 __init__.py
        │       ├── 📄 __init__.py
        │       ├── 📄 admin.py
        │       ├── 📄 apps.py
        │       └── 📄 tests.py
        └── 📂 project1
👉          └── 📄 settings.py
```

```py
# ...略...


INSTALLED_APPS = [
    # ...略...
    # あなたが追加したアプリケーション
    # ...略...


    # [OAAA1001o2o0g6o0] 連続名1.0巻
    'apps1.consecutive_name_vol1o0',


    # ...略...
    # Djangoの標準アプリケーション
    # ...略...
]


# ...略...
```
