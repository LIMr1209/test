import asyncio
from aiohttp import ClientSession

# url = "http://127.0.0.1:8080/?id=1"
url = "http://127.0.0.1:8080/index"

async def make_call():
    async with ClientSession() as session:
        response = await session.request(method='GET', url=url)
    return "ok"

async def main():
    tasks = [make_call() for x in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())