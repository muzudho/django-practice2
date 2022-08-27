# BOF O3o2o_1o0g2o_4o1o0

import pandas as pd


class UrlsXAutogenRender:
    def __init__(self, file_path_o):
        self._file_path_o = file_path_o
        self._head_text = ""
        self._body_text = ""
        self._module = ""
        self._real_class_name = ""
        self._alias_class_name = pd.NA
        self._comment = pd.NA

    @property
    def file_path_o(self):
        """ファイル パス オブジェクト"""
        return self._file_path_o

    @property
    def head_text(self):
        """ヘッド テキスト"""
        return self._head_text

    @head_text.setter
    def head_text(self, value):
        self._head_text = value

    @property
    def body_text(self):
        """本文"""
        return self._body_text

    @body_text.setter
    def body_text(self, value):
        self._body_text = value

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
    def comment(self):
        """コメント"""
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value

    def create_comment_phrase(self):
        """コメント句"""
        if pd.isnull(self._comment):
            # 省略可
            return ""
        else:
            return f"""
    # {self._comment}"""

    def create_alias_class_name_phrase(self):
        if pd.isnull(self.alias_class_name):
            return ""
        else:
            return f" as {self.alias_class_name}"

# EOF O3o2o_1o0g2o_4o1o0
