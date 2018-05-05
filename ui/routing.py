from django.conf.urls import url

from ui import consumers


websocket_urlpatterns = [
    url(r'^ws/index/$', consumers.IndexConsumer),
]