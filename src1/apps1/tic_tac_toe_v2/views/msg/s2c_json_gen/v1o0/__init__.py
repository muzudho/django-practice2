# BOF OA16o3o_2o0g1o0

class S2cJsonGen:
    """サーバーからクライアントへ送るJSON構造の変数を生成

    `s2c_` は サーバーからクライアントへ送る変数の目印
    """

    @staticmethod
    def create_end(winner):
        """対局終了

        Parameters
        ----------
        winner : str
            勝者

        Returns
        -------
        doc : dict
            クライアントへ送る
        """
        return {
            'type': 'send_message',  # type属性は必須
            's2c_event': "S2C_End",
            's2c_winner': winner,
        }

    @staticmethod
    def create_moved(dst_sq, piece_moved):
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
            's2c_event': 'S2C_Moved',
            's2c_sq': dst_sq,
            's2c_pieceMoved': piece_moved,
        }

    @staticmethod
    def create_start():
        """対局開始

        Returns
        -------
        doc : dict
            クライアントへ送る
        """
        return {
            'type': 'send_message',  # type属性は必須
            's2c_event': "S2C_Start",
        }


# EOF OA16o3o_2o0g1o0
