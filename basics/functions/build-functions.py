'===========================Встроенные функции=============================='
# map, filter, reduce, zip, enumerate

'ZIP'
# соеденяет несколько последовательностей (получает генератор, в котором элементы - tuple)(zip abject)
# list_1 = [1,2,3,4]
# list_2 = ['a','b','c',]
# list_3 = [10.5, 20.0, 1.3, 0.5]
# zipped = zip(list_1, list_2, list_3)
# print(zipped) # <zip object at 0x104cc5b00>
# print(list(zipped)) # [(1, 'a', 10.5), (2, 'b', 20.0), (3, 'c', 1.3)]
# print(tuple(zipped)) # ((1, 'a', 10.5), (2, 'b', 20.0), (3, 'c', 1.3))
# print(dict(zipped)) # будет работать только с двумя листами в zip()

'ENUMERATE'
# номерует последовательность (по деволту с 0), (тоже возвращает генератор)
# <enumirate object 0x7kjf8392sjd90>

# enumerated = enumerate('hello world', 100) # [(100, 'h'), (101, 'e'), (102, 'l'), (103, 'l'), (104, 'o'), (105, ' '), (106, 'w'), (107'o'), (108, 'r'), (109, 'l'), (110, 'd')] 
# print(enumerated) # <enumerate object at 0x1026d5580>
# print(list(enumerated)) # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, ' '), (6, 'w'), (7, 'o'), (8, 'r'), (9, 'l'), (10, 'd')]
# for elem in list(enumerated):
#     print(elem)

'MAP'
# # принимает функцию и последовательность
# # записывает в новую последоватальность результат функции, принимает каждый элемент последовательности
# # <mep object 0x7djsf9jidf9qj>

# list_ = ['1', '2', '3', '4']
# mapped = map(int, list_) # <map object at 0x7f5441f40cd0>
# print(list(mapped)) # [1, 2, 3, 4]

# list_2 = ['skk1', '55', 'hsdh222', '662']
# mapped_2 = map(str.isdigit, list_2)
# print(list(mapped_2)) # [False, True, False, True]

# list_ = [12, 34, 1, 2, 6]
# def pow_(x):
#     return x ** 2

# print(list(map(pow_, list_)))          # [144, 1156, 1, 4, 36]

# print(list(map(lambda x:x**2, list_))) # [144, 1156, 1, 4, 36]

# str_ = 'hello world'
# mapped = map(str.upper, str_)
# print(''.join(list(mapped))) # HELLO WORLD

# print(''.join(list(map(str.upper, 'hello world')))) # HELLO WORLD

'FILTER'
# возвращает генератор с элементами, прошедшими фильтрацию (какое-то условие), принимает функсию и последовательность
# <filter object 0x7f5441f40cd0>

# list_ = [12, -23, 0, -1, -34, 38]
# filtered = filter(lambda x: x >= 0, list_)
# print(list(filtered)) # [12, 0, 38]

# users = [
#     {'name': 'makers', 'age':20},
#     {'name': 'anonym', 'age':15},
#     {'name': 'sem', 'age':25}
# ]
# filtered = filter(lambda x: x['age'] > 18, users)
# print(list(filtered)) # [{'name': 'makers', 'age': 20}, {'name': 'sem', 'age': 25}]
'----------------------------------------'
# users = [
#     {'name': 'makers', 'age':20},
#     {'name': 'anonym', 'age':15},
#     {'name': 'sem', 'age':25}
# ]
# filtered = filter(lambda x: x['name'].startswith('a'), users)
# print(list(filtered)) # [{'name': 'anonym', 'age': 15}]

'REDUCE'
# тоже принимает функцию и последовательность, но возвращает один элемент (передоваемая функция должна принимает два аргумента)
# импортирует из functools

# from functools import reduce

# list_ = [1,23,4,1,5,10]
# res = reduce(lambda x, y: x * y, list_)
# print(res) # 4600


'=================вывести юзеров кому больше 18 используя reduce=============='
# users = [
#     {'name': 'makers', 'age':20},
#     {'name': 'anonym', 'age':15},
#     {'name': 'sem', 'age':25}
# ]

# from functools import reduce
# def func(x, y):
#     if x ['age'] < y['age']:
#         return x
#     else:
#         return y
    
# reduce(func, users)
# print(reduce(func, users)) # {'name': 'anonym', 'age': 15}

'==================выведите самое маленькое число=========================='
# list_ = [1,2,4,6,1,9,-1,6,-12]
# from functools import reduce
# def func(x, y):
#     if x < y:
#         return x
#     else:
#         return y
# reduce(func, list_)
# print(reduce(func, list_)) # -12
