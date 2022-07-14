# 目的

何か所にも同じ HTML （＝ボイラープレート）があるような悪いコードを書く癖を止められる技術を早い学習段階で取得したい  

# はじめに

この記事は Lesson0 から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    │   │   └── 📂 practice              # アプリケーション名
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice
    │   │       │       └── 📂 v0o0o1
    │   │       │           └── 📄 page1.html
    │   │       └── 📂 views
    │   │           └── 📂 v0o0o1
    │   │               └── 📄 pages.py
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト名
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets.py
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

# Step 2. 画面作成 - page2_base.html ファイル

以下のファイルを作成してほしい。

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice
                └── 📂 templates
                    └── 📂 practice
                        └── 📂 v0o0o1
👉                          └── 📄 page2_base.html
```

```html
<html>
    <head>
        <title>{% block title %}ページ２{% endblock %}</title>
    </head>
    <body>
        <!-- -->
        {% block section1 %}
        <h1>セクション１</h1>
        <p>コンテンツ１</p>
        {% endblock section1 %}

        <!-- 伸びることを想定したリスト -->
        {% block section2 %}
        <h1>セクション２</h1>
        <p>
            <ol>
                <li>
                    しりとり
                </li>
                <li>
                    りんご
                </li>
                {% block section2_footer %}
                <!-- -->
                {% endblock section2_footer %}
            </ol>
        </p>
        {% endblock section2 %}

        <!-- -->
        {% block section3 %}
        <h1>セクション３</h1>
        <p>コンテンツ３</p>
        {% endblock section3 %}
    </body>
</html>
```

# Step 3. 画面作成 - page2_patch1.html.txt ファイル

👇 以下のファイルを新規作成してほしい。  
自動フォーマットされてくないので、拡張子をテキストファイルにしておく  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice
                └── 📂 templates
                    └── 📂 practice
                        └── 📂 v0o0o1
                            ├── 📄 page2_base.html
👉                          └── 📄 page2_patch1.html.txt
```

```html
{% extends "practice/v0o0o1/page2_base.html" %}
{#          -------------------------------
            1
1. host1/apps1/practice/templates/practice/v0o0o1/page2_base.html
                                  -------------------------------
#}

<!-- -->
{% block title %}ページ２（その２）{% endblock %}

<!-- -->
{% block section1 %}
    <h1>第１区画</1>
    <ul>
        <li>あ</li>
        <li>い</li>
        <li>う</li>
    </ul>
{% endblock section1 %}

<!-- 伸びることを想定したリスト -->
{% block section2_footer %}
    <li>
        ごりら
    </li>
    <li>
        らっぱ
    </li>
    <!-- ブロックの名前は早い者勝ちで再定義できないので、変える -->
    {% block section2_footer_patch1 %}
    {% endblock section2_footer_patch1 %}
{% endblock section2_footer %}
```

# Step 4. ビュー作成 - pages.py ファイル

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice
                ├── 📂 templates
                │   └── 📂 practice
                │       └── 📂 v0o0o1
                │           ├── 📄 page2_base.html
                │           └── 📄 page2_patch1.html.txt
                └── 📂 views
                    └── 📂 v0o0o1
👉                      └── 📄 pages.py
```

```py
from django.http import HttpResponse
from django.template import loader


# ...中略...


class Page2Patch1():
    """ページ２ パッチ１"""

    def render(request):
        """描画"""

        template = loader.get_template('practice/v0o0o1/page2_patch1.html.txt')
        #                               -------------------------------------
        #                               1
        # 1. host1/apps1/practice/templates/practice/v0o0o1/page2_patch1.html.txt を取得
        #                                   -------------------------------------

        context = {}
        return HttpResponse(template.render(context, request))
```

# Step 5. サブ ルート編集 - urls_practice.py

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice              # アプリケーション名
        │       ├── 📂 templates
        │       │   └── 📂 practice
        │       │       └── 📂 v0o0o1
        │       │           ├── 📄 page2_base.html
        │       │           └── 📄 page2_patch1.html.txt
        │       └── 📂 views
        │           └── 📂 v0o0o1
        │               └── 📄 pages.py
        └── 📂 project1
👉          ├── 📄 urls_practice.py          # こちら
❌          └── 📄 urls.py                   # これではない
```

```py
from django.urls import path


# ...中略...


from apps1.practice.views.v0o0o1.pages import Page2Patch1
#    --------------------------- -----        -----------
#    1                           2            3
# 1. ディレクトリー名
# 2. Python ファイル名。拡張子抜き
# 3. クラス名


# ...中略...


urlpatterns = [


    # ...中略...


    # ページ２ パッチ１
    path('practice/page2_patch1', Page2Patch1.render, name='page2_patch1'),
    #     ---------------------   ------------------        ------------
    #     1                       2                         3
    #
    # 1. 例えば `http://example.com/practice/page2_patch1` のようなURLのパスの部分
    #                              ----------------------
    # 2. Page2Patch1 クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page2_patch1' %} のような形でURLを取得するのに使える
]
```

# Step 6. Webページにアクセスする

📖 [http://localhost:8000/practice/page2_patch1](http://localhost:8000/practice/page2_patch1)  

# 次の記事

📖 [DjangoのHTMLのボイラープレートを減らすテンプレートを作るのも減らそう！](https://qiita.com/muzudho1/items/606d314c01543666c51b)  

# 参考にした記事

📖 [The Django template language](https://docs.djangoproject.com/en/4.0/ref/templates/language/) - これを読むのがよい  
