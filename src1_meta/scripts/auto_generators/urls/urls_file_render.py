# BOF O3o2o_1o0g2o_4o2o0

class UrlsFileRender:
    def __init__(self, file_path_o):
        self._file_path_o = file_path_o
        self._path_render_list = []
        self._head_text = ""
        self._body_text = ""

    @property
    def file_path_o(self):
        """ファイル パス オブジェクト"""
        return self._file_path_o

    @property
    def path_render_list(self):
        return self._path_render_list

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

# EOF O3o2o_1o0g2o_4o2o0
