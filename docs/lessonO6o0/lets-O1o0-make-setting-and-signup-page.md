# 目的

ゲーム対局サーバーに、参加ユーザーが集まるよう、ユーザー別にライフスタイルにあったサービスを提供したい  

# 手段

とりあえず、会員制サイトを作る  

1. ユーザー登録（サインアップ）
2. ログイン（サインイン）
3. 指定のメールアドレスへパスワードの変更画面URLを送る機能

を付ける方法を説明する  

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
    ├── 📂 host1
    │   ├── 📂 apps1
    │   │   ├── 📂 portal_v1                # アプリケーション名
    │   │   └── 📂 practice_v1
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト名
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

# Step 1. Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step 2. SMTP設定 - 例えばGoogleアカウント

パスワードを忘れたとき、パスワード変更画面のURLがメールで飛んでくる仕掛けはよくある。  
そのメールを飛ばすサーバーは、例えばGoogleのを借りることにする  

Googleのアカウントから、  

`[Googleアカウント] - [セキュリティ] - [Googleへのログイン] - [アプリパスワード]` と進んでほしい。  
アプリの名前は、例えば `DjangoPractice` とでもしておけばいいだろう。  
すると 16桁の **アプリパスワード** が発行される。覚えておかなくていいと表示されるかも知れないが、一旦覚えてほしい  

# Step 3. 環境変数作成 - ".env" ファイル

🚫ソースにパスワードをハードコーディングしてリモートのGitリポジトリにプッシュすると被害に遭うだろう。  

パスワードのような漏れて困るものは ソースではなく 📄 `.env` ファイルに書くのを習慣にし、  
このファイルは 📄 `.gitignore` ファイルを設定することで（あるいは既に設定してあって） リモートのGitリポジトリにプッシュしないようにしてほしい  

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
👉      └── 📄 .env
```

```plaintext
EMAIL_HOST_USER=あなたのGmailアドレス
EMAIL_HOST_PASSWORD=あなたのGmailアドレスのアプリパスワード
```

あなたのGmailのパスワードを書くのではなく、Gmailの**アプリ**パスワードを書くという違いに気を付けてほしい  

# Step 4. ドッカーコンポーズ編集 - docker-compose.yml ファイル

👇 以下のファイルの該当箇所を追加してほしい

```plaintext
    └── 📂 host1
        ├── 📄 .env
👉      └── 🐳 docker-compose.yml
```

```yaml
# ...略...


services:


  # ...略...


  # Djangoアプリ
  web:


    # ...略...


    environment:


      # ...略...


      # 以下を追加
      - EMAIL_HOST_USER=${EMAIL_HOST_USER}
      - EMAIL_HOST_PASSWORD=${EMAIL_HOST_PASSWORD}


# ...略...
```

意味としては `${.envファイルの中の変数名}` の内容を、 Dockerコンテナの環境変数に入れている。  
最近の Docker は、`docker-compose.yml` と同じ階層の `.env` ファイルを勝手に読み込んでくれる  

# Step 5. Pythonパッケージ編集 - requirements.txt ファイル

👇 以下の既存ファイルの末尾にでも追加してほしい  

```plaintext
    └── 📂 host1
        ├── 📄 .env
        ├── 🐳 docker-compose.yml
👉      └── 📄 requirements.txt
```

```shell
# ...略...


# ユーザー認証
django-allauth>=0.32.0
```

# Step 6. Dockerコンテナのビルド

requirements.txt を編集したので...  

👇 以下のコマンドを打鍵してほしい  

```shell
# requirements.txtを変更したので、Pythonパッケージのインストールをやり直します
docker-compose build
```

# Step 7. 設定編集 - settings.py ファイル

👇 以下の既存ファイルに該当箇所を追加してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 project1
👉      │   └── 📄 settings.py
        ├── 📄 .env
        ├── 🐳 docker-compose.yml
        └── 📄 requirements.txt
```

