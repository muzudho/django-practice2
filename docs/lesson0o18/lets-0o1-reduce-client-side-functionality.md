# 目的

`Play Again` （再戦）するかどうかは、プレイヤーが選べるのではなく、サーバー側が選ぶようにしたい  
そこで `Play Again` ボタンを外す  

# はじめに

この記事は Lesson0 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂host_local1                   # Djangoとは関係ないもの
    │    ├── 📂sockapp1
    │    └── 📂websockapp1
    ├── 📂host1                         # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂apps1
    │   │   ├── 📂allauth_customized    # アプリケーション
    │   │   ├── 📂portal                # アプリケーション
    │   │   ├── 📂practice              # アプリケーション
    │   │   │   ├── 📂migrations
    │   │   │   └── 📂models
    │   │   │       └── 📂v0o0o1
    │   │   │           └── 📄m_room.py
    │   │   ├── 📂tic_tac_toe_v1        # アプリケーション
    │   │   └── 📂tic_tac_toe_v2        # アプリケーション
    │   │       ├── 📂migrations
    │   │       │   └── 📄__init__.py
    │   │       ├── 📂static
    │   │       │   └── 📂tic_tac_toe_v2
    │   │       │       └── 📂o0o1
    │   │       │           └── 📂think
    │   │       │               ├── 📄concepts.js
    │   │       │               ├── 📄engine.js
    │   │       │               ├── 📄judge_ctrl.js
    │   │       │               ├── 📄position.js
    │   │       │               ├── 📄things.js
    │   │       │               └── 📄user_ctrl.js
    │   │       ├── 📂templates
    │   │       │   └── 📂tic_tac_toe_v2
    │   │       │       └── 📂o0o1
    │   │       │           └── 📂think
    │   │       │               └── 📄engine_manual.html
    │   │       ├── 📂views
    │   │       │   └── 📂v2o0o1
    │   │       │       └── 📂think
    │   │       │           └── 📂engine_manual
    │   │       │               ├── 📄__init__.py
    │   │       │               └── 📄v_render.py
    │   │       ├── 📄__init__.py
    │   │       ├── 📄admin.py
    │   │       ├── 📄apps.py
    │   │       └── 📄tests.py
    │   ├── 📂data
    │   ├── 📂project1                  # プロジェクト
    │   │   ├── 📄__init__.py
    │   │   ├── 📄asgi.py
    │   │   ├── 📄settings_secrets_example.txt
    │   │   ├── 📄settings.py
    │   │   ├── 📄urls_accounts.py
    │   │   ├── 📄urls_practice.py
    │   │   ├── 📄urls_tic_tac_toe_v1.py
    │   │   ├── 📄urls_tic_tac_toe_v2.py
    │   │   ├── 📄urls.py
    │   │   ├── 📄ws_urls_tic_tac_toe_v1.py
    │   │   └── 📄wsgi.py
    │   ├── 📂project2                  # プロジェクト
    │   ├── 🐳docker-compose-project2.yml
    │   ├── 🐳docker-compose.yml
    │   ├── 🐳Dockerfile
    │   ├── 📄manage.py
    │   └── 📄requirements.txt
    └── 📄.gitignore
```

# Step 1. Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. フォルダー作成 - apps1/tic_tac_toe_v3 フォルダー

👇 以下のフォルダーを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂tic_tac_toe_v3            # アプリケーション (Ver. Three)
```

# Step 3. アプリケーション作成

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python manage.py startapp tic_tac_toe_v3 ./apps1/tic_tac_toe_v3
#                                                     -------------- ----------------------
#                                                     1              2
# 1. 任意のDjangoアプリケーション名
# 2. 既存のディレクトリーへのパス
```

# Step 4. 今回使わないファイルの削除

👇 以下のファイルを削除してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂tic_tac_toe_v3            # アプリケーション (Ver. Three)
                ├── 📂migrations
                │   └── 📄__init__.py
                ├── 📄__init__.py
                ├── 📄admin.py
                ├── 📄apps.py
👉              ├── 📄models.py
                ├── 📄tests.py
👉              └── 📄views.py
```

