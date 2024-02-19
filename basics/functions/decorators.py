'============== Функция высшего порядка ================='
# функция высшего порядка - это функция которая принимает в аргументы другую функцию, создает внутри себя другую функцию, вызывает функцию и возвращает его

# def func1():
#     return 'hi'

# def func2(func_): 
#     print(func_())

# func2(func1) # hi

'============= Декараторы ==============================='
# деораторы - это функция высшего порядка, которая нужна для расширение функционала другой функции не изменяя ее (функция обереток)

# def decorator_glushitel(func): 
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         res = 'тихо ' + text 
#         print(res)
#     return wrapper 


# def gun():
#     return 'стрелять'

# wrapper = decorator_glushitel(gun) # тихо стрелять
# wrapper() # способ использовать декоратор в ручную

'----------------------------------------------'

# def decorator_glushitel(func): 
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         res = 'тихо ' + text 
#         print(res)
#     return wrapper 

# @decorator_glushitel
# def gun():
#     return 'стрелять'

# gun() # способ использовать декоратор при поиощи синтаксического сахара

'==========================================================='
# from datetime import datetime

# def decarator(func):
#     def wrapper(): 
#         print('start:', datetime.now())
#         func()
#         print('finish:', datetime.now())
#     return wrapper 

# def hello(): 
#     print('hello world') 

# wrapper = decarator(hello)
# wrapper()
'=========================================================='
# from datetime import datetime

# def func_start_time(func): 
#     def wrapper(*args, **kwargs):
#         print('start:', datetime.now())
#         func(*args, **kwargs)
#     return wrapper

# @func_start_time
# def sum_(a, b): 
#     print(a + b)

# sum_(20, 20) # 40
'==========================================================='
# def decarator(num): 
#     def iner_decarator(func): 
#         def wrapper(*args, **kwargs): 
#             for i in range(num):
#                 func(*args, **kwargs)
#         return wrapper 
#     return iner_decarator

# @decarator(10)
# def hello(): 
#     print('hello world')

# hello()

'==============================================================='
# def call_function(func):
#     def wrapper(*args, **kwargs):
#         print('Вызываю функцию', func.name)
#         func(*args, **kwargs)
#         print('Вызов функции', func.name, 'прошел успешно')
#     return wrapper


# @call_function
# def first():
#     print("hello world")
#     return "hello world"

# first()
'=============================================='
# from datetime import datetime

# def func_start_time(func):
#     def wrapper(*args, **kwargs):
#         print('Функция запущена ', datetime.now())
#         func(*args, **kwargs)
#     return wrapper

# @func_start_time
# def func():
#     print('Hello world')

# func() # Hello world