# обращение с функцией как с обьектом


def factorian(n):
    ''' :return n'''
    return 1 if n < 2 else n * factorian(n-1)

def reverse(word):
    return word[::-1]

def main():
    print(factorian(42))
    print(factorian.__doc__)
    print(factorian.__name__)
    print(type(factorian))
    fact = factorian
    print(fact(5))
    result = map(factorian, range(11))
    print(list(result))
    print('++++++++++++++++++++++++')

    # функции высшего порядка (возвращают или принимают другие функции )
    fruits = ['caju', 'atemoia', 'cają', 'açaí', 'acerola']
    result = sorted(fruits, key=len)
    print(result)

    result = reverse('testing')
    print(result)

    result2 = sorted('testing', reverse=True)
    print(result2)



if __name__ == '__main__':
    main()



