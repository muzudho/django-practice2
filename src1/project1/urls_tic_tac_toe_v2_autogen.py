# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.tic_tac_toe_v2.views.think.engine_manual.v1o0 import EngineManual


urlpatterns = [
    # OA16o2o0gA16o1o0 〇×ゲーム v2 思考エンジン手動
    path('tic-tac-toe/v2/engine-manual/', EngineManual.render, name='practice_v1_vuetify_textarea1_to_model'),
]

# EOF O3o2o_1o0g4o0
