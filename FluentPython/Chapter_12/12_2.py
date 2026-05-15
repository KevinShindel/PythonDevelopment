# проблема множественного наследования
class A:

    def ping(self):
        print('ping: ', self)


class B(A):

    def pong(self):
        print('pong :', self)


class C(A):

    def pong(self):
        print('PONG :', self)


class D(B, C):

    def ping(self):  # MRO - Method Resolution Order - порядок разрешения
        super(D, self).ping()
        print('post-ping :', self)

    def pingpong(self):
        self.ping()
        super(D, self).ping()
        self.pong()
        super(D, self).pong()
        C.pong(self)

    def super_ping(self):
        super(B, self).ping() # вызвать явно метод ping класса B
        super().ping() # функция super следует порядку вызовов __mro__


def main():
    d = D()
    d.pong() # выполняем метод pong класса B
    C.pong(d) # выполнить метод pong класса С
    print(D.__mro__) # посмотреть порядок выполнения методов
    d.super_ping()
    d.pingpong()
    d.pingpong()


if __name__ == '__main__':
    main()
