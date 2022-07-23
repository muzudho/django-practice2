from apps1.tic_tac_toe_v2.websocks.o1o0.gui.consumer_base import TicTacToeV2ConsumerBase
#                       ^ two                                              ^ two
#    ----- -------------- ----------------- -------------        -----------------------
#    1     2              3                 4                    5
# 1,3. ディレクトリー名
# 1. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

from .message_converter import TicTacToeV3o1o0MessageConverter
#                                        ^three
#    ]-----------------        -------------------------------
#    12                        3
# 1. このファイルと同じディレクトリー
# 2. Python ファイル名。拡張子抜き
# 3. クラス名


class TicTacToeV3o1o0ConsumerCustom(TicTacToeV2ConsumerBase):
    """Webソケット用コンシューマー"""

    def __init__(self):
        super().__init__()
        self._messageConverter = TicTacToeV3o1o0MessageConverter()
        #                                  ^three

    async def on_receive(self, doc_received):
        """クライアントからメッセージを受信したとき

        Returns
        -------
        response
        """

        return await self._messageConverter.on_receive(self.scope, doc_received)
