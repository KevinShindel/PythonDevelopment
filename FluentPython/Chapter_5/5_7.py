# получение информации о параметрах
from inspect import signature


def clip(text: str, max_len=80):
    pass


def tag(name, *content, cls=None, **kwargs):
    pass


def main():
    sig = signature(clip)  # созадём сигнатуру
    print(sig)
    print(str(sig))
    for name, param in sig.parameters.items(): # итерируем аргументы метода
        print(param.kind, ':', name, '=', param.default)

    sig = signature(tag) # создаём сигнатуру функции
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpeg', 'cls': 'framed'} # создаём словарь аргументов
    bound_args = sig.bind(**my_tag) # <BoundArguments (name='img', cls='framed', kwargs={'title': 'Sunset Boulevard', 'src': 'sunset.jpeg'})> # байндим аргументы в сигнатуру
    print(bound_args)



if __name__ == '__main__':
    main()