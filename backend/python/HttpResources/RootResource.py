from twisted.web import resource
from HttpResources.CharacterSheetResource import CharacterSheetResource

class CorsResource(resource.Resource):
    def __init__(self, childResource):
        resource.Resource.__init__(self)
        self.childResource = childResource

    def getChild(self, path, request):
        request.setHeader("Access-Control-Allow-Origin", "*")
        request.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
        request.setHeader("Access-Control-Allow-Headers", "Content-Type")
        request.setHeader("Access-Control-Max-Age", "3600")
        return self.childResource

class RootResource(resource.Resource):
    def __init__(self):
        resource.Resource.__init__(self)
        self.putChild(b"api/v1/character", CorsResource(CharacterSheetResource()))