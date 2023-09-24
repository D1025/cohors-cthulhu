from twisted.web import resource
from HttpResources.CharacterSheetResource import CharacterSheetResource
from HttpResources.ChatResource import ChatHistoryResource

class RootResource(resource.Resource):
    def __init__(self):
        resource.Resource.__init__(self)
        self.putChild(b"character", CharacterSheetResource())
        self.putChild(b"chat", ChatHistoryResource())