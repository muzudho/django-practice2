# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/v1/page-to-be-added-2)  

# 目標

パッチを当てるようにテンプレートを改修したい  

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
    │   │       │       ├── 📂 page_the_hello
    │   │       │       │   └── 📄 v1o0.html
    │   │       │       └── 📂 page_to_be_added
    │   │       │           ├── 📄 v1o0.html
    │   │       │           └── 📄 v2o0.html.txt
    │   │       └── 📂 views
    │   │           ├── 📂 page_the_hello
    │   │           │   └── 📂 v1o0
    │   │           │       └── 📄 __init__.py
    │   │           └── 📂 page_to_be_added
    │   │               └── 📂 v2o0
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

## Step O3o3o0g1o0 Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step O3o3o0g2o0 画面作成 - page_to_be_added/v3o0.html.txt ファイル

👇 以下のファイルを新規作成してほしい。  
自動フォーマットされてくないので、拡張子をテキストファイルにしておく  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 page_to_be_added
👉                          └── 📄 v3o0.html.txt
```

```html
{% extends "practice_v1/page_to_be_added/v2o0.html.txt" %}
<!-- -->
{#          ------------------------------------------
            1
1. src1/apps1/practice_v1/templates/practice_v1/page_to_be_added/v2o0.html.txt
                                    ------------------------------------------
#}

<!-- 伸びることを想定したリスト -->
{% block section2_footer_patch1 %}
    <li>
        ぱんだ
    </li>
    <li>
        だるま
    </li>
    <!-- ブロックの名前は早い者勝ちで再定義できないので、変える -->
    {% block section2_footer_patch2 %}
    {% endblock section2_footer_patch2 %}
{% endblock section2_footer_patch1 %}

<!-- page2_patch1 を飛び越して page2_base のブロックも変更可能 -->
{% block section3 %}
<h1>せくしょん　さん</h1>
<p>こんてんつ　さん</p>
{% endblock section3 %}
```

## Step O3o3o0g3o0 ビュー作成 - page_to_be_added/v3o0 フォルダー

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 page_to_be_added
                │           └── 📄 v3o0.html.txt
                └── 📂 views
                    └── 📂 page_to_be_added
                        └── 📂 v3o0                 # Three
👉                          └── 📄 __init__.py
```

```py
# BOF O3o3o0g3o0

from django.shortcuts import render


class PageToBeAdded():
    """O3o3o0g3o0 追加されるページ"""

    def render(request):
        """描画"""

        template_path = 'practice_v1/page_to_be_added/v3o0.html.txt'
        #                                             ^three
        #               ------------------------------------------
        #               1
        # 1. src1/apps1/practice_v1/templates/practice_v1/page_to_be_added/v3o0.html.txt を取得
        #                                     ------------------------------------------

        context = {}
        return render(request, template_path, context)

# EOF O3o3o0g3o0
```

## ~~Step O3o3o0g4o0~~

Merged to O3o3o0g4o1o0  

## Step O3o3o0g4o1o0 ルート編集 - urls.csv ファイル

👇 以下の既存ファイルの末尾に追記してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 apps1
    │       └── 📂 practice_v1              # アプリケーション名
    │           ├── 📂 templates
    │           │   └── 📂 practice_v1
    │           │       └── 📂 page_to_be_added
    │           │           └── 📄 v3o0.html.txt
    │           └── 📂 views
    │               └── 📂 page_to_be_added
    │                   └── 📂 v3o0
    │                       └── 📄 __init__.py
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
...略... file,path,name,comment,module,class,alias,method
...略...


../src1/project1/urls_practice_autogen.py,practice/v1/page-to-be-added-2,,"O3o3o0g4o1o0 練習ページ ２回追加されたページ",apps1.practice_v1.views.page_to_be_added.v3o0,PageToBeAdded,PageToBeAdded2,render
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

## Step O3o3o0g5o0 Webページにアクセスする

📖 [http://localhost:8000/practice/v1/page-to-be-added-2](http://localhost:8000/practice/v1/page-to-be-added-2)  

# 次の記事

📖 [Djangoでスーパーユーザーを追加しよう！](https://qiita.com/muzudho1/items/cf21fa75e23e1f987153)  
