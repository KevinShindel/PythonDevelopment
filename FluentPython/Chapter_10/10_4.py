# хэширование и ускорение оператора ==

import operator, functools


class Vector:

    def __init__(self, components):
        self._components = components

    def __eq__(self, other):
        # return tuple(self) == tuple(other)
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0) # fn -> iterable -> initiator


def main():
    res = functools.reduce(operator.xor, range(6))
    print(res)


if __name__ == '__main__':
    main()
