# See also: ð [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
from django.conf.urls import url

# ãÃã²ã¼ã  v2o1o0
from apps1.tic_tac_toe_v2.websocks.o1o0.gui.consumer_custom import TicTacToeV2o1o0ConsumerCustom
#    ----- -------------- ----------------- ---------------        -----------------------------
#    1     2              3                 4                      5
#    ------------------------------------------------------
#    6
# 1. éçºèç¨ãã£ã¬ã¯ããªã¼ã®ä¸é¨
# 2. ã¢ããªã±ã¼ã·ã§ã³ ãã©ã«ãã¼å
# 3. ãã£ã¬ã¯ããªã¼å
# 4. Python ãã¡ã¤ã«åãæ¡å¼µå­æã
# 5. ã¯ã©ã¹å
# 6. ã¢ã¸ã¥ã¼ã«å


websocket_urlpatterns = [

    # ãÃã²ã¼ã  v2
    url(r'^tic-tac-toe/v2/playing/(?P<kw_room_name>\w+)/$',
        # -----------------------------------------------
        # 1
        TicTacToeV2o1o0ConsumerCustom.as_asgi()),
    #   ---------------------------------------
    #   2
    # 1. ä¾ãã° `ws://example.com/tic-tac-toe/v2/playing/Elephant/` ã®ãããªURLã®ãã¹ã®é¨å
    #                            --------------------------------
    #    kw_room_name ã¯å¤æ°ã¨ãã¦æ¸¡ããã
    # 2. ã¯ã©ã¹åã¨ã¡ã½ããã URL ã ASGIå½¢å¼ã«ãã
]
