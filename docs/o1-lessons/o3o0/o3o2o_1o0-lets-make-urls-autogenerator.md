# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1.0/hello2/ver1.0/)  

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
../src1/project1/urls_autogen.py,,,"集約ファイル",,,,
../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/hello2/ver1.0/,practice_vol1o0_hello2,"o3o2o_1o0g1o0 練習1.0巻 こんにちわ1.0版",apps1.practice_vol1o0.views.page_the_hello.ver1o0,PageTheHello,,render
```

## Step O3o2o_1o0g2o_1o0 Pythonパッケージインストール - pandas

👇 以下のコマンドを打鍵してほしい  

```shell
pip install pandas
```

## Step O3o2o_1o0g2o0 スクリプト作成 - src1_meta/scripts/auto_generators/urls.py ファイル

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
# BOF O3o2o_1o0g2o0

import os
import pandas as pd


class UrlsAutoGenerator:
    def __init__(self):
        self._summary_file_to_export = None

    def execute(self):
        # CSV 読取
        df = pd.read_csv('data/urls.csv')
        #                 -------------
        #                 1
        # 1. `src1_meta/data/urls.csv` を読取
        #               -------------

        # print(df)
        """
        Examples
        --------
                                                       file                           path                    name  ...         class alias  method
        0                  ../src1/project1/urls_autogen.py                            NaN                     NaN  ...           NaN   NaN     NaN
        1  ../src1/project1/urls_practice_vol1o0_autogen.py  practice/vo1o0/hello2/ver1o0/  practice_vol1o0_hello2  ...  PageTheHello   NaN  render
        """

        print(f"Current working directory:{os.getcwd()}")

        # URL設定ファイル自動生成
        self.write_url_some_files(df)

        # 集約ファイル自動生成
        self.write_url_summary_file(df)

    def write_url_some_files(self, df):
        """URL設定ファイル自動生成"""

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
                print(
                    f"書き出すファイル名の末尾は `_autogen.py` にしてください。 basename:{basename}")
                continue

            method = row["method"]
            if pd.isnull(method):
                # method列が空なら集約ファイルとします
                self._summary_file_to_export = file_to_export
                continue

            if not file_to_export in head_text_of_files:
                # 新規ファイル
                head_text_of_files[file_to_export] = ""
                body_text_of_files[file_to_export] = ""

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
            name = row["name"]

            # コメント
            if pd.isnull(comment):
                # 省略可
                comment_phrase = ""
            else:
                comment_phrase = f"""
    # {comment}"""

            # パス
            if pd.isnull(path):
                # 空文字列の指定があり得ます。
                # pandas は空文字列と NaN を区別せず NaN にするので、空文字列に変換します
                path = ""

            # 名前
            if pd.isnull(name):
                # 省略可
                name_phrase = ""
            else:
                name_phrase = f", name='{name}'"

            body_text_of_files[file_to_export] += f"""{comment_phrase}
    path('{path}', {virtual_class_name}.{method}{name_phrase}),
"""

        # 各ファイル書出し
        for file_to_export in head_text_of_files.keys():
            # ファイル書出し
            with open(file_to_export, 'w', encoding="utf8") as f:
                print(f"Write... {file_to_export}")
                f.write(f'''# BOF O3o2o_1o0g4o0

from django.urls import path

{head_text_of_files[file_to_export]}

urlpatterns = [{body_text_of_files[file_to_export]}]

# EOF O3o2o_1o0g4o0
''')

    def write_url_summary_file(self, df):
        """集約ファイル自動生成"""

        text = """# BOF O3o2o_1o0g4o0

from django.urls import include, path

# O3o1o0gA11o0 総合ルート編集
from .settings import PROJECT_NAME
#    ]--------        ------------
#    12               3
# 1. 同じディレクトリー
# 2. `src1/projectN/settings.py`
#                   --------
# 3. 変数


urlpatterns = [
"""

        # Distinct
        file_stems_to_export = set()
        df = df.reset_index()  # make sure indexes pair with number of rows
        for index, row in df.iterrows():
            file_to_export = row["file"]
            basename = os.path.basename(file_to_export)
            if not basename.endswith("_autogen.py"):
                print(
                    f"書き出すファイル名の末尾は `_autogen.py` にしてください。 basename:{basename}")
                continue

            method = row["method"]
            if pd.isnull(method):
                # Ignored. method列が空なら集約ファイルとします
                continue

            # 拡張子を除去
            file_stem = basename[:-3]

            file_stems_to_export.add(file_stem)

        # 辞書順ソート
        file_stems_to_export = list(file_stems_to_export)
        file_stems_to_export.sort()

        # 各ファイル
        for file_stem_to_export in file_stems_to_export:
            text += f"""    path('', include(f'{{PROJECT_NAME}}.{file_stem_to_export}')),
"""

        text += """]

# EOF O3o2o_1o0g4o0
"""

        # ファイル書出し
        with open(self._summary_file_to_export, 'w', encoding="utf8") as f:
            print(f"Write... {self._summary_file_to_export}")
            f.write(text)


if __name__ == "__main__":
    urlsAutoGenerator = UrlsAutoGenerator()
    urlsAutoGenerator.execute()

# EOF O3o2o_1o0g2o0
```

