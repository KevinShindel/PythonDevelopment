# номарлизация Unicode
from unicodedata import normalize, name

def main():
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1, s2)
    print(len(s1), len(s2))
    print(s1 == s2)

def text_normalization():
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(len(s1), len(s2))
    print(len(normalize('NFC', s1)), len(normalize('NFC', s2))) # номрализация типа композиция
    print(len(normalize('NFD', s1)), len(normalize('NFD', s2))) # нормализация типа декомпозиция

    ohm = '\u2126'
    print(name(ohm))
    ohm_c = normalize('NFC', ohm)
    print(ohm, ohm_c)

    s1 = '½'
    s2 = '¾'
    print(normalize('NFKC', s1))
    print(normalize('NFKC', s2))
    print(name(s1))
    print(name(s2))


if __name__ == '__main__':
    # main()
    text_normalization()