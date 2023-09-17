import json
from sqlalchemy import create_engine, exists
from twisted.web import resource

from sqlalchemy.orm import sessionmaker

from decouple import config

from models.CharacterSheet import CharacterSheet

class CharacterSheetResource(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
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
                response = json.dumps({"error": "Character not found"})
                request.setResponseCode(404) 
        else:
            response = json.dumps({"error": "Name parameter is missing"})
            request.setResponseCode(400) 

        session.close()
        return response.encode('utf-8')