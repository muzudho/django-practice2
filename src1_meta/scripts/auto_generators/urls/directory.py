# BOF O3o2o_1o0g2o_4o4o0

import glob


class Directory:

    @staticmethod
    def search(path):

        # パスに "this/is/a/pen/../paper" が含まれていれば、 "this/is/a/paper" に解決する処理
        path = path.resolve()

        # 名前がマッチしているファイルを探す
        print(f"[Directory search] path:{path}")
        target_files = glob.glob(f"{path}/urls_*_autogen.py")
        print(f"[Directory search] len(target_files):{len(target_files)}")

        for file in target_files:
            print(f"[Directory search] file:{file}")

        return Directory(target_files)

    def __init__(self, target_files):
        self._target_files = target_files

# EOF O3o2o_1o0g2o_4o4o0
