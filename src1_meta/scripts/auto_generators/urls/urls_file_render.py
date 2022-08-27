# BOF O3o2o_1o0g2o_4o2o0

class UrlsFileRender:
    def __init__(self):
        self._path_render_list = []

    @property
    def path_render_list(self):
        return self._path_render_list

    def create_file_text(self):
        return f'''# BOF O3o2o_1o0g4o0

from django.urls import path

{self._create_import_paragraphs()}

urlpatterns = [{self.create_path_items()}]

# EOF O3o2o_1o0g4o0
'''

    def _create_import_paragraphs(self):
        s = ""
        for path_rdr in self._path_render_list:
            s += path_rdr.create_head_text()
        return s

    def create_path_items(self):
        s = ""
        for path_rdr in self._path_render_list:
            s += path_rdr.create_body_text()
        return s

# EOF O3o2o_1o0g2o_4o2o0
