# 目的

（※いわゆる CRUD の C と U）  

`http://localhost:8000/practice/v1/rooms/upsert/` へアクセスすると、部屋の新規作成を、  
`http://localhost:8000/practice/v1/rooms/upsert/4/` へアクセスすると、主キーが 4 の部屋の更新をしたい  

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

# はじめに

この記事は LessonO1 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    ├── 📂 host_local1                   # Djangoとは関係ないもの
    │    ├── 📂 sockapp1
    │    └── 📂 websockapp1
    ├── 📂 host1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1    # アプリケーション
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   ├── 📂 practice_v1              # アプリケーション
    │   │   │   ├── 📂 migrations
    │   │   │   └── 📂 models
    │   │   │       └── 📂 o1
    │   │   │           └── 📄 m_room.py
    │   │   ├── 📂 tic_tac_toe_v1        # アプリケーション
    │   │   └── 📂 tic_tac_toe_v2        # アプリケーション
    │   │       ├── 📂 migrations
    │   │       │   └── 📄 __init__.py
    │   │       ├── 📂 static
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o1
    │   │       │           └── 📂 think
    │   │       │               ├── 📄 concepts.js
    │   │       │               ├── 📄 engine.js
    │   │       │               ├── 📄 judge_ctrl.js
    │   │       │               ├── 📄 position.js
    │   │       │               ├── 📄 things.js
    │   │       │               └── 📄 user_ctrl.js
    │   │       ├── 📂 templates
    │   │       │   └── 📂 tic_tac_toe_v2
    │   │       │       └── 📂 o1
    │   │       │           └── 📂 think
    │   │       │               └── 📄 engine_manual.html
    │   │       ├── 📂 views
    │   │       │   └── 📂 o1
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

# Step 2. 画面作成 - upsert.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 o1
                            └── 📂 room
👉                              └── 📄 upsert.html
```

```html
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

# Step 3. フォーム作成 - f_room.py ファイル

HTMLタグの `<form>～</form>` の子要素を自動生成させよう。  

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 forms
👉              │   └── 📄 f_room.py
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 o1
                            └── 📂 room
                                └── 📄 upsert.html
```

```py
from django.forms import ModelForm

from apps1.practice_v1.models.o1.m_room import Room
#          -----------           ------        ----
#          1.1                   1.2           2
#    ----------------------------------
#    1
# 1, 1.2 ディレクトリー
# 1.1 アプリケーション
# 2. `1.2` に含まれる __init__.py ファイルにさらに含まれるクラス


class RoomForm(ModelForm):
    class Meta:
        model = Room  # モデル指定
        fields = ('name', 'board', 'record',)  # フィールド指定
```

# Step 4. ビュー モジュール編集 - room フォルダー

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 forms
                │   └── 📄 f_room.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o1
                │           └── 📂 room
                │               └── 📄 upsert.html
                └── 📂 views
                    └── 📂 o1
                        └── 📂 room
👉                          └── 📄 __init__.py
```

```py
class RoomV():
    # ...略...


    # 新規作成または更新のページ
    _path_of_upsert_page = "practice_v1/o1/room/upsert.html"
    #                       -------------------------------
    #                       1
    # 1. `host1/apps1/practice_v1/templates/practice_v1/o1/room/upsert.html` を取得
    #                                       -------------------------------


    # ...略...


    @staticmethod
    def render_upsert(request, id=None):
        """新規作成または更新のページ"""

        # 以下のファイルはあとで作ります
        from .v_upsert import render_upsert
        #    ---------        -------------
        #    1                2
        # 1. `host1/apps1/practice_v1/views/o1/room/v_upsert.py`
        #                                           --------
        # 2. `1.` に含まれる関数

        return render_upsert(request, id, RoomV._path_of_upsert_page)
```

# Step 5. ビュー モジュール作成 - v_upsert ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 forms
                │   └── 📄 f_room.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o1
                │           └── 📂 room
                │               └── 📄 upsert.html
                └── 📂 views
                    └── 📂 o1
                        └── 📂 room
                            ├── 📄 __init__.py
