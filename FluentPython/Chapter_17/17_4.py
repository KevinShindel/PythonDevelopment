# запуск процессов с помощью ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor

from Chapter_17.base import BaseParser


class ProcessPoolParser(BaseParser):

    def download_many(self, cc_list):
        ''' использование ProcessPoolExecutor не даёт существенного ускорения '''
        with ProcessPoolExecutor(max_workers=self.WORKERS) as executor:
            results = executor.map(self.download_one, cc_list)
        return len(list(results))


if __name__ == '__main__':
    ProcessPoolParser.main()