# тексты и байты

def unicode_normalization():
    text = '''
    Ein kleiner Mensch stirbt nur zum Schein
    wollte ganz alleine sein
    das kleine Herz stand still für Stunden
    so hat man es für tot befunden
    es wird verscharrt in nassem Sand
    mit einer Spieluhr in der Hand
    '''
    byte_text = bytes(text.encode('utf8'))

    r = byte_text.decode(encoding='ascii', errors='ignore')

    print(r)
    
    s = 'für'
    print(len(s))
    b = s.encode(encoding='utf-8')
    print(len(b))
    s = b.decode(encoding='ascii', errors='ignore')
    print(len(s))
    print(s)


if __name__ == '__main__':
    unicode_normalization()