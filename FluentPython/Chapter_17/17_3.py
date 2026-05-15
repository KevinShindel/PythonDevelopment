# подробное описание загрузки данных в многопотоке
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor

from Chapter_17.base import BaseParser


class ThreadPoolSubmitParser(BaseParser):

    def download_many(self, cc_list):
        ''' выполнить задачи в многопотоке '''
        cc_list = cc_list[:5] # обрезаем кол-во флагов до 5
        with ThreadPoolExecutor(max_workers=3) as executor:  # создаём поток
            to_do = [] # временных список для отдачи задач
            for cc in sorted(cc_list):  # сортируем список
                future = executor.submit(self.download_one, cc) # добавление задачи в очередь
                to_do.append(future)  # добавление будующих обьектов
                msg = 'Scheduled for {}: {}'
                print(msg.format(cc, future))
            results = []
            for future in as_completed(to_do):  # получение выполненых задач
                res = future.result()  # получить результат задачи
                msg = '{} result: {!r}'.format(future, res)
                print(msg)
                results.append(res)

        return len(results)


if __name__ == '__main__':
    ThreadPoolSubmitParser().main()
