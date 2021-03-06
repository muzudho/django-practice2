# See also:
#     ð [Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)
#     ð [Channels - Consumers](https://channels.readthedocs.io/en/latest/topics/consumers.html)
#     ð [Channels - Channel Layers](https://channels.readthedocs.io/en/stable/topics/channel_layers.html)
from channels.generic.websocket import AsyncWebsocketConsumer


class WebsockPractice1V1Consumer(AsyncWebsocketConsumer):
    """éåæã®Webã½ã±ããã®ã³ã³ã·ã¥ã¼ãã¼"""

    async def connect(self):
        """æ¥ç¶æ"""
        print("Connected")
        await self.accept()

    async def disconnect(self, close_code):
        """åæ­æ"""
        print("Disconnected")

    async def receive(self, text_data):
        """ã¡ãã»ã¼ã¸åä¿¡æ
        Receive message from WebSocket.
        """
        print("Received")
        # Send message to WebSocket
        await self.send(text_data=f"Echo: {text_data}")

    async def send_message(self, res):
        """ã¡ãã»ã¼ã¸éä¿¡æ
        Receive message from room group
        """
        print("Sent message")
        # Send message to WebSocket
        await self.send(text_data=res)
