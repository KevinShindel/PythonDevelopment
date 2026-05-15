# форматирование при выводе
import datetime


def main():
    br1 = 1/2.43 # курс бразильского реала к доллару
    print(br1)
    r = format(br1, '0.4f') # функция форматирования для типа float с 4 цифрами после запятой
    print(r)
    s = '1 BRL = {rate:0.2f} USD'.format(rate=br1)  # форматирование методом подстановки переменной rate
    print(s)
    print(format(2/3, '%'))
    print(format(25, 'b'))
    now = datetime.datetime.now()
    d = format(now, '%H:%M:%S')
    print(d)
    s = 'Сейчас {:%I:%M %p}'.format(now)
    print(s)


if __name__ == '__main__':
    main()
