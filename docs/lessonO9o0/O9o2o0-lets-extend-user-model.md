# サンプルを見る

📖 [http://tic.warabenture.com:8000/practice/v1/extends-user-list/](http://tic.warabenture.com:8000/practice/v1/extends-user-list/)  

# 目的

Django に最初から付いている User モデルを拡張したい  

試しに 対局マッチング状況を表す match_state プロパティを追加するものとし、  
その値は 整数とし、  
0 を休憩中， 1 を対局申込中， 2 を対局案内中， 3 を対局中， 4 を観戦中 とする  

# はじめに

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key       | Value                                     |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Auth      | allauth                                   |
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_v1        # アプリケーション
    │   │   ├── 📂 portal_v1                    # アプリケーション
    │   │   └── 📂 practice_v1                  # アプリケーション
    │   ├── 📂 data
    │   ├── 📂 project1                         # プロジェクト
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

# Step O9o2o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step O9o2o0g2o0 User モデル拡張 - user_profile/v1o0.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 models
                    └── 📂 user_profile
👉                      └── 📄 v1o0.py
```

```py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """O9o2o0g2o0 Userモデル拡張"""

    # この User オブジェクトの下に Profile オブジェクトをぶら下げると思ってください
    #
    # Example
    # -------
    #
    # user = User.objects.get(pk=user_id)
    # print(user.profile.match_state)
    #
    # OneToOneField - 1対1対応のリレーション。 デフォルトで Unique 属性
    #
    # * `on_delete` - 必須。 models.CASCADE なら、親テーブルのレコードが消されると、子テーブルのレコードも削除されます
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)

    # 対局のマッチング状態
    #
    # 0 を休憩中， 1 を対局申込中， 2 を対局案内中， 3 を対局中， 4 を観戦中 とする
    #
    # * `blank` - 未指定でもセーブを受け入れるなら真
    # * `default` - 初期値
    match_state = models.IntegerField(
        '対局のマッチング状態', null=True, blank=True, default=0)

    def __str__(self):
        """このオブジェクトを文字列にしたとき返るもの"""
        return f"{self.user}'s profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """O9o2o0g2o0 新規作成"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """O9o2o0g2o0 保存"""

    if hasattr(instance, 'profile'):
        # * ここを通らないといけない
        instance.profile.save()
    else:
        # * ここに来るようならおかしい。管理画面から Profile モデルを追加し、User に紐づけるステップをやっていないのではないか？
        print("Userオブジェクトがprofile属性を持っていなかった。ここに来るようならおかしい。管理画面から Profile モデルを追加し、User に紐づけるステップをやっていないのではないか？(^～^)")


# この行が何をやっているか分からないが、分からないからサンプルの真似をしておく（＾～＾）
# 📖 [Extending the User model with custom fields in Django](https://stackoverflow.com/questions/44109/extending-the-user-model-with-custom-fields-in-django)
post_save.connect(create_user_profile, sender=User)
```

# Step O9o2o0g3o0 マイグレーション ファイル作成 - コマンド実行

（このマイグレーションのステップは今はまだやらなくていいかもしれない）  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
# cd src1

docker-compose run --rm web python3 manage.py makemigrations practice_v1 --settings project1.settings
#                                                            -----------            -----------------
#                                                            1                      2
# 1. アプリケーション
# 2. src1/project1/settings.py
#         -----------------
```

👇 以下のディレクトリーとファイルが生成される。  
生成されなかったら、先に進んで、必要になったときにここに戻ってきて やってほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 migrations
                │   ├── 📄 __init__.py
                │   ├── ...略...
👉              │   └── 📄 0003_profile.py       # 名前は異なることがある
                └── 📂 models
                    └── 📂 user_profile
                        └── 📄 v1o0.py
```

👆 この生成されたファイルは マイグレーション ファイル と呼ぶらしい  

まだ マイグレーション作業は完了していない  

# Step O9o2o0g4o0 マイグレーション対象確認 - コマンド実行＜その２＞

```shell
docker-compose run --rm web python3 manage.py showmigrations --settings project1.settings
#                                                                       -----------------
#                                                                       1
# 1. src1/project1/settings.py
#         -----------------
```

👆 マイグレーションする前に、マイグレーションが終わっているもの、マイグレーションがまだ終わっていないものを確認  

```plaintext
[X] 0001_hoge ... マイグレーションが終わっている
[ ] 0002_fuga ... マイグレーションが終わっていない。これからやる
```

# Step O9o2o0g5o0 マイグレーション -  コマンド実行＜その３＞

```shell
docker-compose run --rm web python3 manage.py migrate --settings project1.settings
#                                                                -----------------
#                                                                1
# 1. src1/project1/settings.py
#         -----------------
```

👆 ここまでやって マイグレーション という作業が終わるらしい  

# Step O9o2o0g6o0 マイグレーション確認 - コマンド実行＜その４＞

```shell
docker-compose run --rm web python3 manage.py showmigrations --settings project1.settings
#                                                                       -----------------
#                                                                       1
# 1. src1/project1/settings.py
#         -----------------
```

👆 マイグレーションした後に、マイグレーションされたものを確認  

# Step O9o2o0g7o0 モデルヘルパー編集 - user/v1o0/__init__.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models
                │   └── 📂 user_profile
                │       └── 📄 v1o0.py
                └── 📂 models_helper
                    └── 📂 user
                        └── 📂 v1o0
👉                          └── 📄 __init__.py
```

```py
class MhUser():
    """O9o1o0g3o0 ユーザー モデルヘルパー"""


    # ...略...


    # O9o2o0g7o0 以下のファイルはあとで作ります
    from .mh_get_extends_user_dic import get_extends_user_dic
    #    ------------------------        --------------------
    #    1                               2
    # 1. `src1/apps1/practice_v1/model_helper/user/v1o0/mh_get_extends_user_dic.py`
    #                                                   -----------------------
    # 2. `1.` に含まれる関数
```

# Step O9o2o0g8o0 モデルヘルパー モジュール作成 - mh_get_extends_user_dic.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models
                │   └── 📂 user_profile
                │       └── 📄 v1o0.py
                └── 📂 models_helper
                    └── 📂 user
                        └── 📂 v1o0
                            ├── 📄 __init__.py
👉                          └── 📄 mh_get_extends_user_dic.py
```

```py
from django.contrib.auth import get_user_model  # カスタムした User
# from django.contrib.auth.models import User   # デフォルトの User


def get_extends_user_dic():
    """O9o2o0g8o0 （拡張済）会員登録ユーザー一覧"""
    User = get_user_model()

    # 会員登録ユーザー一覧
    user_resultset = User.objects.all().select_related('profile')
    #                                  --------------------------
    #                                  1
    # 1. これを付けて何が起こっているか分からないが、サンプルでよく付けているのを見かけるので真似する。外しても動く。
    #    User クラスを拡張して作った Profile クラスの OneToOneField フィールドの名前を指している

    # 使いやすい形に変換する
    user_dic = dict()

    for user in user_resultset:

        user_dic[user.pk] = {
            "pk": user.pk,
            # 日付型はJSONに変換できないので、先に文字列に変換しておく
            "last_login": user.last_login.strftime("%Y-%m-%d %H:%M:%S"),
            "username": user.username,
            "is_active": user.is_active,
            "match_state": user.profile.match_state
        }

    return user_dic
```

# Step O9o2o0g9o0 画面編集 - extends_user_list.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models
                │   └── 📂 user_profile
                │       └── 📄 v1o0.py
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_extends_user_dic.py
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 extends_user_list
👉                          └── 📄 v1o0.html
```

```html
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!DOCTYPE html>
<!-- See also: https://qiita.com/zaburo/items/ab7f0eeeaec0e60d6b92 -->
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>会員登録ユーザー一覧</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <!-- v-app-bar に app プロパティを指定しないなら、背景画像を付けてほしい -->
                <v-app-bar app dense elevation="4">
                    <v-app-bar-nav-icon></v-app-bar-nav-icon>
                    <v-toolbar-title>ゲーム対局サーバー</v-toolbar-title>
                </v-app-bar>
                <v-main>
                    <v-container>
                        <h3>会員登録ユーザー一覧</h3>
                        <v-simple-table>
                            <template v-slot:default>
                                <thead>
                                    <tr>
                                        <th>ID</th>
                                        <th>ユーザー名</th>
                                        <th>アクティブか</th>
                                        <th>最終ログイン</th>
                                        <th>マッチング状態</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="user in vu_userDic" :key="user.pk">
                                        {% comment %} Vue で二重波括弧（braces）は変数の展開に使っていることから、 Python のテンプレートに二重波括弧を変数の展開に使わないよう verbatim で指示します。 {% endcomment %} {% verbatim %}
                                        <td>{{ user.pk }}</td>
                                        <td>{{ user.username }}</td>
                                        <td>{{ user.is_active }}</td>
                                        <td>{{ user.last_login }}</td>
                                        <td>{{ user.match_state }}</td>
                                        {% endverbatim %}
                                    </tr>
                                </tbody>
                            </template>
                        </v-simple-table>
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
        <script>
            let vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // "vu_" は 「vue1.dataのメンバー」 の目印
                    vu_userDic: JSON.parse("{{ dj_extends_user_str|escapejs }}"),
                },
            });
        </script>
    </body>
</html>
```

# Step O9o2o0gA10o0 ビュー作成 - extends_user_list/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models
                │   └── 📂 user_profile
                │       └── 📄 v1o0.py
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_extends_user_dic.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 extends_user_list
                │           └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 extends_user_list
                        └── 📂 v1o0
👉                          └── 📄 __init__.py
```

```py
class ExtendsUserListV():
    """O9o2o0gA10o0 （拡張済）会員一覧ビュー"""

    # そのページ
    _path_of_this_page = "practice_v1/extends_user_list/v1o0.html"
    #                     ---------------------------------------
    #                     1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/extends_user_list/v1o0.html` を取得
    #                                      ---------------------------------------

    @staticmethod
    def render(request):
        """描画"""

        # 以下のファイルはあとで作ります
        from .v_render import render_extends_user_list
        #    ---------        ------------------------
        #    1                2
        # 1. `src1/apps1/practice_v1/views/extends_user_list/v1o0/v_render.py`
        #                                                         --------
        # 2. `1.` に含まれる関数

        return render_extends_user_list(request, ExtendsUserListV._path_of_this_page)
```

# Step O9o2o0gA11o0 ビュー作成 - extends_user_list/v_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 models
                │   └── 📂 user_profile
                │       └── 📄 v1o0.py
                ├── 📂 models_helper
                │   └── 📂 user
                │       └── 📂 v1o0
                │           ├── 📄 __init__.py
                │           └── 📄 mh_get_extends_user_dic.py
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 extends_user_list
                │           └── 📄 v1o0.html
                └── 📂 views
                    └── 📂 extends_user_list
                        └── 📂 v1o0
                            ├── 📄 __init__.py
👉                          └── 📄 v_render.py
```

```py
import json
from django.shortcuts import render

# ユーザー モデルヘルパー
from apps1.practice_v1.models_helper.user.v1o0 import MhUser
#          -----------                    ----        ------
#          11                             12          2
#    -----------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


def render_extends_user_list(request, lp_extends_user_list):
    """O9o2o0gA11o0 描画 - （拡張済）会員登録ユーザー一覧

    Parameters
    ----------
    lp_extends_user_list : str
        ローカルパス
    """

    context = {
        # "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
        # Vue に渡すときは、 JSON オブジェクトではなく、 JSON 文字列です
        'dj_extends_user_str': json.dumps(MhUser.get_extends_user_dic()),
        #   --------                                 --------
    }

    return render(request, lp_extends_user_list, context)
```

# Step O9o2o0gA12o0 ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 models
        │       │   └── 📂 user_profile
        │       │       └── 📄 v1o0.py
        │       ├── 📂 models_helper
        │       │   └── 📂 user
        │       │       └── 📂 v1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 mh_get_extends_user_dic.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 v1o0
        │       │           └── 📄 extends_user_list.html
        │       └── 📂 views
        │           └── 📂 extends_user_list
        │               └── 📂 v1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_render.py
        └── 📂 project1                      # プロジェクト
👉          └── 📄 urls_practice.py
```

```py
# ...略...


# O9o2o0gA12o0 （拡張済）会員一覧
from apps1.practice_v1.views.extends_user_list.v1o0 import ExtendsUserListV
#          -----------                         ----        ----------------
#          11                                  12          2
#    ----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス


urlpatterns = [
    # ...略...


    # O9o2o0gA12o0 （拡張済）会員一覧
    path('practice/v1/extends-user-list/',
         # -----------------------------
         # 1
         ExtendsUserListV.render, name='practice_v1_extends_user_list'),
    #    -----------------------        -----------------------------
    #    2                              3
    # 1. 例えば `http://example.com/practice/v1/extends-user-list/` のような URL のパスの部分
    #                              ------------------------------
    # 2. ExtendsUserListV クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_v1_extends_user_list' %} のような形でURLを取得するのに使える
]
```

# Step O9o2o0gA13o0 管理画面へモデル登録 - admin.py ファイル編集

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 models
        │       │   └── 📂 user_profile
        │       │       └── 📄 v1o0.py
        │       ├── 📂 models_helper
        │       │   └── 📂 user
        │       │       └── 📂 v1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 mh_get_extends_user_dic.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 extends_user_list
        │       │           └── 📄 v1o0.html
        │       ├── 📂 views
        │       │   └── 📂 extends_user_list
        │       │       └── 📂 v1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
👉      │       └── 📄 admin.py
        └── 📂 project1                      # プロジェクト
            └── 📄 urls_practice.py
```

```py
# ...略...


# O9o2o0gA13o0 Userの拡張
from .models.user_profile.v1o0 import Profile
#    -------------------------        -------
#    1                                2
# 1. このファイルと同じディレクトリにある `models/user_profile/v1o0.py` ファイルの拡張子抜き
#                                      ------------------------
# 2. クラス


# ...略...


# Register your models here.
#   └── * 管理画面にモデルが表示されるようになる
#       └── * `manage.py makemigrations` コマンドの実行対象になる

# O9o2o0gA13o0 Userの拡張
admin.site.register(Profile)
```

👆 管理画面に Profile オブジェクトが表示されるようにした  

# Step O9o2o0gA14o0 スーパーユーザーでWebの管理画面へアクセス

👇 スーパーユーザーでログインすること  

📖 [http://localhost:8000/admin](http://localhost:8000/admin)  

👇 画面左に以下のように表示されていればOK  

```plaintext
+----------------------------------+
| PRACTICE                         |
+-------------+--------+-----------+
| Profiles    | ➕ Add | 🖊 Change |
+-------------+--------+-----------+
```

👆 `Profiles` リンクをクリックしてほしい  

```plaintext
[ ] PROFILE
--- -------
[ ] あなたの名前's profile
```

👆 あなたの名前をクリックしてほしい  

```plaintext
User: [あなたの名前]▽ 🖊 ➕
対局のマッチング状況: 0

                [Save and add another] [Save and continue editing] [SAVE]
```

👆 あなたのプロフィールに、User が紐づいているようにデータを登録（SAVE）しておいてほしい  

# Step O9o2o0gA15o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/extends-user-list/](http://localhost:8000/practice/v1/extends-user-list/)  

# Step O9o2o0gA16o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                    # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 models
        │       │   └── 📂 user_profile
        │       │       └── 📄 v1o0.py
        │       ├── 📂 models_helper
        │       │   └── 📂 user
        │       │       └── 📂 v1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 mh_get_extends_user_dic.py
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 extends_user_list
        │       │           └── 📄 v1o0.html
        │       ├── 📂 views
        │       │   └── 📂 extends_user_list
        │       │       └── 📂 v1o0
        │       │           ├── 📄 __init__.py
        │       │           └── 📄 v_render.py
        │       └── 📄 admin.py
        └── 📂 project1                      # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/extends-user-list/,（拡張済）会員一覧
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでアクティブユーザーの一覧を作ろう！](https://qiita.com/muzudho1/items/bea77e8a69c5c805e1d7)  

# 参考にした記事

📖 [How to Extend Django User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)  
📖 [【django】モデルのフィールドについて：フィールドの型・オプション一覧](https://office54.net/python/django/model-field-options)  
📖 [DjangoでMigrationsのリセット方法（既存のデータベースを残したまま）](https://dot-blog.jp/news/how-to-reset-django-migrations/)  
📖 [Django : How to use select_related for a OneToOneField?](https://stackoverflow.com/questions/38701919/django-how-to-use-select-related-for-a-onetoonefield)  
📖 [Django2.0から必須になったon_deleteの使い方](https://djangobrothers.com/blogs/on_delete/)  
📖 [【django】モデルのリレーションフィールド：ForeignKey、OneToOneField、ManyToManyField](https://office54.net/python/django/model-field-relation)  
📖 [One-to-one relationships](https://docs.djangoproject.com/en/4.0/topics/db/examples/one_to_one/)  
📖 [One-To-One Relationship (OneToOneField)](https://medium.com/django-rest/one-to-one-relationships-onetoonefield-917cfd2e4ce3)  
📖 [Managers](https://docs.djangoproject.com/en/4.0/topics/db/managers/)  
📖 [Django 'model' object is not iterable](https://stackoverflow.com/questions/56374741/django-model-object-is-not-iterable)  

## UserとProfileのリレーション

📖 [RelatedObjectDoesNotExist: User has no userprofile](https://stackoverflow.com/questions/36317816/relatedobjectdoesnotexist-user-has-no-userprofile)  

## 日付型の文字列変換

📖 [How To Convert Python Datetime To String](https://appdividend.com/2022/03/22/how-to-convert-datetime-to-string-in-python/#:~:text=To%20convert%20Python%20datetime%20to%20string%2C%20use%20the%20strftime(),%2C%20time%2C%20or%20datetime%20object.)  
