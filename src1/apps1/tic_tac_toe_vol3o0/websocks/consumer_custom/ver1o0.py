# BOF [OA24o1o0g3o0]

# 〇×ゲーム2.0巻 ウェブソケットGUIコンシューマー1.0版
from apps1.tic_tac_toe_vol2o0.websocks.gui.consumer.ver1o0 import ConsumerBase
#                         ^two
#          ------------------                       ------        ------------
#          11                                       12            2
#    -----------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれている __init__.py ファイルにさらに含まれるクラス

# 〇×ゲーム2.0巻 ウェブソケットGUIメッセージ駆動1.0版
from apps1.tic_tac_toe_vol2o0.websocks.gui.message_manager.ver1o0 import MessageManager
#          ------------------                              ------        --------------
#          11                                              12            2
#    ------------------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス

# [OA16o3o0gA10o_1o0] 〇×ゲーム2.0巻 - WebソケットGUI Endメッセージハンドラー 1.0版
from apps1.tic_tac_toe_vol2o0.websocks.gui.c2s_handlers.end.ver1o0 import EndC2sHandler

# [OA24o1o0g3o_1o0] 〇×ゲーム3.0巻 - WebソケットGUI Moveメッセージハンドラー 1.0版
from apps1.tic_tac_toe_vol3o0.websocks.gui.c2s_handlers.move.ver1o0 import MoveC2sHandler
#                         ^

# [OA16o3o0gA10o_3o0] 〇×ゲーム2.0巻 - WebソケットGUI Startメッセージハンドラー 1.0版
from apps1.tic_tac_toe_vol2o0.websocks.gui.c2s_handlers.start.ver1o0 import StartC2sHandler


class TicTacToeV3o1o0ConsumerCustom(ConsumerBase):
    """OA24o1o0g3o0 Webソケット用コンシューマー"""

    def __init__(self):
        super().__init__()
        self._messageManager = MessageManager()
        self._messageManager.addMessageHandler('C2S_End', EndC2sHandler())
        self._messageManager.addMessageHandler('C2S_Moved', MoveC2sHandler())
        self._messageManager.addMessageHandler('C2S_Start', StartC2sHandler())

    async def on_receive(self, doc_received):
        """クライアントからメッセージを受信したとき

        Returns
        -------
        response
        """

        return await self._messageManager.execute(self.scope, doc_received)

# EOF [OA24o1o0g3o0]
