# サンプルを見る

📖 [http://tic.warabenture.com:8000/practice/v1/page-to-be-added-2](http://tic.warabenture.com:8000/practice/v1/page-to-be-added-2)  

# 目的

パッチを当てるようにテンプレートを改修したい  

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
    │   │   └── 📂 practice_v1              # アプリケーション名
    │   │       ├── 📂 templates
    │   │       │   └── 📂 practice_v1
    │   │       │       ├── 📂 o1o0
    │   │       │       │   └── 📄 page_the_hello.html
    │   │       │       │   └── 📄 page_to_be_added.html
    │   │       │       └── 📂 o2o0
    │   │       │           └── 📄 page_to_be_added.html.txt
    │   │       └── 📂 views
    │   │           ├── 📂 o1o0
    │   │           │   └── 📂 page_the_hello
    │   │           │       └── 📄 __init__.py
    │   │           └── 📂 o2o0
    │   │               └── 📂 page_to_be_added
    │   │                   └── 📄 __init__.py
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

# Step O3o3o0g1o0 Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

# Step O3o3o0g2o0 画面作成 - o3o0/page_to_be_added.html.txt ファイル

👇 以下のファイルを新規作成してほしい。  
自動フォーマットされてくないので、拡張子をテキストファイルにしておく  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1
                └── 📂 templates
                    └── 📂 practice_v1
                        └── 📂 o3o0     # Three
👉                          └── 📄 page_to_be_added.html.txt
```

```html
{% extends "practice_v1/o2o0/page_to_be_added.html.txt" %}
<!-- -->
{#          ------------------------------------------
            1
1. src1/apps1/practice_v1/templates/practice_v1/o2o0/page_to_be_added.html.txt
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

# Step O3o3o0g3o0 ビュー作成 - o3o0/page_to_be_added フォルダー

👇 以下の既存のファイルを編集してほしい  

```plaintext
    └── 📂 src1
        └── 📂 apps1
            └── 📂 practice_v1
                ├── 📂 templates
                │   └── 📂 practice_v1
                │       └── 📂 o3o0
                │           └── 📄 page_to_be_added.html.txt
                └── 📂 views
                    └── 📂 o3o0     # Three
                        └── 📂 page_to_be_added
👉                          └── 📄 __init__.py
```

```py
from django.shortcuts import render


class PageToBeAdded():
    """O3o3o0g3o0 追加されるページ"""

    def render(request):
        """描画"""

        # * `lp_` - Local path
        lp_this_page = 'practice_v1/o3o0/page_to_be_added.html.txt'
        #                            ^three
        #               ------------------------------------------
        #               1
        # 1. src1/apps1/practice_v1/templates/practice_v1/o3o0/page_to_be_added.html.txt を取得
        #                                     ------------------------------------------

        context = {}
        return render(request, lp_this_page, context)
```

# Step O3o3o0g4o0 サブ ルート編集 - urls_practice.py

👇 以下の既存ファイルを編集してほしい  

```plaintext
    └── 📂 src1
        ├── 📂 apps1
        │   └── 📂 practice_v1              # アプリケーション名
        │       ├── 📂 templates
        │       │   └── 📂 practice_v1
        │       │       └── 📂 o3o0
        │       │           └── 📄 page_to_be_added.html.txt
        │       └── 📂 views
        │           └── 📂 o3o0
        │               └── 📂 page_to_be_added
        │                   └── 📄 __init__.py
        └── 📂 project1
👉          ├── 📄 urls_practice.py          # こちら
❌          └── 📄 urls.py                   # これではない
```

```py
from django.urls import path


# ...中略...


# 練習ページ ２回追加されたページ
from apps1.practice_v1.views.o3o0.page_to_be_added import PageToBeAdded as PageToBeAdded2
#                             ^three
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


    # 練習ページ２ ２回追加されたページ
    path('practice/v1/page-to-be-added-2',
         # -----------------------------
         # 1
         PageToBeAdded2.render, name='page_to_be_added_2'),
    #    ---------------------        ------------------
    #    2                            3
    #
    # 1. 例えば `http://example.com/practice/v1/page-to-be-added-2` のようなURLのパスの部分
    #                              ------------------------------
    # 2. PageToBeAdded2 (別名)クラスの render 静的メソッド
    # 3. HTMLテンプレートの中で {% url 'page_to_be_added_2' %} のような形でURLを取得するのに使える
]
```

# Step O3o3o0g5o0 Webページにアクセスする

📖 [http://localhost:8000/practice/v1/page-to-be-added-2](http://localhost:8000/practice/v1/page-to-be-added-2)  

# 次の記事

📖 [Djangoでスーパーユーザーを追加しよう！](https://qiita.com/muzudho1/items/cf21fa75e23e1f987153)  
