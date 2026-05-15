# глубокое копирование
from copy import copy, deepcopy


class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def main():
    bus1 = Bus(['Alice', 'Bob', 'Bill', 'Charlie', 'David'])
    bus2 = copy(bus1)
    bus3 = deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3), )
    bus1.drop('Bill')
    print(bus1.passengers)
    print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers), )
    print(bus3.passengers)


if __name__ == '__main__':
    main()