```py
# ...略...

INSTALLED_APPS = [
    # あなたが追加したアプリケーション


    # ...略...


    # 以下を追加
    'apps1.allauth_customized_v1',


    # ...略...


    # Djangoの標準アプリケーション


    # ...略...


    # 以下を追加
    # ユーザー認証のためのアプリケーション
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

# ...略...

# 調べ終わったら消す
#print(
#    f"os.path.join(BASE_DIR, 'apps1/practice_v1/templates')={os.path.join(BASE_DIR, 'apps1/practice_v1/templates')}")
# Example: `/code/apps1/practice_v1/templates`

TEMPLATES = [
    {
        # ...略... ; Example: 'BACKEND'

        'DIRS': [
            # ...略...


            # allauth
            os.path.join(BASE_DIR, 'apps1/allauth_customized_v1/templates'),
            #                       -------------------------------------
            #                       10
            # Example: `/host1/apps1/allauth_customized_v1/templates/account/signup.html`
            #                        ---------------------          --------
            #                        11                             2
            #                  -------------------------------------
            #                  10
            # 10. テンプレート ディレクトリーへのパス
            # 11. アプリケーション
            # 2. まるで `http://example.com/account` という素材フォルダーがあるかのように扱われる
            #                             --------
        ],


        # ...略... ; Example: 'APP_DIRS', 'OPTIONS'
    },
]


# ...略... ; Example: 'WSGI_APPLICATION, 'DATABASES', ... 'STATIC_URL', 'DEFAULT_AUTO_FIELD'


# 以下を、ファイルの末尾にでも追加
# +----
# | Allauth
# |
# https://sinyblog.com/django/django-allauth/

SITE_ID = 1 # 動かしているサイトを識別するID
LOGIN_REDIRECT_URL = 'home' # ログイン後に遷移するURL, または name の指定
LOGIN_URL = 'login' # ログインしていないときに飛ばされる先のURL, または name の指定

# ログアウト後に遷移するURL, または name の指定
# ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/v1/login/'
#                                -------------------
#                                1
# 1. 例えば `http://example.com/accounts/v1/login/` というURLのパスの部分
#                             -------------------
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'

EMAIL_HOST = 'smtp.gmail.com' # メールサーバの指定
EMAIL_PORT = 587 # ポート番号の指定
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER') # メールサーバのGmailのアドレス
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD') # メールサーバのGmailのパスワード
EMAIL_USE_TLS = True # TLSの設定（TRUE,FALSE)
# |
# | Allauth
# +----
```

# Step 8. Dockerコンテナのビルド

settings.py を編集してアプリケーションを追加したので...  

👇 以下のコマンドを打鍵してほしい  

```shell
docker-compose run --rm web python3 manage.py makemigrations --settings project1.settings
#                                                                       -----------------
#                                                                       1
# 1. host1/project1/settings.py
#          -----------------

docker-compose run --rm web python3 manage.py migrate --settings project1.settings
#                                                                -----------------
#                                                                1
# 1. host1/project1/settings.py
#          -----------------
```

# Step 9. 機能強化 - form_html_parser.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 allauth_customized_v1            # アプリケーション
        │       └── 📂 static
        │           └── 📂 allauth_customized_v1    # アプリケーションと同名
        │               └── 📂 o1o0
👉      │                   └── 📄 form_html_parser.js
        ├── 📂 project1
        │   └── 📄 settings.py
        ├── 📄 .env
        ├── 🐳 docker-compose.yml
        └── 📄 requirements.txt
```

👇以下のファイルは 大雑把に作ったものなので、 django-allauth パッケージのHTML出力の仕様が変わったら作り直してほしい  

