# одиночная диспетчеризация и обобщенные функции
from collections.abc import MutableSequence
from functools import singledispatch
import html
from numbers import Integral


def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>%s</pre>' % content


@singledispatch  # регистрируем базовую функцию
def htmlize2(obj):
    content = html.escape(repr(obj))
    return '<pre>%s</pre>' % content


@htmlize2.register(str) # специализированая функция регистрирует тип значений
def _(text): # имена функций не существенны и могут быть произвольно именованы
    content = html.escape(text).replace('\n', '<br />\n')
    return '<p>{0}</p>'.format(content)


@htmlize2.register(Integral)  # регистрация типов данных int
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize2.register(tuple)  # можно указать несколько типов с помощью нескольких декораторов
@htmlize2.register(MutableSequence)
def _(seq):
    inner = '<li>\n</li>'.join(htmlize2(item) for item in seq)
    return '<ul>\n</li>' + inner + '</li>\n</ul>'


def main():
    # print(htmlize({1,2,3}))
    # print(htmlize(abs))
    # print(htmlize(['alpha', 66, {1,2,3}]))
    print(htmlize2(16))
    print(htmlize2('some string'))
    print(htmlize2((1,2,3,4,5)))


if __name__ == '__main__':
    main()
