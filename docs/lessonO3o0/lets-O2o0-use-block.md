# 目的

何か所にも同じ HTML （＝ボイラープレート）があるような悪いコードを書く癖を止められる技術を早い学習段階で取得したい  

# はじめに

この記事は LessonO[1 0] から順に全部やってこないと ソースが足りず実行できないので注意されたい。  
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
    │   │   └── 📂 practice_v1              # アプリケーション名
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1
    │   │       │       └── 📂 o1o0
    │   │       │           └── 📄 page_the_hello.html
    │   │       └── 📂 views
    │   │           └── 📂 o1o0
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

# Step O[1 0] Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd host1

# Docker コンテナ起動
docker-compose up
```

# Step O[2 0] 画面作成 - page_to_be_added.html ファイル

以下のファイルを作成してほしい。

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 o1o0
👉                          └── 📄 page_to_be_added.html
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

# Step O[3 0] 画面作成 - o2o0/page_to_be_added.html.txt ファイル

👇 以下のファイルを新規作成してほしい。  
自動フォーマットされてくないので、拡張子をテキストファイルにしておく  

```plaintext
    └── 📂 host1
        └── 📂 apps1
            └── 📂 practice_v1
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 o2o0     # Two
👉                          └── 📄 page_to_be_added.html.txt
```

```html
{% extends "practice_v1/o1o0/page_to_be_added.html" %}
{#          --------------------------------------
            1
1. host1/apps1/practice_v1/templates/practice_v1/o1o0/page_to_be_added.html
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

# Step O[4 0] ビュー モジュール作成 - o2o0/page_to_be_added フォルダー

👇 以下のファイルを新規作成してほしい

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1                  # アプリケーション
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           └── 📄 page_the_hello.html
        │       └── 📂 views
        │           └── 📂 o2o0     # Two
        │               └── 📂 page_to_be_added
👉      │                   └── 📄 __init__.py
        └── 📂 project1
            └── 📄 settings.py
```

```py
from django.http import HttpResponse
from django.template import loader


class PageToBeAdded():
    """追加されるページ"""

    def render(request):
        """描画"""

        template = loader.get_template(
            'practice_v1/o2o0/page_to_be_added.html.txt')
        #                 ^two
        #    ------------------------------------------
        #    1
        # 1. host1/apps1/practice_v1/templates/practice_v1/o2o0/page_to_be_added.html.txt を取得
        #                                      ------------------------------------------

        context = {}
        return HttpResponse(template.render(context, request))
```

# Step O[5 0] サブ ルート編集 - urls_practice.py

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 host1
        ├── 📂 apps1
        │   └── 📂 practice_v1              # アプリケーション名
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o1o0
        │       │           ├── 📄 page2_base.html
        │       │           └── 📄 page2_patch1.html.txt
        │       └── 📂 views
        │           └── 📂 o2o0
        │               └── 📂 page_to_be_added
        │                   └── 📄 __init__.py
        └── 📂 project1
👉          ├── 📄 urls_practice.py          # こちら
❌          └── 📄 urls.py                   # これではない
```

```py
from django.urls import path


# ...中略...


# 練習ページ １回追加されたページ
from apps1.practice_v1.views.o2o0.page_to_be_added import PageToBeAdded as PageToBeAdded1
#          -----------            ----------------        -------------    --------------
#          11                     12                      2                3
#    ---------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py ファイルにさらに含まれるクラス
# 3. `2.` の別名


# ...中略...


urlpatterns = [


    # ...中略...


    # 練習ページ２ １回追加されたページ
    path('practice/v1/page-to-be-added-1',
         # -----------------------------
         # 1
         PageToBeAdded1.render, name='page_to_be_added_1'),
    #    ---------------------        ------------------
    #    2                            3
    #
    # 1. 例えば `http://example.com/practice/v1/page-to-be-added-1` のようなURLのパスの部分
    #                              ------------------------------
    # 2. PageToBeAdded1 (別名)クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page_to_be_added_1' %} のような形でURLを取得するのに使える
]
```

# Step O[6 0] Webページにアクセスする

📖 [http://localhost:8000/practice/v1/page-to-be-added-1](http://localhost:8000/practice/v1/page-to-be-added-1)  

# 次の記事

📖 [DjangoのHTMLのボイラープレートを減らすテンプレートを作るのも減らそう！](https://qiita.com/muzudho1/items/606d314c01543666c51b)  

# 参考にした記事

📖 [The Django template language](https://docs.djangoproject.com/en/4.0/ref/templates/language/) - これを読むのがよい  
