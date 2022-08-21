# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.portal_v1.views.portal.v1o0 import Portal as PortalO1o0


urlpatterns = [
    # O5o1o0gA11o1o0 ポータルの練習
    path('practice/v1/portal', PortalO1o0.render, name='practice_v1_portal'),
]

# EOF O3o2o_1o0g4o0
