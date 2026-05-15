# загрузка с помощью concurrent.futures
from concurrent.futures import ThreadPoolExecutor

from Chapter_17.base import BaseParser

'''
Основные классы
 ThreadPoolExecutor -> интерфейс потоков
 ProcessPoolExecutor -> интерфейс процессов
'''


class ThreadPoolParser(BaseParser):

    def download_many(self, cc_list):
        with ThreadPoolExecutor(max_workers=self.WORKERS) as executor:
            result = executor.map(self.download_one, cc_list)
        return len(list(result))


if __name__ == '__main__':
    ThreadPoolParser().main()  # 1.47s
