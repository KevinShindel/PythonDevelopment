
class ArithmeticProgression:

    def __init__(self, begin, step, end=None): #
        self._begin = begin
        self._step = step
        self._end = end

    def __iter__(self):
        result = type(self._begin + self._step)(self._begin)
        forever = self._end is None
        idx = 0
        while forever or result < self._end:
            yield result
            idx += 1
            result = self._begin + self._step * idx


def aritprog_gen(begin, step, end=None):
    ''' функциональая релизация '''
    result = type(begin+step)(begin)
    forever = end is None
    idx = 0
    while forever or result < end:
        yield result
        idx += 1
        result = begin + step * idx

def main():
    a = ArithmeticProgression(1, 1)
    i = iter(a)
    print(next(i))
    print(next(i))
    print(next(i))

if __name__ == '__main__':
    main()