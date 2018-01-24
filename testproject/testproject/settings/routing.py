from channels.routing import route
from .comsumers import websocket_receive

channe_routing = [
        route("websocket.receive", websocket_receive, path=r"^/chtest/"),
        ]
