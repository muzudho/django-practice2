# 目標

URLの設定はめんどうだ。自動化しよう  

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

# 手順

## Step. Dockerコンテナの起動

（していなければ） Docker コンテナを起動しておいてほしい  

```shell
# docker-compose.yml ファイルを置いてあるディレクトリーへ移動してほしい
cd src1

# Docker コンテナ起動
docker-compose up
```

## Step o3o2o_1o0g1o0 データ作成 - src1_meta/data/urls.csv ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1     # 既存
    └── 📂 src1_meta
        └── 📂 data
👉          └── 📄 urls.csv
```

```csv
file,path,name,comment,module,class,alias,method
../src1/project1/urls_practice_autogen.py,practice/v1/hello2,practice_v1_hello2,"O3o1o0gA10o0 こんにちわページ",apps1.practice_v1.views.page_the_hello.v1o0,PageTheHello,,render
```

## Step o3o2o_1o0g2o0 スクリプト作成 - src1_meta/scripts/auto_generators/urls.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1     # 既存
    └── 📂 src1_meta
        ├── 📂 data
        │   └── 📄 urls.csv
        └── 📂 scripts
            └── 📂 auto_generators
                └── 📄 urls.py
```

```py
# BOF o3o2o_1o0g2o0

import os
import pandas as pd


def main():
    # CSV 読取
    df = pd.read_csv('data/urls_practice.csv')
    #                 ----------------------
    #                 1
    # 1. `src1_meta/data/urls_practice.csv` を読取
    #               ----------------------

    # print(df)
    """
    Examples
    --------
                                            file                        path            name                comment                                       module         class  alias  method
    0  src1/project1/urls_practice_autogen.py  practice/v1/hello2  practice_v1_hello2  O3o1o0gA10o0 こんにちわページ  apps1.practice_v1.views.page_the_hello.v1o0  PageTheHello    NaN  render
    """

    print(f"Current working directory:{os.getcwd()}")

    # 書き出すテキスト
    head_text_of_files = {}
    body_text_of_files = {}

    # 各行
    df = df.reset_index()  # make sure indexes pair with number of rows
    for index, row in df.iterrows():

        file_to_export = row['file']
        # 誤上書き防止のため、ファイル名の末尾は `_autogen.py` かチェックします
        basename = os.path.basename(file_to_export)
        if not basename.endswith("_autogen.py"):
            print(f"書き出すファイル名の末尾は `_autogen.py` にしてください。 basename:{basename}")
            continue

        if not file_to_export in head_text_of_files:
            # 新規ファイル
            head_text_of_files[file_to_export] = ""
            body_text_of_files[file_to_export] = ""

        # 追記
        module = row["module"]
        class_name = row["class"]
        alias = row['alias']
        if pd.isnull(alias):
            alias_phrase = ""
            virtual_class_name = class_name
        else:
            alias_phrase = f" as {alias}"
            virtual_class_name = alias

        head_text_of_files[file_to_export] += f"from {module} import {class_name}{alias_phrase}\n"

        comment = row["comment"]
        path = row["path"]
        method = row["method"]
        name = row["name"]
        if pd.isnull(name):
            name_phrase = ""
        else:
            name_phrase = f", name='{name}'"

        body_text_of_files[file_to_export] += f"""
    # {comment}
    path('{path}', {virtual_class_name}.{method}{name_phrase}),
"""

    # 各ファイル書出し
    for file_to_export in head_text_of_files.keys():
        # ファイル書出し
        with open(file_to_export, 'w') as f:
            print(f"Write... {file_to_export}")
            f.write(f'''from django.urls import path

{head_text_of_files[file_to_export]}

urlpatterns = [{body_text_of_files[file_to_export]}]
''')


if __name__ == "__main__":
    main()

# EOF o3o2o_1o0g2o0
```

## Step o3o2o_1o0g3o0 コマンド実行

```shell
# ディレクトリーを移動してほしい
# cd src1_meta

python -m scripts.auto_generators.urls
```

Output:  

```plaintext
Current working directory:C:\Users\むずでょ\Documents\GitHub\django-practice2\src1_meta
Write... ../src1/project1/urls_practice_autogen.py
```

## Step o3o2o_1o0g4o0 コマンド実行

👇 以下のファイルが自動生成されていることを確認してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 project1
👉  │       └── 📄 urls_practice_autogen.py
    └── 📂 src1_meta
        ├── 📂 data
        │   └── 📄 urls.csv
        └── 📂 scripts
            └── 📂 auto_generators
                └── 📄 urls.py
```

```py
from django.urls import path

from apps1.practice_v1.views.page_the_hello.v1o0 import PageTheHello


urlpatterns = [
    # O3o1o0gA10o0 こんにちわページ
    path('practice/v1/hello2', PageTheHello.render, name='practice_v1_hello2'),
]
```

## Step o3o2o_1o0g5o0 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 project1
    │       ├── 📄 urls_practice_autogen.py
👉  │       └── 📄 urls.py                   # こっち
    └── 📂 src1_meta
        ├── 📂 data
        │   └── 📄 urls.csv
        └── 📂 scripts
            └── 📂 auto_generators
                └── 📄 urls.py
```

```py
# ...略... urlpatterns = [
# ...略... ]


urlpatterns.append(path('', include(f'{PROJECT_NAME}.urls_practice_autogen')))
```

## Step o3o2o_1o0g6o0 Webページにアクセスする

📖 [http://localhost:8000/practice/v1/hello2](http://localhost:8000/practice/v1/hello2)  

# 次の記事

📖 [DjangoのHTMLのボイラープレートを減らすテンプレートを使おう！](https://qiita.com/muzudho1/items/7dcfc068e0bec009d371)  

# 参考にした記事

## Python

📖 [Writing Unicode text to a text file?](https://stackoverflow.com/questions/6048085/writing-unicode-text-to-a-text-file)  

## Pandas

📖 [pandas.isnull](https://pandas.pydata.org/docs/reference/api/pandas.isnull.html)  