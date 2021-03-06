# See also: ð[Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class TicTacToeV1Consumer(AsyncJsonWebsocketConsumer):
    """éåæã®Webã½ã±ããã®ã³ã³ã·ã¥ã¼ãã¼"""

    async def connect(self):
        """æ¥ç¶æ"""
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'room_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        """åæ­æ"""
        print("Disconnected")
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """ã¡ãã»ã¼ã¸åä¿¡æ
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        print(
            f"[Debug] Consumer1 receive text_data={text_data}")  # ã¡ããã¨åãã¦ãããããªãæ¶ã
        response = json.loads(text_data)
        event = response.get("event", None)
        message = response.get("message", None)
        if event == 'MOVE':
            # Send message to room group
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',  # typeå±æ§ã¯å¿é 
                'message': message,
                "event": "MOVE"
            })

        if event == 'START':
            # Send message to room group
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',  # typeå±æ§ã¯å¿é 
                'message': message,
                'event': "START"
            })

        if event == 'END':
            # Send message to room group
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',  # typeå±æ§ã¯å¿é 
                'message': message,
                'event': "END"
            })

    async def send_message(self, res):
        """ã¡ãã»ã¼ã¸éä¿¡æ
        Receive message from room group
        """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "payload": res,
        }))
