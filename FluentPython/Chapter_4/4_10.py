# база данных Unicode
import re
import unicodedata


def main():
    ''' демонстрация работы с метаданными символов в базе данных unicode'''
    re_digit = re.compile(r'\d')
    sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
    for char in sample:
        print(
            'U+%04x' % ord(char), # кодовая позиция в формате U+0000
            char.center(6), # отцентрованый символ
            're_dig' if re_digit.match(char) else '-'.center(6),  # соотв. регулярному выражению?
            'isdig' if char.isdigit() else '-'.center(6), #
            'isnum' if char.isnumeric() else '-', #
            format(unicodedata.numeric(char), '5.2f'), # выражение в числовом значении
            unicodedata.name(char), # имя символа Unicode 
            sep='\t'
        )


if __name__ == '__main__':
    main()
