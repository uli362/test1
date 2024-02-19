# '====================String==================='
# #строки - неизменяемые тип данных, который предназначен для хранение текста, заключенного в одинарные либо двойные кавычки 

# string1 = 'строки с одинарными ковычками'
# string2 = 'не правильная строка"
# string4 = "Dont't" # внутри двойной кавычки все одинарные - просто символы
# string5 = '''
# много строчный текст в одинарных кавычках, тут можно ставить 'любые' "кавычки" '''

# string6 = 'helllo' + 'world'
# print(string6)

# string7 = 'A' * 8 
# print(string7)

# '=======================Экранизация строк=================='
# '\n' # он переносит текст на новую строку
# print('hello\nword')

# '\t' # это табуляция 
# print('hello\tworld')
# #helo    world

# str1 = 'don\'t' # отображает кавычку
# print(str1)

# str2 = "don\"t"
# print(str2) 

# str3 = 'Символ -  \\'
# print(str3)

# '\v'# перенос на новую строку со смещением вправо на длину предыдушей строки
# print('hello\vworld\vmakers\vbootcamp')

# '\r' # перернос каретки на начоло строки
# print('makers bootcamp\rHi')
# # Hikers bootcamp

# '===========форматирование строк============'
# #1
# title = 'Iphone14'
# price = 150 
# format_1 = 'Мой телефон', title, 'стоит', price, 'долларов'
# print(format_1)
# format_2 = f'мой телефон {title} стоит {price}$'
# print(format_2)

# string = 'название: {} Цена: {}$'
# print(string.format('Iphone', 150))

# #3
# string = 'название: %s цена:%s'
# print(string % ('iphone', 150))

# '=============Методы строк==========='
# # методы - функции, которые относятся к определенному классу, к ним можно обращаяться через точку  
# #print(dir(str))

# string = 'hello world' 
# print(string.upper()) # makers -> MAKERS
# price(string.lower()) # MAKERS -> makers
# price(string.swapcase()) # MaKErS -> mAkeRs

# print(string.title()) # hello world -> Hello World
# print(string.capitalize()) # hello world -> Hello word
# print(string.center(10)) # '   hello  ''
# print(string.count('l')) #hello -> 2

# price(string.startswith('a')) #False
# price(string.startswith('h')) #True
# price(string.startswith('H')) #False
# price(string.endswith('d')) #False
# price(string.endswith('llo')) #True
# #startswith это проверяет начало текста
# #endswith это проверяет конец текста

# string = 'makers'
# print(string.islower()) # makers -> true
# print(string.islower()) # MAKERS -> Folse
# # islower проверяет только маленькие слова

# string = '1235243'
# print(string.isdigit()) # True
# # isdigit проверяет только цифр

# string = 'makers123123'
# print(string.isalnum) #True - проверка на то что является ли строка с числами или с буквами или все вместе, но не символы

# string = 'hello.world.makers.bootcamp'
# print(string.split('.')) 
# #split делит слово по '.'



# '=============Индексы================'
# byltrc - порядковый номер элемента в последовательности (символа в строке), (индексация начинается с 0)

# 'h e l l o  w o r d' 
#1 2 3 4 5 6 7 8 9 10
#-10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# string = 'hello word'
# print(string[0]) #h
# print(strring[7]) #o
# print(strring[10]) #d
# print(strring[-1]) #d

# срезы подстрака(какая то часть строки)
# string[start:end:step]

# string = 'hello world'
# print(string[3:8]) # 'lo wo'
# print(string[6:]) # 'world'
# print(string[:]) # 'hello world'
# print(string[::-1]) 'dlrow olleh'
# print(string[::2]) # 'hlowrd'
# print(string[::3]) # 'hlwl
# print(string[::4]) # 'hor'

# string = 'hello'
# string = string.upper() #hello -> HELLO
# print(string)