```js
class DjangoAllauthFormParser {
    constructor() {

    }

    get htmlString() {
        return this._htmlString;
    }

    parseHtmlString(name, htmlString) { 
        this._htmlString = htmlString;
        console.log(`${name} htmlString=${this.htmlString}`);
        // Examples:
        //
        // signup.html
        // <input type="text" name="username" placeholder="Username" autocomplete="username" minlength="1" maxlength="150" required id="id_username">
        // <label for="id_email">E-mail (optional):</label></th><td><input type="email" name="email" placeholder="E-mail address" autocomplete="email" id="id_email">
        // <label for="id_password1">Password:</label></th><td><input type="password" name="password1" placeholder="Password" autocomplete="new-password" required id="id_password1">
        // <label for="id_password2">Password (again):</label></th><td><input type="password" name="password2" placeholder="Password (again)" autocomplete="new-password" required id="id_password2">
        //
        // login.html
        // <input type="text" name="login" placeholder="Username" autocomplete="username" maxlength="150" required id="id_login">
        // <input type="password" name="password" placeholder="Password" autocomplete="current-password" required id="id_password">
        // <input type="checkbox" name="remember" id="id_remember">
        //
        // 両端の < > を外せば、 string か、 string="string" のパターンになっているが、エスケープシーケンスが入っていると難しい
        // 決め打ちをしてしまうのが簡単

        // signup.html
        const reUsername = /<input type="text" name="username" placeholder="(.*)" autocomplete="(.*)" minlength="(\d+)" maxlength="(\d+)" required id="(\w+)">/;
        const reEmail = /<input type="email" name="email" placeholder="(.*)" autocomplete="(.*)" id="(\w+)">/;
        const rePassword1 = /<input type="password" name="password1" placeholder="(.*)" autocomplete="(.*)" required id="(\w+)">/;
        const rePassword2 = /<input type="password" name="password2" placeholder="(.*)" autocomplete="(.*)" required id="(\w+)">/;

        // login.html
        const reLogin = /<input type="text" name="login" placeholder="(.*)" autocomplete="(.*)" maxlength="(\d+)" required id="(\w+)">/;
        const rePassword = /<input type="password" name="password" placeholder="(.*)" autocomplete="(.*)" required id="(\w+)">/;
        const reRemember = /<input type="checkbox" name="remember" id="(\w+)">/;

        // signup.html username
        {
            let groups = reLogin.exec(htmlString);
            if (groups) {
                console.log(`username placeholder=[${groups[1]}] autocomplete=[${groups[2]}] minlength=[${groups[3]}] maxlength=[${groups[4]}] id=[${groups[5]}]`)

                return {
                    type: "text",
                    name: "username",
                    placeholder: groups[1],
                    autocomplete: groups[2],
                    minlength: parseInt(groups[3]),
                    maxlength: parseInt(groups[4]),
                    id: groups[5],
                };
            }
        }

        // signup.html email
        {
            let groups = reLogin.exec(htmlString);
            if (groups) {
                console.log(`email placeholder=[${groups[1]}] autocomplete=[${groups[2]}] id=[${groups[3]}]`)

                return {
                    type: "email",
                    name: "email",
                    placeholder: groups[1],
                    autocomplete: groups[2],
                    id: groups[3],
                };
            }
        }

        // signup.html password1
        {
            let groups = reLogin.exec(htmlString);
            if (groups) {
                console.log(`password1 placeholder=[${groups[1]}] autocomplete=[${groups[2]}] id=[${groups[3]}]`)

                return {
                    type: "password",
                    name: "password1",
                    placeholder: groups[1],
                    autocomplete: groups[2],
                    id: groups[3],
                };
            }
        }

        // signup.html password2
        {
            let groups = reLogin.exec(htmlString);
            if (groups) {
                console.log(`password2 placeholder=[${groups[1]}] autocomplete=[${groups[2]}] id=[${groups[3]}]`)

                return {
                    type: "password",
                    name: "password2",
                    placeholder: groups[1],
                    autocomplete: groups[2],
                    id: groups[3],
                };
            }
        }

        // login.html login
        {
            let groups = reLogin.exec(htmlString);
            if (groups) {
                console.log(`login placeholder=[${groups[1]}] autocomplete=[${groups[2]}] maxlength=[${groups[3]}] id=[${groups[4]}]`)

                return {
                    type: "text",
                    name: "login",
                    placeholder: groups[1],
                    autocomplete: groups[2],
                    maxlength: parseInt(groups[3]),
                    id: groups[4],
                };
            }
        }

        // login.html password
        {
            let groups = rePassword.exec(htmlString);
            if (groups) {
                console.log(`password placeholder=[${groups[1]}] autocomplete=[${groups[2]}] id=[${groups[3]}]`)

                return {
                    type: "password",
                    name: "password",
                    placeholder: groups[1],
                    autocomplete: groups[2],
                    id: groups[3],
                }
            }
        }

        // login.html remember
        {
            let groups = reRemember.exec(htmlString);
            if (groups) {
                console.log(`remember id=[${groups[1]}]`)

                return {
                    type: "checkbox",
                    name: "remember",
                    id: groups[1],
                }
            }
        }

        return {
            type: "undefined",
            name: "unknown",
        }
    }
}
```

