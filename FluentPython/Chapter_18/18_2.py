# загрузка с помощью asyncio, aiohttp
import asyncio, aiohttp # модуль aiohttp нужен для HTTP
from Chapter_17.base import BaseParser


class AioHttpParser(BaseParser):

    async def get_flag(self, cc: str):  # повторно используем метод get_flag
        ''' yield from -> необходим для обхода блокировки сопрограммы '''
        url = '{}/{cc}.gif'.format(self.BASE_URL, cc=cc.lower() + '-flag')
        async with aiohttp.request('GET', url) as response:  # блокирующие операции реализованы в виде сопрограмм
            return await response.read()

    async def download_one(self, cc):
        image = await self.get_flag(cc)   # блокирующие операции реализованы в виде сопрограмм
        self.show(cc)
        if image:
            self.save_flag(img=image, filename=cc.lower() + '.gif')
        return cc

    def download_many(self, cc_list):
        loop = asyncio.get_event_loop()  # получаем ссылку на цикл обработки событий
        to_do = [self.download_one(cc) for cc in sorted(cc_list)] # строим цикл генератор для загрузки обьектов
        wait_coro = asyncio.wait(to_do)  # неблокирующая функция, которая завершается по окончанию всех сопрограмм
        res, _ = loop.run_until_complete(wait_coro) # выполняем цикл обработки событий пока сопрограмма wait_coro не завершится
        loop.close()  # заканчиваем цикл обработки событий
        return len(res)


if __name__ == '__main__':
    AioHttpParser().main()  # 2.06s
