import random
import asyncio
import aiohttp

from aiohttp import web
from config.get_config import get_config

config = get_config()
routes = web.RouteTableDef()


@routes.view("/ws/question")
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for message in ws:
        if message.type == aiohttp.WSMsgType.TEXT:
            print(message.data)
            if message.data == 'close':
                await ws.close()
            else:
                await ws.send_str(message.data + '. It\'s answer')
    return ws


@routes.view("/ws/random_number")
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    while True:
        try:
            await ws.send_str(str(random.randint(1, 10)))
            await asyncio.sleep(5)
        except:
            return ws
