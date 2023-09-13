from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint

from SocketServer.Factory import AppWebSocketFactory
from SocketServer.Protocol import AppWebSocketProtocol


if __name__ == '__main__':
    factory = AppWebSocketFactory("ws://localhost:8080")
    factory.protocol = AppWebSocketProtocol

    endpoint = TCP4ServerEndpoint(reactor, 8080)
    endpoint.listen(factory)

    print("Serwer WebSocket jest gotowy do przyjmowania połączeń.")
    
    reactor.run()