# замыкания

'''
Определение замыкания
Замыкание - это функция с расширеной областью видимости
которая охватывает все неглобальные переменные, на которые
есть ссылки в теле функции хотя они в нем не определены.
'''


# пример

# avg(10) -> 10
# avg(11) -> 10.5
# avg(12) -> 11


class Averager:  # реализация на ООП

    def __init__(self):
        self.series = []

    def __call__(self, new_value, *args, **kwargs):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value) # доступ вложенной функции к внешней неглобальной переменной
        total = sum(series)
        return total / len(series)

    return averager


def main():
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

if __name__ == '__main__':
    main()
