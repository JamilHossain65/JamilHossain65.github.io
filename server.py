from simple_http_server import route, server
    
@route("/")
def index():
    return {"Jamil": "Hossaain"}   

server.start()