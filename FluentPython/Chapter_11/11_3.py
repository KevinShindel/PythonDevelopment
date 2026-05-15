# ABC в стандартной библиотеке
from abc import ABC
from collections.abc import *

'''
Iterable, Container, Sized
класс Iterable поддерживает итерирование методом __iter__
класс Container поддерживает  оператор in методом __contains__
класс Sized функцию len() методом __len__

Sequence, Mapping, Set
основные типы неизменяемых коллекций

MappingView
наследует ItemsView, KeysView, ValuesView которые предоставляют
методы .items(), .keys(), values() соответсвенно 

Callable, Hashable
Основное назначение поддеркжа безопастного способа выяснять 
является ли обьект вызываемый или хэшируемым

Iterator
является подклассом Iterable 
'''
