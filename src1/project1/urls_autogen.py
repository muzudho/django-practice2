# AutoGenBegin O3o2o_1o0g4o0

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
    path('', include(f'{PROJECT_NAME}.urls_consecutive_name_vol1o0_autogen')),
    path('', include(f'{PROJECT_NAME}.urls_launcher_vol1o0_autogen')),
    path('', include(f'{PROJECT_NAME}.urls_lifegame_vol1o0_autogen')),
    path('', include(f'{PROJECT_NAME}.urls_practice_vol1o0_autogen')),
    path('', include(f'{PROJECT_NAME}.urls_tic_tac_toe_vol1o0_autogen')),
    path('', include(f'{PROJECT_NAME}.urls_tic_tac_toe_vol2o0_autogen')),
    path('', include(f'{PROJECT_NAME}.urls_tic_tac_toe_vol3o0_autogen')),
]

# AutoGenEnd O3o2o_1o0g4o0
