# обработка текстовых файлов

def main():
    file = open('rammstein.txt', 'w', encoding='latin_1')
    file.write('das kleine Herz stand still für Stunden')
    file.close()

    handler = open(file='rammstein.txt', mode='r', encoding='latin_1')
    result = handler.read()
    print(result)
    handler.close()


if __name__ == '__main__':
    main()
