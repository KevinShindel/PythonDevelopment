# документирование свойств класса

class Foo:

    @property
    def bar(self):
        ''' The bar property'''
        return self.__dict__['bar']

    @bar.setter
    def bar(self, value):
        self.__dict__['bar'] = value


def main():
    help(Foo.bar)
    help(Foo)

if __name__ == '__main__':
    main()
