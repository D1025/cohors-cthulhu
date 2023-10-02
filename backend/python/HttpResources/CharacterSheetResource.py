import json
from sqlalchemy import create_engine, exists
from twisted.web import resource, server

from sqlalchemy.orm import sessionmaker

from decouple import config

from models.CharacterSheet import CharacterSheet

class CharacterSheetResource(resource.Resource):
    isLeaf = True
    
    def render_OPTIONS(self, request):

        request.setHeader("Access-Control-Allow-Origin", "*")
        request.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
        request.setHeader("Access-Control-Allow-Headers", "Content-Type")
        request.setHeader("Access-Control-Max-Age", "3600")
        request.setHeader("Content-Length", "0")
        request.setResponseCode(204)
        request.finish()
        return server.NOT_DONE_YET


    def render_GET(self, request):
        request.setHeader("Access-Control-Allow-Origin", "*")
        request.setHeader("Content-Type", "application/json")
        engine = create_engine(config('DATABASE_URL'))
        Session = sessionmaker(bind=engine)
        session = Session()
        params = request.args

        if b'name' in params:
            nameParam = params[b'name'][0].decode('utf-8')
            character = session.query(CharacterSheet).filter_by(nickname=nameParam).first()
            if character:
                response = json.dumps(character.to_dict())
                request.setResponseCode(200)
            else:
                character = CharacterSheet(nameParam)
                response = json.dumps(character.to_dict())
                request.setResponseCode(200)
        else:
            response = json.dumps({"error": "Name parameter is missing"})
            request.setResponseCode(400) 

        session.close()
        return response.encode('utf-8')