'========================Области видимости==========================='
# LEGB - local encloused global build-in
'==================Build-in========================'
# встроенное пространство имен (list, print, dict, len, input)
'==================Global=========================='
# все переменные, которые мы создали внутри файла 
# чтобы посмотреть все глобальные переменные, можно использовать функсию globals
# a = 10
# b = 'hello'
# print(globals())

'======================enclosed=================='
# замкнутое пространство имен - это локальное пространство, у которого есть внутренеее локальное пространство

# var = 'global' # хранится в глобальном пространстве

# def func():
#     var = 'enclosed' # замкнутое пространство
#     def inner_func():
#         var = 'local' # локальное пространство
#         print(var) #local
#     print(var) # enclosed
#     inner_func()
# print(var) # global
# func()

'===================Local======================'
# local - локальное пространство именн - которое находится внутри функсии

# a = 10
# def func(a, b):
#     res = a + b
#     print(res)
#     print(locals())
#     print(globals())
# func(10, 5) # {'a': 10, 'b': 5, 'res': 15}

# count = 0
# def count_():
#     global count
#     count+=1
#     print(count)

# count_()
# count_()
# count_()
# count_()

# def count_(num):
#     count = 0
#     def inner_count_():
#         nonlocal count
#         count+=1
#         print(count)
#     for i in range(num):
#         inner_count_()
# count_(12)

# def func():
#     print('hello world')
#     return func

# func()()()()()
