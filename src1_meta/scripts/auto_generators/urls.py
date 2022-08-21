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
    0  src1/project1/urls_practice_autogen.py  practice/v1/page-the-hello  page_the_hello  O3o1o0gA10o0 こんにちわページ  apps1.practice_v1.views.page_the_hello.v1o0  PageTheHello    NaN  render
    """

    print(f"Current working directory:{os.getcwd()}")

    # 各行
    df = df.reset_index()  # make sure indexes pair with number of rows
    for index, row in df.iterrows():

        file_to_export = row['file']
        # 誤上書き防止のため、ファイル名の末尾は `_autogen.py` かチェックします
        basename = os.path.basename(file_to_export)
        if not basename.endswith("_autogen.py"):
            print(f"書き出すファイル名の末尾は `_autogen.py` にしてください。 basename:{basename}")
            continue

        # ファイル書出し
        with open(file_to_export, 'w') as f:
            print(f"Write... {file_to_export}")
            f.write('W.I.P\n')


if __name__ == "__main__":
    main()

# EOF o3o2o_1o0g2o0
