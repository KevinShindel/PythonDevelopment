# сворачивание регистра
from unicodedata import name, normalize


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold()


def main():
    symbol = 'μ'
    n = name(symbol)
    print(n)
    micro_m = symbol.casefold()
    print(symbol, micro_m)

    s1 = 'café'
    s2 = 'cafe\u0301'
    result = nfc_equal(s1, s2)
    print(result)
    result = fold_equal(s1, s2)
    print(result)




if __name__ == '__main__':
    main()
