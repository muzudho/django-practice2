# 目的

サーバーに、部屋を記憶したい  

# はじめに

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key              | Value                                     |
| ---------------- | ----------------------------------------- |
| OS               | Windows10                                 |
| Container        | Docker                                    |
| Database         | Postgresql, (Redis)                       |
| Program Language | Python 3                                  |
| Web framework    | Django                                    |
| Auth             | allauth                                   |
| Frontend         | Vuetify                                   |
| Data format      | JSON                                      |
| Others           | (Socket), Web socket                      |
| Editor           | Visual Studio Code （以下 VSCode と表記） |

参考にした元記事は 📖[DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92) だ。  
わたしの記事は単に **やってみた** ぐらいの位置づけだ  

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 host_local1                      # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    ├── 📂 host1                            # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   ├── 📂 tic_tac_toe_v1           # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2           # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o1o0
    │   │       │           └── 📂 think
    │   │       │               ├── 📄 concepts.js
    │   │       │               ├── 📄 engine.js
    │   │       │               ├── 📄 judge_ctrl.js
    │   │       │               ├── 📄 position.js
    │   │       │               ├── 📄 things.js
    │   │       │               └── 📄 user_ctrl.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o1o0
    │   │       │           └── 📂 think
    │   │       │               └── 📄 engine_manual.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 o1o0
    │   │       │       └── 📂 think
    │   │       │           └── 📂 engine_manual
    │   │       │               ├── 📄 __init__.py
    │   │       │               └── 📄 v_render.py
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
    │   │   ├── 📄 urls_tic_tac_toe_v1.py
    │   │   ├── 📄 urls_tic_tac_toe_v2.py
    │   │   ├── 📄 urls.py
    │   │   ├── 📄 ws_urls_tic_tac_toe_v1.py
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

# Step 2. モデル作成 - m_room.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1              # アプリケーション
                └── 📂 models
                    └── 📂 o1o0
👉                      └── 📄 m_room.py
```

```py
# See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92
from django.db import models


class Room(models.Model):
    """部屋のモデル"""

    # プロパティの仕様を決める感じで

    # 部屋名
    # -----
    # Example: Elephant
    name = models.CharField('部屋名', max_length=25)

    # 対局者_先手Id
    # ------------
    # Example: 1
    sente_id = models.IntegerField('対局者_先手Id', null=True, blank=True)

    # 対局者_後手Id
    # ------------
    # Example: 2
    gote_id = models.IntegerField('対局者_後手Id', null=True, blank=True)

    # 盤面
    # ----
    # Example: ..O.X.X..
    # +--+--+--+
    # |  |  | O|
    # +--+--+--+
    # |  | X|  |
    # +--+--+--+
    # | X|  |  |
    # +--+--+--+
    board = models.CharField('盤面', max_length=9)

    # 棋譜
    # ----
    # Example: 426
    record = models.CharField('棋譜', max_length=9)

    def __str__(self):
        """このオブジェクトを文字列にしたとき返るもの"""
        return self.name
```

# Step 3. データベースへモデル登録 - admin.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1              # アプリケーション
                └── 📂 models
                    ├── 📂 o1o0
                    │   └── 📄 m_room.py
👉                  └── 📄 admin.py
```

👇 追加したものだけ示す  

```py
# ...略...


# 対局部屋
from .models.o1o0.m_room import Room
#    -------------------        ----
#    1                          2
# 1. このファイルと同じディレクトリにある `models/o1o0/m_room.py` ファイルの拡張子抜き
#                                      ------------------
# 2. クラス名


# ...略...


# Register your models here.
#   └── * 管理画面にモデルが表示されるようになる
#       └── * `manage.py makemigrations` コマンドの実行対象になる


# ...略...


admin.site.register(Room)
```

これにより、 👇 以下の２つを満たす  

* 管理画面に Room オブジェクトが表示される
* マイグレーションの対象になる

# Step 4. マイグレーションファイル作成 - makemigrations コマンド

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

docker-compose run --rm web python3 manage.py makemigrations practice_v1 --settings project1.settings
#                                                            -----------            -----------------
#                                                            1                      2
# 1. アプリケーション
# 2. host1/project1/settings.py
#          -----------------
```

👇 以下のファイルが生成される  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                      # アプリケーション
                ├── 📂 migrations
                │   ├── 📄 ...略...
👉              │   └── 📄 0004_room.py          # ファイル名は一例です
                └── 📂 models
                    └── 📂 o1o0
                        └── 📄 m_room.py
```

👆 このファイルは マイグレーション ファイル と呼ぶらしい  

まだ マイグレーション作業は完了していない  

# Step 5. マイグレーション - migrate コマンド

```shell
docker-compose run --rm web python manage.py migrate
```

👆 ここまでやって マイグレーション という作業が終わるらしい  

# Step 6. スーパーユーザーでWebの管理画面へアクセス

👇 スーパーユーザーでログインすること  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

👇 画面左に以下のように表示されていればOK  

```plaintext
+----------------------------------+
| PRACTICE                         |
+-------------+--------+-----------+
| Rooms       | ➕ Add | 🖊 Change |
+-------------+--------+-----------+
```

# Step 7. Room を３つほど追加してほしい

`➕ Add` をクリックしてほしい  

```plaintext
部屋名:
      ----------------

対局者_先手Id:
             ----------------

対局者_後手Id:
             ----------------

盤面:
    ----------------

棋譜:
    ----

                [Save and add another] [Save and continue editing] [SAVE]
```

👆入力フォームが出てくるから、３件ほど適当に追加してほしい。  

入力例:  

```plaintext
部屋名        対局者_先手Id  対局者_後手Id  盤面       棋譜
-----------  ------------  ------------  ---------  ---------
Elephant                1             2  XOXOXOXOX  012345678
Giraffe                 3             4  XOXOXOXOX  012345678
Lion                    5             6  XOXOXOXOX  012345678
```

`[SAVE]` が追加ボタンのようだ。  

# Step 8. 登録した Room を確認してほしい

`➕ Add` の左側にある `Rooms` リンクをクリックしてほしい。  
一覧画面が出てくる  

３つの部屋が出てくればOKだ  

# 次の記事

📖 [Djangoでゲーム対局部屋を一覧しよう！](https://qiita.com/muzudho1/items/346c286d4f99850afe23)  
