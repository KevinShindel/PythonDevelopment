# Паттерн Комманда

'''
Комманда
Цель паттерна - разорвать связь между Инициатором и Получателем.
'''


class MacroCommand:

    def __init__(self, commands):
        ''' конструктор хранит список комманд '''
        self.commands = list(commands)

    def __call__(self, *args, **kwargs):
        ''' метод вызывает комманды '''
        for command in self.commands:
            command()
