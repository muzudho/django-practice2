# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.launcher_vol1o0.views.launcher.ver1o0 import Launcher as LauncherView1o0g1o0
from apps1.launcher_vol1o0.views.launcher.ver2o0 import Launcher as LauncherView1o0g2o0


urlpatterns = [
    # O5o1o0gA11o1o0 ランチャー1.0巻 1.0版
    path('launcher/vol1.0/ver1.0/', LauncherView1o0g1o0.render, name='launcher_vol1o0_ver1o0'),

    # O5o2o0g8o1o0 ランチャー1.0巻 2.0版
    path('', LauncherView1o0g2o0.render, name='home'),
]

# EOF O3o2o_1o0g4o0
