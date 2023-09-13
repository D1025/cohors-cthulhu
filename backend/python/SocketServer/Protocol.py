import json
from autobahn.twisted.websocket import WebSocketServerProtocol
from twisted.python import log

from backend.python.enums.JsonType import JsonType

class AppWebSocketProtocol(WebSocketServerProtocol):
    def onConnect(self, request):
        print(f"Połączono z {request.peer}")
        self.factory.register(self)

    def onMessage(self, payload, isBinary):
        if not isBinary:
            try:
                message = json.loads(payload.decode())
                type = JsonType[message['type'].upper()]
                print(f"Odebrano dane: {message}")
            except:
                type = JsonType.NOTHING
            if type != JsonType.NOTHING:  
                self.factory.broadcast(message)

    def sendJSON(self, data):
        json_str = json.dumps(data)
        self.sendMessage(json_str.encode(), isBinary=True)

    def connectionLost(self, reason):
        print(f"Rozłączono z {self.peer}")
        self.factory.unregister(self)
        