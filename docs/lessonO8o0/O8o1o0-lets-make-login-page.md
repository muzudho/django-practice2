# サンプルを見る

📖 [http://tic.warabenture.com:8000/accounts/v1/login/](http://tic.warabenture.com:8000/accounts/v1/login/) - ログイン  
📖 [http://tic.warabenture.com:8000/accounts/v1/logout/](http://tic.warabenture.com:8000/accounts/v1/logout/) - ログアウト  

# 目的

見た目がマシな　ログイン（ユーザー認証）のページがほしい  

# はじめに

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
連載の目次: 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae)  

この記事のアーキテクチャ:  

| Key       | Value                                     |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   ├── 📂 portal_v1                # アプリケーション
    │   │   └── 📂 practice_v1              # アプリケーション
    │   ├── 📂 data
    │   ├── 📂 project1                     # プロジェクト
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings.py
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

# Step O8o1o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step O8o1o0g2o0 テンプレート作成 - login.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1                            # あなたの開発用ディレクトリー。任意の名前
        └── 📂 apps1
            └── 📂 allauth_customized_v1    # アプリケーション
                └── 📂 templates
                    └── 📂 account          # allauth のディレクトリー構成を真似ます
👉                      └── 📄 login.html
```

```html
<!--
    📖[login.html](https://github.com/pennersr/django-allauth/blob/master/allauth/templates/account/login.html)
-->

<!--
    # See also: 📖[Custom Signup View in django-allauth](https://tech.serhatteker.com/post/2020-06/custom-signup-view-in-django-allauth/)
-->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
<!-- -->
{% load i18n %}
<!-- -->
{% load account socialaccount %}
<!-- -->
{% get_providers as socialaccount_providers %}
<!-- -->
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css" rel="stylesheet" />
        <link href="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css" rel="stylesheet" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
        <!--                                                ===================
                                                            1
            1. Example: `http://example.com/static/favicon.ico`
                                            ==================
        -->
        <title>サインイン</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <!-- v-app-bar に app プロパティを指定しないなら、背景画像を付けてほしい -->
                <v-app-bar app dense elevation="4">
                    <v-app-bar-nav-icon></v-app-bar-nav-icon>
                    <v-toolbar-title>サインイン</v-toolbar-title>
                </v-app-bar>
                <v-main>
                    <v-container>
                        <h3>もし会員登録をしてないなら</h3>
                        {% if socialaccount_providers %}

                        <!-- 👇ここらへん分からない -->
                        <p>{% blocktrans with site.name as site_name %}Please sign in with one of your existing third party accounts. Or, <a href="{{ signup_url }}">sign up</a> for a {{ site_name }} account and sign in below:{% endblocktrans %}</p>
                        <div class="socialaccount_ballot">
                            <ul class="socialaccount_providers">
                                <!-- -->
                                {% include "socialaccount/snippets/provider_list.html" with process="login" %}
                                <!-- -->
                            </ul>

                            <div class="login-or">or</div>
                        </div>
                        <!-- -->
                        {% include "socialaccount/snippets/login_extra.html" %}
                        <!-- 👆ここらへん分からない -->

                        <!-- -->
                        {% else %}
                        <!-- 👇こっちが出てくる -->
                        <p>もし　あなたがアカウントを　まだ作っていないなら、まず <v-btn class="my-4" color="primary" :href="createPathOfSignup()">サインアップ</v-btn> してください</p>
                        <!-- 👆こっちが出てくる -->
                        {% endif %}
                        <!-- -->
                    </v-container>
                    <v-container>
                        <h3>サインイン（利用開始）</h3>
                        <form class="login" method="POST" :action="createPathOfSignin()">
                            <!-- -->
                            {% csrf_token %}
                            <!-- 手動フォーム作成 ここから -->
                            {{ form.non_field_errors }}

                            <!-- ユーザー名 -->
                            <div class="fieldWrapper">
                                {{ form.login.errors }}
                                <v-text-field name="login" v-model="vu_userName.value" :rules="vu_userName.rules" counter="16" label="ユーザー名" required hint="使える文字 a-z， 0-9． 先頭に数字は使えません。 最大 16 文字"></v-text-field>
                            </div>

                            <div class="fieldWrapper">
                                {{ form.password.errors }}
                                <v-text-field type="password" name="password" v-model="vu_password" counter label="パスワード" required></v-text-field>
                            </div>
                            <div class="fieldWrapper">
                                {{ form.remember.errors }}
                                <v-checkbox v-model="vu_rememberFlag" label="パスワードを入力したままにする"></v-checkbox>
                            </div>
                            <!-- 手動フォーム作成 ここまで -->
                            <!-- -->
                            {% if redirect_field_value %}
                            <!-- -->
                            <input type="hidden" name="{{ redirect_field_name }}" value="{{ redirect_field_value }}" />
                            <!-- -->
                            {% endif %}
                            <!-- -->
                            <v-btn class="my-4" color="primary" type="submit">サインイン</v-btn>
                            <a class="button secondaryAction" href="{% url 'account_reset_password' %}">パスワードを忘れたら</a>
                        </form>
                    </v-container>
                </v-main>
            </v-app>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>

        <script src="{% static 'allauth_customized_v1/o1o0/form_html_parser.js' %}"></script>
        <!--            ======================================================
                        1
            1. `src1/apps1/allauth_customized_v1/static/allauth_customized_v1/o1o0/form_html_parser.js`
                                                 =====================================================
        -->

        <script>
            let vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // "vu_" は 「vue1.dataのメンバー」 の目印

                    // HTMLタグ文字列が渡されるので、解析します
                    vu_loginFormDoc: new DjangoAllauthFormParser().parseHtmlString("login", "{{ form.login|escapejs }}"),

                    // ユーザー名
                    vu_userName: {
                        value: "",
                        rules: [
                            // FIXME ここでルールを色々書いているが、モデル側で対応していないので、モデル側も対応してほしい
                            (value) => !!value || "Required", // 空欄の禁止
                            (v) => v.length <= 16 || "Max 16 characters", // 文字数上限
                            (value) => {
                                const pattern = /^[a-z][a-z0-9]*$/; // 正規表現で指定
                                return pattern.test(value) || "Invalid format";
                            },
                        ],
                    },

                    vu_passwordFormDoc: new DjangoAllauthFormParser().parseHtmlString("password", "{{ form.password|escapejs }}"),
                    vu_password: "",

                    vu_rememberFormDoc: new DjangoAllauthFormParser().parseHtmlString("form", "{{ form.remember|escapejs }}"),
                    vu_rememberFlag: false,

                    // vu_pathOfSignup: "{{ signup_url }}", // django-allauth のデフォルト
                    vu_pathOfSignup: "{% url 'signup' %}",
                    // vu_pathOfSignin: "{% url 'account_login' %}", // django-allauth のデフォルト
                    vu_pathOfSignin: "{% url 'login' %}",
                    {% block vue1_data_footer %}
                    {% endblock vue1_data_footer %}
                },
                methods: {
                    createPathOfSignin() {
                        let path = `${location.protocol}//${location.host}${this.vu_pathOfSignin}`;
                        //          --------------------  ---------------]-----------------------
                        //          1                     2               3
                        // 1. protocol
                        // 2. host
                        // 3. path
                        console.log(`SignIn path=[${path}]`);
                        return path;
                    },
                    createPathOfSignup() {
                        let path = `${location.protocol}//${location.host}${this.vu_pathOfSignup}`;
                        //          --------------------  ---------------]-----------------------
                        //          1                     2               3
                        // 1. protocol
                        // 2. host
                        // 3. path
                        console.log(`SignUp path=[${path}]`);
                        return path;
                    },
                },
            });
        </script>
    </body>
