import json
from autobahn.twisted.websocket import WebSocketServerFactory

class AppWebSocketFactory(WebSocketServerFactory):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clients = set()

    def register(self, client):
        self.clients.add(client)

    def unregister(self, client):
        self.clients.remove(client)

    def broadcast(self, message):
        for client in self.clients:
            json_endode = json.dumps(message).encode('utf-8')
            print(f"Wysyłanie {json_endode} do {client.peer}")
            client.sendMessage(json_endode)