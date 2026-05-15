# создание подкласса ABC
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDesk2(collections.MutableSequence):

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self) -> int:
        ''' метод получения длины списка '''
        return len(self._cards)

    def __getitem__(self, item) -> Card:
        ''' метод получения значения '''
        return self._cards[item]

    def __setitem__(self, key, value) -> None:
        ''' метод установки значения '''
        self._cards[key] = value

    def __delitem__(self, key) -> None:   # этот метод требует MutableSequence
        ''' метод удаления значения '''
        del self._cards[key]

    def insert(self, index: int, value) -> None:   # этот метод требует MutableSequence
        ''' метод вставки '''
        self._cards.insert(index, value)
