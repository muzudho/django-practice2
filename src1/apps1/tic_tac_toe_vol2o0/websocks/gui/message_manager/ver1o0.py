# BOF [OA16o3o0g8o0]

class MessageManager():
    """[OA16o3o0g8o0] 〇×ゲーム v2 メッセージ駆動"""

    def __init__(self):
        self.addMessageListenerAsync = {}

    def addMessageListener(self, name, setMessage):
        self.addMessageListenerAsync[name] = setMessage

    async def execute(self, scope, doc_received):
        """クライアントからサーバーへ送られてきた変数を解析し、
        サーバーからクライアントへ送信するメッセージの作成"""

        # ログインしていなければ AnonymousUser
        # user = scope["user"]
        # print(f"[MessageManager execute] user=[{user}]")

        # メッセージ名 (Client to server)
        messageName = doc_received.get("message_name", None)

        if(messageName in self.addMessageListenerAsync):
            response_json = await self.addMessageListenerAsync[messageName].on_message_received(scope, doc_received)
            return response_json

        raise ValueError(
            f"[MessageManager execute] unknown message name: {messageName}")


# EOF [OA16o3o0g8o0]
