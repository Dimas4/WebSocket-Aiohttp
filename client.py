import asyncio

import aiohttp


URL = 'http://localhost:8050/ws/random_number'


async def main():
    session = aiohttp.ClientSession()
    async with session.ws_connect(URL) as ws:
        while True:
            message = await ws.receive()
            print(message)

    await session.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
