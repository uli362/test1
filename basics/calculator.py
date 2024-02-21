# num1 = int(input('введите первое число: '))
# num2 = input('операция: ')
# num3 = int(input('введите второе число: '))
# if num2 == '+':
#     print(num1 + num3)
# elif num2 == '-':
#     print(num1 - num3)
# elif num2 == '/':
#     print(num1 / num3)
# elif num2 == '*':
#     print(num1 * num3)
# elif num2 == '//':
#     print(num1 // num3)
# else:
#     print('Ошибка')

# # result = num1 + num3
# # result = num1 - num3
# # print(result)
# # if num1 - num3:
# #     print(f'{num}')
    


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

'-----------------------------------------------------------------'
name1 = {'age':273, sum:6600}
name2 = {'age':1880, sum:6600}
name3 = {'age':2245, sum:8500}
name4 = {'age':4445, sum:6600}
name5 = {'age':654, sum:6600}
name6 = {'age':2435, sum:6600}
name7 = {'age':8810, sum:3600}
name8 = {'age':990, sum:6600}
name9 = {'age':7896, sum:6600}
name10 = {'age':77776, sum:9000}
oper = input('введите операцию')
if oper == '+':
    print(name1 + name3 + name5 + name7 + name8 + name10)
    # print(name1 + name2 + name3 name4 name5 name6 name7 )
else:
    print("ошибkа ")