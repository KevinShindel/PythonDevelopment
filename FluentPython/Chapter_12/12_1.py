# наследование хорошо или плохо
from collections import UserDict


class DoppelDict(dict): # встроенные типы не предназначены для переопределения

    def __setitem__(self, key, value): # переопределенный метод не вызывается
        super().__setitem__(key, [value] * 2)


class DoppelDict2(UserDict): # для корректного оверрайда нужно использовать специальные классы

    def __setitem__(self, key, value):  # переопределенный метод не вызывается
        super().__setitem__(key, [value] * 2)


def main():
    dd = DoppelDict(one=1)
    print(dd)
    dd['two'] = 2 # override работает только тут
    print(dd)
    dd.update(three=3) # метод не использует setitem
    print(dd)

    dd2 = DoppelDict2(one=1) # метод отрабатывает корректно
    print(dd2)
    dd2['two'] = 2 # метод отрабатывает корректно
    print(dd2)
    dd2.update(three=3) # метод отрабатывает корректно
    print(dd2)

if __name__ == '__main__':
    main()