# Step 5. アプリケーション設定変更 - apps.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂tic_tac_toe_v3            # アプリケーション (Ver. Three)
                ├── 📂migrations
                │   └── 📄__init__.py
                ├── 📄__init__.py
                ├── 📄admin.py
👉              ├── 📄apps.py
                └── 📄tests.py
```

```py
from django.apps import AppConfig


class TicTacToeV3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # * 変更前
    # name = 'tic_tac_toe_v3'
    # * 変更後
    name = 'apps1.tic_tac_toe_v3'
    #       ------------
    #       1
    # 1. `host1/apps1/tic_tac_toe_v3/apps.py`
    #           --------------------
```

# Step 6. アプリケーション登録 - settings.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂tic_tac_toe_v3            # アプリケーション (Ver. Three)
        │       ├── 📂migrations
        │       │   └── 📄__init__.py
        │       ├── 📄__init__.py
        │       ├── 📄admin.py
        │       ├── 📄apps.py
        │       └── 📄tests.py
        └── 📂project1
👉          └── 📄settings.py
```

```py
INSTALLED_APPS = [
    # あなたが追加したアプリケーション


    # ...中略...


    'apps1.tic_tac_toe_v3',


    # ...中略...


]
```

これで、 `host1/apps1/tic_tac_toe_v3` フォルダーは tic_tac_toe_v3 アプリケーションとして認識される。  
例えば、 tic_tac_toe_v3 フォルダーの直下に置いた static フォルダーが Django の静的リソースの検索対象のパスになるといったメリットがある  

# Step 7. 対局画面作成 - playing.html.txt ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂tic_tac_toe_v3            # アプリケーション (Ver. Three)
        │       ├── 📂migrations
        │       │   └── 📄__init__.py
        │       ├── 📂templates
        │       │   └── 📂tic_tac_toe_v3    # アプリケーションと同名
        │       │       └── 📂o0o1
👉      │       │           └── 📄playing.html.txt
        │       ├── 📄__init__.py
        │       ├── 📄admin.py
        │       ├── 📄apps.py
        │       └── 📄tests.py
        └── 📂project1
            └── 📄settings.py
