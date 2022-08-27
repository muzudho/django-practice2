# BOF O3o2o_1o0g2o0

import os
import pandas as pd

# O3o2o_1o0g2o_3o0
from .file_path import FilePath
#    ]---------        --------
#    12                3
# 1. 同じディレクトリー
# 2. file_path.py
#    ---------
# 3. クラス名

# O3o2o_1o0g2o_4o1o0
from .urls_x_autogen_render import UrlsXAutogenRender


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

        # 書き出すファイル
        file_map = {}

        # 各行
        df = df.reset_index()  # make sure indexes pair with number of rows
        for index, row in df.iterrows():
            # 出力先ファイルパスオブジェクト
            file_path_o, err = FilePath.create_or_err(row['file'])
            if not err is None:
                print(err)
                continue

            method = row["method"]
            if pd.isnull(method):
                # method列が空なら集約ファイルとします
                self._summary_file_to_export = file_path_o.value
                continue

            # 新規ファイル作成
            if not file_path_o.value in file_map:
                file_map[file_path_o.value] = UrlsXAutogenRender(file_path_o)

            file_o = file_map[file_path_o.value]

            file_o.module = row["module"]
            file_o.real_class_name = row["class"]
            file_o.alias_class_name = row['alias']

            file_map[file_path_o.value].head_text += file_o.create_head_text()

            file_o.comment = row["comment"]
            file_o.path = row["path"]
            name = row["name"]

            # コメント
            comment_phrase = file_o.create_comment_phrase()

            # 名前
            if pd.isnull(name):
                # 省略可
                name_phrase = ""
            else:
                name_phrase = f", name='{name}'"

            file_map[file_path_o.value].body_text += f"""{comment_phrase}
    path('{file_o.path}', {file_o.virtual_class_name}.{method}{name_phrase}),
"""

        # 各ファイル書出し
        for file_path, file_o in file_map.items():
            # ファイル書出し
            with open(file_path, 'w', encoding="utf8") as f:
                print(f"Write... {file_path}")
                f.write(f'''# BOF O3o2o_1o0g4o0

from django.urls import path

{file_o.head_text}

urlpatterns = [{file_o.body_text}]

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
            # 出力先ファイル名オブジェクト
            file_path_o, err = FilePath.create_or_err(row['file'])
            if not err is None:
                print(err)
                continue

            method = row["method"]
            if pd.isnull(method):
                # Ignored. method列が空なら集約ファイルとします
                continue

            # ステムをリストに追加
            file_stems_to_export.add(file_path_o.stem)

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

# EOF O3o2o_1o0g2o0
