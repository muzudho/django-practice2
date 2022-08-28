# BOF OA16o3o0g8o0

class TicTacToeV2MessageDriven():
    """OA16o3o0g8o0 〇×ゲーム v2 メッセージ駆動"""

    def __init__(self):
        self._handlersAsync = {}

    def addHandler(self, c2s_type, handlerAsync):
        self._handlersAsync[c2s_type] = handlerAsync

    async def execute(self, scope, doc_received):
        """クライアントからサーバーへ送られてきた変数を解析し、
        サーバーからクライアントへ送信するメッセージの作成"""

        # ログインしていなければ AnonymousUser
        # user = scope["user"]
        # print(f"[TicTacToeV2MessageDriven execute] user=[{user}]")

        # `c2s_` は クライアントからサーバーへ送られてきた変数の目印
        c2s_type = doc_received.get("c2s_type", None)

        if(c2s_type in self._handlersAsync):
            response_json = await self._handlersAsync[c2s_type](scope, doc_received)
            return response_json

        raise ValueError(
            f"[TicTacToeV2MessageDriven execute] unknown c2s_type: {c2s_type}")


# EOF OA16o3o0g8o0
