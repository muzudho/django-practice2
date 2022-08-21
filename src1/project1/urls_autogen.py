# BOF O3o2o_1o0g4o0

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
    path('', include(f'{PROJECT_NAME}.urls_portal_autogen')),
    path('', include(f'{PROJECT_NAME}.urls_practice_autogen')),
    path('', include(f'{PROJECT_NAME}.urls_tic_tac_toe_v1_autogen')),
    path('', include(f'{PROJECT_NAME}.urls_tic_tac_toe_v2_autogen')),
    path('', include(f'{PROJECT_NAME}.urls_tic_tac_toe_v3_autogen')),
]

# EOF O3o2o_1o0g4o0
