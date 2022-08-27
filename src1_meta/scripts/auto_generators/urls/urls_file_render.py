# BOF O3o2o_1o0g2o_4o2o0

class UrlsFileRender:
    def __init__(self):
        self._path_render_list = []
        self._head_text = ""
        self._body_text = ""

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

    def create_head_text(self):
        s = ""
        for path_rdr in self._path_render_list:
            s += path_rdr.create_head_text()
        return s

    def create_body_text(self):
        s = ""
        for path_rdr in self._path_render_list:
            s += path_rdr.create_body_text()
        return s

# EOF O3o2o_1o0g2o_4o2o0
