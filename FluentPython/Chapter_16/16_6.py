# использование yield from


def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i


def gen2():
    yield from range(1, 10)


def main():
    res = list(gen())
    print(res)
    res = list(gen2())
    print(res)


if __name__ == '__main__':
    main()
