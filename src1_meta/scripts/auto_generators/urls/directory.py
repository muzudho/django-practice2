# BOF O3o2o_1o0g2o_4o4o0

import glob
from pathlib import Path


class Directory:

    @staticmethod
    def search(path):

        # パスに "this/is/a/pen/../paper" が含まれていれば、 "this/is/a/paper" に解決する処理
        path = path.resolve()

        # 名前がマッチしているファイルを探す
        print(f"[Directory search] path:{path}")
        target_path_objects = glob.glob(f"{path}/urls_*_autogen.py")
        print(
            f"[Directory search] len(target_path_objects):{len(target_path_objects)}")

        # 文字列のリストに変換
        target_path_str_list = []

        for target_path_o in target_path_objects:
            print(f"[Directory search] target_path_o:{target_path_o}")
            target_path_str_list.append(str(target_path_o))

        return Directory(target_path_str_list)

    def __init__(self, target_path_str_list):
        self._target_path_str_list = target_path_str_list

    def remove_all(self, removee_file_str_list):
        for file_str in removee_file_str_list:
            s = str(Path(file_str).absolute().resolve())
            try:
                self._target_path_str_list.remove(s)
            except ValueError as e:
                print(f"[Directory remove_all] failed e:{e}")
                pass

# EOF O3o2o_1o0g2o_4o4o0