👉                          └── 📄 v_upsert.py
```

```py
from django.shortcuts import render, get_object_or_404, redirect

from apps1.practice_v1.models.o1.m_room import Room
#          -----------           ------        ----
#          1.1                   1.2           2
#    ----------------------------------
#    1
# 1, 1.2 ディレクトリー
# 1.1 アプリケーション
# 2. `1.2` に含まれる __init__.py ファイルにさらに含まれるクラス

# 部屋フォーム
from apps1.practice_v1.forms.f_room import RoomForm
#    ----- ----------- ----- ------        --------
#    1     2           3     4             5
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


@staticmethod
def render_upsert(request, id, path_of_upsert_page):
    """新規作成または更新のページ"""

    if id:  # idがあるとき（更新の時）
        # idで検索して、結果を戻すか、404エラー
        room = get_object_or_404(Room, pk=id)
    else:  # idが無いとき（作成の時）
        room = Room()

    # POSTの時（作成であれ更新であれ送信ボタンが押されたとき）
    if request.method == 'POST':
        # フォームを生成
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():  # バリデーションがOKなら保存
            room = form.save(commit=False)
            room.save()
            return redirect('practice_v1_rooms')
    else:  # GETの時（フォームを生成）
        form = RoomForm(instance=room)

    # 作成・更新画面を表示
    return render(request, path_of_upsert_page, dict(form=form, id=id))
```

# Step 6. ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 forms
        │       │   └── 📄 f_room.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1
        │       │           └── 📂 room
        │       │               └── 📄 delete.html
        │       └── 📂 views
        │           └── 📂 o1
        │               └── 📂 room
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_delete.py
        └── 📂 project1                          # プロジェクト
👉          └── 📄 urls_practice.py
```

```py
# ...略...


urlpatterns = [
    # ...略...


    # 対局部屋の新規作成
    path('practice/v1/rooms/upsert/', RoomV.render_upsert,
         # ------------------------   -------------------
         # 1                          2
         name='practice_v1_rooms_create'),
    #          ------------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/rooms/upsert/` のような URL のパスの部分
    #                              -------------------------
    # 2. RoomV クラスの render_upsert メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_rooms_create' %} のような形でURLを取得するのに使える

    # 対局部屋の更新
    path('practice/v1/rooms/upsert/<int:id>/', RoomV.render_upsert,
         # ---------------------------------   -------------------
         # 1                                   2
         name='practice_v1_rooms_update'),
    #          ------------------------
    #          3
    # 1. 例えば `http://example.com/practice/v1/rooms/upsert/<数字列>/` のような URL のパスの部分
    #                              ----------------------------------
    #    数字列は `2.` の関数の引数 id で取得できる
    # 2. RoomV クラスの render_upsert メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_rooms_update' %} のような形でURLを取得するのに使える
]
```

# Step 7. Web画面へアクセス

👇 作成するとき、部屋ID は付けるな  

📖 [http://localhost:8000/practice/v1/rooms/upsert/](http://localhost:8000/practice/v1/rooms/upsert/)  

👇 更新するとき、部屋ID を付けろ。 部屋ID は適宜変えてほしい  

📖 [http://localhost:8000/practice/v1/rooms/upsert/5/](http://localhost:8000/practice/v1/rooms/upsert/5/)  

# Step 8. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
        │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 forms
        │       │   └── 📄 f_room.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1
        │       │           └── 📂 room
        │       │               └── 📄 delete.html
        │       └── 📂 views
        │           └── 📂 o1
        │               └── 📂 room
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_delete.py
        └── 📂 project1                          # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/rooms/upsert/,対局部屋の新規作成
/practice/v1/rooms/upsert/5/,対局部屋の更新
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでユーザーホームを作ろう！](https://qiita.com/muzudho1/items/37532c83235b7f9e60c9)  

# 参考にした記事

📖 [DjangoでCRUD](https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92)
