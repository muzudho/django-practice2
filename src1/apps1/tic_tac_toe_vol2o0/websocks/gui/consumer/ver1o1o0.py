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

# OA16o3o_2o0g1o_1o0 〇×ゲーム2.0巻 S2cメッセージ End 1.0版
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.end.ver1o0 import EndS2cMessage

# OA16o3o_2o0g1o0 〇×ゲーム2.0巻 S2C JSON ジェネレーター1.0版
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.commands.ver1o0 import S2cJsonGenCommands as CommandsGen
#          ------------------                                 ------        ------------------    -----------
#          11                                                 12            2                     3
#    ---------------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス
# 3. `2.` の別名


class TicTacToeV2o1o0ConsumerCustom(TicTacToeV2ConsumerBase):
    """OA16o3o0gA10o0 Webソケット用コンシューマー"""

    def __init__(self):
        super().__init__()

        self._messageDriven = TicTacToeV2MessageDriven()
        self._messageDriven.addHandler('C2S_End', self.on_end)
        self._messageDriven.addHandler('C2S_Moved', self.on_move)
        self._messageDriven.addHandler('C2S_Start', self.on_start)

    async def on_receive(self, doc_received):
        """クライアントからメッセージを受信したとき

        Returns
        -------
        response
        """

        return await self._messageDriven.execute(self.scope, doc_received)

    async def on_end(self, scope, doc_received):
        """対局終了時"""
        print("[TicTacToeV2MessageDriven on_end]")
        # TODO 現状、クライアント側から勝者を送ってきているが、勝敗判定のロジックはサーバー側に置きたい
        winner = doc_received.get("c2s_winner", None)

        args = {
            "player1": winner
        }

        return EndS2cMessage(args).asDict()

    async def on_move(self, scope, doc_received):
        """駒を置いたとき"""

        # `s2c_` は サーバーからクライアントへ送る変数の目印
        c2s_sq = doc_received.get("c2s_sq", None)
        piece_moved = doc_received.get("c2s_pieceMoved", None)
        print(
            f"[TicTacToeV2MessageDriven on_move] C2S_Moved c2s_sq=[{c2s_sq}] piece_moved=[{piece_moved}]")

        args = {
            "sq1": c2s_sq,
            "piece1": piece_moved,
        }

        return CommandsGen.create_moved(args)

    async def on_start(self, scope, doc_received):
        """対局開始時"""
        print("[TicTacToeV2MessageDriven on_start]")

        args = {}

        return CommandsGen.create_start(args)

# EOF OA16o3o0gA10o0
