# See also: ð [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# Webã½ã±ããã®ç·´ç¿ï¼
from apps1.practice_v1.websocks.o1o0.consumer import WebsockPractice1V1Consumer
#    ------------------------------- --------        --------------------------
#    1                               2               3
# 1. ãã£ã¬ã¯ããªã¼å
# 2. Python ãã¡ã¤ã«åãæ¡å¼µå­æã
# 3. ã¯ã©ã¹å

# Webã½ã±ããã®ç·´ç¿ï¼
from apps1.practice_v1.websocks.o1o0.consumer_as_json import WebsockPractice2V1Consumer
#                                                                         ^two
#    ------------------------------- ----------------        --------------------------
#    1                               2                       3
# 1. ãã£ã¬ã¯ããªã¼å
# 2. Python ãã¡ã¤ã«åãæ¡å¼µå­æã
# 3. ã¯ã©ã¹å


websocket_urlpatterns = [

    # Webã½ã±ããã®ç·´ç¿ï¼
    url(r'^websock-practice1/v1/$', WebsockPractice1V1Consumer.as_asgi()),
    #     -----------------------   ------------------------------------
    #     1                         2
    # 1. ä¾ãã° `ws://example.com/websock-practice1/v1/` ã¨ãã£ãURLã®ãã¹ã®é¨å
    #                            ----------------------
    # 2. WebsockPractice1V1Consumer ã¯ã©ã¹ã® as_asgi éçã¡ã½ããã®è¿å´å¤

    # Webã½ã±ããã®ç·´ç¿ï¼
    url(r'^websock-practice2/v1/$', WebsockPractice2V1Consumer.as_asgi()),
    #                      ^two                    ^two
    #     -----------------------   ------------------------------------
    #     1                         2
    # 1. ä¾ãã° `ws://example.com/websock-practice2/v1/` ã¨ãã£ãURLã®ãã¹ã®é¨å
    #                            ----------------------
    # 2. WebsockPractice2V1Consumer ã¯ã©ã¹ã® as_asgi éçã¡ã½ããã®è¿å´å¤
]
