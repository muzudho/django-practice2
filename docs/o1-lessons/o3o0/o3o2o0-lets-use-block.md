# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1.0/page-to-be-added-1/ver1.0/)  

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
    │   │   └── 📂 practice_vol1o0              # アプリケーション名
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_vol1o0
    │   │       │       └── 📂 page_the_hello
    │   │       │           └── 📄 ver1o0.html
    │   │       └── 📂 views
    │   │           └── 📂 page_the_hello
    │   │               └── 📂 ver1o0
    │   │                   └── 📄 __init__.py
    │   ├── 📂 data
    │   ├── 📂 project1                  # プロジェクト名
    │   │   ├── 📄 __init__.py
    │   │   ├── 📄 asgi.py
    │   │   ├── 📄 settings_secrets.py
    │   │   ├── 📄 settings.py
    │   │   ├── 📄 urls_autogen.py
    │   │   ├── 📄 urls_practice_vol1o0_autogen.py
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

## Step O3o2o0g2o0 画面作成 - page_to_be_added/ver1o0.html ファイル

以下のファイルを作成してほしい。

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_vol1o0
                └── 📂 templates
                    └── 📂 practice_vol1o0
                        └── 📂 page_to_be_added
👉                          └── 📄 ver1o0.html
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
            └── 📂 practice_vol1o0
                └── 📂 templates
                    └── 📂 practice_vol1o0
                        └── 📂 page_to_be_added
                            ├── 📄 ver1o0.html
👉                          └── 📄 ver2o0.html.txt
```

```html
<!-- BOF O3o2o0g3o0 -->

{% extends "practice_vol1o0/page_to_be_added/ver1o0.html" %}
{#          --------------------------------------------
            1
1. src1/apps1/practice_vol1o0/templates/practice_vol1o0/page_to_be_added/ver1o0.html
                                        ----------------------------------------
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

<!-- EOF O3o2o0g3o0 -->
```

## Step O3o2o0g4o0 ビュー作成 - page_to_be_added/v2o0 フォルダー

👇 以下のファイルを新規作成してほしい

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_vol1o0                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_vol1o0
        │       │       └── 📂 page_to_be_added
        │       │           ├── 📄 ver1o0.html
        │       │           └── 📄 ver2o0.html.txt
        │       └── 📂 views
        │           └── 📂 page_to_be_added
        │               └── 📂 ver2o0             # Two
👉      │                   └── 📄 __init__.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
# BOF O3o2o0g4o0

from django.shortcuts import render


class PageToBeAdded():
    """O3o2o0g4o0 練習1.0巻 追加されるページ2.0版"""

    def render(request):
        """描画"""

        template_path = 'practice_vol1o0/page_to_be_added/v2o0.html.txt'
        #                                                  ^two
        #                ----------------------------------------------
        #                1
        # 1. `src1/apps1/practice_vol1o0/templates/practice_vol1o0/page_to_be_added/v2o0.html.txt` を取得
        #                                          ----------------------------------------------

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
    │   │   └── 📂 practice_vol1o0                  # アプリケーション
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_vol1o0
    │   │       │       └── 📂 page_to_be_added
    │   │       │           ├── 📄 ver1o0.html
    │   │       │           └── 📄 ver2o0.html.txt
    │   │       └── 📂 views
    │   │           └── 📂 page_to_be_added
    │   │               └── 📂 ver2o0             # Two
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


../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/page-to-be-added-1/ver1.0/,,"O3o2o0g5o1o0 練習ページ １回追加されたページ",apps1.practice_vol1o0.views.page_to_be_added.ver2o0,PageToBeAdded,PageToBeAdded1,render
```

## Step O3o2o0g5o2o0 ルート編集 - コマンド打鍵

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

## Step O3o2o0g6o0 Webページにアクセスする

📖 [http://localhost:8000/practice/vol1.0/page-to-be-added-1/ver1.0/](http://localhost:8000/practice/vol1.0/page-to-be-added-1/ver1.0/)  

# 次の記事

📖 [DjangoのHTMLのボイラープレートを減らすテンプレートを作るのも減らそう！](https://qiita.com/muzudho1/items/606d314c01543666c51b)  

# 参考にした記事

📖 [The Django template language](https://docs.djangoproject.com/en/4.0/ref/templates/language/) - これを読むのがよい  
