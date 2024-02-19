'===================Словари================'
# # dict - изменяемые, интерируемый, неупорядоченный, неиндексируемый тип данных, для хранение данных в парах(ключ:значение)
# user = {'name':'sultan', 'age':20, 'nick':'katana'}
# print(user['age']) #20
# print(ser['nick']) #katana
# print(ser['name']) #sultan

# {ключь:значение, ключь:значение...}
# ключь - не изменяемый тип данных, уникальный
# значение - любые: и изменяемый, и неизменяемый тип данных. Могут повторятся

'====================Создание================'
# dict1 = {'a':1, 'b':2}
# dict2 = dict([('a',1),('b',2)])
# dict3 = dict(['a1','b2'])
# dict4 = {}
# dict4['name'] = 'tima'
# dict4['age'] = 100
# dict4['nick'] = 'collection'
# print(dict4) # {'name': 'tima', 'age': 100, 'nick': 'collection'}

'=====================Методы словарей==========================='
# # get - метод, который значение по ключу, если такого ключа нет то возвращается дефолтное значение, чаще всего None
# user = {
#     'name':'Nick',
#     'age': 100,
#     'telephone_number':'+1234567'
# }
# # print(user['afasda']) # KeyError
# print(user.get('age', 'нет такого ключа')) # 100
# print(user.get('name')) # Nick
# print(user.get('id')) # None

# #pop - удаляет пару по ключу и возвращает значение
# dict_ = {'a':1, 'b':2, 'c':3}
# popped_values = dict_.pop('a')
# print(popped_values) # 1
# print(dict_) # {'b': 2, 'c': 3}

# #popitem - удаляет последнюю пару и возвращает её
# dict_ = {'a':1, 'b':2, 'c':3}
# popped_values = dict_.popitem()
# print(popped_values) # ('c', 3)

# # update - разширяет словар парами из второго словаря
# dict1 = {1:'a',2:'b'}
# dict2 = {2:'c',4:'d'}
# dict1.update(dict2)
# print(dict1) # {1: 'a', 2: 'c', 4: 'd'}

# # clear - очищает словарь 
# dict_ = {1:1, 2:2, 3:3}
# dict_.clear()
# print(dict_) # {}

# # fromkeys - метод для создание нового словаря, используя список ключей
# dict_ = dict.fromkeys([1,2])
# print(dict_) # {1: None, 2: None}

# dict2 = dict.fromkeys('abcd', 0)
# print(dict2) # {'a': 0, 'b': 0, 'c': 0, 'd': 0}

# # items - метод, который достает [((ключь, значение),(ключь знвчеие)...)]
# # key - метод, который возвращает ключи
# # values - метод, который возвращает значение
# dict_ = {'a': 1, 'b': 2, 'c': 3 }
# print(dict_.values()) # [1, 2, 3])
# print(dict_.keys()) # (['a', 'b', 'c'])
# print(dict_.items()) # ([('a', 1), ('b', 2), ('c', 3)])

# '===================Циклы с dict====================='
# dict_ = {'a': 1, 'b': 2, 'c': 3}
# for i in dict_:
#     print(i) #