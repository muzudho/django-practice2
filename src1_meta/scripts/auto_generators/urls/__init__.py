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
from .path_render import PathRender

# O3o2o_1o0g2o_4o2o0
from .urls_file_render import UrlsFileRender

# O3o2o_1o0g2o_4o3o0
from .urls_summary_render import UrlsSummaryRender


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

            path_rdr = PathRender()
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

        # 各ファイル書出し
        for file_path, urls_file_o in urls_file_map.items():
            # ファイル書出し
            with open(file_path, 'w', encoding="utf8") as f:
                print(f"Write... {file_path}")
                f.write(urls_file_o.create_file_text())

    def write_url_summary_file(self, df):
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
                # Ignored. method列が空なら無視します。集約ファイル
                continue

            # ステムをリストに追加
            urls_summary_render.add_stem(file_path_o.stem)

        text = UrlsSummaryRender.create_header_text()
        text += urls_summary_render.create_path_items_text()
        text += UrlsSummaryRender.create_footer_text()

        # ファイル書出し
        with open(self._summary_file_to_export, 'w', encoding="utf8") as f:
            print(f"Write... {self._summary_file_to_export}")
            f.write(text)

# EOF O3o2o_1o0g2o0
