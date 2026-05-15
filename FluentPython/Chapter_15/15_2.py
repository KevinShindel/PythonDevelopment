# контекстные менеджеры и блоки with

'''
Протокол контекстного менеджера состоит из
методов __enter__ и __exit__
'''
import contextlib


def main():
    with open('filename.txt', 'r') as handler: # handler это результат вызова метода __enter__
        src = handler.read(60)
    print(len(src))

# утилиты contexlib
'''
    contextlib.closing() # функция для построения контекстных менеджеров для реализации __enter__ / __close__
    contextlib.suppress() # для временного игнорирования заданых исключений
    @contextlib.contextmanager # декоратор для построения контекстных менеджеров
    contextlib.ContextDecorator # базовый класс для опеределения контекстных менеджеров
    contextlib.ExitStack # составляет композицию из переменного числа контекстных менеджеров
'''

# использование декоратора @contextlib.contextmanager


@contextlib.contextmanager # применяем декоратор
def looking_glass():
    import sys
    original_write = sys.stdout.write # сохраняем исходный метод

    def rev_write(text):  # функция для замыкания
        original_write(text[::-1])
        sys.stdout.write = rev_write # заменяем функцию
        yield 'JABBERWOCKY' # отдаём значение которое будет связано с правой частью блока with
        sys.stdout.write = original_write # восстанавливаем исходное значение функции

def main2():
    with looking_glass() as what:
        print('Alice Bob Snowflake')
        print(what)



if __name__ == '__main__':
    main2()


