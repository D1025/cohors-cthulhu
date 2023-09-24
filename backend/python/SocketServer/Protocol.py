import json
from autobahn.twisted.websocket import WebSocketServerProtocol
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

from enums.JsonType import JsonType

from service.RollService import rollFromMessage, rollFromJson
from service.DamageService import damageFromText, damageFromJson

from models.Chat import Chat


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
                engine = create_engine(config('DATABASE_URL'))
                Session = sessionmaker(bind=engine)
                session = Session()
                if type == JsonType.MESSAGE:
                    if message['message'].startswith("/roll"):
                        roll_data = rollFromMessage(message['message'])
                        roll_data['nickname'] = message['nickname']
                        chat = Chat()
                        chat.createRoll(roll_data['nickname'], roll_data['attributeValue'], roll_data['skillValue'], roll_data['focus'], roll_data['attribute'], roll_data['skill'], roll_data['rolls'], roll_data['complication'], roll_data['successes'])
                        chat.addToDatabase(session=session)
                        self.factory.broadcast(roll_data)
                    elif message['message'].startswith("/damage"):
                        damage_data = damageFromText(message['message'])
                        damage_data['nickname'] = message['nickname']
                        chat = Chat()
                        chat.createDamage(damage_data['nickname'], damage_data['damage'], damage_data['effects'], damage_data['rolls'])
                        chat.addToDatabase(session=session)
                        self.factory.broadcast(damage_data)
                    else:
                        chat = Chat()
                        chat.createMessage(message['nickname'], message['message'])
                        chat.addToDatabase(session=session)
                        self.factory.broadcast(message)
                if type == JsonType.ROLL:
                    roll_data = rollFromJson(message)
                    roll_data['nickname'] = message['nickname']
                    chat = Chat()
                    chat.createRoll(roll_data['nickname'], roll_data['attributeValue'], roll_data['skillValue'], roll_data['focus'], roll_data['attribute'], roll_data['skill'], roll_data['rolls'], roll_data['complication'], roll_data['successes'])
                    chat.addToDatabase(session=session)
                    self.factory.broadcast(roll_data)
                if type == JsonType.DAMAGE:
                    damage_data = damageFromJson(message)
                    damage_data['nickname'] = message['nickname']
                    chat = Chat()
                    chat.createDamage(damage_data['nickname'], damage_data['damage'], damage_data['effects'], damage_data['rolls'])
                    chat.addToDatabase(session=session)
                    self.factory.broadcast(damage_data)
                session.close()
            except:
                type = JsonType.NOTHING 
                

    def sendJSON(self, data):
        json_str = json.dumps(data)
        self.sendMessage(json_str.encode(), isBinary=True)

    def connectionLost(self, reason):
        print(f"Rozłączono z {self.peer}")
        self.factory.unregister(self)
        