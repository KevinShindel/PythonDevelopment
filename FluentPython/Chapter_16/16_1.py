# сопрограммы
# базовое поведение генератора используемого в качестве сопрограммы
import inspect


def simple_coroutine(): # сопрограмма объяляется также как обычная функция
    print('--> coroutine started')
    x = yield # yield используется в выражении присваивания
    print('--> coroutine recived', x)


def simple_coro2(a):
    print('--> Started: a=', a)
    b = yield a
    print('--> Recieved: b=', b)
    c = yield a + b
    print('--> Recieved: c=', c)




def main():
    my_coro = simple_coroutine() # вызываем функцию что бы получить генератор
    status = inspect.getgeneratorstate(my_coro)
    print(status)
    print(next(my_coro))  # мы не можем ему послать данные пока он не достиг yield
    status = inspect.getgeneratorstate(my_coro)
    print(status)
    # print(my_coro.send(42)) # отправляем данные в генератор, и он продолжает работу
    status = inspect.getgeneratorstate(my_coro)
    print(status)
    my_coro = simple_coroutine()
    # my_coro.send(1729) # TypeError: can't send non-None value to a just-started generator
    # next(my_coro) # это инициализация сопрограммы

    my_coro = simple_coro2(14)
    status = inspect.getgeneratorstate(my_coro)
    print(status)
    next(my_coro)
    status = inspect.getgeneratorstate(my_coro)
    print(status)
    my_coro.send(14)
    my_coro.send(28)
    my_coro.send(99) # StopIteration
    status = inspect.getgeneratorstate(my_coro)
    print(status)




'''
Сопрограмма может находится в одном из 4х состояний, узнать это можно 
с помощью функции inspect.getgeneratorstate()
'GEN_CREATED' --> Ожидает выполенния
'GEN_RUNNING' --> Выполняется 
'GEN_SUSPENDED' --> Приостановлено в выражении yield
'GEN_CLOSED' --> Выполнено
 
'''


if __name__ == '__main__':
    main()
