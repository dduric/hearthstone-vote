from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from data.models import State


@receiver(post_save, sender=State)
def state_update(sender, instance, **kwargs):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        'index_group',
        {
            'type': 'game_message',
            'message': f'SENT FROM A SIGNAL: {instance.value}',
        }
    )
