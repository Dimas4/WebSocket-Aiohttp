import random
import asyncio

from aiohttp import web
from config.get_config import get_config

config = get_config()
routes = web.RouteTableDef()


@routes.view("/ws/random_number")
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    while True:
        try:
            await asyncio.sleep(5)
            await ws.send_str(str(random.randint(1, 10)))
        except:
            return ws
