from django.urls import path

from apps1.practice_v1.views.page_the_hello.v1o0 import PageTheHello


urlpatterns = [
    # O3o1o0gA10o0 ‚±‚ñ‚É‚¿‚íƒy[ƒW
    path('practice/v1/page-the-hello', PageTheHello.render, name='page_the_hello'),
]
