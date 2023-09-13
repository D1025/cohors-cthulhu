import json
from autobahn.twisted.websocket import WebSocketServerProtocol
from twisted.python import log

class AppWebSocketProtocol(WebSocketServerProtocol):
    def onConnect(self, request):
        print(f"Połączono z {request.peer}")
        self.factory.register(self)

    def onMessage(self, payload, isBinary):
        if not isBinary:
            try:
                message = json.loads(payload.decode())
                print(f"Odebrano dane: {message}")
            except:
                message = payload.decode()
            self.factory.broadcast(message)

    def sendJSON(self, data):
        json_str = json.dumps(data)
        self.sendMessage(json_str.encode(), isBinary=True)

    def connectionLost(self, reason):
        print(f"Rozłączono z {self.peer}")
        self.factory.unregister(self)