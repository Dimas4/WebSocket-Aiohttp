import asyncio
import aiohttp


URL = "http://localhost:8050/ws/question"


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(URL) as ws:
            await ws.send_str('question')

            async for message in ws:
                print(message)

                await ws.send_str(input("Question: "))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
