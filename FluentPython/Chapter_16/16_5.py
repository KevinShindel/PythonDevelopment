# возврат значения из сопрограммы
import collections

Result = collections.namedtuple('Result', 'count average')


def averager():
    total, count, average = 0,0,None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)

def main():
    coro_avg = averager()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(0.5)
    try:
        coro_avg.send(None)
    except StopIteration as exc: # обходим исключение что бы получить результат
        val = exc.value
    print(val)

if __name__ == '__main__':
    main()