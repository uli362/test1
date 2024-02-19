'====================comprehensions==================='
# генератор - с помощью которого мы можем создавать последовательности испoльзуя цикл for в одну строку

# элемент for элемент in последовательность
# элемент for элемент in последовательность if фильтр
# элемент1 if условие1 else элемент2 for элемент in gоследовательность

# comp_ = [for i in range(10)]
# print(comp_)

# comp_1 = []
# for i in range():
#     if i % 2 == 0:
#         comp_1.append(i)
#     else:
#         compr_1.append('elem')
# print(comp_1)

# 'создайте новый лист используя старый. В новом листе должны быть только True значение'
# list_ = [12, None, 'hi', 123, 1, 6, 2, True, 0, False]
# new_list_ = [i for i in list_ if bool(i)]
# print(new_list_) # [12, 'hi', 123, 1, 6, 2, True]

# new_list_2 = [i if bool(i) else 0 for i in list_]
# print(new_list_2) # [12, 0, 'hi', 123, 1, 6, 2, True, 0, 0]

# new_list_2 = []
# for i in list_:
#     if bool(i):
#         new_list_2.append(i)
#     else:
#         new_list_2.append(0)
# print(new_list_2) # [12, 0, 'hi', 123, 1, 6, 2, True, 0, 0]

# list_ = [12, 3, 0, 34, 9, 7]
# new_list_ = ['четное' if i % 2 == 0 else 'нечетное' for i in list_]
# print(new_list_) # ['четное', 'нечетное', 'четное', 'четное', 'нечетное', 'нечетное']

# list_ = [1, 'hi', 123, 'hello world', True, 'makers', False]
# new_list_2 = []
# for i in list_:
#     if type(i) == str:
#         new_list_2.append(i)

# new_list = [i for i in list_ if type(i) == str]
# print(new_list) # ['hi', 'hello world', 'makers']

# new_list = [i ** 2 for i in list_ if type(i) == int]
# print(new_list) # [1, 15129]

'========================Виды comprehension======================='
# list comprehension -> []
# dict comprehension -> {:}
# set comprehension -> {}
# comprehension генератор -> ()

'DICT COMPREHENSION'
# # {1:1, 2:4, 3:9, 4:16, i:i**2}
# dict_ = {i:'values' for i in range(1,5)}
# print(dict_) # {1: 'values', 2: 'values', 3: 'values', 4: 'values'}

# dict_ = {'a':1, 'b':2, 'c':3}
# new_dict_ = {v:k for k,v in dict_.items()}
# print(new_dict_) # {1: 'a', 2: 'b', 3: 'c'}

# new_dict_2 = {v**2:v for v in dict_.values() if v % 2 == 0}
# print(new_dict_2) # {4: 2}

'SET COMPREHENSION'
# set_ = {i for i in range(11) if i % 2 == 0}
# print(set_) # {0, 2, 4, 6, 8, 10}

# set_1 = {12, 34, 1, 'hi', 'hello', 123, None,}
# set_2 = {i.upper() for i in set_1 if type(i) == str}
# print(set_1) # {1, 34, None, 'hello', 123, 12, 'hi'}
# print(set_2) # {'HELLO', 'HI'}

'====================Вложенные comprehension====================='
# создайте словарь, где ключами будут числа от 1 до 5, а значение - списки с числами от 1 до этого числа
dict_ = {}
for i in range(1,6):
    key = i
    values = [j for j in range(1, i+1)]
    dict_[key] = values
print(dict_) # {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

dict_ = {i: [j for j in range(1, i+1)] for i in range(1,6)}
print(dict_) # {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}
