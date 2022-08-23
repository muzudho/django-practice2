# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/v1/auto_redirect/)  

# 目標

待っていると　対局が付くページがほしい  

## 詳細

いきなり作るのは難しいので、まず サーバーサイドで時計を見て  
0分、5分、10分、... のような 分が 5 で割り切れるタイミングで  
クライアントのページをリダイレクトする  

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

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1                            # あなたのDjangoサーバー開発用ディレクトリー。任意の名前
    │   ├── 📂 apps1
    │   │   ├── 📂 allauth_customized_vol1o0    # アプリケーション
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

## Step OA21o2o0g1o0 Dockerコンテナの起動

👇 （していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step OA21o2o0g2o0 機能強化 - auto_reload/v2o0.js ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                └── 📂 static
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 auto_reload
👉                          └── 📄 v2o0.js
```

```js
// OA21o2o0g2o0

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

## Step OA21o2o0g3o0 テンプレート編集 - auto_reload/v1o1o0.html.txt ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 auto_reload
                │           └── 📄 v2o0.js
                └── 📂 templates
                    └── 📂 practice_v1          # アプリケーションと同名
                        └── 📂 auto_reload
👉                          └── 📄 v1o1o0.html.txt
```

```html
{# OA21o2o0g3o0 #}
<!-- -->
{% extends "practice_v1/auto_reload/v1o0.html" %}
{#          ---------------------------------
            1
1. src1/apps1/practice_v1/templates/practice_v1/auto_reload/v1o0.html
                                    ---------------------------------
#}

{% load static %} {# 👈あとで static "URL" を使うので load static します #}

{% block script_src %}
<script src="{% static 'practice_v1/clock/v1o0.js' %}"></script>
<script src="{% static 'practice_v1/auto_reload/v2o0.js' %}"></script>
<!--                                             ^two
                =======================================
    `src1/apps1/practice_v1/static/practice_v1/auto_reload/v2o0.js`
                            ======================================
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

## Step OA21o2o0g4o0 ビュー作成 - auto_redirect/v1o0 フォルダー

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 auto_reload
                │           └── 📄 v2o0.js
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 auto_reload
                │           └── 📄 v1o1o0.html.txt
                └── 📂 views
                    └── 📂 auto_redirect
                        └── 📂 v1o0
👉                          └── 📄 __init__.py
```

```py
class AutoRedirectV():
    """OA21o2o0g4o0 リダイレクト ビュー"""

    # 自動リダイレクト ページ
    _path_of_redirecter_page = "practice_v1/auto_reload/v1o1o0.html.txt"
    #                                                    ^^^one o one
    #                           ---------------------------------------
    #                           1
    # 1. `src1/apps1/practice_v1/templates/practice_v1/auto_reload/o1o1o0.html.txt` を取得
    #                                      ---------------------------------------

    @staticmethod
    def render_auto_redirect(request):
        """描画 - 自動リダイレクト"""

        # 以下のファイルはあとで作ります
        from .v_redirect import render_auto_redirect
        #    -----------        --------------------
        #    1                  2
        # 1. `src1/apps1/practice_v1/views/auto_redirect/v1o0/v_redirect.py`
        #                                                     ----------
        # 2. `1.` に含まれる関数

        return render_auto_redirect(request, AutoRedirectV._path_of_redirecter_page)
```

## Step OA21o2o0g5o0 ビュー作成 - auto_redirect/v1o0/v_redirect.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1                  # アプリケーション
                ├── 📂 static
                │   └── 📂 practice_v1
                │       └── 📂 auto_reload
                │           └── 📄 v2o0.js
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 auto_reload
                │           └── 📄 v1o1o0.html.txt
                └── 📂 views
                    └── 📂 auto_redirect
                        └── 📂 v1o0
                            ├── 📄 __init__.py
👉                          └── 📄 v_redirect.py
```

```py
# BOF OA21o2o0g5o0

import datetime
from django.shortcuts import render


def render_auto_redirect(request, auto_redirect_tp):
    """OA21o2o0g5o0 描画 - 自動リダイレクト ページ

    Parameters
    ----------
    auto_redirect_tp : str
        Template path
    """

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

    return render(request, auto_redirect_tp, context)

# EOF OA21o2o0g5o0
```

## ~~Step OA21o2o0g6o0~~

Merged to OA21o2o0g6o1o0  

## Step OA21o2o0g6o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_v1                  # アプリケーション
    │           ├── 📂 static
    │           │   └── 📂 practice_v1
    │           │       └── 📂 auto_reload
    │           │           └── 📄 v2o0.js
    │           ├── 📂 templates
    │           │   └── 📂 practice_v1
    │           │       └── 📂 auto_reload
    │           │           └── 📄 v1o1o0.html.txt
    │           └── 📂 views
    │               └── 📂 auto_redirect
    │                   └── 📂 v1o0
    │                       ├── 📄 __init__.py
    │                       └── 📄 v_redirect.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_autogen.py,practice/v1/auto_redirect/,practice_v1_auto_redirect,"OA21o2o0g6o1o0 自動リダイレクトページ",apps1.practice_v1.views.auto_redirect.v1o0,AutoRedirectV,,render_auto_redirect
```

## Step OA21o1o0g7o2o0 ルート編集 - コマンド打鍵

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

## Step OA21o2o0g7o0 Web画面へアクセス

📖 [http://localhost:8000/practice/v1/auto_redirect/](http://localhost:8000/practice/v1/auto_redirect/)  

## Step OA21o2o0g8o0 ランチャーのリンク用データ追加 - finished-lessons.csv ファイル

👇 以下の既存ファイルの最終行に追記してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   ├── 📂 portal_v1                        # アプリケーション
        │   │   └── 📂 data
👉      │   │       └── 📄 finished-lessons.csv
        │   └── 📂 practice_v1                      # アプリケーション
        │       ├── 📂 static
        │       │   └── 📂 practice_v1
        │       │       └── 📂 auto_reload
        │       │           └── 📄 v2o0.js
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 auto_reload
        │       │           └── 📄 v1o1o0.html.txt
        │       └── 📂 views
        │           └── 📂 auto_redirect
        │               └── 📂 v1o0
        │                   ├── 📄 __init__.py
        │                   └── 📄 v_redirect.py
        └── 📂 project1                          # プロジェクト
            └── 📄 urls_practice.py
```

👇 冗長なスペース，冗長なダブルクォーテーション，末尾のカンマ は止めてほしい  

```csv
/practice/v1/auto_redirect/,自動リダイレクト
```

👇 ランチャーにリンクが追加されていることを確認してほしい 

📖 [http://localhost:8000/](http://localhost:8000/)  

# 次の記事

📖 [Djangoの〇×ゲームのPlayAgainボタンを外そう！](https://qiita.com/muzudho1/items/d4bfde69c1656616f8ce)  
