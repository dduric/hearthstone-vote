import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class IndexConsumer(WebsocketConsumer):
    
    def connect(self):
        self.room_group_name = 'index_channel'
        
        # Join index_channel
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
        self.send(text_data=json.dumps({
            'message': 'successfully connected to index_channel',
        }))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'game_message',
                'message': message,
            }
        )
    
    # Receive message from room group
    def game_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))