# サンプルを見る

📖 [この記事のゴール](http://tic.warabenture.com:8000/practice/vol1.0/hello-alias/ver1.0/)  

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
    │   │       │       └── 📂 hello
    │   │       │           └── 📄 ver1o0.html
    │   │       └── 📂 views
    │   │           └── 📂 hello
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

## Step [O3o2o_1o0g1o0] データ作成 - src1_meta/data/urls.csv ファイル

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
../src1/project1/urls_practice_vol1o0_autogen.py,practice/vol1.0/hello-alias/ver1.0/,practice_vol1o0_hello_alias,"O3o2o_1o0g1o0 練習1.0巻 こんにちわ別名1.0版",apps1.practice_vol1o0.views.hello.ver1o0,HelloView,,render
```

## Step [O3o2o_1o0g2o_1o0] Pythonパッケージインストール - pandas

👇 以下のコマンドを打鍵してほしい  

```shell
pip install pandas
```

## Step [O3o2o_1o0g2o_1o0] スクリプト作成 - __init__.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1     # 既存
    └── 📂 src1_meta
        ├── 📂 data
        │   └── 📄 urls.csv
        └── 📂 scripts
            └── 📂 auto_generators
                └── 📂 urls
👉                  └── 📄 __init__.py
```

👇 中身は空っぽでよい  

```py
```

## Step [O3o2o_1o0g2o_2o0] スクリプト作成 - file_path.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1     # 既存
    └── 📂 src1_meta
        ├── 📂 data
        │   └── 📄 urls.csv
        └── 📂 scripts
            └── 📂 auto_generators
                └── 📂 urls
                    ├── 📄 __init__.py
👉                  └── 📄 file_path.py
```

```py
# BOF [O3o2o_1o0g2o_2o0]

import os


class FilePath:
    """ファイルパス

    Examples
    --------
    C:\this\is\a\base.name
                 ---]-----
                 111 112
                 ---------
                 11
    ----------------------
    10

    10. file path
    11. basename
    111. stem
    112. extension with dot
    """

    @staticmethod
    def create_or_err(file_path):
        # ファイル名オブジェクト
        file_path_o = FilePath(file_path)

        if file_path_o.is_valid():
            return file_path_o, None

        return None, file_path_o._last_err

    def __init__(self, value):
        # 値
        self._value = value
        # 最後のエラーメッセージ
        self._last_err = None
        # ベースネーム
        self._basename = None
        # ステム
        self._stem = None

    @property
    def value(self):
        """値"""
        return self._value

    @property
    def last_err(self):
        """最後のエラーメッセージ"""
        return self._last_err

    @property
    def basename(self):
        """ベースネーム"""
        if self._basename is None:
            self._basename = os.path.basename(self.value)

        return self._basename

    @property
    def stem(self):
        """ステム"""
        if self._stem is None:
            # 拡張子を除去
            self._stem = self.basename[:-3]

        return self._stem

    def is_valid(self):
        """ファイル名が `urls_*_autogen.py` な感じかチェックします"""

        basename = os.path.basename(self._value)

        if basename.startswith("urls_") and basename.endswith("_autogen.py"):
            return True

        self._last_err = f"書き出すファイル名の先頭は `urls_`、 末尾は `_autogen.py` にしてください。 basename:{basename}"
        return False

# EOF [O3o2o_1o0g2o_2o0]
```

## Step [O3o2o_1o0g2o_3o0] スクリプト作成/テスト作成 - file_path.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1     # 既存
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📂 urls
    │               ├── 📄 __init__.py
    │               └── 📄 file_path.py
    └── 📂 tests
        └── 📂 src1_meta
            └── 📂 scripts
                └── 📂 auto_generators
                    └── 📂 urls
👉                      └── 📄 file_path.py
```

```py
# BOF [O3o2o_1o0g2o_3o0]

"""テスト
# cd {testsのあるディレクトリー}

python -m tests.src1_meta.scripts.auto_generators.urls.file_path
"""
from src1_meta.scripts.auto_generators.urls.file_path import FilePath


def test_ok1():
    # 出力先ファイルパスオブジェクト
    file_path_o, err = FilePath.create_or_err(
        'C:\\this\\is\\a\\urls_path_autogen.py')
    if not err is None:
        print(f"F\n{err}")
        return

    print(".", end="")  # Succeed


def test_not_starts_with_urls():
    # 出力先ファイルパスオブジェクト
    file_path_o, err = FilePath.create_or_err(
        'C:\\this\\is\\a\\path_autogen.py')
    if err == "書き出すファイル名の先頭は `urls_`、 末尾は `_autogen.py` にしてください。 basename:path_autogen.py":
        print(".", end="")
        return

    print("F")  # Failed


def test_not_ends_with_autogen():
    # 出力先ファイルパスオブジェクト
    file_path_o, err = FilePath.create_or_err(
        'C:\\this\\is\\a\\urls_path.py')
    if err == "書き出すファイル名の先頭は `urls_`、 末尾は `_autogen.py` にしてください。 basename:urls_path.py":
        print(".", end="")
        return

    print("F", end="")


if __name__ == '__main__':
    test_ok1()
    test_not_starts_with_urls()
    test_not_ends_with_autogen()

# EOF [O3o2o_1o0g2o_3o0]
```

## Step [O3o2o_1o0g2o_4o0] スクリプト作成/テスト実行 - file_path.py ファイル

👇 以下のディレクトリーから、コマンドを打鍵してほしい  

```plaintext
👉  📂
    ├── 📂 src1
    ├── 📂 src1_meta
    └── 📂 tests
        └── 📂 src1_meta
            └── 📂 scripts
                └── 📂 auto_generators
                    └── 📂 urls
                        └── 📄 file_path.py
```

Input:  

```shell
# cd {testsのあるディレクトリー}

python -m tests.src1_meta.scripts.auto_generators.urls.file_path
```

Output:  

```plaintext
...
```

👆 エラーが表示されていなければオーケーだ  

## Step [O3o2o_1o0g2o_4o1o0] スクリプト作成 - path_renderer.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📂 urls
    │               ├── 📄 __init__.py
    │               ├── 📄 file_path.py
👉  │               └── 📄 path_renderer.py
    └── 📂 tests
        └── 📂 src1_meta
            └── 📂 scripts
                └── 📂 auto_generators
                    └── 📂 urls
                        └── 📄 file_path.py
```

```py
# BOF [O3o2o_1o0g2o_4o1o0]

import pandas as pd


class PathRenderer:
    def __init__(self):
        self._module = ""
        self._real_class_name = ""
        self._alias_class_name = pd.NA
        self._method = ""
        self._comment = pd.NA
        self._path = pd.NA
        self._name = pd.NA

    @property
    def module(self):
        """モジュール"""
        return self._module

    @module.setter
    def module(self, value):
        self._module = value

    @property
    def real_class_name(self):
        """実クラス名"""
        return self._real_class_name

    @real_class_name.setter
    def real_class_name(self, value):
        self._real_class_name = value

    @property
    def alias_class_name(self):
        """クラスの別名"""
        return self._alias_class_name

    @alias_class_name.setter
    def alias_class_name(self, value):
        self._alias_class_name = value

    @property
    def virtual_class_name(self):
        """実際的なクラス名"""
        if pd.isnull(self.alias_class_name):
            return self.real_class_name
        else:
            return self.alias_class_name

    @property
    def method(self):
        """メソッド"""
        return self._method

    @method.setter
    def method(self, value):
        self._method = value

    @property
    def comment(self):
        """コメント"""
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value

    @property
    def path(self):
        """パス"""
        return self._path

    @path.setter
    def path(self, value):
        if pd.isnull(value):
            # 空文字列の指定があり得ます。
            # pandas は空文字列と NaN を区別せず NaN にするので、空文字列に変換します
            self._path = ""
            return

        self._path = value

    @property
    def name(self):
        """名前"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def create_header_text(self):
        return f"from {self.module} import {self.real_class_name}{self._create_alias_class_name_phrase()}\n"

    def _create_alias_class_name_phrase(self):
        if pd.isnull(self.alias_class_name):
            return ""
        else:
            return f" as {self.alias_class_name}"

    def create_urlpatterns_item_text(self):
        # コメント
        comment_phrase = self._create_comment_phrase()
        # name引数
        name_arg = self._create_name_arg()

        return f"""{comment_phrase}
    path('{self.path}', {self.virtual_class_name}.{self.method}{name_arg}),
"""

    def _create_comment_phrase(self):
        """コメント句"""
        if pd.isnull(self._comment):
            # 省略可
            return ""
        else:
            return f"""
    # {self._comment}"""

    def _create_name_arg(self):
        """名前引数"""
        if pd.isnull(self.name):
            # 省略可
            return ""
        else:
            return f", name='{self.name}'"

# EOF [O3o2o_1o0g2o_4o1o0]
```

## Step [O3o2o_1o0g2o_4o1o1o0] スクリプト作成/テスト作成 - path_renderer.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📂 urls
    │               ├── 📄 __init__.py
    │               ├── 📄 file_path.py
    │               └── 📄 path_renderer.py
    └── 📂 tests
        └── 📂 src1_meta
            └── 📂 scripts
                └── 📂 auto_generators
                    └── 📂 urls
                        ├── 📄 file_path.py
👉                      └── 📄 path_renderer.py
```

```py
# BOF [O3o2o_1o0g2o_4o1o1o0]

"""テスト
# cd {testsのあるディレクトリー}

python -m tests.src1_meta.scripts.auto_generators.urls.path_renderer
"""
from src1_meta.scripts.auto_generators.urls.path_renderer import PathRenderer


def test_ok1():
    # Test data
    path_rdr = PathRenderer()
    path_rdr.method = "render"
    path_rdr.module = "src1.this.is.a.file"
    path_rdr.real_class_name = "HelloClass"
    path_rdr.alias_class_name = "GoodMorningClass"
    path_rdr.comment = "This is a text."
    path_rdr.path = "C:\\This\\Is\\A\\Path\\urls_example_autogen.py"
    path_rdr.name = "home"

    actual = path_rdr.create_header_text()
    expected = """from src1.this.is.a.file import HelloClass as GoodMorningClass
"""

    if not actual == expected:
        print(
            f"F\nimport_statement failed. actual:[{actual}] expected:[{expected}]\n")
        return

    actual = path_rdr.create_urlpatterns_item_text()
    expected = """
    # This is a text.
    path('C:\\This\\Is\\A\\Path\\urls_example_autogen.py', GoodMorningClass.render, name='home'),
"""

    print(".", end="")  # Succeed

    if not actual == expected:
        print(
            f"F\nurlpatterns_item_text failed. actual:[{actual}] expected:[{expected}]\n")
        return

    print(".", end="")


if __name__ == '__main__':
    test_ok1()

# EOF [O3o2o_1o0g2o_4o1o1o0]
```

## Step [O3o2o_1o0g2o_4o1o2o0] スクリプト作成/テスト実行 - path_renderer.py ファイル

👇 以下のディレクトリーから、コマンドを打鍵してほしい  

```plaintext
👉  📂
    ├── 📂 src1
    ├── 📂 src1_meta
    └── 📂 tests
        └── 📂 src1_meta
            └── 📂 scripts
                └── 📂 auto_generators
                    └── 📂 urls
                        └── 📄 path_renderer.py
```

Input:  

```shell
# cd {testsのあるディレクトリー}

python -m tests.src1_meta.scripts.auto_generators.urls.path_renderer
```

Output:  

```plaintext
..
```

👆 エラーが表示されていなければオーケーだ  

## Step [O3o2o_1o0g2o_4o2o0] スクリプト作成 - urls_file_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1     # 既存
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📂 urls
    │               ├── 📄 __init__.py
    │               ├── 📄 file_path.py
    │               ├── 📄 path_renderer.py
👉  │               └── 📄 urls_file_render.py
    └── 📂 tests
        └── 📂 src1_meta
            └── 📂 scripts
                └── 📂 auto_generators
                    └── 📂 urls
                        ├── 📄 file_path.py
                        └── 📄 path_renderer.py
```

```py
# BOF [O3o2o_1o0g2o_4o2o0]

class UrlsFileRender:
    def __init__(self):
        self._path_render_list = []

    @property
    def path_render_list(self):
        return self._path_render_list

    def create_file_text(self):
        return f'''# AutoGenBegin [O3o2o_1o0g4o0]

from django.urls import path

{self._create_import_paragraphs()}

urlpatterns = [{self.create_path_items()}]

# AutoGenEnd [O3o2o_1o0g4o0]
'''

    def _create_import_paragraphs(self):
        s = ""
        for path_rdr in self._path_render_list:
            s += path_rdr.create_header_text()
        return s

    def create_path_items(self):
        s = ""
        for path_rdr in self._path_render_list:
            s += path_rdr.create_urlpatterns_item_text()
        return s

# EOF [O3o2o_1o0g2o_4o2o0]
```

## Step [O3o2o_1o0g2o_4o3o0] スクリプト作成 - urls_summary_render.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1     # 既存
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📂 urls
    │               ├── 📄 __init__.py
    │               ├── 📄 file_path.py
    │               ├── 📄 path_renderer.py
    │               ├── 📄 urls_file_render.py
👉  │               └── 📄 urls_summary_render.py
    └── 📂 tests
        └── 📂 src1_meta
            └── 📂 scripts
                └── 📂 auto_generators
                    └── 📂 urls
                        ├── 📄 file_path.py
                        └── 📄 path_renderer.py
```

```py
# BOF [O3o2o_1o0g2o_4o3o0]

from pathlib import Path


class UrlsSummaryRender:

    @staticmethod
    def create_header_text():
        return """# AutoGenBegin [O3o2o_1o0g4o0]

from django.urls import include, path

# [O3o1o0gA11o0] 総合ルート編集
from .settings import PROJECT_NAME
#    ]--------        ------------
#    12               3
# 1. 同じディレクトリー
# 2. `src1/projectN/settings.py`
#                   --------
# 3. 変数


urlpatterns = [
"""

    @staticmethod
    def create_footer_text():
        return """]

# AutoGenEnd [O3o2o_1o0g4o0]
"""

    def __init__(self):
        self._file_stems = set()
        self._file_path = None

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value

    @property
    def parent_directory(self):
        print(
            f"[UrlsSummaryRender parent_directory] self._file_path:{self._file_path}")
        return Path(self._file_path).parent.absolute()

    def add_stem(self, stem):
        self._file_stems.add(stem)

    def create_file_text(self):
        s = UrlsSummaryRender.create_header_text()
        s += self.create_path_items_text()
        s += UrlsSummaryRender.create_footer_text()
        return s

    def create_path_items_text(self):
        # 辞書順ソート
        file_stems = list(self._file_stems)
        file_stems.sort()

        s = ""
        # 各ファイル
        for stem in file_stems:
            s += f"""    path('', include(f'{{PROJECT_NAME}}.{stem}')),
"""
        return s

# EOF [O3o2o_1o0g2o_4o3o0]
```

## Step [O3o2o_1o0g2o_4o4o0] スクリプト作成 - file_collection.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1     # 既存
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📂 urls
    │               ├── 📄 __init__.py
👉  │               ├── 📄 file_collection.py
    │               ├── 📄 file_path.py
    │               ├── 📄 path_renderer.py
    │               ├── 📄 urls_file_render.py
    │               └── 📄 urls_summary_render.py
    └── 📂 tests
        └── 📂 src1_meta
            └── 📂 scripts
                └── 📂 auto_generators
                    └── 📂 urls
                        ├── 📄 file_path.py
                        └── 📄 path_renderer.py
```

```py
# BOF [O3o2o_1o0g2o_4o4o0]

import glob
from pathlib import Path


class FileCollection:

    @staticmethod
    def find_to(path_pattern):

        # 名前がマッチしているファイルを探す
        # print(f"[FileCollection find_to] path_pattern:{path_pattern}")
        target_path_objects = glob.glob(path_pattern)
        print(
            f"[DirectFileCollectionory find_to] len(target_path_objects):{len(target_path_objects)}")

        # 文字列のリストに変換
        target_path_str_list = []

        for target_path_o in target_path_objects:
            # print(f"[FileCollection find_to] target_path_o:{target_path_o}")
            target_path_str_list.append(str(target_path_o))

        return FileCollection(target_path_str_list)

    def __init__(self, target_path_str_list):
        self._target_path_str_list = target_path_str_list

    @property
    def target_path_str_list(self):
        return self._target_path_str_list

    def remove_all(self, removee_file_str_list):
        for file_str in removee_file_str_list:
            s = str(Path(file_str).absolute().resolve())
            try:
                self._target_path_str_list.remove(s)
            except ValueError as e:
                print(f"[FileCollection remove_all] Remove failed. error:{e}")
                pass

# EOF [O3o2o_1o0g2o_4o4o0]
```

## Step [O3o2o_1o0g2o0] スクリプト作成 - urls/__init__.py ファイル

👇 以下の既存ファイルを編集してほしい  

```plaintext
    ├── 📂 src1     # 既存
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📂 urls
👉  │               ├── 📄 __init__.py
    │               ├── 📄 file_path.py
    │               ├── 📄 path_renderer.py
    │               ├── 📄 urls_file_render.py
    │               └── 📄 urls_summary_render.py
    └── 📂 tests
        └── 📂 src1_meta
            └── 📂 scripts
                └── 📂 auto_generators
                    └── 📂 urls
                        └── 📄 file_path.py
```

```py
# BOF [O3o2o_1o0g2o0]

import os
import pandas as pd
from pathlib import Path

# [O3o2o_1o0g2o_3o0]
from .file_path import FilePath
#    ]---------        --------
#    12                3
# 1. 同じディレクトリー
# 2. file_path.py
#    ---------
# 3. クラス名

# [O3o2o_1o0g2o_4o1o0]
from .path_renderer import PathRenderer

# [O3o2o_1o0g2o_4o2o0]
from .urls_file_render import UrlsFileRender

# [O3o2o_1o0g2o_4o3o0]
from .urls_summary_render import UrlsSummaryRender

# [O3o2o_1o0g2o_4o4o0]
from .file_collection import FileCollection


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
                                                       file                                path                         name  ...      class alias  method
        0                  ../src1/project1/urls_autogen.py                                 NaN                          NaN  ...        NaN   NaN     NaN
        1  ../src1/project1/urls_practice_vol1o0_autogen.py  practice/vo1o0/hello-alias/ver1o0/  practice_vol1o0_hello_alias  ...  HelloView   NaN  render
        """

        print(f"Current working directory:{os.getcwd()}")

        # URL設定ファイル自動生成
        urls_file_map = self.create_urls_file_map(df)

        # 集約ファイル自動生成
        urls_summary_render = self.create_url_summary_render(df)

        # 集約ファイルが置いてあるディレクトリー
        path1 = urls_summary_render.parent_directory
        # パスに "this/is/a/pen/../paper" が含まれていれば、 "this/is/a/paper" に解決する処理
        path1 = path1.resolve()
        # 検索対象
        file_collection = FileCollection.find_to(f"{path1}/urls_*_autogen.py")
        # 生成対象のファイルを除外
        file_collection.remove_all(urls_file_map.keys())
        # 残ったファイルは削除対象
        for file_path in file_collection.target_path_str_list:
            abs_path = str(Path(file_path).absolute().resolve())
            print(f"* [ ] Remove {abs_path}")

        # どんなファイルを書き出すかの一覧を出力
        for file_path, urls_file_o in urls_file_map.items():
            abs_path = str(Path(file_path).absolute().resolve())
            print(f"* [ ] Write {abs_path}")

        abs_path = str(Path(self._summary_file_to_export).absolute().resolve())
        print(f"* [ ] Write {abs_path}")
        print(f"Ok? (y/n)")
        key = input()

        if key.upper() == "Y":
            # ファイルの削除
            for file_path in file_collection.target_path_str_list:
                abs_path = str(Path(file_path).absolute().resolve())
                print(f"Remove... {abs_path}")
                os.remove(abs_path)

            # 各ファイル書出し
            for file_path, urls_file_o in urls_file_map.items():
                abs_path = str(Path(file_path).absolute().resolve())
                # ファイル書出し
                with open(abs_path, 'w', encoding="utf8") as f:
                    print(f"Write... {abs_path}")
                    f.write(urls_file_o.create_file_text())

            # ファイル書出し
            abs_path = str(
                Path(self._summary_file_to_export).absolute().resolve())
            with open(abs_path, 'w', encoding="utf8") as f:
                print(f"Write... {abs_path}")
                f.write(urls_summary_render.create_file_text())

    def create_urls_file_map(self, df):
        """URL設定ファイル自動生成"""

        # `urls_*_autogen.py` ファイル描画オブジェクト
        urls_file_map = {}

        # 各行
        df = df.reset_index()  # make sure indexes pair with number of rows
        for index, row in df.iterrows():

            # 出力先ファイルパスオブジェクト
            file_path_o, err = FilePath.create_or_err(row['file'])
            if not err is None:
                print(err)
                continue

            method_temp = row["method"]
            if pd.isnull(method_temp):
                # method列が空なら集約ファイルとします
                self._summary_file_to_export = file_path_o.value
                continue

            path_rdr = PathRenderer()
            path_rdr.method = method_temp
            path_rdr.module = row["module"]
            path_rdr.real_class_name = row["class"]
            path_rdr.alias_class_name = row['alias']
            path_rdr.comment = row["comment"]
            path_rdr.path = row["path"]
            path_rdr.name = row["name"]

            # urls_*_aurogen.py ファイル オブジェクト取得
            if not file_path_o.value in urls_file_map:
                urls_file_map[file_path_o.value] = UrlsFileRender()

            urls_file_o = urls_file_map[file_path_o.value]
            urls_file_o.path_render_list.append(path_rdr)

        return urls_file_map

    def create_url_summary_render(self, df):
        """集約ファイル自動生成"""

        urls_summary_render = UrlsSummaryRender()

        # Distinct
        df = df.reset_index()  # make sure indexes pair with number of rows
        for index, row in df.iterrows():
            # 出力先ファイル名オブジェクト
            file_path_o, err = FilePath.create_or_err(row['file'])
            if not err is None:
                print(err)
                continue

            method_temp = row["method"]
            if pd.isnull(method_temp):
                # Ignored. method列が空なら集約ファイル
                urls_summary_render.file_path = row["file"]
                continue

            # ステムをリストに追加
            urls_summary_render.add_stem(file_path_o.stem)

        return urls_summary_render

# EOF [O3o2o_1o0g2o0]
```

## Step [O3o2o_1o0g2o1o0] スクリプト作成 - urls/__main__.py ファイル

👇 以下のファイルを新規作成してほしい  

```plaintext
    ├── 📂 src1     # 既存
    ├── 📂 src1_meta
    │   ├── 📂 data
    │   │   └── 📄 urls.csv
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📂 urls
    │               ├── 📄 __init__.py
👉  │               ├── 📄 __main__.py
    │               ├── 📄 file_path.py
    │               ├── 📄 path_renderer.py
    │               ├── 📄 urls_file_render.py
    │               └── 📄 urls_summary_render.py
    └── 📂 tests
        └── 📂 src1_meta
            └── 📂 scripts
                └── 📂 auto_generators
                    └── 📂 urls
                        └── 📄 file_path.py
```

```py
# BOF [O3o2o_1o0g2o1o0]

from .__init__ import UrlsAutoGenerator


def main():
    urlsAutoGenerator = UrlsAutoGenerator()
    urlsAutoGenerator.execute()


if __name__ == "__main__":
    main()

# EOF [O3o2o_1o0g2o1o0]
```

## Step [O3o2o_1o0g3o0] コマンド実行

👇 以下のディレクトリーから、コマンドを打鍵してほしい  

```plaintext
    📂
    ├── 📂 src1
👉  ├── 📂 src1_meta
    │   └── 📂 scripts
    │       └── 📂 auto_generators
    │           └── 📄 urls.py
    └── 📂 tests
```

```shell
# ディレクトリーを移動してほしい
# cd src1_meta

# See also: [O3o2o_1o0g2o0]
python -m scripts.auto_generators.urls
```

Output:  

```plaintext
Current working directory:C:\Users\むずでょ\Documents\GitHub\webgl-practice\me\src1_meta
[UrlsSummaryRender parent_directory] self._file_path:../src1/project1/urls_autogen.py
[DirectFileCollectionory find_to] len(target_path_objects):0
[FileCollection remove_all] Remove failed. error:list.remove(x): x not in list
* [ ] Write C:\Users\むずでょ\Documents\GitHub\django-practice2\src1\project1\urls_practice_vol1o0_autogen.py
* [ ] Write C:\Users\むずでょ\Documents\GitHub\django-practice2\src1\project1\urls_autogen.py
Ok? (y/n)
```

Input:  

```plaintext
y
```

Output:  

```plaintext
Write... C:\Users\むずでょ\Documents\GitHub\django-practice2\src1\project1\urls_warabenture_vol1o0_autogen.py
Write... C:\Users\むずでょ\Documents\GitHub\django-practice2\src1\project1\urls_autogen.py
```

## Step [O3o2o_1o0g4o0] 確認

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
# AutoGenBegin [O3o2o_1o0g4o0]

from django.urls import include, path

# [O3o1o0gA11o0] 総合ルート編集
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

# AutoGenEnd [O3o2o_1o0g4o0]
```

📄 urls_practice_vol1o0_autogen.py

```py
# AutoGenBegin [O3o2o_1o0g4o0]

from django.urls import path

from apps1.practice_vol1o0.views.hello.ver1o0 import HelloView


urlpatterns = [
    # [O3o2o_1o0g1o0] 練習1.0巻 こんにちわ別名1.0版
    path('practice/vol1.0/hello-alias/ver1.0/', HelloView.render, name='practice_vol1o0_hello_alias'),
]

# AutoGenEnd [O3o2o_1o0g4o0]
```

## Step [O3o2o_1o0g5o0] 総合ルート編集 - urls.py

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


# [O3o2o_1o0g5o0] 自動生成されたURL設定
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


# [O3o2o_1o0g5o0] 自動生成されたURL設定
urlpatterns.extend(urlpatterns_autogen)
```

## Step [O3o2o_1o0g6o0] Webページにアクセスする

📖 [http://localhost:8000/practice/vol1.0/hello-alias/ver1.0/](http://localhost:8000/practice/vol1.0/hello-alias/ver1.0/)  

## トラブルシューティング

もし、 `TemplateDoesNotExist at /` といったエラーメッセージが出てきた場合、  
同じURLを指す複数の `path( ... )` が urlpatterns変数に設定されていることが考えられる。  
がんばって重複しないようにしてほしい  

# 次の記事

📖 [DjangoのHTMLのボイラープレートを減らすテンプレートを使おう！](https://qiita.com/muzudho1/items/7dcfc068e0bec009d371)  

# 参考にした記事

## Python

📖 [Writing Unicode text to a text file?](https://stackoverflow.com/questions/6048085/writing-unicode-text-to-a-text-file)  
📖 [`Usage of __main__.py in Python`](https://www.geeksforgeeks.org/usage-of-__main__-py-in-python/)  
📖 [[Django] 自動テストについてのまとめ](https://qiita.com/okoppe8/items/eb7c3be5b9f6be244549)  

## Pandas

📖 [pandas.isnull](https://pandas.pydata.org/docs/reference/api/pandas.isnull.html)  
