# BOF OA16o3o0g8o0

# OA16o3o_2o0g1o0 S2C JSON ジェネレーター
from apps1.tic_tac_toe_v2.views.msg.s2c_json_gen.commands.v1o0 import S2cJsonGenCommands as CommandsGen
#          --------------                                 ----        ------------------    -----------
#          11                                             12          2                     3
#    ---------------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス
# 3. `2.` の別名


class TicTacToeV2MessageConverter():
    """OA16o3o0g8o0 サーバープロトコル"""

    async def on_receive(self, scope, doc_received):
        """クライアントからサーバーへ送られてきた変数を解析し、
        サーバーからクライアントへ送信するメッセージの作成"""

        # ログインしていなければ AnonymousUser
        user = scope["user"]
        print(f"[TicTacToeV2MessageConverter on_receive] user=[{user}]")

        # `c2s_` は クライアントからサーバーへ送られてきた変数の目印
        event = doc_received.get("c2s_event", None)

        if event == 'C2S_End':
            # 対局終了時
            print(f"[TicTacToeV2MessageConverter on_receive] C2S_End")

            self.on_end(scope, doc_received)

            # TODO 現状、クライアント側から勝者を送ってきているが、勝敗判定のロジックはサーバー側に置きたい
            winner = doc_received.get("c2s_winner", None)

            return CommandsGen.create_end(winner)

        elif event == 'C2S_Moved':
            # 駒を置いたとき
            # `s2c_` は サーバーからクライアントへ送る変数の目印
            c2s_sq = doc_received.get("c2s_sq", None)
            piece_moved = doc_received.get("c2s_pieceMoved", None)
            print(
                f"[TicTacToeV2MessageConverter on_receive] C2S_Moved c2s_sq=[{c2s_sq}] piece_moved=[{piece_moved}]")

            await self.on_move(scope, doc_received)

            return CommandsGen.create_moved(c2s_sq, piece_moved)

        elif event == 'C2S_Start':
            # 対局開始時
            print(f"[TicTacToeV2MessageConverter on_receive] C2S_Start")

            self.on_start(scope, doc_received)

            return CommandsGen.create_start()

        raise ValueError(f"Unknown event: {event}")

    def on_end(self, scope, doc_received):
        """対局終了時"""
        # print("[TicTacToeV2MessageConverter on_end] ignored")
        pass

    async def on_move(self, scope, doc_received):
        """駒を置いたとき"""
        # print("[TicTacToeV2MessageConverter on_move] ignored")
        pass

    def on_start(self, scope, doc_received):
        """対局開始時"""
        # print("[TicTacToeV2MessageConverter on_start] ignored")
        pass

# EOF OA16o3o0g8o0
