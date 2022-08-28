# BOF [OA16o3o0gA10o_3o0]

# [OA16o3o_2o0g1o_3o0] Startメッセージ
from apps1.tic_tac_toe_vol2o0.views.msg.s2c_json_gen.messages.start.ver1o0 import StartS2cMessage


class StartC2sHandler:
    async def on_message_received(self, scope, doc_received):
        """対局開始時"""
        return StartS2cMessage({}).asDict()

# EOF [OA16o3o0gA10o_3o0]
