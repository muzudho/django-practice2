# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1.0/rooms/delete/ver1.0/1/) - 部屋IDは適宜変えてほしい  

# 目標

（※いわゆる CRUD の D）  

`http://localhost:8000/practice/vol1.0/rooms/delete/ver1.0/4/` へアクセスすると、  
id が 4 の部屋を削除したい  

## 詳細

表示例:  

```plaintext
部屋の削除

「Lion」を削除しました。

戻る
```

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is          | This is                                   |
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
    ├── 📂 src1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 accounts_vol1o0    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_vol1o0              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 room
    │   │   │           └── 📄 ver1o0.py
    │   │   ├── 📂 tic_tac_toe_vol1o0        # アプリケーション
    │   │   └── 📂 tic_tac_toe_vol2o0        # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_vol2o0
    │   │       │       ├── 📂 gui
    │   │       │       └── 📂 think
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_vol2o0
    │   │       │       ├── 📂 gui
    │   │       │       └── 📂 think
    │   │       ├── 📂 views
    │   │       │   ├── 📂 gui
    │   │       │   └── 📂 think
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
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📄 urls.py
    ├── 📂 src2_local                   # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# 手順

## Step OA18o4o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA18o4o0g2o0 画面作成 - delete.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_vol1o0          # アプリケーションと同名
                        └── 📂 room
                            └── 📂 delete
👉                              └── 📄 ver1o0.html
```

```html
<!-- BOF OA18o4o0g2o0 -->
<!-- -->
<!DOCTYPE html>
<!-- See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92 -->
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>部屋削除</title>
        <!-- Bootstrap -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />
    </head>
    <body>
        <div class="container">
            <h3>部屋の削除</h3>
            <div class="card" style="width: 18rem">「{{ room.name }}」を削除しました。</div>
            <a href="{% url 'practice_vol1o0_rooms' %}" class="btn btn-default btn-sm">戻る</a>
        </div>
        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
</html>
<!-- EOF OA18o4o0g2o0 -->
```

## Step OA18o4o0g3o0 ビュー編集 - room/v1o0 フォルダー

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 room
                │           └── 📂 delete
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 room
                        └── 📂 ver1o0
👉                          └── 📄 __init__.py
```

```py
class RoomV():
    """OA18o2o0g5o0 対局部屋ビュー"""
    # ...略...


    # OA18o4o0g3o0 練習1.0巻 削除1.0版
    _path_of_delete_page = "practice_vol1o0/room/delete/ver1o0.html"
    #                       ---------------------------------------
    #                       1
    # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/room/delete/ver1o0.html` を取得
    #                                          ---------------------------------------


    # ...略...


    @staticmethod
    def render_delete(request, id):
        """OA18o4o0g3o0 練習1.0巻 削除1.0版"""

        # 以下のファイルはあとで作ります
        from ..delete.ver1o0 import render_delete
        #    ---------------        -------------
        #    1                      2
        # 1. `src1/apps1/practice_vol1o0/views/room/delete/ver1o0.py`
        #                                           -------------
        # 2. `1.` に含まれる関数

        return render_delete(request, id, RoomV._path_of_delete_page)
```

## Step OA18o4o0g4o0 ビュー作成 - room/delete/v1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0                  # アプリケーション
                ├── 📂 templates
                │   └── 📂 practice_vol1o0
                │       └── 📂 room
                │           └── 📂 delete
                │               └── 📄 ver1o0.html
                └── 📂 views
                    └── 📂 room
                        ├── 📂 delete
👉                      │   └── 📄 ver1o0.py
                        └── 📂 ver1o0
                            └── 📄 __init__.py
```

```py
# BOF OA18o4o0g4o0

from django.shortcuts import render, get_object_or_404

# 部屋モデル
from apps1.practice_vol1o0.models.room.ver1o0 import Room
#          ---------------             ------        ----
#          11                          12            2
#    ----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_delete(request, room_pk, room_delete_tp):
    """OA18o4o0g4o0 削除ページ

    Parameters
    ----------
    room_delete_tp : str
        Template path
    """

    room = get_object_or_404(Room, pk=room_pk)  # idを指定してメンバーを１人取得

    name = room.name  # 名前だけまだ使う
    room.delete()
    context = {
        'room': {
            'name': name
        }
    }
    return render(request, room_delete_tp, context)

# EOF OA18o4o0g4o0
```

## ~~Step OA18o4o0g5o0~~

Merged to OA18o4o0g5o1o0  

## Step OA18o4o0g5o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_vol1o0                  # アプリケーション
    │           ├── 📂 templates
    │           │   └── 📂 practice_vol1o0
    │           │       └── 📂 room
    │           │           └── 📂 delete
    │           │               └── 📄 ver1o0.html
    │           └── 📂 views
    │               └── 📂 room
    │                   ├── 📂 delete
    │                   │   └── 📄 ver1o0.py
    │                   └── 📂 ver1o0
    │                       └── 📄 __init__.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/rooms/delete/ver1.0/<int:id>/,practice_vol1o0_rooms_delete,"OA18o4o0g5o1o0 練習1.0巻 対局部屋の削除1.0版",apps1.practice_vol1o0.views.room.ver1o0,RoomV,RoomVV1o0,render_delete
```

## Step OA18o4o0g5o2o0 ルート編集 - コマンド打鍵

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

## Step OA18o4o0g6o0 Web画面へアクセス

👇 部屋の番号は適宜変えてほしい  

📖 [http://localhost:8000/practice/vol1.0/rooms/delete/ver1.0/1/](http://localhost:8000/practice/vol1.0/rooms/delete/ver1.0/1/)  

## Step OA18o4o0g7o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_vol1o0                      # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 room
        │       │           └── 📂 delete
        │       │               └── 📄 ver1o0.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 room
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_delete.py
        └── 📂 project1                          # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/vol1.0/rooms/delete/ver1o0/1/,OA18o4o0g7o0 練習1.0巻 対局部屋の削除1.0版 Id=1
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでゲーム対局部屋を作成または更新しよう！](https://qiita.com/muzudho1/items/6eaf6cf90fe5a6519184)  
