# ссылки на обьекты

def main():
    a = [1, 2, 3]
    b = a
    a.append(4)
    print(b)
    charles = {'name': 'Charles L.', 'born': 1832}
    lewis = charles
    print(lewis is charles)
    print(id(lewis), id(charles))
    lewis['balance'] = 950
    print(charles)
    print(a is b)

    # оператор == сравнивает значения обьектов , а оператор is их идентификаторы
    # оператор is работает быстрее чем ==

    # относительная неизменяемость кортежей
    print('+++++++++++++++++++++')
    t1 = (1,2, [30,40])
    t2 = (1,2, [30,40])
    print(t1 == t2)
    print(id(t1[-1]))
    t1[-1].append(99)
    print(t1)

    # поверхносное копирование
    print('+++++++++++++++++++++')
    l1 = [3, 5, [55, 44], (7, 8, 9)]
    l2 = list(l1) # поверхносная копия l1
    print(l1 is l2)
    print(l1 == l2)
    print('+++++++++++++++++++++')

    l1.append(100) # добавление не отражается на l2
    l1[1].remove(55) # удаляем 55 из вложеного списка l1, это отражается на l2
    print('l1: ', l1)
    print('l2: ', l2)
    l2[1] += [33, 22]  # изменяется список l2, что отражается на l1
    l2[2] += [10, 11]
    print('l1: ', l1)
    print('l2: ', l2)


if __name__ == '__main__':
    main()
