'===================exceptions===================='
# исключение - обьекты, которые обрывают работу кода, если не были обработаны
'SyntaxError'
# исключение, которое выходитб когда в коде допушена синтоксическая ошибка
'-----------------------------------'
'NameError'
'print(adabd)'
# исключение, который выходитБ когда мы обращаемся к несуществующей переменной
'------------------------------------'
'IndexError'
'''
lest_ = [1,2,3,4]
list_[1000]
'''
# исключение, выходит при обращении к несуществующему индексу
'-----------------------------------'
'KeyError'
'''
dict_ = {'a':1, 'b':2}
print(dict_['c'])
'''
# исключение, которое выходит при обращение к несуществующему ключу
'-------------------------------------------'
'ValuError'
# когда мы передаем в функцию не коректный для неё тип данных
'''
int('10d')
'''
# когда мы распаковываем иитерируемый обьект на несколько переменных и кол-во переменных не совпадает с кол-во значений
'''
a, b, c = [1,2]
'''
'-------------------------------------------'
'TypeError'
# когда мы пытаемся использовать методы не свойственные какому- то типу данных
# когда мы пытаемся передать функцию больше или меньше аргументов, чем принимает функцию
'''
for i in 123456789:
    ...
'''
'''
5 + '5'
'''
'''
{[1,2,3]:'a'}
'''
'-------------------------------------------'
'ZironDivisionError'
# выходит когда делим что-то на 0
'''
45 / 0 | 100 // 0 | 3 % 0
'''
'-------------------------------------------'
'AtributeError'
# выходит, когда мы обращаемся к несуществующему атрибуту или методу обьект(тип данных)
'''
[1,2,3].replace(1. 5)
'''
'-------------------------------------------'
'indentationError'
# выходит, когда мы делаем неправильно используем отступы
'''
    a = 5
'''
'''
for i in range(10)
print(i)
'''
Exception
# ислючение, которую создали, чтобы его вызывать 

'====================Вызов исключений======================'
# raise NameError ('я вызвал name_error')

'===================Try except=========================='
# # это конструкция, которая помогает обрабатывать исключения
# try: # конструкцию try использует если разработчик не уверен или знает что в коде ошибка и хочет обработать её в except
#     num = int(input('введите число: '))
# except ValueError: # конструкция except нужна для обработка исключения, в данном случие иксключение VallyError
#     print('введите число, а не символы')
# else: # срабатывает когда не вышло ошибки, исключение (когда не сработал except)
#     print('вы ввели число {None}')
# finally: # работает всегда
#     print('до свидание')
'-------------------------------------------'
# try:
#     print(number)
# except (NameError, VallyError):
#     print('Нет такой переменной')
# except ZeroDivisionError:
#     print('нельзя делить на ноль')
'-------------------------------------------'
try:
    raise Exception
except:  # отлавливает все ошибки
    print("отлавлена любая ошибка")

try: 
    raise ValueError
except Exception: # отлавливается все ошибки
    print("отлавлена любая ошибка")
'--------------------------------------------'
try:
    print(1)
finally:
    print(2)
    