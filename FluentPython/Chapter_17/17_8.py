# использование futures.as_completed
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from Chapter_17.base import BaseParser


class FuturesCompletedParser(BaseParser):

    def download_many(self, cc_list):
        with ThreadPoolExecutor(max_workers=self.WORKERS) as executor:
            to_do_map = {}
            for cc in sorted(cc_list):
                future = executor.submit(self.download_one, cc) # планирует выполенние одного вызываемого обьекта, первый аргумент сам обьекта остальные параметры
                to_do_map[future] = cc
            done_iter = as_completed(to_do_map) # возвращает итератор который отдаёт будущие обьекты по мере их выполнения
            for future in tqdm(done_iter, total=len(cc_list)):
                try:
                    future.result()
                except Exception as Err:
                    error_msg = 'ERROR {}'.format(Err)
                else:
                    error_msg = ''
                if error_msg:
                    print('*** Error for {}: {}***'.format(cc, error_msg))
        return len(cc_list)


if __name__ == '__main__':
    FuturesCompletedParser().main()
