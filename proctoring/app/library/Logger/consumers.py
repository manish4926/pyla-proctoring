import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.channel_name = 'chat_channel'
        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Broadcast the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
