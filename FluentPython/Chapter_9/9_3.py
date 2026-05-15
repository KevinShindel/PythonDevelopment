# хэшируемый класс

class Vector2D:

    def __init__(self, x, y):
        self.__x = float(x) # делаем все переменные защищенными
        self.__y = float(y)

    @property # создаём метод для чтения
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __hash__(self): # оверрайдим метод __hash__
        return hash(self.x) ^ hash(self.y)


def main():
    v1 = Vector2D(3, 4)
    h = hash(v1)  # TypeError: unhashable type
    print(h)
    v2 = Vector2D(3.1, 4.2)
    h2 = hash(v2)
    print(h, h2)


if __name__ == '__main__':
    main()

