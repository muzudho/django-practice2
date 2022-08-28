# BOF OA16o3o_2o0g1o0


class S2cJsonGenCommands:
    """サーバーからクライアントへ送るJSON構造の変数を生成

    `s2c_` は サーバーからクライアントへ送る変数の目印
    """

    @staticmethod
    def create_moved(args):
        """駒を動かした

        Parameters
        ----------
        sq : int
            移動先
        piece_moved : string
            動かした駒

        Returns
        -------
        doc : dict
            クライアントへ送る
        """
        return {
            'type': 'send_message',  # type属性は必須
            's2c_type': 'S2C_Moved',
            's2c_sq': args["sq1"],
            's2c_pieceMoved': args["piece1"],
        }

    @staticmethod
    def create_start(args):
        """対局開始

        Returns
        -------
        doc : dict
            クライアントへ送る
        """
        return {
            'type': 'send_message',  # type属性は必須
            's2c_type': "S2C_Start",
        }


# EOF OA16o3o_2o0g1o0
