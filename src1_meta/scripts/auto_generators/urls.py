# BOF o3o2o_1o0g2o0

import os
import pandas as pd


class UrlsAutoGenerator:
    def __init__(self):
        self._summary_file_to_export = None

    def execute(self):
        # CSV 読取
        df = pd.read_csv('data/urls.csv')
        #                 ----------------------
        #                 1
        # 1. `src1_meta/data/urls_practice.csv` を読取
        #               ----------------------

        # print(df)
        """
        Examples
        --------
                                                file                        path            name                comment                                       module         class  alias  method
        0  src1/project1/urls_practice_autogen.py  practice/v1/page-the-hello  page_the_hello  O3o1o0gA10o0 こんにちわページ  apps1.practice_v1.views.page_the_hello.v1o0  PageTheHello    NaN  render
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
            with open(file_to_export, 'w', encoding="utf8") as f:
                print(f"Write... {file_to_export}")
                f.write(f'''from django.urls import path

{head_text_of_files[file_to_export]}

urlpatterns = [{body_text_of_files[file_to_export]}]
''')

    def write_url_summary_file(self, df):
        """集約ファイル自動生成"""

        text = """from django.urls import include, path

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

        # 各ファイル
        for file_stem_to_export in file_stems_to_export:
            text += f"""    path('', include(f'{{PROJECT_NAME}}.{file_stem_to_export}')),
"""

        text += """]
"""

        # ファイル書出し
        with open(self._summary_file_to_export, 'w', encoding="utf8") as f:
            print(f"Write... {self._summary_file_to_export}")
            f.write(text)


if __name__ == "__main__":
    urlsAutoGenerator = UrlsAutoGenerator()
    urlsAutoGenerator.execute()

# EOF o3o2o_1o0g2o0
