from http import server
import json
from twisted.web.resource import Resource
from twisted.internet import defer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Chat import Chat

from decouple import config

class ChatHistoryResource(Resource):
    isLeaf = True
    
    def render_OPTIONS(self, request):
        request.setHeader('Access-Control-Allow-Origin', '*')
        request.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        request.setHeader('Access-Control-Allow-Headers', 'Content-Type')
        request.setHeader('Access-Control-Max-Age', '3600')
        request.setHeader('Content-Length', '0')
        request.setResponseCode(204)
        request.finish()
        return server.NOT_DONE_YET

    def render_GET(self, request):
        range_header = request.getHeader('Range')
        if range_header:
            start, end = range_header.split('-')
            start = int(start)
            end = int(end)
        else:
            start = 0
            end = 19

        engine = create_engine(config('DATABASE_URL'))
        Session = sessionmaker(bind=engine)
        session = Session()
        messages = session.query(Chat).order_by(Chat.timestamp.desc())[start:end+1]

        request.setHeader('Content-Type', 'application/json')
        request.setHeader('Access-Control-Expose-Headers', 'Content-Range')
        request.setHeader('Content-Range', f'items {start}-{end}/{len(messages)}')

        response = json.dumps([message.to_dict() for message in messages])

        session.close()
        request.setResponseCode(200)
        return response.encode('utf-8')