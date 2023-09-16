from twisted.internet import reactor, endpoints
from twisted.internet.endpoints import TCP4ServerEndpoint
from HttpResources.CharacterSheetResource import CharacterSheetResource
from twisted.web import resource
from HttpResources.CharacterSheetResource import CharacterSheetResource

from twisted.web import server

from SocketServer.Factory import AppWebSocketFactory
from SocketServer.Protocol import AppWebSocketProtocol


from decouple import config

from database.InitDatabase import create_database

if __name__ == '__main__':
    create_database()
    
    factory = AppWebSocketFactory(f"{config('FACTORY_SOCKET')}:{config('FACTORY_PORT')}")
    factory.protocol = AppWebSocketProtocol

    endpoint = TCP4ServerEndpoint(reactor, int(config('FACTORY_PORT')))
    endpoint.listen(factory)

    print(f"Serwer WebSocket jest gotowy do przyjmowania połączeń na porcie {config('FACTORY_PORT')}")
    
    characterSheetResource = CharacterSheetResource()
    root = resource.Resource()
    root.putChild("character".encode('utf-8'), characterSheetResource)
    endpoints.serverFromString(reactor, config('HTTP_PORT')).listen(server.Site(root))
    
    print(f"Serwer HTTP jest gotowy do przyjmowania połączeń na porcie {config('HTTP_PORT')}")
    
    reactor.run()