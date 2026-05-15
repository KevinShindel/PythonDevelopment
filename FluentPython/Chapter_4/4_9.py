# сортировка unicode-текстов
import locale, pyuca


def unicode_sort_text():
    ''' сортировка текста от локали '''
    locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8') # установка локали
    fruits = ['caju', 'atemoia', 'cają', 'açaí', 'acerola']
    f = sorted(fruits)
    print(f)
    f = sorted(fruits, key=locale.strxfrm) # преобразование строки в соотв. с локалью для сортировки
    print(f)

def pyuca_sorted():
    ''' алгоритм упорядочивания Unicode '''
    collate = pyuca.Collator() # ининциация
    fruits = ['caju', 'atemoia', 'cają', 'açaí', 'acerola']
    print(fruits)
    sorted_fruits = sorted(fruits, key=collate.sort_key) # передача ключа сортировки
    print(sorted_fruits)



if __name__ == '__main__':
    unicode_sort_text()