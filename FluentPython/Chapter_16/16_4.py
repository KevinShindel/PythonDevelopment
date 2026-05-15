# завершение сопрограммы и обработка исключений

class DemoException(Exception):
    ''' Exception example for demo '''


def demo_exc_handling():
    print('--> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print(' DemoException handled. Continuing')
        else:
            print('--> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run!')


def demo_finally():
    print('--> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print(' DemoException handled. Continuing')
            else:
                print('--> coroutine received: {!r}'.format(x))
    finally:
        print('--> coroutine ending')


def main():
    exc_cor = demo_exc_handling()
    next(exc_cor)
    exc_cor.send(11)
    exc_cor.send(22)
    exc_cor.throw(DemoException)
    exc_cor.close()

    exc_cor = demo_exc_handling()
    next(exc_cor)
    exc_cor.throw(ZeroDivisionError)

if __name__ == '__main__':
    main()