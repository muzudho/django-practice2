# Webソケット コンシューマー v1.0
from apps1.tic_tac_toe_v2.websocks.gui.consumer.v1o0 import TicTacToeV2ConsumerBase
#          --------------                       ----        -----------------------
#          11                                   12          2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス

# Webソケット メッセージコンバーター v1.1.0
from apps1.tic_tac_toe_v2.websocks.gui.message_converter.v1o0 import TicTacToeV2MessageConverter
#          --------------                                ----        -----------------------
#          11                                            12          2
#    --------------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス


class TicTacToeV2o1o0ConsumerCustom(TicTacToeV2ConsumerBase):
    """OA16o3o0gA10o0 Webソケット用コンシューマー"""

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
