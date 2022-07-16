from apps1.tic_tac_toe_v2.websocks.o1o0.gui.consumer_base import TicTacToeV2ConsumerBase
#    ----- -------------- ----------------- -------------        -----------------------
#    1     2              3                 4                    5
# 1,3. ディレクトリー名
# 1. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名

from apps1.tic_tac_toe_v2.websocks.o1o0.gui.message_converter import TicTacToeV2MessageConverter
#    ----- -------------- ----------------- -----------------        ---------------------------
#    1     2              3                 4                        5
# 1,3. ディレクトリー名
# 1. アプリケーション フォルダー名
# 4. Python ファイル名。拡張子抜き
# 5. クラス名


class TicTacToeV2ConsumerCustom(TicTacToeV2ConsumerBase):
    """Webソケット用コンシューマー"""

    def __init__(self):
        super().__init__()
        self._messageConverter = TicTacToeV2MessageConverter()

    async def on_receive(self, doc_received):
        """クライアントからメッセージを受信したとき

        Returns
        -------
        response
        """

        return await self._messageConverter.on_receive(self.scope, doc_received)
