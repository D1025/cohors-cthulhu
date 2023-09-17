import json
import re
from autobahn.twisted.websocket import WebSocketServerProtocol
from twisted.python import log

from enums.JsonType import JsonType

from service.RollService import rollFromMessage, rollFromJson
from service.DamageService import damageFromText, damageFromJson


class AppWebSocketProtocol(WebSocketServerProtocol):
    def onConnect(self, request):
        print(f"Połączono z {request.peer}")
        self.factory.register(self)

    def onMessage(self, payload, isBinary):
        if not isBinary:
            try:
                message = json.loads(payload.decode())
                print(f"Odebrano dane: {message}")
                type = JsonType[message['type'].upper()]
                if type == JsonType.MESSAGE:
                    if message['message'].startswith("/roll"):
                        roll_data = rollFromMessage(message['message'])
                        roll_data['nickname'] = message['nickname']
                        self.factory.broadcast(roll_data)
                    elif message['message'].startswith("/damage"):
                        damage_data = damageFromText(message['message'])
                        damage_data['nickname'] = message['nickname']
                        self.factory.broadcast(damage_data)
                    else:
                        self.factory.broadcast(message)
                if type == JsonType.ROLL:
                    roll_data = rollFromJson(message)
                    roll_data['nickname'] = message['nickname']
                    self.factory.broadcast(roll_data)
                if type == JsonType.DAMAGE:
                    damage_data = damageFromJson(message)
                    damage_data['nickname'] = message['nickname']
                    self.factory.broadcast(damage_data)
            except:
                type = JsonType.NOTHING 
                

    def sendJSON(self, data):
        json_str = json.dumps(data)
        self.sendMessage(json_str.encode(), isBinary=True)

    def connectionLost(self, reason):
        print(f"Rozłączono z {self.peer}")
        self.factory.unregister(self)
        