# 目的

待っていると　対局が付くページがほしい  

いきなり作るのは難しいので、まず サーバーサイドで時計を見て  
0分、5分、10分、... のような 分が 5 で割り切れるタイミングで  
クライアントのページをリダイレクトする  

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

# Step 2. 機能強化 - v0o0o2/reloader.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                  # アプリケーション
                └── 📂static
                    └── 📂practice          # アプリケーションと同名
                        └── 📂v0o0o2        # 0.0.two
👉                          └── 📄reloader.js
```

```js
/**
 * 内部で使用する変数
 *
 * * vue1
 *
 * @param {number} intervalMilliseconds
 */
function startReloadingAutomatically(intervalMilliseconds) {
    setInterval(() => {
        // setInterval に渡すラムダ関数の中で this を使うのは、正しく理解する知識が難しいので避けます
        const redirectUrl = vue1.createRedirectUrl();

        if (redirectUrl) {
            // リダイレクトします
            window.location.href = redirectUrl;
        } else {
            // JavaScript では、空文字列は 偽
            // リロードします
            location.reload();
        }
    }, intervalMilliseconds);
}
```

# Step 3. テンプレート編集 - reloader_with_redirect.html ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                  # アプリケーション
                ├── 📂static
                │   └── 📂practice
                │       └── 📂v0o0o1
                │           └── 📄reloader.js
                └── 📂templates
                    └── 📂practice          # アプリケーションと同名
                        └── 📂v0o0o2        # 0.0.two
👉                          └── 📄reloader_with_redirect.html.txt
```

```html
{% extends "practice/v0o0o1/reloader.html" %}
{#          -----------------------------
            1
1. host1/apps1/practice/templates/practice/v0o0o1/reloader.html
                                  -----------------------------
#}

{% load static %} {# 👈あとで static "URL" を使うので load static します #}

{% block script_src %}
<script src="{% static 'practice/v0o0o1/clock.js' %}"></script>
<script src="{% static 'practice/v0o0o2/reloader.js' %}"></script>
<!--                                  ^two
                        ===========================
    `host1/apps1/practice/static/practice/v0o0o2/reloader.js`
                                 ===========================
-->
{% endblock script_src %}


{% block data_trailing %}
    // "dj_" は 「Djangoがレンダーに埋め込む変数」 の目印
    vu_redirectPath: "{{ dj_redirect_path|escapejs }}",
{% endblock data_trailing %}


{% block methods_trailing %}
    /**
        * vue1.createRedirectUrl() のように使えます
        */
    createRedirectUrl() {
        if (!this.vu_redirectPath) {
            // JavaScript では、空文字列を not すると 真
            // リダイレクトしたくないときは空文字列を送る、という取り決めをしておきます
            return "";
        }

        let url = `${location.protocol}//${location.host}${this.vu_redirectPath}`;
        //         --------------------  ---------------]-----------------------
        //         1                     2               3
        // 1. protocol
        // 2. host
        // 3. path
        console.log(`redirect url=[${url}]`);
        return url;
    },
{% endblock methods_trailing %}
```

# Step 4. ビュー モジュール作成 - redirecter フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                  # アプリケーション
                ├── 📂static
                │   └── 📂practice
                │       └── 📂v0o0o1
                │           └── 📄reloader.js
                ├── 📂templates
                │   └── 📂practice
                │       └── 📂v0o0o2
                │           └── 📄reloader_with_redirect.html.txt
                └── 📂views
                    └── 📂v0o0o2            # 0.0.two
                        └── 📂redirecter
👉                          └── 📄__init__.py
```

```py
class RedirecterV():
    """リダイレクト ビュー"""

    # 自動リダイレクト ページ
    _path_of_redirecter_page = "practice/v0o0o2/reloader_with_redirect.html.txt"
    #                                         ^two
    #                           -----------------------------------------------
    #                           1
    # 1. `host1/apps1/practice/templates/practice/v0o0o2/reloader_with_redirect.html.txt` を取得
    #                                    -----------------------------------------------

    @staticmethod
    def render_redirect(request):
        """描画 - 自動リダイレクト"""

        # 以下のファイルはあとで作ります
        from .v_redirect import render_redirect
        #    -----------        ---------------
        #    1                  2
        # 1. `host1/apps1/practice/views/v0o0o2/redirecter/v_redirect.py`
        #                                                  ----------
        # 2. `1.` に含まれる関数

        return render_redirect(request, RedirecterV._path_of_redirecter_page)
```

