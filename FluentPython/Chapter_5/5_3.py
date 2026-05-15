# анонимные функции

def main():
    ''' использование lambda функции '''
    fruits = ['caju', 'atemoia', 'cają', 'açaí', 'acerola', 'strawberry', 'watermelon', 'banana']
    data = sorted(fruits, key=lambda word: word[::-1])
    print(data)


def callable_test():
    ''' проверка обьектов на исполняемость '''
    test = [abs, str, 11]
    result = [callable(c) for c in test]  # [True, True, False]
    print(result)


if __name__ == '__main__':
    main()
    callable_test()
