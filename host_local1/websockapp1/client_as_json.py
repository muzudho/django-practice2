# See also:
#     ð [GitHub andrewgodwin/channels-examples/multichat/chat/consumers.py](https://github.com/andrewgodwin/channels-examples/blob/master/multichat/chat/consumers.py)
#     ð [Python WebSocketéä¿¡ã®ä»æ¹ï¼ã¯ã©ã¤ã¢ã³ãç·¨](https://www.raspberrypirulo.net/entry/websocket-client)
#     ð [websocket-client - Examples](https://websocket-client.readthedocs.io/en/latest/examples.html)
#     ð [GitHub - websocket-client](https://github.com/websocket-client/websocket-client)
import sys
import traceback
import websocket

try:
    import thread  # è¦ã¤ãããªã
except ImportError:
    import _thread as thread  # websocket-client ã® GitHub ã§ã¯ãã£ã¡ãä½¿ããã¦ãã

import time
import argparse
from main_finally import MainFinally


class ClientAsJson():

    def __init__(self, url):

        # ãããã¯ã­ã°ã®è¡¨ç¤º/éè¡¨ç¤ºè¨­å®
        websocket.enableTrace(True)

        # WebSocketAppã¯ã©ã¹ãçæ
        self.websockApp = websocket.WebSocketApp(url,
                                                 on_open=lambda ws: self.on_open(
                                                     ws),
                                                 on_close=lambda ws, close_status_code, close_msg: self.on_close(
                                                     ws, close_status_code, close_msg),
                                                 on_message=lambda ws, msg: self.on_message(
                                                     ws, msg),
                                                 on_error=lambda ws, msg: self.on_error(ws, msg))

    def on_message(self, ws, message):
        """ã¡ãã»ã¼ã¸åä¿¡ã«å¼ã°ããé¢æ°"""
        print("receive : {}".format(message))

    def on_error(self, ws, error):
        """ã¨ã©ã¼æã«å¼ã°ããé¢æ°"""
        print("### error ###")
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        """ãµã¼ãã¼ããåæ­æã«å¼ã°ããé¢æ°"""
        print("### closed ###")

    def on_open(self, ws):
        """ãµã¼ãã¼ããæ¥ç¶æã«å¼ã°ããé¢æ°"""
        thread.start_new_thread(self.run_worker, ())

    def run_worker(self, *args):
        """ãµã¼ãã¼ããæ¥ç¶æã«ã¹ã¬ããã§èµ·åããé¢æ°"""
        while True:
            time.sleep(0.1)
            input_data = input("send JSON:")
            self.websockApp.send(input_data)

    def clean_up(self):
        self.websockApp.close()
        print("thread terminating...")

    def run_forever(self):
        """websocketã¯ã©ã¤ã¢ã³ãèµ·å"""
        self.websockApp.run_forever()


# ãã®ãã¡ã¤ã«ãç´æ¥å®è¡ããã¨ãã¯ãä»¥ä¸ã®é¢æ°ãå¼ã³åºãã¾ã
if __name__ == "__main__":

    class Main1:
        def __init__(self):
            self._client = None

        def on_main(self):
            parser = argparse.ArgumentParser(
                description='ãµã¼ãã¼ã®ã¢ãã¬ã¹ã¨ãã¼ããæå®ãã¦ããã­ã¹ããéä¿¡ãã¾ã')
            parser.add_argument('--host', default="127.0.0.1",
                                help='ãµã¼ãã¼ã®ãã¹ããè¦å®å¤:127.0.0.1')
            parser.add_argument('--port', type=int,
                                default=8000, help='ãµã¼ãã¼ã®ãã¼ããè¦å®å¤:8000')
            args = parser.parse_args()

            # FIXME ãã®URLã®åãè¾¼ã¿ãå¤ã«åºããªããï¼
            url = f"ws://{args.host}:{args.port}/websock-practice2/v1/"
            #                                    ---------------------
            #                                    1
            # 1. URLãåãããããã«æ³¨æ
            self._client = ClientAsJson(url)
            self._client.run_forever()
            return 0

        def on_except(self, e):
            """ããã§ä¾å¤ã­ã£ãã"""
            traceback.print_exc()

        def on_finally(self):
            if self._client:
                self._client.clean_up()

            print("âããã§çµãã")
            return 1

    sys.exit(MainFinally.run(Main1()))
