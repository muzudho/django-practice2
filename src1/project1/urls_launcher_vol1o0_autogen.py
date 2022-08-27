# AutoGenBegin O3o2o_1o0g4o0

from django.urls import path

from apps1.launcher_vol1o0.views.finished_lesson.ver1o0 import Launcher as LauncherView1o0g1o0
from apps1.launcher_vol1o0.views.finished_lesson.ver2o0 import Launcher as LauncherView1o0g2o0


urlpatterns = [
    # O5o1o0gA11o1o0 ランチャー1.0巻 終了したレッスン1.0版
    path('launcher/vol1.0/finished-lesson/ver1.0/', LauncherView1o0g1o0.render),

    # O5o2o0g8o1o0 ランチャー1.0巻 終了したレッスン2.0版
    path('', LauncherView1o0g2o0.render, name='home'),
]

# AutoGenEnd O3o2o_1o0g4o0