</html>
```

# Step O8o1o0g3o0 ビュー モジュール作成 - login フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 allauth_customized_v1    # アプリケーション
                ├── 📂 templates
                │   └── 📂 account
                │       └── 📄 login.html
                └── 📂 views
                    └── 📂 o1o0
                        └── 📂 login
👉                          └── 📄 __init__.py
```

```py
# See also: 📖[Custom Signup View in django-allauth](https://tech.serhatteker.com/post/2020-06/custom-signup-view-in-django-allauth/)
from allauth.account.views import LoginView


class AccountsV1LoginView(LoginView):
    """django-allauth のログイン ビューをカスタマイズします
    📖[views.py](https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py)
    """

    # ファイルパス（使ってるか分からない）
    template_name = "allauth_customized_v1/templates/account/login.html"
    #                --------------------------------------------------
    #                1
    # 1. src1/apps1/allauth_customized_v1/templates/account/login.html を取得
    #               --------------------------------------------------
```

# Step O8o1o0g4o0 サブ ルート作成 - urls_accounts.py

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 allauth_customized_v1    # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 account
        │       │       └── 📄 login.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 login
        │                   └── 📄 __init__.py
        └── 📂 project1
👉          ├── 📄 urls_accounts.py          # こちら
❌          └── 📄 urls.py                   # これではない
```

```py
# ...略...


