# слабые ссылки

import weakref

def main():
    a_set = {0,1}
    wref = weakref.ref(a_set) # получение обьекта ссылки
    print(wref)
    print(wref())
    a_set = {2, 3, 4}
    print(wref())
    print(wref() is None)


if __name__ == '__main__':
    main()
