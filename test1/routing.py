from django.urls import re_path
from .consumers import *

websocket_urlpatterns = [
    # re_path(r'ws/some_path/$', consumers.LatestRecordConsumer.as_asgi()),
    # re_path(r'^ws/test/(?P<room_name>\w+)/$', TestT.as_asgi()),

    re_path(r"^ws/test2/", Test2.as_asgi()),

    # re_path(r'^ws/signal/(?P<room_name>\w+)/$', SignalConsumer.as_asgi()),
]
