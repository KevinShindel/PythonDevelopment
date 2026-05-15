# защитное программирование при наличии изменяемых обьектов


class TwilightBus:

    def __init__(self, passengers=None):
        if passengers is not None:
            self.passengers = passengers  # синоним basketball_team
            self.passengers = list(passengers)  # в реальности нужно сделать копию параметра
        else:
            self.passengers = [] # чётко создаем пустой список

    def drop(self, name):
        self.passengers.remove(name) # операции в дейсвительности меняют список baseketball_team


def main():
    basketball_team = ['Sue', 'Tina', 'Diana', 'Pat']
    bus = TwilightBus(basketball_team)
    bus.drop('Tina')
    bus.drop('Pat')
    print(basketball_team)

if __name__ == '__main__':
    main()


