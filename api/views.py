from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def state_update(request):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        'index_group',
        {
            'type': 'game_message',
            'message': f'SENT FROM A SIGNAL: {request.POST}',
        }
    )

    return HttpResponse('OK')
