# 〇×ゲーム v2 コンシューマー v1.0
from apps1.tic_tac_toe_v2.websocks.gui.consumer.v1o0 import TicTacToeV2ConsumerBase
#                       ^two
#          --------------                       ----        -----------------------
#          11                                   12          2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれている __init__.py ファイルにさらに含まれるクラス

# 〇×ゲーム v3 メッセージコンバーター v1.0
from ..message_converter.v1o0 import TicTacToeV3g1o0MessageConverter
#                                             ^three
#    ------------------- ----        -------------------------------
#    1                   2           3
# 1. このファイルの隣のディレクトリー
# 2. Python ファイル。拡張子抜き
# 3. クラス


class TicTacToeV3o1o0ConsumerCustom(TicTacToeV2ConsumerBase):
    """OA24o1o0g3o0 Webソケット用コンシューマー"""

    def __init__(self):
        super().__init__()
        self._messageConverter = TicTacToeV3g1o0MessageConverter()
        #                                  ^three

    async def on_receive(self, doc_received):
        """クライアントからメッセージを受信したとき

        Returns
        -------
        response
        """

        return await self._messageConverter.on_receive(self.scope, doc_received)