# ログイン（入場）
from apps1.allauth_customized_v1.views.o1o0.login import AccountsV1LoginView
#          ---------------------            -----        -------------------
#          11                               12           2
#    --------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. クラス


urlpatterns = [
    # ...中略...


    # ログイン（入場）
    path("accounts/v1/login/", view=AccountsV1LoginView.as_view(),
         # -----------------        -----------------------------
         # 1                        2
         name="login"),
    #          -----
    #          3
    # 1. 例えば `http://example.com/accounts/v1/login/` のような URL のパスの部分
    #                              -------------------
    # 2. allauth の LoginView をカスタマイズしたオブジェクト
    # 3. HTMLテンプレートの中で {% url 'login' %} のような形でURLを取得するのに使える
]
```

# Step O8o1o0g5o0 Web画面へアクセス

📖 [http://localhost:8000/accounts/v1/login/](http://localhost:8000/accounts/v1/login/)  

👆 ログイン ページを開く  

既にログインしているなら、  

📖 [http://localhost:8000/accounts/v1/logout/](http://localhost:8000/accounts/v1/logout/)  

👆 ログアウトを試してほしい  

# Step O8o1o0g6o0 ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 allauth_customized_v1    # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 account
        │       │       └── 📄 login.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📄 v_login.py
        └── 📂 project1
            ├── 📄 urls_accounts.py
            └── 📄 urls.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/accounts/v1/login/,ログイン（入場）
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでログインしていないと見れないページ，およびログアウト機能を付けよう！](https://qiita.com/muzudho1/items/9f1ae4d0debc0b8aa4b1)  

# 関連する記事

📖 [login.html](https://github.com/pennersr/django-allauth/blob/master/allauth/templates/account/login.html) - テンプレートの原型  

## form関連

📖 [Working with forms](https://docs.djangoproject.com/en/4.0/topics/forms/) - 一番詳しい  
📖 [forms.py](https://github.com/pennersr/django-allauth/blob/master/allauth/account/forms.py) - 原型  
📖 [How can I render Django Form with vuetify?](https://stackoverflow.com/questions/63993890/how-can-i-render-django-form-with-vuetify)  
📖 [vue.js - Vuetifyの入力値でDjangoのテンプレートタグを使用する方法は？](https://tutorialmore.com/questions-2757963.htm)  
📖 [Anyone know how to use vuetify with django form?](https://forum.djangoproject.com/t/anyone-know-how-to-use-vuetify-with-django-form/4807)  
📖 [Source code for django.forms.boundfield](https://docs.djangoproject.com/en/2.2/_modules/django/forms/boundfield/)  
📖 [DjangoのFormクラスを使う](https://qiita.com/taumu/items/4587a91c4d7d2db165b3)  

## User関連

📖 [RelatedObjectDoesNotExist: User has no userprofile](https://stackoverflow.com/questions/36317816/relatedobjectdoesnotexist-user-has-no-userprofile)  
📖 [How to resolve the "psycopg2.errors.UndefinedTable: relation "auth_user" does not exist" when running django unittests on Travis](https://stackoverflow.com/questions/56355516/how-to-resolve-the-psycopg2-errors-undefinedtable-relation-auth-user-does-no) - `migrations/__init__.py` は消してはダメ？  
