# BOF OA16o3o_2o0g1o_2o0

class MovedS2cMessage:
    def __init__(self, args):
        """設定"""
        self._sq = args["sq1"]
        self._pieceMoved = args["piece1"]

    def asDict(self):
        """Dict形式で取得"""
        return {
            'type': 'send_message',         # type属性は必須
            'event': 'S2C_Moved',    # Server to client
            'sq': self._sq,
            'piece': self._pieceMoved,
        }

# EOF OA16o3o_2o0g1o_2o0
