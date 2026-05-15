# альтернативы map, filter, reduce

def factorian(n):
    ''' :return n'''
    return 1 if n < 2 else n * factorian(n-1)


def main():
    fact = factorian
    result = list(map(fact, range(6))) # пример использования map
    result = list(map(factorian, filter(lambda n: n % 2, range(6)))) # использование map и filter
    result = [factorian(n) for n in range(6) if n % 2] # списковое включение


