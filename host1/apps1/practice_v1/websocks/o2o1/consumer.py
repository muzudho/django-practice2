# See also:
#     📖 [Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)
#     📖 [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
#     📖 [Channels - Channel Layers](https://channels.readthedocs.io/en/stable/topics/channel_layers.html)
from channels.generic.websocket import AsyncWebsocketConsumer


class WebsockPractice1V1Consumer(AsyncWebsocketConsumer):
    """非同期のWebソケットのコンシューマー"""

    async def connect(self):
        """接続時"""
        print("Connected")
        await self.accept()

    async def disconnect(self, close_code):
        """切断時"""
        print("Disconnected")

    async def receive(self, text_data):
        """メッセージ受信時
        Receive message from WebSocket.
        """
        print("Received")
        # Send message to WebSocket
        await self.send(text_data=f"Echo: {text_data}")

    async def send_message(self, res):
        """メッセージ送信時
        Receive message from room group
        """
        print("Sent message")
        # Send message to WebSocket
        await self.send(text_data=res)
