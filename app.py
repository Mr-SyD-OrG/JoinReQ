from flask import Flask
app = Flask(__name__)
from aiohttp import web

from aiohttp import web
from route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
    
@app.route('/')
def hello_world():
    return 'TechVJ'


if __name__ == "__main__":
    app.run()
    app = web.AppRunner(await web_server())
    app.setup()
    web.TCPSite(app, "0.0.0.0", 8080).start()
    print("Web Response Is Running......🕸️")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
