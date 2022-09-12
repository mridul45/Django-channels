from django.urls import re_path

websocket_urlpattern = [
	re_path(r'ws/chat/(?P<room_name>\w+)',consumers.ChatRoomConsumers),
]