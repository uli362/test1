# '=======логические и условные операторы========'
# # логические операторы - вырожение, которые возвращают True, если вырожение верно, False - если вырожение не верно
# 'равенство'
# 5 == 6 # False
# 5 == 5 # True

# 'не равенсто'
# 4 != 5 # True
# 5 != 5 # False

# 'больше'
# 10 > 0 # True
# -5 > 2 # False

# 'меньше'
# 5 < 4 # False
# 5 < 10 # True

# 'больше и равно'
# 5 >= 10 # False
# 10 >= 5 # True
# 5 >= 5 # True


# '========== And, Or, Not==========='
# # and - и
# # or - или
# # not - не
# a = 5
# b = 6
# # True  и   True
# a == 5 and b == 6 # True
# # True  и  False --> False
# a == 5 and b == 3 # False
# # False и  False
# a > 10 and b < 2 # False

# # возвратится true, если с права true И с лева true.
# # если хотябы с одной стороны будет Folse, либо сразу в двух сторонах то возвратится folse

# 'OR'
# a = 20
# b = 5

# # True или True --> True
# a == 20 or b > 1
# #True или False --> True
# a == 20 or b < 1
# #False или True --> True
# a > 100 or b == 5
# #False или False --> False
# a < 10 or b < 1

# #если хотябы одна часть выражения True, то будет True

# 'HOT'

# # not False - True
# # not True - False
# a= 5 
# not a < 10 # False
# not a != 5 # True
# not not not not not a != 10 # True

# '============Boolean Type============'
# # Булевый тип данных имеет всего 2 значение

# # булевый тип данных используется в условных операторах, для выполнения сутеативных задач

# bool(1) # True
# bool(0) # Folse
# bool(-123) #True

# bool(hello) # True
# bool(' ') # True
# bool('') # False

# bool(True) #True
# bool(False) # False

# bool([]) # False
# bool([[]]) # True


# '================None Type=================='
# # None - неизменямый тип данных с одним значением - None, который используется для обозночения отсутсвие значение
# a = None 
# print(a)

# bool(None) # False
# bool('None') # True


'===============условные операторы============='
# # условные операторы - конструкция, которая используется для того, чтобы при разных входных дыанных код работал по разному

# '--------------------------'
# if условие 1:
#     тело1 
# '-------------' 
# if условие1 : 
#      тело1 #тело1 будет выполнятся если условие1 - true 
# else:
#      тело2: #тело2 будет работать во всех других случая 
#      '-----------------'

# if условие1:
#      тело1 
# elif условие2:
#      тело2 
# '----------------'     
# if условие1:
#      тело1 
# elif условие2:
#      тело2 
# else: 
#      тело3


num1 = int(input('Введите первое число: '))
num2 = int(input('ВВедите второе число: '))
operator = input('введите оператор: ')
if operator  == '+':
    print(num1+num2)
elif operator == '-':
    print(num1-num2)
    print(num1*num2)
elif operator == '/':
    print(num1/num2)
elif operator == '**':
    print(num1**num2)
elif operator == '%' :
    print(num1%num2)
else:
    ('ошибка,повторите попытку!')

'тернарный оператор'
#тернарный оператор - условие в одну строку 
#telo1 if uslovie else telo2