# Step 10. テンプレート編集 - signup.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 allauth_customized_v1            # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 allauth_customized_v1    # アプリケーションと同名
        │       │       └── 📂 o1o0
        │       │           └── 📄 form_html_parser.js
        │       └── 📂 templates
        │           └── 📂 account                  # ディレクトリ構成を allauth アプリケーション に合わせる
👉      │               └── 📄 signup.html
        ├── 📂 project1
        │   └── 📄 settings.py
        ├── 📄 .env
        ├── 🐳 docker-compose.yml
        └── 📄 requirements.txt
```

```html
<!--
    # See also: 📖[Custom Signup View in django-allauth](https://tech.serhatteker.com/post/2020-06/custom-signup-view-in-django-allauth/)
-->
{% load static %} {# 👈あとで static "URL" を使うので load static します #}
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
        <title>サインアップ</title>
    </head>
    <body>
        <div id="app">
            <v-app>
                <!-- v-app-bar に app プロパティを指定しないなら、背景画像を付けてほしい -->
                <v-app-bar app dense elevation="4">
                    <v-app-bar-nav-icon></v-app-bar-nav-icon>
                    <v-toolbar-title>サインアップ</v-toolbar-title>
                </v-app-bar>
                <v-main>
                    {% block section_login %}
                    <!--
                    <v-container>
                        <h3>既にアカウントを持っているなら</h3>
                        <v-btn class="my-4" color="primary" :href="createPathOfSignin()">サインイン</v-btn>
                    </v-container>
                    -->
                    {% endblock section_login %}
                    <v-container>
                        <h3>会員登録するなら</h3>
                        <form class="signup" id="signup_form" method="post" :action="createPathOfSignup()">
                            <!-- -->
                            {% csrf_token %}
                            <!-- -->
                            <!-- 手動フォーム作成 ここから -->
                            {{ form.non_field_errors }}

                            <!-- ユーザー名 -->
                            <div class="fieldWrapper">
                                {{ form.username.errors }}
                                <v-text-field name="username" v-model="vu_userName.value" :rules="vu_userName.rules" minlength="1" maxlength="16" counter="16" label="ユーザー名" required hint="使える文字 a-z， 0-9． 先頭に数字は使えません。 最大 16 文字"></v-text-field>
                            </div>

                            <div class="fieldWrapper">
                                {{ form.email.errors }}
                                <v-text-field name="email" v-model="vu_email" counter label="E-mali"></v-text-field>
                            </div>
                            <div class="fieldWrapper">
                                {{ form.password1.errors }}
                                <v-text-field type="password" name="password1" v-model="vu_password1" counter label="パスワード" required></v-text-field>
                            </div>
                            <div class="fieldWrapper">
                                {{ form.password2.errors }}
                                <v-text-field type="password" name="password2" v-model="vu_password2" counter label="パスワード（再入力）" required></v-text-field>
                            </div>
                            <!-- 手動フォーム作成 ここまで -->
                            {% if redirect_field_value %}
                            <!-- -->
                            <input type="hidden" name="{{ redirect_field_name }}" value="{{ redirect_field_value }}" />
                            <!-- -->
                            {% endif %}
                            <!-- -->
                            <v-btn class="my-4" color="primary" type="submit">サインアップ &raquo;</v-btn>
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
            1. host1/apps1/allauth_customized_v1/static/allauth_customized_v1/o1o0/form_html_parser.js
                                                ======================================================
        -->

        <script>
            let vue1 = new Vue({
                el: "#app",
                vuetify: new Vuetify(),
                data: {
                    // "vu_" は 「vue1.dataのメンバー」 の目印

                    // HTMLタグ文字列が渡されるので、解析します
                    vu_usernameFormDoc: new DjangoAllauthFormParser().parseHtmlString("username", "{{ form.username|escapejs }}"),

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

                    vu_emailFormDoc: new DjangoAllauthFormParser().parseHtmlString("email", "{{ form.email|escapejs }}"),
                    vu_email: "",

                    vu_password1FormDoc: new DjangoAllauthFormParser().parseHtmlString("password1", "{{ form.password1|escapejs }}"),
                    vu_password1: "",

                    vu_password2FormDoc: new DjangoAllauthFormParser().parseHtmlString("password2", "{{ form.password2|escapejs }}"),
                    vu_password2: "",

                    vu_pathOfSignup: "{% url 'signup' %}",
                    {% block vue1_data_footer %}
                    // vu_pathOfSignin: "{{ login_url }}", // django-allauth のデフォルト
                    // vu_pathOfSignin: "｛％ url 'login' ％｝",
                    {% endblock vue1_data_footer %}
                },
                methods: {
                    createPathOfSignin() {
                        let url = `${location.protocol}//${location.host}${this.vu_pathOfSignin}`;
                        //         --------------------  ---------------]-----------------------
                        //         1                     2               3
                        // 1. protocol
                        // 2. host
                        // 3. path
                        console.log(`SignIn url=[${url}]`);
                        return url;
                    },
                    createPathOfSignup() {
                        let url = `${location.protocol}//${location.host}${this.vu_pathOfSignup}`;
                        //         --------------------  ---------------]-----------------------
                        //         1                     2               3
                        // 1. protocol
                        // 2. host
                        // 3. path
                        console.log(`SignUp url=[${url}]`);
                        return url;
                    },
                },
            });
        </script>
    </body>
</html>
```

# Step 11. ビュー モジュール作成 - accounts フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 allauth_customized_v1            # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 allauth_customized_v1        # アプリケーションと同名
        │       │       └── 📂 o1o0
        │       │           └── 📄 form_html_parser.js
        │       ├── 📂 templates
        │       │   └── 📂 account                   # ディレクトリ構成を allauth アプリケーション に合わせる
        │       │       └── 📄 signup.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📂 accounts
👉      │                   └── 📄 __init__.py
        ├── 📂 project1
        │   └── 📄 settings.py
        ├── 📄 .env
        ├── 🐳 docker-compose.yml
        └── 📄 requirements.txt
```

```py
# See also: 📖[Custom Signup View in django-allauth](https://tech.serhatteker.com/post/2020-06/custom-signup-view-in-django-allauth/)
from allauth.account.views import SignupView


class AccountsV1SignupView(SignupView):
    """django-allauth のサインアップ ビューをカスタマイズします
    📖[views.py](https://github.com/pennersr/django-allauth/blob/master/allauth/socialaccount/views.py)
    """

    # ファイルパス
    template_name = "account/signup.html"
    #                -------------------
    #                1
    # 1. `host1/apps1/allauth_customized_v1/templates/account/signup.html` を取得
    #                                                 -------------------

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...
```

# Step 12. サブ ルート作成 - urls_accounts.py

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 allauth_customized_v1            # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 allauth_customized_v1        # アプリケーションと同名
        │       │       └── 📂 o1o0
        │       │           └── 📄 form_html_parser.js
        │       ├── 📂 templates
        │       │   └── 📂 account                   # ディレクトリ構成を allauth アプリケーション に合わせる
        │       │       └── 📄 signup.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📄 v_accounts.py
        ├── 📂 project1
        │   ├── 📄 settings.py
👉      │   ├── 📄 urls_accounts.py          # 新規作成
❌      │   └── 📄 urls.py                   # これではない
        ├── 📄 .env
        ├── 🐳 docker-compose.yml
        └── 📄 requirements.txt
```

```py
from django.urls import include, path  # include 追加
from django.views.generic import TemplateView  # 追加

# サインアップ（会員登録）
from apps1.allauth_customized_v1.views.o1o0.accounts import AccountsV1SignupView
#          ---------------------            --------        --------------------
#          11                               12              2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. クラス


urlpatterns = [
    # See also: https://sinyblog.com/django/django-allauth/

    # ログイン後に戻ってくるWebページの指定
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #    --  -----------------------------------------------        ----
    #    1   2                                                      3
    # 1. URL に パスを付けなかったときにマッチする
    # 2. 最初から用意されているビュー
    # 3. このパスを 'home' という名前で覚えておく

    # allauth の URLのパスのコピー
    path('accounts/v1/', include('allauth.urls')),
    #     ------------   -----------------------
    #     1
    # 1. 例えば `http://example.com/accounts/v1/` のような URLのパスの部分
    #                              ------------
    # 2. allauth アプリケーションに含まれる `allauth/urls.py` の urlpatterns 、
    #                                     ------------
    #    例えば `login/` のようなパスを (1.) のパスにぶら下げる形で全てコピーします

    # サインアップ（会員登録）
    path("accounts/v1/signup/", view=AccountsV1SignupView.as_view(),
         # ------------------        ------------------------------
         # 1                        2
         name="signup"),
    #          ------
    #          3
    # 1. 例えば `http://example.com/accounts/v1/signup/` のような URL のパスの部分にマッチする
    #                              -------------------
    # 2. allauth の SignupView をカスタマイズしたオブジェクト
    # 3. HTMLテンプレートの中で {% url 'signup' %} のような形でURLを取得するのに使える
]
```

# Step 13. 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 allauth_customized_v1                # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 allauth_customized_v1        # アプリケーションと同名
        │       │       └── 📂 o1o0
        │       │           └── 📄 form_html_parser.js
        │       ├── 📂 templates
        │       │   └── 📂 account                      # ディレクトリ構成を allauth アプリケーション に合わせる
        │       │       └── 📄 signup.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📄 v_accounts.py
        ├── 📂 project1
        │   ├── 📄 settings.py
❌      │   ├── 📄 urls_accounts.py          # これではない
👉      │   └── 📄 urls.py                   # こっち
        ├── 📄 .env
        ├── 🐳 docker-compose.yml
        └── 📄 requirements.txt
```

```py
from django.urls import include, path


# ...略...


urlpatterns = [


    # ...略...


    # 認証
    path('', include('project1.urls_accounts')),
    #    --           ----------------------
    #      1          2
    # 1. 例えば `http://example.com/` のような URLの直下
    # 2. `host1/project1/urls_accounts.py` の urlpatterns を (1.) にぶら下げる
    #           ----------------------
]
```

# Step 14. Webページへアクセス

📖 [http://localhost:8000/accounts/v1/signup/](http://localhost:8000/accounts/v1/signup/)  

👆 サインアップ ページを開く  
メールが届くことも確認してほしい  

あとは アカウントを作成したり、パスワードを忘れたときの手続きを試してほしい  

// 既にログインしているなら、  
//
// 📖 [http://localhost:8000/accounts/v1/logout/](http://localhost:8000/accounts/v1/logout/)  
//
// 👆 ログアウトを試してほしい  

# Step 15. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   ├── 📂 portal_v1
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 allauth_customized_v1            # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 allauth_customized_v1
        │       │       └── 📂 o1o0
        │       │           └── 📄 form_html_parser.js
        │       ├── 📂 templates
        │       │   └── 📂 account
        │       │       └── 📄 signup.html
        │       └── 📂 views
        │           └── 📂 o1o0
        │               └── 📄 v_accounts.py
        ├── 📂 project1
        │   ├── 📄 settings.py
        │   ├── 📄 urls_accounts.py
        │   └── 📄 urls.py
        ├── 📄 .env
        ├── 🐳 docker-compose.yml
        └── 📄 requirements.txt
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/accounts/v1/signup/,サインアップ
/accounts/v1/logout/,サインアウト
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoでdataフォルダーを壊してしまったときのリセット方法を覚えよう！](https://qiita.com/muzudho1/items/1ecaac80568c981fcd59)  

# 関連する記事

📚 [Djangoで、django-allauthのテンプレートを差し替えよう！](https://qiita.com/muzudho1/items/6120055b2a8eb4e28527)  

# 参考にした記事

## Django関連

📖 [Django 管理コマンド manage.py まとめ](https://qiita.com/okoppe8/items/7e3de8a4dd40b48debea)  

## Docker関連

📖 [docker-compose.ymlで.envファイルに定義した環境変数を使う](https://kitigai.hatenablog.com/entry/2019/05/08/003000)  

## form関連

📖 [Working with forms](https://docs.djangoproject.com/en/4.0/topics/forms/) - 一番詳しい  
📖 [forms.py](https://github.com/pennersr/django-allauth/blob/master/allauth/account/forms.py) - 原型  
📖 [How can I render Django Form with vuetify?](https://stackoverflow.com/questions/63993890/how-can-i-render-django-form-with-vuetify)  
📖 [vue.js - Vuetifyの入力値でDjangoのテンプレートタグを使用する方法は？](https://tutorialmore.com/questions-2757963.htm)  
📖 [Anyone know how to use vuetify with django form?](https://forum.djangoproject.com/t/anyone-know-how-to-use-vuetify-with-django-form/4807)  
📖 [Source code for django.forms.boundfield](https://docs.djangoproject.com/en/2.2/_modules/django/forms/boundfield/)  
📖 [DjangoのFormクラスを使う](https://qiita.com/taumu/items/4587a91c4d7d2db165b3)  

## 認証関連

📖 [爆速で作れるDjangoユーザ認証機能【django-allauth】](https://sinyblog.com/django/django-allauth/)  
📖 [Django 認証機能がうまく反映されない](https://qiita.com/cardene/items/00fc55a6ba4915cf83e9)  
📖 [django-allauth Installation](https://django-allauth.readthedocs.io/en/latest/installation.html)  
📖 [pennersr / django-allauth](https://github.com/pennersr/django-allauth/blob/master/allauth/templates/account/signup.html) - テンプレートの原型   
📖 [django-allauth Templates](https://django-allauth.readthedocs.io/en/latest/templates.html)  
📖 [Custom Signup View in django-allauth](https://tech.serhatteker.com/post/2020-06/custom-signup-view-in-django-allauth/)  
📖 [【Django】django-allauthのformやhtmlを上書きする方法](https://qiita.com/NOIZE/items/0522825a1de1d6aa4a2b)  
📖 [【Django】認証のViewをカスタマイズする方法 テンプレート編](https://allneko.club/django/auth-views-customize/)  
📖 [Redmineにて、メールのgmail（2段階認証設定）に送付するときに行った対処法](https://zenn.dev/gashi/articles/67e6c244942ef1318395)  
📖 [【Django】認証したユーザー（super, staff, active）の権限でアクセス制限・表示制限を設定する](https://office54.net/python/django/django-access-limit)  
