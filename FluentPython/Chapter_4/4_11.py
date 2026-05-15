# str и bytes в регулярных выражениях
import os, re, sys



def main():
    re_numbers_str = re.compile(r'\d+')
    re_words_str = re.compile(r'\w+')

    re_numbers_bytes = re.compile(rb'\d+')
    re_words_bytes = re.compile(rb'\w+')

    text_str = ('Ramanujan saw \u0be7\u0bed\u0be8\u0bef as 1729 = 1³ + 12³  = 9³ + 10³.')
    text_bytes = text_str.encode('utf-8')
    print('text', repr(text_str) , sep='\n')
    print('Numbers')

    print('str  :'.ljust(4), re_numbers_str.findall(text_str))
    print('bytes'.ljust(4), re_numbers_bytes.findall(text_bytes))
    print('Words')
    print('str  :'.ljust(4), re_words_str.findall(text_str))
    print('bytes'.ljust(4), re_words_bytes.findall(text_bytes))


def os_bytes_str():
    ''' опеределение кодировки для последовательности байтов в именах файлов '''
    sy_encoding = sys.getfilesystemencoding() # получить кодек по-умолчанию
    print(sy_encoding)

    py_name_str = os.listdir('example')[0]  # ['digits-of-π.txt']
    pi_name_bytes = os.listdir(b'example')[0]  # [b'digits-of-\xcf\x80.txt']
    print(py_name_str)
    print(pi_name_bytes)

    pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')
    print(pi_name_str)


if __name__ == '__main__':
    # main()
    os_bytes_str()


