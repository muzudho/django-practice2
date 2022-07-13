# 目的

現在、対局中かどうかを調べられるようにしたい  

# 手段

ゲーム対局部屋にチェックインさせる  

ここで、以下の２つはこの記事では実装しない  

* 対局が終わったことを示すチェックアウト
* 多面指しのために複数の部屋に入ることへの考慮

# 詳細

ゲーム対局部屋に入るときは当該 Room モデルのレコードの sente_id または gote_id フィールドに 自分のユーザーIdを上書きし、  
自分の Profile レコードの match_state フィールドを 3 （対局中）に上書きする  

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

# Step 2. 対局申込ビュー モジュール編集 - match_application フォルダー

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂tic_tac_toe_v3            # アプリケーション (Ver. Three)
                └── 📂views
                    └── 📂o0o1              # (v3).0.one
                        └── 📂match_application
👉                          └── 📄__init__.py
```

```py
class MatchApplicationV():
    # ...略...


    # * 以下を削除
    # @staticmethod
    # def on_sent(request):
    #     """送信後"""
    #     # 拡張したい挙動があれば、ここに書く
    #     pass

    # * 以下を追加
    @staticmethod
    def on_sent(request):
        """送信後"""

        # 以下のファイルはあとで作ります
        from .v_on_sent import match_application_on_sent
        #    ----------        -------------------------
        #    1                 2
        # 1. `host1/apps1/tic_tac_toe_v3/views/o0o1/match_application/v_on_sent.py`
        #                                                             ---------
        # 2. `1.` に含まれる関数

        return match_application_on_sent(request)
```

# Step 3. 対局申込ビュー モジュール作成 - v_on_sent.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂tic_tac_toe_v3            # アプリケーション (Ver. Three)
                └── 📂views
                    └── 📂o0o1              # (v3).0.one
                        └── 📂match_application
                            ├── 📄__init__.py
👉                          └── 📄v_on_sent.py
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
    #     f"[match_application_on_sent] po_room_name=[{po_room_name}] len={len(room_table_qs)}")

    if 1 <= len(room_table_qs):
        # （名前被りがあったなら）先頭の１つを取得
        room = room_table_qs[0]
        # print(f"[match_application_on_sent] first room=[{room}]")
        # print(
        #     f"[match_application_on_sent] first room .name=[{room.name}] .sente_id=[{room.sente_id}] .gote_id=[{room.gote_id}] .board=[{room.board}] .record=[{room.record}]")
    else:
        # 新規作成
        room = Room()
        room.name = po_room_name
        # print(f"[match_application_on_sent] new room=[{room}]")

    # print(f"[match_application_on_sent] request.user={request.user}")
    # print(
    #     f"[match_application_on_sent] request.user.is_authenticated={request.user.is_authenticated}")

    if request.user.is_authenticated:
        # ログインしたユーザーだった

        user_pk = request.user.pk
        # print(
        #     f"[match_application_on_sent] user_pk={user_pk} room.sente_id={room.sente_id} room.gote_id={room.gote_id}")

        # デバッグ
        # user = User.objects.get(pk=user_pk)
        # print(
        #     f"[match_application_on_sent] user username={user.username}")

        # 自分の Profile レコード 取得
        profile = Profile.objects.get(user__pk=user_pk)
        #                             --------
        #                             1
        # 1. Profile テーブルと 1対1 で紐づいている親テーブル User の pk フィールド

        # print(f"[match_application_on_sent] profile={profile}")
        # print(
        #     f"[match_application_on_sent] profile.match_state={profile.match_state}")

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
        #     f"[match_application_on_sent] room .name=[{room.name}] .sente_id=[{room.sente_id}] .gote_id=[{room.gote_id}] .board=[{room.board}] .record=[{room.record}]")
        # TODO バリデーションチェック
        room.save()

        # print(
        #     f"[match_application_on_sent] prifile .match_state=[{profile.match_state}]")
        # TODO バリデーションチェック
        profile.save()

        # print(f"[match_application_on_sent] ★ 更新終わり")
    else:
        # ゲストだった
        # print(f"[match_application_on_sent] ★ ゲスト")
        pass
```

# Step 4. Web画面へアクセス

先手と後手で、２人分のプレイヤーのアカウントがほしい。  
このゲームは２人用なので、Webページを２窓で開き、片方が X プレイヤー、もう片方が O プレイヤーとして遊んでほしい  

１つのPCで ２つのアカウントをアクティブにする方法が分からないが、  
今のところ 厳密に作れてはいないので、以下の手順で行う  

👇 以下のリンクから `サインアップ` して２人目のアカウントを用意してほしい  

📖 [http://localhost:8000/accounts/v1/signup/](http://localhost:8000/accounts/v1/signup/)  

👇 サインアップしたら、ログインしてほしい  

📖 [http://localhost:8000/accounts/v1/login/](http://localhost:8000/accounts/v1/login/)  

👇 そして `Elephant` 部屋に `X` 番として入ってほしい  

📖 [http://localhost:8000/tic-tac-toe/v3/match-application/](http://localhost:8000/tic-tac-toe/v3/match-application/)  

ここで、ログアウトしたなら対局部屋を追い出されるべきだが、まだそこまで作っていない。  

👇 そこで、対局部屋のブラウザ画面を残したまま 今のユーザーをログアウトしてほしい  

📖 [http://localhost:8000/accounts/v1/login/](http://localhost:8000/accounts/v1/logout/)  

👇 スーパーユーザー でログインしなおして、  

📖 [http://localhost:8000/accounts/v1/login/](http://localhost:8000/accounts/v1/login/)  

👇 `Elephant` 部屋に `O` 番として入ってほしい  

📖 [http://localhost:8000/tic-tac-toe/v3/match-application/](http://localhost:8000/tic-tac-toe/v3/match-application/)  

👇 部屋、ユーザーを確認するには、管理画面を使うのが確実だ。  
スーパーユーザーのまま、管理画面に入っていてほしい  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

部屋に入っているユーザーの主キーが記録されていることを確認してほしい  

また、既存でない部屋名でも ちゃんとユーザーの主キーが記録されることを確認してほしい  

# 次の記事

📖 [Djangoでゲーム対局部屋をモニターしよう！](https://qiita.com/muzudho1/items/e5e6e6ba76da401c4c00)  

# 参考にした記事

📖 [Create Django model or update if exists](https://stackoverflow.com/questions/14115318/create-django-model-or-update-if-exists)  
📖 [How can I get the username of the logged-in user in Django?](https://stackoverflow.com/questions/16906515/how-can-i-get-the-username-of-the-logged-in-user-in-django)  
