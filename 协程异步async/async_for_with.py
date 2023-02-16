import asyncio


class AsyncManagerText:
    def __init__(self, file):
        self.file = open(file, 'w')

    async def __aenter__(self):
        return self.file

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


async def test_with():
    a = AsyncManagerText('1111')
    async with a as file:
        file.write('111')


# asyncio.run(test_with())

class AsyncIterable:
    def __init__(self, length):
        self.data = list(range(length))
        self.index = -1
        self.length = length

    async def fetch_data(self):
        self.index += 1
        if self.index < self.length:
            return self.data[self.index]
        else:
            return None

    def __aiter__(self):
        return self

    async def __anext__(self):
        data = await self.fetch_data()
        if data != None:
            return data
        else:
            raise StopAsyncIteration()


async def test_for():
    a = AsyncIterable(10)
    async for i in a:
        print(i)


asyncio.run(test_for())
