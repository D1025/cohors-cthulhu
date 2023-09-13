from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol

class MyWebSocketProtocol(WebSocketServerProtocol):
    def onConnect(self, request):
        print(f"Połączono z {request.peer}")

    def onMessage(self, payload, isBinary):
        if not isBinary:
            print(f"Odebrano dane: {payload.decode()}")

if __name__ == '__main__':
    factory = WebSocketServerFactory("ws://localhost:8080")
    factory.protocol = MyWebSocketProtocol

    endpoint = TCP4ServerEndpoint(reactor, 8080)
    endpoint.listen(factory)

    print("Serwer WebSocket jest gotowy do przyjmowania połączeń.")
    
    # Rozpocznij pętlę reaktora Twisted
    reactor.run()