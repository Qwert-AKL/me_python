#int() --> int(input())
#bool() --> bool('любой символ') выдаст True. bool('') или None  или "0" выдаст False
#str() - строки
#list() list('gjdf') получим список
#tuple() tuple('gjdf') получим получим кортеж
#dict() - словарь
#set() -множество

salary=[2300,1800.80,5000,1234.58354,7500.123, 4000.43]   #список запрплат
print(len(salary)) # количество в списке зарплат/сотрудников получающие зарплаты
print(sum(salary))  #сумма всех зарплат
print(sum(salary)/len(salary)) #средня заплата в компании
print(max(salary))  #максимальная зарплата в компании
print(min(salary)) #минимальная зарплата в компании
print(round(sum(salary)/len(salary),2))    #средня заплата в компании round с двумя знаками после запятой
names = ['Алексей', 'Матвей', 'Данила', 'Алёна', 'Ласка', 'Лекс']
# zipped=zip(names,salary) # zip -собирает в один список
zipped = dict(zip(names, salary))  # можно сразу собрать в словарь
# print(zipped)       # выдаст объект
# print(list(zipped))       # получаем список с элементами картежей
print(zipped['Алексей'])         # обращение к словарю по ключу