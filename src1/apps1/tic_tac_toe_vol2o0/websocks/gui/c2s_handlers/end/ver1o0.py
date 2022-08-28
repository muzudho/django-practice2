# BOF OA16o3o0gA10o_1o0

# OA16o3o_2o0g1o_1o0 Endメッセージ
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.end.ver1o0 import EndS2cMessage
#          ------------------                                     ------        -------------
#          11                                                     12            2
#    -------------------------------------------------------------------
#    10
# 10, 12. ディレクトリー
# 11. アプリケーション
# 2. `12.` に含まれる __init__.py にさらに含まれるクラス


class EndC2sHandler:

    async def on_message_received(self, scope, doc_received):
        """対局終了時"""
        return EndS2cMessage({
            # TODO 現状、勝者は、クライアント側から送ってきたものをそのまま返しているが、勝敗判定のロジックはサーバー側に置きたい
            "player1": doc_received.get("c2s_winner", None)
        }).asDict()

# EOF OA16o3o0gA10o_1o0
