# эксперименты с executor.map
from time import sleep, strftime
from concurrent.futures import ThreadPoolExecutor


def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):
    msg = '{}loiter({}): doing for {}s...'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done'
    display(msg.format('\t'*n,n))
    return n * 10


def main():
    display('Scripts starting')
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(loiter, range(5)) # map блокирует вызовы и возвращает список в том же порядке
    display('results:', results)
    display('Waiting for individual results:')
    for i, result in enumerate(results):
        display('result {}: {}'.format(i, result))


if __name__ == '__main__':
    main()

