num1 = int(input('введите первое число: '))
num2 = input('операция: ')
num3 = int(input('введите второе число: '))
if num2 == '+':
    print(num1 + num3)
elif num2 == '-':
    print(num1 - num3)
elif num2 == '/':
    print(num1 / num3)
elif num2 == '*':
    print(num1 * num3)
elif num2 == '//':
    print(num1 // num3)
else:
    print('Ошибка')

# result = num1 + num3
# result = num1 - num3
# print(result)
# if num1 - num3:
#     print(f'{num}')
    


'=============Второй способ калькулятора==================='

# def calc_():
#     try:
#         num1 = float(input('Enter number: ')) 
#         num2 = float(input('Enter number: '))  
#         oper = input('Enter oper: ')  
#         if oper == '+':
#             print(num1+num2)
#         elif oper == '-':
#             print(num1-num2)
#         elif oper == '/':
#             print(num1/num2)
#         elif oper == '*':
#             print(num1*num2)
#         elif oper == '**':
#             print(num1**num2)
#         else:
#             raise KeyError
#     except KeyError:
#         print('вы ввели не ту операцию')
#     except ValueError:
#         print('введите число, а не символы')
#     except ZeroDivisionError:
#         print('нельзя делить на ноль')



# calc_()