from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint

from SocketServer.Factory import AppWebSocketFactory
from SocketServer.Protocol import AppWebSocketProtocol

from decouple import config

from backend.resources.database.InitDatabase import create_database

if __name__ == '__main__':
    create_database()
    
    factory = AppWebSocketFactory(f"{config('FACTORY_SOCKET')}:{config('FACTORY_PORT')}")
    factory.protocol = AppWebSocketProtocol

    endpoint = TCP4ServerEndpoint(reactor, int(config('FACTORY_PORT')))
    endpoint.listen(factory)

    print(f"Serwer WebSocket jest gotowy do przyjmowania połączeń na porcie {config('FACTORY_PORT')}")
    
    reactor.run()