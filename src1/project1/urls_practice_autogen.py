# BOF O3o2o_1o0g4o0

from django.urls import path

from apps1.practice_v1.views.page_the_hello.v1o0 import PageTheHello
from apps1.practice_v1.views.page_to_be_added.v2o0 import PageToBeAdded as PageToBeAdded1
from apps1.practice_v1.views.page_to_be_added.v3o0 import PageToBeAdded as PageToBeAdded2


urlpatterns = [
    # o3o2o_1o0g1o0 こんにちわページ
    path('practice/v1/hello2', PageTheHello.render, name='practice_v1_hello2'),

    # O3o2o0g5o1o0 練習ページ １回追加されたページ
    path('practice/v1/page-to-be-added-1', PageToBeAdded1.render, name='page_to_be_added_1'),

    # O3o3o0g4o1o0 練習ページ ２回追加されたページ
    path('practice/v1/page-to-be-added-2', PageToBeAdded2.render, name='page_to_be_added_2'),
]

# EOF O3o2o_1o0g4o0
