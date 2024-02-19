'===================List======================'
# списки - изменяемый, индексируемый, упорядочный, итериреруемый тип данных, предназначен для хранение любых данных в определенном порядке

# list1 = [34, 5, 0, 'makers', 'num', [1,2,3], True, False, None] 
# print(list1[4])
# print(list1[-1])

# string = 'hello'
# res = list(string)
# print(string.split()) #['hello']
# print(res) # ['h','e','l','l','o',]

# list_ = []
# list_ = list()
# list_ = [2] * 10
# print(list_)

'======================Методы списков==================='
# # append - добавление элемента в конец
# list_ = []
# list_.append(True)
# list_.append('text')
# list_.append(123)
# list_.append([1,2,3])
# print(list_) # [True, 'test', 123, [1,2,3]]

# # pop - удаляет элемеент из списка по индексу и возвращает удаленный элемент, если не передать индекс в скобки то удаляет последний элемент
# list_ = [5,5,5,5,5,5,5]
# rm_elem = list_.pop(3)
# print(rm_elem) # 5
# print(list_) # 5, 5, 5, 5, 5, 5,

# # remove - удаление элемента из списка по значению
# list_ = [12, 'makers', 124, True, 0, 1, 1, 1,]
# list_.remove('makers')
# list_.pop(1)
# print(list_) #[12, True, 0, 1, 1, 1]

# # count - метод который считает количества элемеентов в списке
# list_ = [0, 12, 'hi', True, False, True, 0, 1, 1, 0]
# count_of_elem = list_.count(1)
# print(count_of_elem) # 4

'----------------------------------'
# # index - возвращает индекс первого вхождение указанного элемента
# list_ = [12, 1, 1, 1, 'hi', None]
# index_ = list_.index('hi') 
# print(index_) # 4

# '-----------------------------------'
# #insert - добавляет элемент список по указанному индексу
# list_ = [1,2,3,'hi',5,1,True,'world']
# list_.insert(4, 'makers')
# print(list_) # [1, 2, 3, 'hi', 'makers', 5, 1, True, 'world']

'-----------------------------------------'
# #extend - добавляет элементы списка в другой список
# list1 = [0,0,0]
# list2 = ['hi', True,None, 123,12]
# list1.extend(list2) # [0, 0, 0, 'hi', True, None, 123, 12]
# print(list1)

'--------------------------------------'
# #reverse - расставляет элементы в обратном порядке
# list_ = [1,2,3,4, None, [1,2,3]]
# list_.reverse()
# print(list_) # [[1, 2, 3], None, 4, 3, 2, 1]

'-------------------------------------'
# #sort - сортирует список, состоящий из элементов одного типа данных
# list_ = [23, 1, 24, 23, 123, 0]
# list_.sort()
# print(list_) # [0, 1, 23, 23, 24, 123]

list_ = ['mekers', 'hi', 'asd', 'qwerty']
list_.sort(key=len, reverse=True)
print(list_) # ['mekers', 'qwerty', 'asd', 'hi']

'=================Tuple===================='
# кортеж - упорядочный, неизменяемый, интерируемый тип данных, литералы (,)
tuple_ = (1,2,3,True, False, None, 'hi')
print(dir(tuple()))
# есть только два метода это - index и count 
