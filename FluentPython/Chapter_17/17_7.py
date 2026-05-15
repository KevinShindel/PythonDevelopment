# знакомство с asyncio
import asyncio
import time

from aiohttp import ClientSession

from Chapter_17.base import BaseParser


class AsyncioParser(BaseParser):

    async def get_flag(self, session: ClientSession,  cc: str):
        url = '{}/{cc}.gif'.format(self.BASE_URL, cc=cc.lower()+'-flag')
        async with session.get(url) as response:
            return await response.read()

    async def download_one(self, session, cc):  # <6>
        image = await self.get_flag(session, cc)  # <7>
        self.show(cc)
        self.save_flag(image, cc.lower() + '.gif')
        return cc

    async def download_many(self, cc_list):
        async with ClientSession() as session:  # <8>
            res = await asyncio.gather(  # <9>
                *[asyncio.create_task(self.download_one(session, cc))
                  for cc in sorted(cc_list)])

        return len(res)

    def main(self):
        t0 = time.time()
        count = asyncio.run(self.download_many(self.POP20_CC))
        elapsed = time.time() - t0
        msg = '\n{} flags downloaded in {:.2f}s'
        print(msg.format(count, elapsed))


if __name__ == '__main__':
    AsyncioParser().main()


