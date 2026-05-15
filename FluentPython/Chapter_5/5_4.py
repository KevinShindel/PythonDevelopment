# пользвательские вызываемые типы
import random


class BingoCage:

    def __init__(self, items):
        ''' принимает произвольные элемент '''
        self.__items = list(items)
        random.shuffle(self.__items)

    def pick(self):
        ''' выбирает один элемент из конструктора '''
        try:
            return self.__items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        ''' метод выполнения '''
        return self.pick()


def bingo_test():
    bingo = BingoCage(range(10))
    print(bingo.pick()) # вызывает метод pick
    print(bingo()) # вызывает метод call


if __name__ == '__main__':
    bingo_test()