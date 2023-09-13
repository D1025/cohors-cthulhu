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
            print(f"Wysyłanie do {client.peer}")
            client.sendMessage(message.encode())