```

```html
{% extends "tic_tac_toe_v2/o0o1/gui/playing_base.html" %}
{#                       ^ two
            -----------------------------------------
            1
1. `host1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/o0o1/gui/playing_base.html`
                                         -----------------------------------------

    自動フォーマットしないでください
    Do not auto fomatting
#}


{% block footer_section1 %}
    <!-- フッターにボタンを置きません -->
{% endblock footer_section1 %}


{% block methods_footer %}
    // フッターのボタンは除きました
{% endblock methods_footer %}
```

# Step 8. 対局申込ビュー モジュール作成 - match_application フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂tic_tac_toe_v3            # アプリケーション (Ver. Three)
        │       ├── 📂migrations
        │       │   └── 📄__init__.py
        │       ├── 📂templates
        │       │   └── 📂tic_tac_toe_v3    # アプリケーションと同名
        │       │       └── 📂o0o1
        │       │           └── 📄playing.html.txt
        │       ├── 📂views
        │       │   └── 📂o0o1              # (v3).0.one
        │       │       └── 📂match_application
👉      │       │           └── 📄__init__.py
        │       ├── 📄__init__.py
        │       ├── 📄admin.py
        │       ├── 📄apps.py
        │       └── 📄tests.py
        └── 📂project1
            └── 📄settings.py
```

```py
class MatchApplicationV():
    """対局申込ビュー"""

    # ページ
    _path_of_page = "tic_tac_toe_v2/o0o1/gui/match_application.html"
    #                             ^two
    #                ----------------------------------------------
    #                1
    # 1. `host1/apps1/tic_tac_toe_v2/templates/tic_tac_toe_v2/o0o1/gui/match_application.html` を取得
    #                                          ----------------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_page
        #    ---------        -----------
        #    1                2
        # 1. `host1/apps1/tic_tac_toe_v3/views/o0o1/match_application/v_render.py`
        #                                                             --------
        # 2. `1.` に含まれる関数

        return render_page(request, MatchApplicationV._path_of_page)
```

# Step 9. 対局申込ビュー モジュール作成 - v_on_sent.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂tic_tac_toe_v3            # アプリケーション (Ver. Three)
        │       ├── 📂migrations
        │       │   └── 📄__init__.py
        │       ├── 📂templates
        │       │   └── 📂tic_tac_toe_v3    # アプリケーションと同名
        │       │       └── 📂o0o1
        │       │           └── 📄playing.html.txt
        │       ├── 📂views
        │       │   └── 📂o0o1              # (v3).0.one
        │       │       └── 📂match_application
        │       │           ├── 📄__init__.py
👉      │       │           └── 📄v_on_sent.py
        │       ├── 📄__init__.py
        │       ├── 📄admin.py
        │       ├── 📄apps.py
        │       └── 📄tests.py
        └── 📂project1
            └── 📄settings.py
```

```py
# from django.contrib.auth.models import User # デバッグ用

from apps1.practice.models.v0o0o1.m_room import Room
#    ----- -------- --------------------        ----
#    1     2        3                           4
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 3. Python ファイル名。拡張子抜き
# 4. クラス名

from apps1.practice.models.v0o0o1.m_user_profile import Profile
#    ----- -------- ----------------------------        -------
#    1     2        3                                   4
# 1,3. ディレクトリー名
# 2. アプリケーション フォルダー名
# 3. Python ファイル名。拡張子抜き
# 4. クラス名


def match_application_on_sent(request):
    """対局申込 - 送信後

    * ログインしていないユーザーが部屋に入っても 何も記録しません
    * ログインしているユーザーが部屋に入ってくると、以下のものを記録します（チェックイン）
    * Room.sente_id または Room.gote_id の空いている方に user.pk を上書き
    * user.profile.match_state を 3 （対局中）に上書き
    """

    # `po_` は POST送信するパラメーター名の目印
    # 部屋名
    po_room_name = request.POST.get("po_room_name")
    # 自分の番。 "X" か "O"。 機能拡張も想定
    my_turn = request.POST.get("po_my_turn")

    # 部屋の取得 または 新規作成
    #
    # * ID ではなく、部屋名から行う
    room_table_qs = Room.objects.filter(name=po_room_name)
    # print(
    #     f"[MatchApplication on_sent] po_room_name=[{po_room_name}] len={len(room_table_qs)}")

    if 1 <= len(room_table_qs):
        # （名前被りがあったなら）先頭の１つを取得
        room = room_table_qs[0]
        # print(f"[MatchApplication on_sent] first room=[{room}]")
        # print(
        #     f"[MatchApplication on_sent] first room .name=[{room.name}] .sente_id=[{room.sente_id}] .gote_id=[{room.gote_id}] .board=[{room.board}] .record=[{room.record}]")
    else:
        # 新規作成
        room = Room()
        room.name = po_room_name
        # print(f"[MatchApplication on_sent] new room=[{room}]")

    # print(f"[MatchApplication on_sent] request.user={request.user}")
    # print(
    #     f"[MatchApplication on_sent] request.user.is_authenticated={request.user.is_authenticated}")

    if request.user.is_authenticated:
        # ログインしたユーザーだった

        user_pk = request.user.pk
        # print(
        #     f"[MatchApplication on_sent] user_pk={user_pk} room.sente_id={room.sente_id} room.gote_id={room.gote_id}")

        # デバッグ
        # user = User.objects.get(pk=user_pk)
        # print(
        #     f"[MatchApplication on_sent] user username={user.username}")

        # 自分の Profile レコード 取得
        profile = Profile.objects.get(user__pk=user_pk)
        #                             --------
        #                             1
        # 1. Profile テーブルと 1対1 で紐づいている親テーブル User の pk フィールド

        # print(f"[MatchApplication on_sent] profile={profile}")
        # print(
        #     f"[MatchApplication on_sent] profile.match_state={profile.match_state}")

        if my_turn == "X":
            # X を取った方は先手とします
            room.sente_id = user_pk
            # ユーザーの状態を対局中（3）にします
            profile.match_state = 3

        elif my_turn == "O":
            # O を取った方は後手とします
            #
            # * 先手と後手が同じユーザーでも構わないものとします
            room.gote_id = user_pk
            # ユーザーの状態を対局中（3）にします
            profile.match_state = 3

        else:
            # それ以外は観戦者として扱う
            # ユーザーの状態を観戦中（4）にします
            profile.match_state = 4

        # 先手と後手の両方が埋まったなら
        if not(room.sente_id is None or room.sente_id == 0 or room.gote_id is None or room.gote_id == 0):
            # 盤と棋譜を空っぽにする
            room.board = ""
            room.record = ""

        # print(
        #     f"[MatchApplication on_sent] room .name=[{room.name}] .sente_id=[{room.sente_id}] .gote_id=[{room.gote_id}] .board=[{room.board}] .record=[{room.record}]")
        # TODO バリデーションチェック
        room.save()

        # print(
        #     f"[MatchApplication on_sent] prifile .match_state=[{profile.match_state}]")
        # TODO バリデーションチェック
        profile.save()

        # print(f"[MatchApplication on_sent] ★ 更新終わり")
    else:
        # ゲストだった
        # print(f"[MatchApplication on_sent] ★ ゲスト")
        pass
```

# Step 10. 対局ビュー モジュール作成 - playing フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂tic_tac_toe_v3            # アプリケーション (Ver. Three)
        │       ├── 📂migrations
        │       │   └── 📄__init__.py
        │       ├── 📂templates
        │       │   └── 📂tic_tac_toe_v3    # アプリケーションと同名
        │       │       └── 📂o0o1
        │       │           └── 📄playing.html.txt
        │       ├── 📂views
        │       │   └── 📂o0o1              # (v3).0.one
        │       │       ├── 📂match_application
        │       │       │   ├── 📄__init__.py
        │       │       │   └── 📄v_on_sent.py
        │       │       └── 📂playing
👉      │       │           └── 📄__init__.py
        │       ├── 📄__init__.py
        │       ├── 📄admin.py
        │       ├── 📄apps.py
        │       └── 📄tests.py
        └── 📂project1
            └── 📄settings.py
```

```py
class PlayingV():
    """対局中ビュー"""

    _path_of_ws_playing = "/tic-tac-toe/v2o0o1/playing/"
    #                                    ^ two
    #                      ----------------------------
    #                      1
    # 1. `ws://example.com:8000/tic-tac-toe/v2o0o1/playing/`
    #                          ---------------------------

    _path_of_html = "tic_tac_toe_v3/o0o1/playing.html.txt"
    #                             ^ three
    #                ------------------------------------
    #                1
    # 1. `host1/apps1/tic_tac_toe_v3/templates/tic_tac_toe_v3/o0o1/playing.html.txt`
    #                                          ------------------------------------

    @staticmethod
    def render(request, kw_room_name):
        """描画"""

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.v2o0o1.gui.playing import playing_expected_pieces
        #                       ^two
        #    ---------------------------------------------        -----------------------
        #    1                                                    2
        # 1. `host1/apps1/tic_tac_toe_v2/views/v2o0o1/gui/playing/__init__.py`
        #           ---------------------------------------------
        # 2. `1.` の `__init__.py` ファイルに含まれる playing_expected_pieces 変数

        # 以下のファイルは既存です
        from apps1.tic_tac_toe_v2.views.v2o0o1.gui.playing.v_render import render_playing
        #                       ^two
        #    ------------------------------------------------------        --------------
        #    1                                                             2
        # 1. `host1/apps1/tic_tac_toe_v2/views/v2o0o1/gui/playing/v_render.py`
        #           ------------------------------------------------------
        # 2. `1.` のファイルに含まれる render_playing 関数

        return render_playing(
            request,
            kw_room_name,
            PlayingV._path_of_ws_playing,
            PlayingV._path_of_html,
            PlayingV.on_update,
            playing_expected_pieces)

    @staticmethod
    def on_update(request):
        """訪問後または送信後"""
        # 拡張したい挙動があれば、ここに書く
        pass
```

# Step 11. ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂tic_tac_toe_v3            # アプリケーション (Ver. Three)
        │       ├── 📂migrations
        │       │   └── 📄__init__.py
        │       ├── 📂templates
        │       │   └── 📂tic_tac_toe_v3    # アプリケーションと同名
        │       │       └── 📂o0o1
        │       │           └── 📄playing.html.txt
        │       ├── 📂views
        │       │   └── 📂o0o1              # (v3).0.one
        │       │       ├── 📂match_application
        │       │       │   ├── 📄__init__.py
        │       │       │   └── 📄v_on_sent.py
        │       │       └── 📂playing
        │       │           └── 📄__init__.py
        │       ├── 📄__init__.py
        │       ├── 📄admin.py
        │       ├── 📄apps.py
        │       └── 📄tests.py
        └── 📂project1                      # プロジェクト
            ├── 📄settings.py
👉          └── 📄urls_practice.py
```

```py
# ...略...


# 〇×ゲーム v3 対局申込中
from apps1.tic_tac_toe_v3.views.o0o1.match_application import MatchApplicationV as TicTacToeV3o0o1MatchApplicationV
#                       ^three
#    ----- -------------- ----------------------------        -----------------    --------------------------------
#    1     2              3                                   4                    5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. クラス名
# 5. '4.' の別名

# 〇×ゲーム v3 対局中
from apps1.tic_tac_toe_v3.views.o0o1.playing import PlayingV as TicTacToeV3o0o1PlayingV
#                       ^three
#    ----- -------------- ------------------        --------    -----------------------
#    1     2              3                         4           5
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. クラス名
# 5. '4.' の別名


urlpatterns = [
    # ...略...


    # 〇×ゲーム v3 対局申込中
    path('tic-tac-toe/v3/match-application/', TicTacToeV3o0o1MatchApplicationV.render,
         # --------------------------------   ---------------------------------------
         # 1                                  2
         name='tic_tac_toe_v3_match_application'),
    #          --------------------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3/match-application/` のような URL のパスの部分
    #                              ---------------------------------
    # 2. TicTacToeV3o0o1MatchApplicationV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3_match_application' %} のような形でURLを取得するのに使える


    # 〇×ゲーム v3 対局中
    path('tic-tac-toe/v3/playing/<str:kw_room_name>/', TicTacToeV3o0o1PlayingV.render,
         # -----------------------------------------   ------------------------------
         # 1                                           2
         name='tic_tac_toe_v3_playing'),
    #          ----------------------
    #          3
    #
    # 1. 例えば `http://example.com/tic-tac-toe/v3/playing/<部屋名>/` のような URL のパスの部分
    #                              --------------------------------
    #    <部屋名> に入った文字列は `2.` のメソッドの kw_room_name 引数に渡されます
    # 2. TicTacToeV3o0o1PlayingV （別名）クラスの render メソッド
    # 3. HTMLテンプレートの中で {% url 'tic_tac_toe_v3_playing' %} のような形でURLを取得するのに使える
]
```

# Step 12. Web画面へアクセス

このゲームは２人用なので、Webページを２窓で開き、片方が X プレイヤー、もう片方が O プレイヤーとして遊んでください  

📖 [http://localhost:8000/tic-tac-toe/v3/match-application/](http://localhost:8000/tic-tac-toe/v3/match-application/)  

# Step 13. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   ├── 📂portal                        # アプリケーション
        │   │   └── 📂data
👉      │   │       └── 📄finished-lessons.csv
        │   └── 📂tic_tac_toe_v3                # アプリケーション (Ver. Three)
        │       ├── 📂migrations
        │       │   └── 📄__init__.py
        │       ├── 📂templates
        │       │   └── 📂tic_tac_toe_v3        # アプリケーションと同名
        │       │       └── 📂o0o1
        │       │           └── 📄playing.html.txt
        │       ├── 📂views
        │       │   └── 📂o0o1                  # (v3).0.one
        │       │       ├── 📂match_application
        │       │       │   ├── 📄__init__.py
        │       │       │   └── 📄v_on_sent.py
        │       │       └── 📂playing
        │       │           └── 📄__init__.py
        │       ├── 📄__init__.py
        │       ├── 📄admin.py
        │       ├── 📄apps.py
        │       └── 📄tests.py
        └── 📂project1                          # プロジェクト
            ├── 📄settings.py
            └── 📄urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/tic-tac-toe/v3/match-application/,〇×ゲーム v3 対局申込中
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでチェックインを作ろう！](https://qiita.com/muzudho1/items/1ce542dd66929d7bce3f)  
