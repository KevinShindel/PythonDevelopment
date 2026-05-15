# Правила видимости переменных

b = 6 # обьявляем глобальную переменную


def f1(a):
    print(a)
    print(b) # NameError: name 'b' is not defined


def f2(a):
    print(a)
    print(b)
    b += 3 # UnboundLocalError: local variable 'b' referenced before assignment


def f3(a):
    global b
    print(a)
    print(b)
    b = 9

def main():
    # f1(3)
    # f2(3)
    f3(3)

if __name__ == '__main__':
    main()