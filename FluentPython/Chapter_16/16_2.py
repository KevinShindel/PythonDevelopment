# соппрограмма для вычисления накопительного среднего


def averager():
    count, total, average = 0, 0, None
    while True:
        term = yield average  # отдаёт значение и принимает новое
        total += term  # считает общую сумму
        count += 1  # простой счётчик
        average = total/count  # высчитывает среднее значение


def main():
    coro = averager()
    next(coro)
    coro.send(10)
    coro.send(20)
    rez = coro.send(40)
    print(rez)

if __name__ == '__main__':
    main()
