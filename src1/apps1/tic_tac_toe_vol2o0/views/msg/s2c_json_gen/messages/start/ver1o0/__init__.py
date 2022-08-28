# BOF OA16o3o_2o0g1o_3o0

class StartS2cMessage:
    def __init__(self, args):
        """設定"""
        pass

    def asDict(self):
        """Dict形式で取得"""
        return {
            'type': 'send_message',  # type属性は必須
            's2c_type': "S2C_Start",
        }

# EOF OA16o3o_2o0g1o_3o0
