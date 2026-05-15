# значение по умолчанию изменяемого типа - не удачная мысль

class HauntedBus:

    def __init__(self, passengers=[]): # если аргумент не передан - используется изменяемый обьект
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name) # применяя методы

    def drop(self, name):
        self.passengers.remove(name)

def main():
    bus1 = HauntedBus(['Alice', 'Bill'])
    print(bus1.passengers) # пока конструктор в порядке
    bus1.pick('Charlie')
    bus1.drop('Alice')
    print(bus1.passengers)
    bus2 = HauntedBus() # тут тоже все окей
    bus2.pick('Charlie')
    print(bus2.passengers) # тут тоже один элемент
    bus3 = HauntedBus()
    print(bus3.passengers) #
    bus3.pick('Dave')
    print(bus2.passengers) # внезано появляется элемент Dave
    # проблема в том что оба инстанса ссылаются на один и тот же список

if __name__ == '__main__':
    main()
