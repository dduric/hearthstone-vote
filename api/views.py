import json

from aioredis.pubsub import Channel
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from jedi.evaluate.context import instance
from redis.client import Redis


@csrf_exempt
def state_update(request):
    redis_conn = Redis('localhost', 6379)
    
    print(redis_conn.smembers('readers'))
    for reply_channel in redis_conn.smembers('readers'):
        Channel(reply_channel).send({
            'text': json.dumps({
                'id': 1,
                'content': 'content',
            })
        })
    
#     async_to_sync(v.group_send)('index_group', {
#         {
#             'type': 'game_message',
#             'message': 'view message',
#         }
#     })
    
    return HttpResponse('OK')