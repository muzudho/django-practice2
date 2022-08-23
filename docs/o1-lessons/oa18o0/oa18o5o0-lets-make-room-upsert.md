# サンプルを見る

📖 [この記事のゴール：新規作成](http://tic.warabenture.com:8000/practice/v1/rooms/upsert/)  
📖 [この記事のゴール：更新](http://tic.warabenture.com:8000/practice/v1/rooms/upsert/5/) - 部屋ID は適宜変えてほしい  

# 目標

（※いわゆる CRUD の C と U）  

`http://localhost:8000/practice/v1/rooms/upsert/` へアクセスすると、部屋の新規作成を、  
`http://localhost:8000/practice/v1/rooms/upsert/4/` へアクセスすると、主キーが 4 の部屋の更新をしたい  

## 詳細

👇 表示例（新規作成のとき）:  

```plaintext
部屋の作成

部屋名:                       盤面:                     棋譜:
       --------------------       --------------------     --------------------

送信
戻る
```

👇 表示例（更新のとき）:  

```plaintext
部屋の更新

部屋名: Lion                  盤面: XOXOXOXOX            年齢: 012345678
       --------------------       --------------------      --------------------

送信
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
    ├── 📂 src1                            # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 room
    │   │   │           └── 📄 v1o0.py
    │   │   ├── 📂 tic_tac_toe_v1           # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2           # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       ├── 📂 gui
    │   │       │       └── 📂 think
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
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
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📄 urls.py
    ├── 📂 src2_local                      # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    └── 📄 .gitignore
```

# 手順

## Step OA18o5o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA18o5o0g2o0 画面作成 - room/upsert/v1o0.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 room
                            └── 📂 upsert
👉                              └── 📄 v1o0.html
```

```html
{# OA18o5o0g2o0 #}
<!-- -->
<!DOCTYPE html>
<!-- See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92 -->
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>部屋の作成/更新</title>
        <!-- Bootstrap -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />
    </head>
    <body>
        <div class="container">

            {% if id %}
            <h3 class="page-header">部屋の更新</h3>
            <form action="{% url 'practice_v1_rooms_update' id=id %}" method="post" class="form-horizontal" role="form">
            {% else %}
            <h3 class="page-header">部屋の作成</h3>
            <form action="{% url 'practice_v1_rooms_create' %}" method="post" class="form-horizontal" role="form">
            {% endif %}

                {% csrf_token %}
                {{ form }}

                <div class="form-group">
                    <div class="col-sm-offset-2 col-sm-10">
                        <button type="submit" class="btn btn-primary">送信</button>
                    </div>
                </div>

            </form>
            <a href="{% url 'practice_v1_rooms' %}" class="btn btn-default btn-sm">戻る</a>
        </div>
        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
</html>
```

## Step OA18o5o0g3o0 フォーム作成 - f_room.py ファイル

HTMLタグの `<form>～</form>` の子要素を自動生成させよう。  

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 forms
👉              │   └── 📄 f_room.py
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 room
                            └── 📂 upsert
                                └── 📄 v1o0.html
```

```py
from django.forms import ModelForm

# 部屋モデル
from apps1.practice_v1.models.room.v1o0 import Room
#          -----------             ----        ----
#          11                      12          2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


class RoomForm(ModelForm):
    """OA18o5o0g3o0 対局部屋フォーム"""

    class Meta:
        model = Room  # モデル指定
        fields = ('name', 'board', 'record',)  # フィールド指定
```

## Step OA18o5o0g4o0 ビュー編集 - room フォルダー

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 forms
                │   └── 📄 f_room.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 room
                │           └── 📂 upsert
                │               └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 room
                        └── 📂 v1o0
👉                          └── 📄 __init__.py
```

```py
class RoomV():
    """OA18o2o0g5o0 対局部屋ビュー"""


    # OA18o5o0g4o0 新規作成または更新のページ
    _path_of_upsert_page = "practice_v1/room/upsert/v1o0.html"
    #                       ---------------------------------
    #                       1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/room/upsert/v1o0.html` を取得
    #                                      ---------------------------------


    # ...略...


    @staticmethod
    def render_upsert(request, id=None):
        """OA18o5o0g4o0 新規作成または更新のページ"""

        # 以下のファイルはあとで作ります
        from ..upsert.v1o0 import render_upsert
        #    -------------        -------------
        #    1                    2
        # 1. `src1/apps1/practice_v1/views/room/upsert/v1o0.py`
        #                                       -----------
        # 2. `1.` に含まれる関数

        return render_upsert(request, id, RoomV._path_of_upsert_page)
```

## Step OA18o5o0g5o0 ビュー作成 - room/upsert/v1o0 ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 forms
                │   └── 📄 f_room.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 room
                │           └── 📂 upsert
                │               └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 room
                        ├── 📂 upsert
👉                      │   └── 📄 v1o0.py
                        └── 📂 v1o0
                            └── 📄 __init__.py
```

```py
# BOF OA18o5o0g5o0

from django.shortcuts import get_object_or_404, redirect, render

# 部屋モデル
from apps1.practice_v1.models.room.v1o0 import Room
#          -----------             ----        ----
#          11                      12          2
#    ----------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス

# 部屋フォーム
from apps1.practice_v1.forms.f_room import RoomForm
#          -----------       ------        --------
#          11                12            2
#    ------------------------------
#    10
# 10, 12. ディレクトリー名
# 11. アプリケーション名
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_upsert(request, id, room_upsert_tp):
    """OA18o5o0g5o0 新規作成または更新のページ

    Parameters
    ----------
    room_upsert_tp : str
        Template path
    """

    if id:  # idがあるとき（更新の時）
        # idで検索して、結果を戻すか、404エラー
        room = get_object_or_404(Room, pk=id)
    else:  # idが無いとき（作成の時）
        room = Room()

    # POSTの時（作成であれ更新であれ送信ボタンが押されたとき）
    if request.method == 'POST':
        # フォームを生成
        form = RoomForm(request.POST, instance=room)

        # Valid なら保存して一覧画面へ
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            return redirect('practice_v1_rooms')

        # Invalid ならフォームを引き継いで再び同じ画面表示へ

    else:  # GETの時（フォームを生成）
        form = RoomForm(instance=room)

    # 作成・更新画面を表示
    return render(request, room_upsert_tp, dict(form=form, id=id))

# EOF OA18o5o0g5o0
```

## ~~Step OA18o5o0g6o0~~

Merged to OA18o5o0g6o1o0  

## Step OA18o5o0g6o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_v1                      # アプリケーション
    │           ├── 📂 forms
    │           │   └── 📄 f_room.py
    │           ├── 📂 templates
    │           │   └── 📂 practice_v1
    │           │       └── 📂 room
    │           │           └── 📂 upsert
    │           │               └── 📄 v1o0.html
    │           └── 📂 views
    │               └── 📂 room
    │                   ├── 📂 upsert
    │                   │   └── 📄 v1o0.py
    │                   └── 📂 v1o0
    │                       └── 📄 __init__.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_tic_tac_toe_v2_autogen.py,practice/v1/rooms/upsert/,practice_v1_rooms_create,"OA18o5o0g6o1o0 対局部屋の新規作成",apps1.practice_v1.views.room.v1o0,RoomV,RoomVV1o0,render_upsert
../src1/project1/urls_tic_tac_toe_v2_autogen.py,practice/v1/rooms/upsert/<int:id>/,practice_v1_rooms_update,"OA18o5o0g6o1o0 対局部屋の更新",apps1.practice_v1.views.room.v1o0,RoomV,RoomVV1o0,render_upsert
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

## Step OA18o5o0g7o0 Web画面へアクセス

👇 作成するとき、部屋ID は付けるな  

📖 [http://localhost:8000/practice/v1/rooms/upsert/](http://localhost:8000/practice/v1/rooms/upsert/)  

👇 更新するとき、部屋ID を付けろ。 部屋ID は適宜変えてほしい  

📖 [http://localhost:8000/practice/v1/rooms/upsert/5/](http://localhost:8000/practice/v1/rooms/upsert/5/)  

## Step OA18o5o0g8o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
        │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 forms
        │       │   └── 📄 f_room.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 room
        │       │           └── 📂 upsert
        │       │               └── 📄 v1o0.html
        │       └── 📂 views
        │           └── 📂 room
        │               ├── 📂 upsert
        │               │   └── 📄 v1o0.py
        │               └── 📂 v1o0
        │                   └── 📄 __init__.py
        └── 📂 project1                          # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/rooms/upsert/,対局部屋の新規作成
/practice/v1/rooms/upsert/5/,対局部屋の更新
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでユーザーホームを作ろう！](https://qiita.com/muzudho1/items/37532c83235b7f9e60c9)  

# 参考にした記事

📖 [DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92)
