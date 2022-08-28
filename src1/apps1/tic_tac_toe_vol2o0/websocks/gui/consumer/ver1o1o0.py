# BOF OA16o3o0gA10o0

# 〇×ゲーム2.0巻 Webソケット コンシューマー1.0版
from apps1.tic_tac_toe_vol2o0.websocks.gui.consumer.ver1o0 import TicTacToeV2ConsumerBase
#          ------------------                       ------        -----------------------
#          11                                       12            2
#    -----------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス

# 〇×ゲーム2.0巻 Webソケット メッセージ駆動1.0版
from apps1.tic_tac_toe_vol2o0.websocks.gui.message_driven.ver1o0 import TicTacToeV2MessageDriven
#          ------------------                             ------        ------------------------
#          11                                             12            2
#    -----------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス

from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.moved.ver1o0 import MovedS2cMessage
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.start.ver1o0 import StartS2cMessage

# OA16o3o0gA10o_1o0 Endメッセージハンドラー
from apps1.tic_tac_toe_vol2o0.websocks.gui.c2s_handlers.end.ver1o0 import EndC2sHandler


class TicTacToeV2o1o0ConsumerCustom(TicTacToeV2ConsumerBase):
    """OA16o3o0gA10o0 Webソケット用コンシューマー"""

    def __init__(self):
        super().__init__()

        self._messageDriven = TicTacToeV2MessageDriven()
        self._messageDriven.addHandler(
            'C2S_End', EndC2sHandler().on_message_received)
        self._messageDriven.addHandler('C2S_Moved', self._on_move)
        self._messageDriven.addHandler('C2S_Start', self._on_start)

    async def on_receive(self, doc_received):
        """クライアントからメッセージを受信したとき

        Returns
        -------
        response
        """
        return await self._messageDriven.execute(self.scope, doc_received)

    async def _on_move(self, scope, doc_received):
        """駒を置いたとき"""
        return MovedS2cMessage({
            # `s2c_` は サーバーからクライアントへ送る変数の目印
            "sq1": doc_received.get("c2s_sq", None),
            "piece1": doc_received.get("c2s_pieceMoved", None),
        }).asDict()

    async def _on_start(self, scope, doc_received):
        """対局開始時"""
        return StartS2cMessage({}).asDict()

# EOF OA16o3o0gA10o0
