'=================Функсия==================='
# # функсия - это именнованный блок коад, который может принимать аргументы и возвращает результаты
# def get_sum(x, y): # x, y - параметры
#     result = x + y
#     return result

# print(get_sum(10, 20)) # 10, 20 - аргументы

"Функсия соблюдает принцип DRY(don't) repeat yoursalf"
'=======================Аргументы и параметры=================='
# параметры - переменные внутри функции, задается при создание функции
# аргументы - значение, которые мы передаем при вызове функции

'=====================Виды параметров===================='
# 1. обьязательные
# 2. не обьязательные
#   1. с дефолтом(со значением по умолчанию)
#   2. args(все позисионные аргументы)
#   3. kwargs(все лишние именнованные аргументы)

'===================Виды аргументов================='
# 1 позиционные (определяется по позиции)
# 2 именованные (по названию (параметр = значение))
'---------------------------------------------------------------------------------------------------------'
# db = [
#     {'name':'Tima', 'password':hash('123456789')},
#     {'name':'Nick', 'password':hash('205221000')}
# ]

# def in_database(name):
#     for user in db:
#         if name == user['name']:
#             return True
#     return False

# def register(name, password, password2):
#     if in_database(name):
#         raise Exception('Юзер с таким именем уже существует')
#     if password != password2:
#         raise Exception ('пароли не совпадают')
#     user = {'name':name, 'password':hash(password)}
#     db.append(user)
#     return 'Вы успешно зарегистрировались'

# def login(name, password):
#     if not in_database(name):
#         raise Exception('Пользователь не найден!')
#     for user in db:
#         if user['name'] == name:
#             if user['password'] != hash(password):
#                 raise Exception('Пароль не верный!')
            
#     return 'Вы успешно залогинились'

# print(register('katana', '123123123', '123123123'))
# print(db)
# print(login('katana', '123123123'))

'============================= lamdba ==============================='
# # lambda - анонимная функсия, которая записывается в одну строчку
# def sum_1(x,y):
#     return x + y

# sum_1(10, 29)
# sum_1(1,5)
# sum_1(20,1)

# sum_2 = lambda x, y: x + y
# print(sum_2(10, 5))