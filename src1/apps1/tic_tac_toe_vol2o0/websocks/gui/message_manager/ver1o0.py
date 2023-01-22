# BOF [OA16o3o0g8o0]

class MessageManager():
    """[OA16o3o0g8o0] 〇×ゲーム v2 メッセージ駆動"""

    def __init__(self):
        self._message_handlers = {}

    def addMessageHandler(self, eventName, message_handler):
        self._message_handlers[eventName] = message_handler

    async def execute(self, scope, doc_received):
        """クライアントからサーバーへ送られてきた変数を解析し、
        サーバーからクライアントへ送信するメッセージの作成"""

        # ログインしていなければ AnonymousUser
        # user = scope["user"]
        # print(f"[MessageManager execute] user=[{user}]")

        # イベント名 (Client to server)
        event = doc_received.get("event", None)

        if(event in self._message_handlers):
            message_handler = self._message_handlers[event]
            if message_handler is None:
                raise ValueError(
                    f"[MessageManager execute] message handler not found. event:{event}")

            response_json = await message_handler.on_message_received(scope, doc_received)
            return response_json

        raise ValueError(
            f"[MessageManager execute] unknown event:{event}")


# EOF [OA16o3o0g8o0]