## Step O3o2o_1o0g3o0 コマンド実行

👇 以下のコマンドを打鍵してほしい  

```shell
# ディレクトリーを移動してほしい
# cd src1_meta

# See also: O3o2o_1o0g2o0
python -m scripts.auto_generators.urls
```

Output:  

```plaintext
Current working directory:C:\Users\むずでょ\Documents\GitHub\django-practice2\src1_meta
Write... ../src1/project1/urls_practice_vol1o0_autogen.py
```

## Step O3o2o_1o0g4o0 確認

👇 以下のファイルが自動生成されていることを確認してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 project1
👉  │       ├── 📄 urls_autogen.py
👉  │       └── 📄 urls_practice_vol1o0_autogen.py
    └── 📂 src1_meta
        ├── 📂 data
        │   └── 📄 urls.csv
        └── 📂 scripts
            └── 📂 auto_generators
                └── 📄 urls.py
```

📄 urls_autogen.py:  

```py
# BOF O3o2o_1o0g4o0

from django.urls import include, path

# O3o1o0gA11o0 総合ルート編集
from .settings import PROJECT_NAME
#    ]--------        ------------
#    12               3
# 1. 同じディレクトリー
# 2. `src1/projectN/settings.py`
#                   --------
# 3. 変数


urlpatterns = [
    path('', include(f'{PROJECT_NAME}.urls_practice_vol1o0_autogen')),
]

# EOF O3o2o_1o0g4o0
```

📄 urls_practice_vol1o0_autogen.py

```py
# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.practice_vol1o0.views.page_the_hello.ver1o0 import PageTheHello


urlpatterns = [
    # O3o1o0gA10o0 こんにちわページ
    path('practice/vol1o0/hello2/ver1o0/', PageTheHello.render),
]

# EOF O3o2o_1o0g4o0
```

## Step O3o2o_1o0g5o0 総合ルート編集 - urls.py

👇 以下のファイルを編集してほしい  

```plaintext
    ├── 📂 src1
    │   └── 📂 project1
    │       ├── 📄 urls_practice_vol1o0_autogen.py
👉  │       └── 📄 urls.py                   # こっち
    └── 📂 src1_meta
        ├── 📂 data
        │   └── 📄 urls.csv
        └── 📂 scripts
            └── 📂 auto_generators
                └── 📄 urls.py
```

```py
# ...略...


# O3o2o_1o0g5o0 自動生成されたURL設定
from .urls_autogen import urlpatterns as urlpatterns_autogen
#    ]------------        -----------    -------------------
#    12                   3              4
# 1. 同じディレクトリー
# 2. `src1/projectN/urls_autogen.py`
#                   ------------
# 3. `2.` に含まれる変数
# 4. `3.` の別名


# ...略... urlpatterns = [
# ...略... ]


# O3o2o_1o0g5o0 自動生成されたURL設定
urlpatterns.extend(urlpatterns_autogen)
```

## Step o3o2o_1o0g6o0 Webページにアクセスする

📖 [http://localhost:8000/practice/vol1o0/hello2/ver1o0/](http://localhost:8000/practice/vol1o0/hello2/ver1o0/)  

## トラブルシューティング

もし、 `TemplateDoesNotExist at /` といったエラーメッセージが出てきた場合、  
同じURLを指す複数の `path( ... )` が urlpatterns変数に設定されていることが考えられる。  
がんばって重複しないようにしてほしい  

# 次の記事

📖 [DjangoのHTMLのボイラープレートを減らすテンプレートを使おう！](https://qiita.com/muzudho1/items/7dcfc068e0bec009d371)  

# 参考にした記事

## Python

📖 [Writing Unicode text to a text file?](https://stackoverflow.com/questions/6048085/writing-unicode-text-to-a-text-file)  

## Pandas

📖 [pandas.isnull](https://pandas.pydata.org/docs/reference/api/pandas.isnull.html)  
