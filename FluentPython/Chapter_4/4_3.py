# обработка ошибок кодирования \ декодирования
import codecs


def replace_underscore(error):
    return (error, ...) # TODO: Write logic for replace text


codecs.register_error('replace_underscore', replace_underscore)


UnicodeError # общее исключение
UnicodeEncodeError # ошибка преобразования str -> bytes
UnicodeDecodeError # ошибка преобразования bytes -> str
SyntaxError # неожиданная кодировка исходного кода


def unicode_encode_error_pass():
    city = 'São Paulo'
    b = city.encode('utf8')

    # d_ascii_strict = b.decode('ascii', errors='strict')
    d_ascii_replaced = b.decode('ascii', errors='replace') # удаляет символы которые не может декдировать
    d_ascii_ignore = b.decode('ascii', errors='ignore') # заменить символы на ? если не сможет декодировать
    d_ascii_under = b.decode('ascii', errors='replace_underscore') # заменить символы на ? если не сможет декодировать

    u16 = b.decode('utf-16')
    u8 = b.decode('utf-8')
    cp_437 = b.decode('cp437')
    latin = b.decode('latin_1')

    print(d_ascii_under)
    print(d_ascii_replaced)
    print(d_ascii_ignore)
    print(latin)
    print(cp_437)
    print(u16)
    print(u8)


def decoding_errors():
    octets = b'Montr\xe9al'
    win = octets.decode('cp1252')
    iso = octets.decode('iso8859_7')
    koi = octets.decode('koi8_r')
    utf = octets.decode('utf8', 'replace') # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte

    print(utf)
    print(win)
    print(iso)
    print(koi)


if __name__ == '__main__':
    # unicode_encode_error_pass()
    decoding_errors()