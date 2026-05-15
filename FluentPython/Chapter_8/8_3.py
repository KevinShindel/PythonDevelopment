# параметры функции как ссылки

def f(a, b):
    a += b
    return a

def main():
    x = 1
    y = 2
    r = f(x, y)
    print(r)
    print(x, y)
    a = [1, 2]
    b = [3, 4]
    r2 = f(a, b)
    print(r2)

if __name__ == '__main__':
    main()