# BOF [OA16o3o0gA10o_2o0]

# [OA16o3o_2o0g1o_2o0] Movedメッセージ
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.moved.ver1o0 import MovedS2cMessage


class MoveC2sHandler:

    async def on_message_received(self, scope, doc_received):
        """駒を置いたとき"""
        return MovedS2cMessage({
            # `s2c_` は サーバーからクライアントへ送る変数の目印
            "sq1": doc_received.get("sq", None),
            "piece1": doc_received.get("piece", None),
        }).asDict()

# EOF [OA16o3o0gA10o_2o0]
