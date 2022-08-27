# BOF O3o2o_1o0g2o_4o3o0

class UrlsSummaryRender:

    @staticmethod
    def create_header_text():
        return """# BOF O3o2o_1o0g4o0

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

    @staticmethod
    def create_footer_text():
        return """]

# EOF O3o2o_1o0g4o0
"""

    def __init__(self):
        self._file_stems = set()

    def add_stem(self, stem):
        self._file_stems.add(stem)

    def create_path_items_text(self):
        # 辞書順ソート
        file_stems = list(self._file_stems)
        file_stems.sort()

        s = ""
        # 各ファイル
        for stem in file_stems:
            s += f"""    path('', include(f'{{PROJECT_NAME}}.{stem}')),
"""
        return s

# EOF O3o2o_1o0g2o_4o3o0
