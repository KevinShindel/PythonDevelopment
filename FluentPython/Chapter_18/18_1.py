# применение пакета asyncio
import threading, itertools, time, sys


class Signal:

    go = True


def spin(msg: str,  signal: Signal):
    status = ...
    write, flush = sys.stdout.write, sys.stdout.flush
    for char, in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(0.3)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    time.sleep(3)
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin,
                               args=('thinking', signal))
    print('spinner object', spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result


def main():
    result = supervisor()
    print('Answer :', result)

if __name__ == '__main__':
    main()
