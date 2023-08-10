# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from .models import *
# from asgiref.sync import sync_to_async
# from channels.db import database_sync_to_async


# class MyConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         await self.send(text_data=json.dumps({
#             'message': message
#         }))

# class LatestRecordConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#         latest_record = Test.objects.latest('id')
#         data = {
#             'id': latest_record.id,
#             'title': latest_record.title,
#         }
#         await self.send(text_data=json.dumps(data))

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         await self.send(text_data=json.dumps({
#             'message': message
#         }))

# class TestT(AsyncWebsocketConsumer):
    # async def connect(self):
    #     await self.channel_layer.group_discard(
    #     self.group_name,
    #     self.channel_name
    #     )
    #     self.accept()
        
    # async def receive(self, text_data):
    #     data = await database_sync_to_async(Test.objects.latest)('id')
    #     self.send(text_data=json.dumps({"data": data}))

        
    # async def disconnect(self, close_code):
    #         await self.channel_layer.group_discard(
    #         self.group_name,
    #         self.channel_name
    #     )
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import *
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer  


# class TestT(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.group_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'group%s' % self.group_name

#         # Получить экземпляр channel layer
#         self.channel_layer = get_channel_layer()

#         # Присоединиться к группе комнаты
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#         await self.accept()

#     # ... (остальной код)

#     async def disconnect(self, close_code):
#         # Удалить пользователя из группы при отключении
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
    
#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         status = await database_sync_to_async(Test.objects.latest)('id')
#         if data['command'] == 1:
#             status.boo=True
#         elif data['command'] == 0:
#             status.boo=False

#         await database_sync_to_async(status.save)()

#         updated_status = await database_sync_to_async(Test.objects.latest)('id')

#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'room_message',
#                 'updated_status': updated_status.boo
#             }
#         )

#     async def room_message(self, event):
#         """
#         Called when someone has messaged our room.
#         """
#         updated_status = event['updated_status']
#         await self.send(text_data=json.dumps({"updated_status":updated_status}))

class Test2(AsyncWebsocketConsumer):
    async def connect(self):
    #     await self.channel_layer.group_discard(
    #     self.group_name,
    #     self.channel_name
    #     )
        await self.accept()

    async def disconnect(self, close_code):
        # await self.channel_layer.group_discard(
        #     self.room_group_name,
        #     self.channel_name
        # )
        pass
    
    async def receive(self, text_data):
        test_data = await database_sync_to_async(Test.objects.latest)('id')
        print(test_data)
        await self.send(text_data=f"{test_data}")