# Step 5. ビュー モジュール作成 - v_redirect ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂host1
        └── 📂apps1
            └── 📂practice                  # アプリケーション
                ├── 📂static
                │   └── 📂practice
                │       └── 📂v0o0o1
                │           └── 📄reloader.js
                ├── 📂templates
                │   └── 📂practice
                │       └── 📂v0o0o2
                │           └── 📄reloader_with_redirect.html.txt
                └── 📂views
                    └── 📂v0o0o2
                        └── 📂redirecter
                            ├──📄__init__.py
👉                          └──📄v_redirect.py
```

```py
import datetime
from django.shortcuts import render


def render_redirect(request, path_of_redirecter_page):
    """描画 - 自動リダイレクト ページ"""

    # 現在日時
    dt_now = datetime.datetime.now()

    # 今何分？
    dt_minute = dt_now.minute

    # 5 で割り切れる分なら、リダイレクト
    if dt_minute % 5 == 0:
        redirect_path = "/tic-tac-toe/v2/match-application/"
        #                ----------------------------------
        #                1
        # 1. `http://example.com/tic-tac-toe/v2/match-application/`
        #                       ----------------------------------
    else:
        # リダイレクトしたくないときは空文字列を送る、と取り決めておきます
        redirect_path = ""

    context = {
        # FIXME 相対パス。 URL を urls.py で変更したいとき、反映されないがどうするか？
        "dj_redirect_path": redirect_path,
    }

    return render(request, path_of_redirecter_page, context)
```

# Step 6. ルート編集 - urls_practice.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   └── 📂practice                  # アプリケーション
        │       ├── 📂static
        │       │   └── 📂practice
        │       │       └── 📂v0o0o1
        │       │           └── 📄reloader.js
        │       ├── 📂templates
        │       │   └── 📂practice
        │       │       └── 📂v0o0o2
        │       │           └── 📄reloader_with_redirect.html.txt
        │       └── 📂views
        │           └── 📂v0o0o2
        │               └── 📂redirecter
        │                   ├──📄__init__.py
        │                   └──📄v_redirect.py
        └── 📂project1                      # プロジェクト
👉          └── 📄urls_practice.py
```

```py
# ...略...


from apps1.practice.views.v0o0o2.redirecter import RedirecterV
#                              ^two
#    ----- -------- -----------------------        -----------
#    1     2        3                              4
# 1,3. ディレクトリー名
# 2. アプリケーション名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


urlpatterns = [
    # ...略...


    # 自動リダイレクト
    path('practice/redirecter/', RedirecterV.render_redirect,
         # -------------------   ---------------------------
         # 1                     2
         name='practice_redirecter'),
    #          -------------------
    #          3
    #
    # 1. 例えば `http://example.com/practice/redirecter/` のような URL のパスの部分
    #                              --------------------
    # 2. RedirecterV クラスの render_redirect メソッド
    # 3. HTMLテンプレートの中で {% url 'practice_redirecter' %} のような形でURLを取得するのに使える
]
```

# Step 7. Web画面へアクセス

📖 [http://localhost:8000/practice/redirecter/](http://localhost:8000/practice/redirecter/)  

# Step 8. ポータルページのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂host1
        ├── 📂apps1
        │   ├── 📂portal                        # アプリケーション
        │   │   └── 📂data
👉      │   │       └── 📄finished-lessons.csv
        │   └── 📂practice                      # アプリケーション
        │       ├── 📂static
        │       │   └── 📂practice
        │       │       └── 📂v0o0o1
        │       │           └── 📄reloader.js
        │       ├── 📂templates
        │       │   └── 📂practice
        │       │       └── 📂v0o0o2
        │       │           └── 📄reloader_with_redirect.html.txt
        │       └── 📂views
        │           └── 📂v0o0o2
        │               └── 📂redirecter
        │                   ├──📄__init__.py
        │                   └──📄v_redirect.py
        └── 📂project1                          # プロジェクト
            └── 📄urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/redirecter/,自動リダイレクト
```

👇 ポータルにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoの〇×ゲームのPlayAgainボタンを外そう！](https://qiita.com/muzudho1/items/d4bfde69c1656616f8ce)  
