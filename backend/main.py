from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol

class MyWebSocketProtocol(WebSocketServerProtocol):
    def onConnect(self, request):
        print(f"Połączono z {request.peer}")
        self.factory.register(self)

    def onMessage(self, payload, isBinary):
        if not isBinary:
            message = payload.decode()
            print(f"Odebrano dane: {message}")
            self.factory.broadcast(message)

    def connectionLost(self, reason):
        print(f"Rozłączono z {self.peer}")
        self.factory.unregister(self)

class MyWebSocketFactory(WebSocketServerFactory):
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

if __name__ == '__main__':
    factory = MyWebSocketFactory("ws://localhost:8080")
    factory.protocol = MyWebSocketProtocol

    endpoint = TCP4ServerEndpoint(reactor, 8080)
    endpoint.listen(factory)

    print("Serwer WebSocket jest gotowy do przyjmowania połączeń.")
    
    reactor.run()