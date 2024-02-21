'=============== Модули и пакеты =================='
# .py - module 
# module - если много модулей то это пакеты 

'=============== file ============================='
# open() - функция, которая открывает файл в определнном режиме 

# r - read (только для чтения)
# w - write (только для записи, каждый рвз файл оочищается )
# a - append (только для дозаписи, добовляется в конец)
# x - создает файл, но если он существует выйдет ошибка

'=============== Read =============================='
file = open('test1.txt', 'r') 
# print(dir(file)) 
# print(file.writable()) # false 
# print(file.readable()) # true 
# print(file.read()) # read file
# file.seek(0) 
# print(file.read())
# print(file.read(5))
# print(file.tell()) # 0
# print(file.readlines()) #['hello\n', 'makers\n', 'world']
# print(file.tell()) # 18
file.close
'read:str, readline:str, readlines:List[str]'
'====================Write======================='
file = open('test1.txt','w')
# file.write('makers\nHELLO WORLD\n')
# file.writelines(['hello world\n', 'makers'])
file.close()

'write(str), writelines(List[str,str])'

'=====================Append============================'
# append - добавляется в конце
file = open('test1.txt', 'a')
# file.write('py33\n')
# file.seek(0)
# file.write('py32')
file.close
'=================Контекстный менеджер========================='
# with
with open('test1.txt') as f:
    print(f.read())

print(f.closed) # True - файл закрылся

