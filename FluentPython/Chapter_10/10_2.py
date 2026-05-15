# протоколы и динамическая типизация
import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDesk:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suit for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        ''' метод получения обьекта '''
        return self._cards[item]

    def __setitem__(self, key, value):
        ''' метод изменения обекта '''
        self._cards[key] = value


def main():
    fd = FrenchDesk()
    card = fd[12:44]
    print(card)
    random.shuffle(fd)



if __name__ == '__main__':
    main()
