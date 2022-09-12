from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocalTypeRouter,URLRouter
import chat.routing

application = ProtocalTypeRouter({
	'websocket': AuthMiddlewareStack(
		URLRouter(
			chat.routing.websocket_urlpattern
		)
	),
})