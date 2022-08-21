# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/v1/page-to-be-added-1)  

# 目標

何か所にも同じ HTML （＝ボイラープレート）があるような悪いコードを書く癖を止められる技術を早い学習段階で取得したい  

# 情報

この記事は Lesson 1. から順に全部やってこないと ソースが足りず実行できないので注意されたい  

| What is   | This is                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------- |
| Lesson 1. | 📖 [DjangoとDockerでゲーム対局サーバーを作ろう！](https://qiita.com/muzudho1/items/eb0df0ea604e1fd9cdae) |

この記事のアーキテクチャ:  

| What is   | This is                                   |
| --------- | ----------------------------------------- |
| OS        | Windows10                                 |
| Container | Docker                                    |
| Editor    | Visual Studio Code （以下 VSCode と表記） |

ディレクトリ構成を抜粋すると 以下のようになっている  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 practice_v1              # アプリケーション名
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1
    │   │       │       └── 📂 page_the_hello
    │   │       │           └── 📄 v1o0.html
    │   │       └── 📂 views
    │   │           └── 📂 page_the_hello
    │   │               └── 📂 v1o0
    │   │                   └── 📄 __init__.py
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト名
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets.py
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_autogen.py
    │   │   ├── 📄 urls_practice_autogen.py
    │   │   ├── 📄 urls_practice.py
    │   │   ├── 📄 urls.py
    │   │   └── 📄 wsgi.py
    │   ├── 📂 project2
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
    └── 📄 .gitignore
```

# 手順

## Step O3o2o0g1o0 Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step O3o2o0g2o0 画面作成 - page_to_be_added/v1o0.html ファイル

以下のファイルを作成してほしい。

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 page_to_be_added
👉                          └── 📄 v1o0.html
```

```html
<html>
    <head>
        <title>{% block title %}追加されるページ{% endblock %}</title>
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

## Step O3o2o0g3o0 画面作成 - page_to_be_added/v2o0.html.txt ファイル

👇 以下のファイルを新規作成してほしい。  
自動フォーマットされてくないので、拡張子をテキストファイルにしておく  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 page_to_be_added
                            ├── 📄 v1o0.html
👉                          └── 📄 v2o0.html.txt
```

```html
{% extends "practice_v1/page_to_be_added/v1o0.html" %}
{#          --------------------------------------
            1
1. src1/apps1/practice_v1/templates/practice_v1/page_to_be_added/v1o0.html
                                    --------------------------------------
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

## Step O3o2o0g4o0 ビュー作成 - page_to_be_added/v2o0 フォルダー

👇 以下のファイルを新規作成してほしい

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 page_to_be_added
        │       │           ├── 📄 v1o0.html
        │       │           └── 📄 v2o0.html.txt
        │       └── 📂 views
        │           └── 📂 page_to_be_added
        │               └── 📂 v2o0             # Two
👉      │                   └── 📄 __init__.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
# BOF O3o2o0g4o0

from django.shortcuts import render


class PageToBeAdded():
    """O3o2o0g4o0 追加されるページ"""

    def render(request):
        """描画"""

        template_path = 'practice_v1/page_to_be_added/v2o0.html.txt'
        #                                             ^two
        #               ------------------------------------------
        #               1
        # 1. src1/apps1/practice_v1/templates/practice_v1/page_to_be_added/v2o0.html.txt を取得
        #                                     ------------------------------------------

        context = {}
        return render(request, template_path, context)

# EOF O3o2o0g4o0
```

## ~~Step O3o2o0g5o0~~

Merged to O3o2o0g5o1o0

## Step O3o2o0g5o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   ├── 📂 apps1
    │   │   └── 📂 practice_v1                  # アプリケーション
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1
    │   │       │       └── 📂 page_to_be_added
    │   │       │           ├── 📄 v1o0.html
    │   │       │           └── 📄 v2o0.html.txt
    │   │       └── 📂 views
    │   │           └── 📂 page_to_be_added
    │   │               └── 📂 v2o0             # Two
    │   │                   └── 📄 __init__.py
    │   └── 📂 project1
    │       └── 📄 settings.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_autogen.py,practice/v1/page-to-be-added-1,page_to_be_added_1,"O3o2o0g5o1o0 練習ページ １回追加されたページ",apps1.practice_v1.views.page_to_be_added.v2o0,PageToBeAdded,PageToBeAdded1,render
```

## Step O3o2o0g5o2o0 ルート編集 - コマンド打鍵

👇 以下のコマンドを打鍵してほしい  

```shell
# がんばって、ディレクトリーを移動してほしい
# cd ../src1_meta

# See also: O3o2o_1o0g2o0
python -m scripts.auto_generators.urls

# がんばって、ディレクトリーを移動してほしい
# cd ../src1

# 設定ファイルを変更したから、サーバーを再起動してほしい
docker-compose restart
```

## Step O3o2o0g6o0 Webページにアクセスする

📖 [http://localhost:8000/practice/v1/page-to-be-added-1](http://localhost:8000/practice/v1/page-to-be-added-1)  

# 次の記事

📖 [DjangoのHTMLのボイラープレートを減らすテンプレートを作るのも減らそう！](https://qiita.com/muzudho1/items/606d314c01543666c51b)  

# 参考にした記事

📖 [The Django template language](https://docs.djangoproject.com/en/4.0/ref/templates/language/) - これを読むのがよい  
