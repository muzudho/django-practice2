# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.practice_v1.views.page_the_hello.v1o0 import PageTheHello


urlpatterns = [
    # O3o1o0gA10o0 こんにちわページ
    path('practice/v1/hello2', PageTheHello.render, name='practice_v1_hello2'),
]

# EOF O3o2o_1o0g4o0
