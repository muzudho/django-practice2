# See also: ð [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# ãÃã²ã¼ã ã®ç·´ç¿ v3.1
from apps1.tic_tac_toe_v3.websocks.o1o0.consumer_custom import TicTacToeV3o1o0ConsumerCustom
#                       ^three
#          --------------               ---------------        -----------------------------
#          11                           12                     2
#    --------------------------------------------------
#    10
# 10. ãã£ã¬ã¯ããªã¼
# 11. ã¢ããªã±ã¼ã·ã§ã³
# 12. Python ãã¡ã¤ã«ãæ¡å¼µå­æã
# 2. ã¯ã©ã¹å


# ...ç¥...


websocket_urlpatterns = [
    # ...ç¥...


    # ãÃã²ã¼ã ã®ç·´ç¿ v3.3
    url(r'^tic-tac-toe/v3.3/playing/(?P<kw_room_name>\w+)/$',
        #                 ^three
        # -------------------------------------------------
        # 1
        TicTacToeV3o1o0ConsumerCustom.as_asgi()),
    #   ---------------------------------------
    #   2
    # 1. ä¾ãã° `ws://example.com/tic-tac-toe/v3.3/playing/Elephant/` ã®ãããªURLã®ãã¹ã®é¨å
    #                            ----------------------------------
    #    kw_room_name ã¯å¤æ°ã¨ãã¦æ¸¡ããã
    # 2. ã¯ã©ã¹åã¨ã¡ã½ããã URL ã ASGIå½¢å¼ã«ãã
]
