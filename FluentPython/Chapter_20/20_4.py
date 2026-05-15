# переопределяющие и непереопределяющие дескрипторы

# вспомогающие функции для отображения
def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


# вспомогающие функции для отображения
def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(cls_name(obj))
    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


class Overriding:
    # дискриптор данных
    def __get__(self, instance, owner):
        print('get', self, instance, owner)


class OverrigdingNoGet:
    # переопределяющий десприптор без __get__
    def __set__(self, instance, value):
        print('set', self, instance, value)


class NonOverriding:
    # маскирующий дескриптор
    def __get__(self, instance, owner):
        print('get', self, instance, owner)


class Managed:
    over = Overriding()
    over_no_get = OverrigdingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('--> Managed.spam({})'.format(display(self)))


def main():
    obj = Managed()
    obj.over
    obj.over = 7
    v = vars(obj)
    obj.over
    obj.__dict__['over'] = 8
    v = vars(obj)
    print(v)
    obj.over

if __name__ == '__main__':
    main()
