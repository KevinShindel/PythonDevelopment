# ограничения слабых ссылок
import weakref


class MyList(list):
    ''' Подскласс list, на экземляр которого можно создать слабую ссылку '''


def main():
    a_list = MyList(range(10))
    wref = weakref.ref(a_list)
    print(wref)

    t1 = (1,2,3)
    t2 = tuple(t1)
    print(t2 is t1)
    t3 = t1[:]
    print(t3 is t1)

    t1 = (1,2,3)
    t3 = (1,2,3)
    print(t3 is t1)
    s1 = 'ABC'
    s2 = 'ABC'
    print(s1 is s2)


if __name__ == '__main__':
    main()
