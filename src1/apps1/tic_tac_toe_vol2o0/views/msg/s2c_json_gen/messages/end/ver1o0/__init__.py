# BOF OA16o3o_2o0g1o_1o0

class EndS2cMessage:
    def __init__(self, args):
        """設定"""
        self._winner = args["player1"]

    def asDict(self):
        """Dict形式で取得"""
        return {
            'type': 'send_message',     # type属性は必須
            'message_name': "S2C_End",  # Server to client
            's2c_winner': self._winner,
        }

# EOF OA16o3o_2o0g1o_1o0
