# del и сборка мусора
import weakref


def main():
    ''' наблюдение за гибелью обьекта '''
    s1 = {1,2,3}
    s2 = s1 # делаем ссылку

    def bye(): # создаём вспомогательную функцию
        print('унесенный ветром')

    ender = weakref.finalize(s1, bye) # регистриуем обратный вызов
    print(ender.alive) # проверяем ссылку на обьект
    del s1 # удаляем первую ссылку
    print(ender.alive)  # проверяем ссылку на обьект
    s2 = 'end' # делаем перепривязку
    print(ender.alive) # видим что обьект уничтожен

if __name__ == '__main__':
    main()
