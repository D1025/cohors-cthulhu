from twisted.web import resource
from HttpResources.CharacterSheetResource import CharacterSheetResource

class RootResource(resource.Resource):
    def __init__(self):
        resource.Resource.__init__(self)
        self.putChild(b"api/v1/character", CharacterSheetResource())