import string, unicodedata


def shave_marks(txt):
    ''' удалить все диакритические знаки '''
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


def shaved_latin_marks(txt):
    ''' Удалить все знаки для набора Latin'''
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # игнорировать диакритеческие знаки базового набора
        keepers.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)


def extreme_normalization():
    url = 'http://en.wikipedia.org/wiki/S%C3%A3o_Paulo'
    shaved = shave_marks(url)
    print(shaved)

    shaved = shaved_latin_marks(url)
    print(shaved)


def dewinize(txt: str):
    ''' преобразование некоторых западных типографических символов в ASCII '''
    return txt.translate(
        str.maketrans(
            {'ü': 'eu'}
        )
    )

def asciize(txt: str):
    ''' удаляет диакретические знаки '''
    no_marks = shaved_latin_marks(txt)
    return unicodedata.normalize('NFKC', no_marks)


if __name__ == '__main__':
    # extreme_normalization()
    text = 'das ½ kleine Herz stand still ¾ für Stunden'
    print(text)
    normalized = dewinize(txt=text)
    print(normalized)
    shaved = asciize(normalized)
    print(shaved)

