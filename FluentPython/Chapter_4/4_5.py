# кодировки по умолчанию
import sys, locale


expressions = """
locale.getpreferredencoding()
type(my_file)
my_file.encoding
sys.stdout.isatty()
sys.stdout.encoding
sys.stdin.isatty()
sys.stdin.encoding
sys.stderr.isatty()
sys.stderr.encoding
sys.getdefaultencoding()
sys.getfilesystemencoding()
"""


def main():
    my_file = open('rammstein.txt', 'r')
    for exp in expressions.split():
        value = eval(exp)
        print(exp.rjust(30), '->', repr(value))

if __name__ == '__main__':
    main()
