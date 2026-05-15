# семантика else

def main():
    for i in range(10):
        print(i)
    else:
        print('end') # если итератор исчерпан - вызвать этот блок кода

    finalize = True
    i = 3
    while finalize:
        i -= 1
        finalize = i
        print(i)
    else:
        print('cycle is done!') # выполняется только если finalize принял ложное значение

    try:
        print('do something')
    except:
        pass
    else:
        pass # do something if no exception in try block


if __name__ == '__main__':
    main()
