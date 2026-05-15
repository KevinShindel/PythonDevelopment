# пристальный взгляд iter
import random


def main():
    d6_iter = iter(lambda: random.randint(1,6), 1) # второй аргумент ограничитель,
    for roll in d6_iter: # если он появляется то вызывает StopIteration
        print(roll)

if __name__ == '__main__':
    main()
