# удаление атрибутов

class BlackKnight:

    def __init__(self):
        self.members = ['левая рука', 'правая рука', 'левая нога', 'правая нога']
        self.phrasses = ['Это всего лишь царапина', 'Это всего лишь поверхносная рана',
                         'Я неуязвим', 'Ну ладно, пусть будет ничья', ]


    @property
    def member(self):
        print('следующий член: ')
        return next(iter(self.members))

    @member.deleter
    def member(self):
        text = 'ЧЕРНЫЙ РЫЦАРЬ (утрачена {}) \n-- {}'
        print(text.format(self.members.pop(0), self.phrasses.pop(0)))

def main():
    knight = BlackKnight()
    m = knight.members
    print(m)
    del knight.member
    del knight.member
    del knight.member
    del knight.member

if __name__ == '__main__':
    main()
